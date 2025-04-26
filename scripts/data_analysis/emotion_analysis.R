# Load required libraries
library(MASS)
library(tidyverse)
library(jsonlite)
library(fmsb)
library(broom)
library(proxy)
library(reshape2)

# Load the dataset
df <- read_csv("data/emotion_data.csv", show_col_types = FALSE)

# Function to extract dominant emotions
extract_dominant_emotions <- function(emotion_list_str) {
  emotion_list <- fromJSON(emotion_list_str, simplifyVector = FALSE) # Parse a JSON string into a list of lists
  emotion_categories <- c("anger", "disgust", "fear", "joy", "sadness", "surprise") # Create a list to store emotions
  # Extract dominant emotions from each dialogue
  dominant_emotions <- map(emotion_list, function(emotions) {
    max_val <- max(unlist(emotions))
    dominant <- names(which.max(unlist(emotions)))
    if (dominant == "neutral") return(NULL)
    return(dominant)
  })
  dominant_emotions <- unlist(dominant_emotions)
  # Count frequency of each emotion
  emotion_counts <- setNames(as.list(rep(0, length(emotion_categories))), emotion_categories)
  if (length(dominant_emotions) > 0) {
    counted_emotions <- as.list(table(dominant_emotions))
    for (emotion in names(counted_emotions)) {
      if (emotion %in% emotion_categories) {
        emotion_counts[[emotion]] <- counted_emotions[[emotion]]
      }
    }
  }
  return(emotion_counts)
}

# Apply the function to the dataset
df <- df %>%
  mutate(dominant_emotions = map(Emotions, extract_dominant_emotions))

# Create a list to store emotions
emotion_categories <- c("anger", "disgust", "fear", "joy", "sadness", "surprise")

# Create a dictionary to store emotion counts
emotion_counts <- setNames(rep(0, length(emotion_categories)), emotion_categories)

# Aggregate counts of each emotion
for (row in df$dominant_emotions) {
  for (emotion in names(row)) {
    if (emotion %in% emotion_categories) {
      emotion_counts[emotion] <- emotion_counts[emotion] + row[[emotion]]
    }
  }
}

# Convert the dictionary to a dataframe
emotion_df <- data.frame(
  Emotion = names(emotion_counts),
  Count = as.numeric(emotion_counts)
) %>%
  arrange(desc(Count))

# Define colors for each emotion
emotion_colors <- c(
  "anger" = "#E12729",
  "disgust" = "#72B043",
  "fear" = "#BC5090",
  "joy" = "#F8CC1B",
  "sadness" = "#43B0F1",
  "surprise" = "#F37324"
)

# Convert emotion to a factor with sorted levels
emotion_df$Emotion <- factor(emotion_df$Emotion, levels = emotion_df$Emotion)

# Compute total count of emotions
emotion_df$Percentage <- (emotion_df$Count / sum(emotion_df$Count)) * 100

# Create a bar chart on emotion counts
ggplot(emotion_df, aes(x = Emotion, y = Count, fill = Emotion)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = paste0(round(Percentage, 1), "%")), 
            vjust = -0.5, size = 5, family = "serif", color = "black") +
  scale_fill_manual(values = emotion_colors) +
  scale_y_continuous(labels = scales::comma, limits = c(0, 35000), breaks = seq(0, 35000, by = 5000)) +
  theme_minimal(base_family = "serif") +
  theme(
    plot.title = element_blank(),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_text(size = 12, color = "black"),
    axis.text.y = element_text(size = 12, color = "black"),
    legend.position = "none"
  )

# Function to compute emotion percentage by gender
calc_emotion_percentages <- function(subset_data, gender) {
  emotion_counts <- setNames(rep(0, length(emotion_categories)), emotion_categories) 
  gender_data <- subset_data %>% filter(Gender == gender)
  # Loop through emotion counts
  for (row in gender_data$dominant_emotions) {
    for (emotion in names(row)) {
      if (emotion %in% emotion_categories) {
        emotion_counts[emotion] <- emotion_counts[emotion] + row[[emotion]]
      }
    }
  }
  total_count <- sum(emotion_counts) # Compute total emotion count
  # Convert counts to percentages
  if (total_count > 0) {
    return((emotion_counts / total_count) * 100)
  } else {
    return(setNames(rep(0, length(emotion_categories)), emotion_categories))
  }
}

# Define the layout
par(mfrow = c(2, 2), mar = c(0, 3, 1, 3), family = "serif", cex.main = 0.8)

# Filter non-player characters
npc_df <- df %>%
  filter(Playability == "NPC")

# Apply the function
male_percents <- calc_emotion_percentages(npc_df, "Male")
female_percents <- calc_emotion_percentages(npc_df, "Female")

# Define ranges
max_min <- data.frame(
  anger = c(30, 0),
  disgust = c(30, 0),
  fear = c(30, 0),
  joy = c(30, 0),
  sadness = c(30, 0),
  surprise = c(30, 0)
)

# Create a dataframe from emotion percentages
radar_data <- data.frame(
  anger = c(male_percents["anger"], female_percents["anger"]),
  disgust = c(male_percents["disgust"], female_percents["disgust"]),
  fear = c(male_percents["fear"], female_percents["fear"]),
  joy = c(male_percents["joy"], female_percents["joy"]),
  sadness = c(male_percents["sadness"], female_percents["sadness"]),
  surprise = c(male_percents["surprise"], female_percents["surprise"])
)

# Combine ranges and emotion percentages
radar_data <- rbind(max_min, radar_data)

# Define colors for each gender
colors <- c("#004c6d", "#de425b")

# Create a radar chart for non-player characters
radarchart(
  radar_data,
  axistype = 1,
  seg = 3,
  pcol = colors,
  plty = 1,
  plwd = 2,
  pfcol = adjustcolor(colors, alpha.f = 0.5),
  cglty = "solid",
  cglwd = 0.5,
  cglcol = "gray",
  axislabcol = "black",
  title = "Non-Player Characters",
  centerzero = TRUE,
  vlcex = 0.8,
  caxislabels = c("0%", "10%", "20%", "30%"),
  calcex = 0.8
)

# Filter player characters
pc_df <- df %>%
  filter(Playability == "PC")

# Apply the function
male_percents <- calc_emotion_percentages(pc_df, "Male")
female_percents <- calc_emotion_percentages(pc_df, "Female")

# Define ranges
max_min <- data.frame(
  anger = c(30, 0),
  disgust = c(30, 0),
  fear = c(30, 0),
  joy = c(30, 0),
  sadness = c(30, 0),
  surprise = c(30, 0)
)

# Create a dataframe from emotion percentages
radar_data <- data.frame(
  anger = c(male_percents["anger"], female_percents["anger"]),
  disgust = c(male_percents["disgust"], female_percents["disgust"]),
  fear = c(male_percents["fear"], female_percents["fear"]),
  joy = c(male_percents["joy"], female_percents["joy"]),
  sadness = c(male_percents["sadness"], female_percents["sadness"]),
  surprise = c(male_percents["surprise"], female_percents["surprise"])
)

# Combine ranges and emotion percentages
radar_data <- rbind(max_min, radar_data)

# Define colors for each gender
colors <- c("#004c6d", "#de425b")

# Create a radar chart for player characters
radarchart(
  radar_data,
  axistype = 1,
  seg = 3,
  pcol = colors,
  plty = 1,
  plwd = 2,
  pfcol = adjustcolor(colors, alpha.f = 0.5),
  cglty = "solid",
  cglwd = 0.5,
  cglcol = "gray",
  axislabcol = "black",
  title = "Player Characters",
  centerzero = TRUE,
  vlcex = 0.8,
  caxislabels = c("0%", "10%", "20%", "30%"),
  calcex = 0.8
)

# Filter player characters in diverse lineups
diverse_pc_df <- df %>%
  filter(Title %in% c("Elder Scrolls Morrowind", "Elder Scrolls Oblivion", 
                      "Elder Scrolls Skyrim", "Final Fantasy VII Remake", 
                      "Final Fantasy X", "Final Fantasy XII", 
                      "Final Fantasy XIII", "Final Fantasy XIII-2", 
                      "Final Fantasy XIV", "Persona 3", 
                      "Persona 4", "Persona 5"),
         Playability == "PC")

# Apply the function
male_percents <- calc_emotion_percentages(diverse_pc_df , "Male")
female_percents <- calc_emotion_percentages(diverse_pc_df , "Female")

# Define ranges
max_min <- data.frame(
  anger = c(30, 0),
  disgust = c(30, 0),
  fear = c(30, 0),
  joy = c(30, 0),
  sadness = c(30, 0),
  surprise = c(30, 0)
)

# Create a dataframe from emotion percentages
radar_data <- data.frame(
  anger = c(male_percents["anger"], female_percents["anger"]),
  disgust = c(male_percents["disgust"], female_percents["disgust"]),
  fear = c(male_percents["fear"], female_percents["fear"]),
  joy = c(male_percents["joy"], female_percents["joy"]),
  sadness = c(male_percents["sadness"], female_percents["sadness"]),
  surprise = c(male_percents["surprise"], female_percents["surprise"])
)

# Combine ranges and emotion percentages
radar_data <- rbind(max_min, radar_data)

# Define colors for each gender
colors <- c("#004c6d", "#de425b")

# Create a radar chart for player characters in diverse lineups
radarchart(
  radar_data,
  axistype = 1,
  seg = 3,
  pcol = colors,
  plty = 1,
  plwd = 2,
  pfcol = adjustcolor(colors, alpha.f = 0.5),
  cglty = "solid",
  cglwd = 0.5,
  cglcol = "gray",
  axislabcol = "black",
  title = "Player Characters in Diverse Lineups",
  centerzero = TRUE,
  vlcex = 0.8,
  caxislabels = c("0%", "10%", "20%", "30%"),
  calcex = 0.8
)

# Filter neutral characters
neutral_df <- df %>%
  filter(Gender == "Neutral")

# Apply the function
neutral_percents <- calc_emotion_percentages(neutral_df, "Neutral")

# Define ranges
max_min <- data.frame(
  anger = c(30, 0),
  disgust = c(30, 0),
  fear = c(30, 0),
  joy = c(30, 0),
  sadness = c(30, 0),
  surprise = c(30, 0)
)

# Create a dataframe from emotion percentages
radar_data <- data.frame(
  anger = c(neutral_percents["anger"]),
  disgust = c(neutral_percents["disgust"]),
  fear = c(neutral_percents["fear"]),
  joy = c(neutral_percents["joy"]),
  sadness = c(neutral_percents["sadness"]),
  surprise = c(neutral_percents["surprise"])
)

# Combine ranges and emotion percentages
radar_data <- rbind(max_min, radar_data)

# Create a radar chart for neutral characters
radarchart(
  radar_data,
  axistype = 1,
  seg = 3,
  pcol = "#488f31",
  plty = 1,
  plwd = 2,
  pfcol = adjustcolor("#488f31", alpha.f = 0.5),
  cglty = "solid",
  cglwd = 0.5,
  cglcol = "gray",
  axislabcol = "black",
  title = "Neutral Characters",
  centerzero = TRUE,
  vlcex = 0.8,
  caxislabels = c("0%", "10%", "20%", "30%"),
  calcex = 0.8
)

# Add a legend
par(xpd = NA)
legend(
  x = -3.2,
  y = -1,
  legend = c("male", "female", "neutral"),
  col = c("#004c6d", "#de425b", "#488f31"),
  pch = 16,
  pt.cex = 1.2,
  bty = "n",
  cex = 1.2,
  horiz = TRUE
)

# Turn off plotting device
dev.off()

# Create a dataframe for non-player charatcers
npc_df <- df %>%
  filter(Gender %in% c("Male", "Female"), Playability == "NPC") %>%
  mutate(
    dominant_emotions = map(dominant_emotions, as.list),
    LineCount = map_dbl(dominant_emotions, ~ sum(as.numeric(.x[emotion_categories]), na.rm = TRUE))
  ) %>%
  unnest_wider(dominant_emotions) %>%
  pivot_longer(cols = all_of(emotion_categories),
               names_to = "emotion",
               values_to = "count") %>%
  filter(LineCount > 0)

# Factor character groups
npc_df <- npc_df %>%
  mutate(Gender = factor(Gender, levels = c("Male", "Female")))

# Run poisson regression on non-player characters 
npc_poisson_result <- npc_df %>%
  group_by(emotion) %>%
  group_split() %>%
  map_dfr(~ {
    model <- glm(count ~ Gender + offset(log(LineCount)), data = .x, family = poisson)
    tidy(model) %>% mutate(emotion = unique(.x$emotion))
  })

# Add rate ratios
npc_poisson_result <- npc_poisson_result %>% 
  mutate(ratio = exp(estimate)) %>%
  rename(gender = term, p = p.value) %>%                     
  select(-estimate, -std.error) %>%
  select(1, emotion, everything()) %>%
  mutate(gender = recode(gender,          
                         `(Intercept)` = "male",
                         `GenderFemale` = "female"))

# Display poisson regression result
print(npc_poisson_result)

# Create a dataframe for player charatcers
pc_df <- df %>%
  filter(Gender %in% c("Male", "Female"), Playability == "PC") %>%
  mutate(
    dominant_emotions = map(dominant_emotions, as.list),
    LineCount = map_dbl(dominant_emotions, ~ sum(as.numeric(.x[emotion_categories]), na.rm = TRUE))
  ) %>%
  unnest_wider(dominant_emotions) %>%
  pivot_longer(cols = c("anger", "disgust", "fear", "joy", "sadness", "surprise"),
               names_to = "emotion",
               values_to = "count") %>%
  filter(LineCount > 0)

# Factor character groups
pc_df <- pc_df %>%
  mutate(Gender = factor(Gender, levels = c("Male", "Female")))

# Run poisson regression on PC characters 
pc_poisson_result <- pc_df %>%
  group_by(emotion) %>%
  group_split() %>%
  map_dfr(~ {
    model <- glm(count ~ Gender + offset(log(LineCount)), data = .x, family = poisson)
    tidy(model) %>% mutate(emotion = unique(.x$emotion))
  })

# Add ratios
pc_poisson_result <- pc_poisson_result %>% 
  mutate(ratio = exp(estimate)) %>%
  rename(gender = term, p = p.value) %>%                     
  select(-estimate, -std.error) %>%
  select(1, emotion, everything()) %>%
  mutate(gender = recode(gender,          
                         `(Intercept)` = "male",
                         `GenderFemale` = "female"))

# Display poisson regression result
print(pc_poisson_result)

# Create a dataframe for player characters in diverse lineups
diverse_pc_df <- pc_df %>%
  filter(Title %in% c("Elder Scrolls Morrowind", "Elder Scrolls Oblivion", 
                      "Elder Scrolls Skyrim", "Final Fantasy VII Remake", 
                      "Final Fantasy X", "Final Fantasy XII", 
                      "Final Fantasy XIII", "Final Fantasy XIII-2", 
                      "Final Fantasy XIV", "Persona 3", 
                      "Persona 4", "Persona 5")
  )

# Factor character groups
diverse_pc_df <- diverse_pc_df %>%
  mutate(Gender = factor(Gender, levels = c("Male", "Female")))

# Run poisson regression on PC characters 
diverse_pc_poisson_result <- diverse_pc_df %>%
  group_by(emotion) %>%
  group_split() %>%
  map_dfr(~ {
    model <- glm(count ~ Gender + offset(log(LineCount)), data = .x, family = poisson)
    tidy(model) %>% mutate(emotion = unique(.x$emotion))
  })

# Add ratios
diverse_pc_poisson_result <- diverse_pc_poisson_result %>% 
  mutate(ratio = exp(estimate)) %>%
  rename(gender = term, p = p.value) %>%                     
  select(-estimate, -std.error) %>%
  select(1, emotion, everything()) %>%
  mutate(gender = recode(gender,          
                         `(Intercept)` = "male",
                         `GenderFemale` = "female"))

# Display poisson regression result
print(diverse_pc_poisson_result)

# Create variables for all character groups
all_df <- df %>%
  mutate(CharacterGroup = case_when(
    Gender == "Male" & Playability == "PC" ~ "male_pc",
    Gender == "Female" & Playability == "PC" ~ "female_pc",
    Gender == "Neutral" & Playability == "PC" ~ "neutral_pc",
    Gender == "Male" & Playability == "NPC" ~ "male_npc",
    Gender == "Female" & Playability == "NPC" ~ "female_npc",
    TRUE ~ NA_character_
  ))

# Create a dataframe for all character groups
all_df <- all_df %>%
  filter(!is.na(CharacterGroup)) %>%
  mutate(
    dominant_emotions = map(dominant_emotions, as.list),
    LineCount = map_dbl(dominant_emotions, ~ sum(as.numeric(.x[emotion_categories]), na.rm = TRUE))
  ) %>%
  unnest_wider(dominant_emotions) %>%
  pivot_longer(cols = c("anger", "disgust", "fear", "joy", "sadness", "surprise"),
               names_to = "emotion",
               values_to = "count") %>%
  filter(LineCount > 0)

# Factor character groups
all_df <- all_df %>%
  mutate(CharacterGroup = factor(CharacterGroup, levels = c("neutral_pc", "male_pc", "female_pc", "male_npc", "female_npc")))

# Run Poisson regression on all character groups
all_poisson_result <- all_df %>%
  group_by(emotion) %>%
  group_split() %>%
  map_dfr(~ {
    model <- glm(count ~ CharacterGroup + offset(log(LineCount)), data = .x, family = poisson)
    tidy(model) %>% mutate(emotion = unique(.x$emotion))
  })

# Add ratios
all_poisson_result <- all_poisson_result %>% 
  mutate(ratio = exp(estimate)) %>%
  rename(gender = term, p = p.value) %>%                     
  select(-estimate, -std.error) %>%
  select(1, emotion, everything()) %>%
  mutate(gender = recode(gender,          
                         `(Intercept)` = "male",
                         `CharacterGroupmale_pc` = "male pc",
                         `CharacterGroupfemale_pc` = "female pc",
                         `CharacterGroupmale_npc` = "male npc",
                         `CharacterGroupfemale_npc` = "female npc"))

# display poisson result
print(all_poisson_result, n = 30)

# Create a dataframe for group distance
distance_df <- all_df %>%
  group_by(CharacterGroup, emotion) %>%
  summarise(count = sum(count), total = sum(LineCount), .groups = "drop") %>%
  mutate(rate = count / total) %>%
  select(CharacterGroup, emotion, rate) %>%
  pivot_wider(names_from = emotion, values_from = rate)

# Compute euclidean distances
distance_matrix <- proxy::dist(distance_df[-1], method = "euclidean")

# Convert to a matrix
distance_matrix <- as.matrix(distance_matrix)

# Define character groups
groups <- c("neutral pc", "male pc", "female pc", "male npc", "female npc")

# Assign row and column names
rownames(distance_matrix) <- groups
colnames(distance_matrix) <- groups

# Display distance matrix
print(distance_matrix)