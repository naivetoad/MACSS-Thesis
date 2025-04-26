# Load required libraries
library(tidyverse)
library(jsonlite)

# Load the emotion dataset
emotion_df <- read_csv("data/all/emotion_data.csv", show_col_types = FALSE)

# Define emotion categories
emotion_categories <- c("anger", "joy")

# Extract dominant emotions from JSON
extract_dominant_emotions <- function(emotion_list_str) {
  emotion_list <- fromJSON(emotion_list_str, simplifyVector = FALSE)
  emotion_counts <- setNames(as.list(rep(0, length(emotion_categories))), emotion_categories)
  dominant_emotions <- map(emotion_list, function(emotions) {
    if (length(emotions) == 0) return(NULL)
    max_val <- max(unlist(emotions))
    dominant <- names(which.max(unlist(emotions)))
    if (dominant == "neutral") return(NULL)
    return(dominant)
  })
  dominant_emotions <- unlist(dominant_emotions)
  if (length(dominant_emotions) > 0) {
    counted <- as.list(table(dominant_emotions))
    for (emotion in names(counted)) {
      if (emotion %in% emotion_categories) {
        emotion_counts[[emotion]] <- counted[[emotion]]
      }
    }
  }
  return(emotion_counts)
}

# Extract dominant emotions
emotion_df <- emotion_df %>%
  mutate(ID = row_number()) %>%
  mutate(dominant_emotions = map(Emotions, extract_dominant_emotions),
         LineCount = map_dbl(dominant_emotions, ~ sum(unlist(.x), na.rm = TRUE))) %>%
  unnest_wider(dominant_emotions) %>%
  mutate(across(all_of(emotion_categories), ~ .x / LineCount))

# Load the liwc dataset
liwc_df <- read_csv("data/all/liwc_data.csv", show_col_types = FALSE)

# Rename variables
liwc_df <- liwc_df %>%
  rename("cognitive processes" = cogproc, 
         causation = cause,
         discrepancy = discrep,
         tentativeness = tentat,
         differentiation = differ,
         affect = Affect,
         "positive tone" = tone_pos,
         "negative tone" = tone_neg,
         "positive emotion" = emo_pos,
         "negative emotion" = emo_neg,
         "social behavior" = socbehav,
         "prosocial behavior" = prosocial,
         politeness = polite,
         moralization = moral,
         communication = comm) %>%
  mutate(ID = row_number())

# Define variables
liwc_categories <- c("cognitive processes", "social behavior", "politeness", "conflict")

# Merge emotion and liwc datasets
combined_df <- liwc_df %>%
  inner_join(emotion_df %>%
               select(ID, all_of(emotion_categories)),
             by = "ID") %>%
  drop_na(all_of(c(liwc_categories, emotion_categories)))

# Prepare pca input
pca_input <- combined_df  %>%
  select(all_of(liwc_categories), all_of(emotion_categories))

# Run pca
pca_result <- prcomp(pca_input, scale. = TRUE)

# Display pca result
summary(pca_result)

# Create data points for characters
pca_points <- as.data.frame(pca_result$x) %>%
  mutate(Gender = combined_df$Gender, Title = combined_df$Title) %>%
  filter(Gender != "Neutral")

pca_points <- pca_points %>%
  mutate(Franchise = case_when(
    grepl("Elder Scrolls", Title) ~ "Elder Scrolls",
    grepl("Final Fantasy", Title) ~ "Final Fantasy",
    grepl("Persona", Title) ~ "Persona",
    grepl("Horizon", Title) ~ "Horizon",
    TRUE ~ "Other"
  )) %>%
  filter(Franchise != "Other") %>%
  mutate(Franchise = as.factor(Franchise))

# Factor gender
pca_points$Gender <- relevel(factor(pca_points$Gender), ref = "Male")

# Run logistic regression
glm_gender <- glm(Gender ~ PC1 + PC2, data = pca_points, family = "binomial")

# Display regression result 
summary(glm_gender)

# Create data for variable arrows
loadings <- as.data.frame(pca_result$rotation[, 1:2]) %>%
  rownames_to_column("variable")

# Scale arrows for better visualization
loadings <- loadings %>%
  mutate(PC1 = PC1 * 1.2,
         PC2 = PC2 * 1.2)

# Adjust text position
loadings$label_x <- loadings$PC1 + c(0.01, 0.03, 0.02, -0.02, -0.1, 0.07) 
loadings$label_y <- loadings$PC2 + c(0.06, -0.04, -0.05, -0.05, 0, 0)

# Compute centroids
centroids <- pca_points %>%
  group_by(Franchise, Gender) %>%
  summarise(PC1 = mean(PC1), PC2 = mean(PC2), .groups = "drop")

# Create a biplot on pca result
ggplot(pca_points, aes(x = PC1, y = PC2)) +
  geom_point(data = centroids, aes(x = PC1, y = PC2, shape = Gender, color = Franchise), 
             size = 4) +
  geom_segment(data = loadings, aes(x = 0, y = 0, xend = PC1, yend = PC2),
               arrow = arrow(length = unit(0.3, "cm")), color = "black") +
  geom_text(data = loadings, aes(x = label_x, y = label_y, label = variable),
            size = 4, color = "black") +
  coord_cartesian(xlim = c(-1, 1), ylim = c(-1, 1)) +
  theme_minimal(base_family = "serif") +
  labs(title = "", x = "Component 1", y = "Component 2")