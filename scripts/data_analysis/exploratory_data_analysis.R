# Load required library
library(tidyverse)

# Load the dataset
df <- read_csv("data/all/dialogue_data.csv", show_col_types = FALSE)

# Summarize statistics
summary_df <- df %>%
  group_by(Title, Year, Country) %>%
  summarise(
    Characters = n(),
    Lines = sum(Lines),
    Sentences = sum(Sentences),
    Words = sum(Words),
    .groups = "drop"
  )

# Display summary statistics
print(summary_df, n = 18)

# Compute words per sentence and words per line
df <- df %>%
  mutate(
    WordsPerSentence = Words / Sentences,
    WordsPerLine = Words / Lines
  )

# Define variables
vars_to_summarize <- c("Words", "Sentences", "Lines", "WordsPerSentence", "WordsPerLine")

# Function to compute descriptive statistics
compute_stats <- function(data, var) {
  x <- data[[var]]
  tibble(
    Variable = var,
    Mean = mean(x, na.rm = TRUE),
    SD = sd(x, na.rm = TRUE)
  )
}

# Apply the function to the dataset
descriptive_df <- df %>%
  group_by(Playability, Gender) %>%
  group_map(
    .f = function(data, keys) {
      map_dfr(vars_to_summarize, ~ compute_stats(data, .x)) %>%
        mutate(Playability = keys$Playability, Gender = keys$Gender)
    }
  ) %>%
  bind_rows()

# Display descriptive statistics
print(descriptive_df, n = 25)

# Run t-test on playability
playability_t_test_result <- map_dfr(vars_to_summarize, function(var) {
  test <- t.test(df[[var]] ~ df$Playability)
  tibble(
    variable = var,
    pc_mean = mean(df[[var]][df$Playability == "PC"], na.rm = TRUE),
    npc_mean = mean(df[[var]][df$Playability == "NPC"], na.rm = TRUE),
    statistic = test$statistic,
    df = test$parameter,
    p = test$p.value
  )
})

# Display t-test result
print(playability_t_test_result)

# Run t-test on gender
gender_t_test_result <- df %>%
  filter(Gender %in% c("Male", "Female")) %>%
  { 
    data_filtered <- .
    map_dfr(vars_to_summarize, function(var) {
      test <- t.test(data_filtered[[var]] ~ data_filtered$Gender)
      tibble(
        variable = var,
        male_mean = mean(data_filtered[[var]][data_filtered$Gender == "Male"], na.rm = TRUE),
        female_mean = mean(data_filtered[[var]][data_filtered$Gender == "Female"], na.rm = TRUE),
        statistic = test$statistic,
        df = test$parameter,
        p = test$p.value
      )
    })
  }

# Display t-test result
print(gender_t_test_result)

# Filter player characters
pc_df <- df %>%
  filter(Playability == "PC", Gender %in% c("Male", "Female", "Neutral")) %>%
  drop_na(any_of(vars_to_summarize))

# Run anova test on gender of player characters
anova_result <- map_dfr(vars_to_summarize, function(var) {
  model <- aov(as.formula(paste(var, "~ Gender")), data = pc_df)
  summary_out <- summary(model)[[1]]
  tibble(
    variable = var,
    statistic = summary_out$`F value`[1],
    df1 = summary_out$Df[1],
    df2 = summary_out$Df[2],
    p = summary_out$`Pr(>F)`[1]
  )
})

# Display anova result
print(anova_result)

# Filter non-player characters
npc_df <- df %>%
  filter(Playability == "NPC", Gender %in% c("Male", "Female"))

# Run t-test on gender of non-player characters
npc_t_test_result <- map_dfr(vars_to_summarize, function(var) {
  test <- t.test(npc_df[[var]] ~ npc_df$Gender)
  tibble(
    variable = var,
    male_mean = mean(npc_df[[var]][npc_df$Gender == "Male"], na.rm = TRUE),
    female_mean = mean(npc_df[[var]][npc_df$Gender == "Female"], na.rm = TRUE),
    statistic = test$statistic,
    df = test$parameter,
    p = test$p.value
  )
})

# Display t-test result
print(npc_t_test_result)

# Compute counts of player characters
male_pc <- sum(df$Gender == "Male" & df$Playability == "PC")
female_pc <- sum(df$Gender == "Female" & df$Playability == "PC")
neutral_pc <- sum(df$Gender == "Neutral" & df$Playability == "PC")
total_pc <- male_pc + female_pc + (neutral_pc * 2)

# Run proportion test on player characters
test <- prop.test(c(male_pc + neutral_pc, female_pc + neutral_pc), c(total_pc, total_pc))

# Create a dataframe from test result
pc_proportion_result <- data.frame(
  male_proportion = test$estimate[1],
  female_proportion = test$estimate[2],
  statistic = test$statistic,
  df = test$parameter,
  p = test$p.value
)

# Display proportion test result
print(pc_proportion_result)

# Compute NPC counts
male_npc <- sum(df$Gender == "Male" & df$Playability == "NPC")
female_npc <- sum(df$Gender == "Female" & df$Playability == "NPC")
total_npc <- female_npc + male_npc

# Run proportion test on non-player characters
test <- prop.test(c(male_npc, female_npc), c(total_npc, total_npc))

# Create a datafraem from test result
npc_proportion_result <- data.frame(
  male_proportion = test$estimate[1],
  female_proportion = test$estimate[2],
  statistic = test$statistic,
  df = test$parameter,
  p = test$p.value
)

# Display proportion test result
print(npc_proportion_result)

# Compute percentage of female words by game
plot_df <- df %>%
  filter(Gender != "Neutral") %>%
  group_by(Title, Year, Country) %>%
  summarize(
    total_words = sum(Words),
    female_words = sum(ifelse(Gender == "Female", Words, 0)),
    .groups = "drop"
  ) %>%
  mutate(female_percentage = female_words / total_words)

# Create a scatter plot on the percentage of female words by game
ggplot(plot_df, aes(x = Year, y = female_percentage, color = Country, size = female_words)) +
  geom_point(alpha = 0.8) +
  geom_text(aes(label = Title), color = "black", size = 3, family = "serif") +
  scale_color_manual(values = c("Japan" = "#2ca02c", "UK" = "#ff7f0e", "US" = "#1f77b4", "Netherlands" = "#d62728")) +
  scale_size_continuous(range = c(5, 25), guide = "none") +
  scale_x_continuous(limits = c(2000, 2025)) +
  scale_y_continuous(labels = scales::percent_format(), limits = c(0, 0.8)) +
  theme_minimal() +
  theme(
    plot.title = element_blank(),
    axis.title = element_blank(),
    axis.text = element_text(family = "serif", size = 10, color = "black"),
    legend.title = element_blank(),
    legend.text = element_text(family = "serif", size = 12, color = "black"),
    legend.position = "bottom"
  )