# Load required libraries
library(tidyverse)
library(broom)

# Load the dataset
df <- read_csv("data/liwc_data.csv", show_col_types = FALSE)

# Rename variables
df <- df %>%
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
         communication = comm
         )

# Define variables
liwc_categories <- c("cognitive processes", "insight", "causation", "discrepancy",
                     "tentativeness", "certitude", "differentiation", "affect",
                     "positive tone", "negative tone", "positive emotion", 
                     "negative emotion", "swear", "social behavior", 
                     "prosocial behavior", "politeness", "conflict", 
                     "moralization", "communication")

# Create a dataframe for player characters
pc_df <- df %>%
  filter(Playability == "PC", Gender %in% c("Male", "Female")) %>% 
  drop_na(any_of(liwc_categories))

# Run t-test on gender of player characters
pc_t_test_result <- map_dfr(liwc_categories, function(cat) {
  test <- t.test(pc_df[[cat]] ~ pc_df$Gender)
  tibble(
    category = cat,
    male_mean = mean(pc_df[[cat]][pc_df$Gender == "Male"], na.rm = TRUE),
    female_mean = mean(pc_df[[cat]][pc_df$Gender == "Female"], na.rm = TRUE),
    statistic = test$statistic,
    df = test$parameter,
    p = test$p.value
  )
})

# Display t-test result
print(pc_t_test_result)

# Create a dataframe for non-player characters
npc_df <- df %>%
  filter(Playability == "NPC", Gender %in% c("Male", "Female")) %>% 
  drop_na(any_of(liwc_categories))

# Run t-test on gender of non-player characters
npc_t_test_result <- map_dfr(liwc_categories, function(cat) {
  test <- t.test(npc_df[[cat]] ~ npc_df$Gender)
  tibble(
    category = cat,
    male_mean = mean(npc_df[[cat]][npc_df$Gender == "Male"], na.rm = TRUE),
    female_mean = mean(npc_df[[cat]][npc_df$Gender == "Female"], na.rm = TRUE),
    statistic = test$statistic,
    df = test$parameter,
    p = test$p.value
  )
})

# Display t-test result
print(npc_t_test_result)

# Create variables for all character groups
df <- df %>%
  mutate(CharacterType = case_when(
    Playability == "PC" & Gender == "Neutral" ~ "neutral_pc",
    Playability == "PC" & Gender == "Male" ~ "male_pc",
    Playability == "PC" & Gender == "Female" ~ "female_pc",
    Playability == "NPC" & Gender == "Male" ~ "male_npc",
    Playability == "NPC" & Gender == "Female" ~ "female_npc",
    Playability == "NPC" & Gender == "Neutral" ~ "neutral_npc",
    TRUE ~ NA_character_
  ),
  CharacterType = factor(CharacterType, levels = c("neutral_pc", "male_pc", "female_pc", "male_npc", "female_npc")))


# Run anova test on all character groups
anova_result <- map_dfr(liwc_categories, function(cat) {
  model <- aov(as.formula(paste0("`", cat, "` ~ CharacterType")), data = df)
  summary_out <- summary(model)[[1]]
  tibble(
    category = cat,
    statistic = summary_out$`F value`[1],
    df1 = summary_out$Df[1],
    df2 = summary_out$Df[2],
    p = summary_out$`Pr(>F)`[1]
  )
})

# Display anova result
print(anova_result)

# Filter significant categories
significant_cats <- anova_result %>%
  filter(p < 0.05) %>%
  pull(category)

# Reshape to long format
df <- df %>%
  pivot_longer(cols = all_of(liwc_categories), names_to = "category", values_to = "score") %>%
  filter(category %in% significant_cats) %>% 
  select(CharacterType, category, score)

# Run tukey test
tukey_result <- df %>%
  group_by(category) %>%
  group_map(~ {
    model <- aov(score ~ CharacterType, data = .x)
    tukey <- TukeyHSD(model)
    tidy_tukey <- as_tibble(tukey$CharacterType, rownames = "comparison")
    tidy_tukey$category <- unique(.y$category)
    tidy_tukey
  }) %>%
  bind_rows() %>%
  select(category, comparison, diff, `p adj`) %>%
  rename(difference = diff, p = "p adj")

# Display tukey test result
print(tukey_result, n = 60)

# Create a dataframe for group distance
distance_df <- tukey_result %>%
  mutate(
    group1 = sub("-.*", "", comparison),
    group2 = sub(".*-", "", comparison),
    distance = abs(difference)
  ) %>%
  select(category, group1, group2, distance)

# Function to create symmetric distance matrix from pairwise differences
build_distance_matrix <- function(df_cat) {
  groups <- unique(c(df_cat$group1, df_cat$group2))
  # Initialize square matrix
  mat <- matrix(0, nrow = length(groups), ncol = length(groups),
                dimnames = list(groups, groups))
  # Fill the matrix
  for (i in seq_len(nrow(df_cat))) {
    g1 <- df_cat$group1[i]
    g2 <- df_cat$group2[i]
    d  <- df_cat$distance[i]
    mat[g1, g2] <- d
    mat[g2, g1] <- d
  }
  as.data.frame(as.table(mat)) %>%
    rename(group1 = Var1, group2 = Var2, distance = Freq)
}

# Apply to each category
distance_df <- distance_df %>%
  group_by(category) %>%
  group_split() %>%
  map_dfr(~ build_distance_matrix(.x) %>% mutate(category = unique(.x$category)))

# Aggregate distances across all categories
distance_matrix <- distance_df %>%
  group_by(group1, group2) %>%
  summarise(
    avg_distance = mean(distance, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_wider(names_from = group2, values_from = avg_distance)

# Display distance matrix
print(distance_matrix)