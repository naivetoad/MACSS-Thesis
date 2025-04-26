# Load required libraries
import ast
import pandas as pd
import re
import string

# Create a list to store folder names
folders = [
    "death_stranding",
    "disco_elysium",
    "elder_scrolls_morrowind",
    "elder_scrolls_oblivion",
    "elder_scrolls_skyrim",
    "final_fantasy_vii_Remake",
    "final_fantasy_x",
    "final_fantasy_xii",
    "final_fantasy_xiii",
    "final_fantasy_xiii_2",
    "final_fantasy_xiv",
    "final_fantasy_xv",
    "hades",
    "horizon_zero_dawn",
    "horizon_forbidden_west",
    "persona_3",
    "persona_4",
    "persona_5",
]

# Load and merge the datasets
concatenated_df = pd.DataFrame()
for folder in folders:
    df = pd.read_csv(f"data/{folder}/data.csv",converters={"Dialogues": ast.literal_eval})
    concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)

# Remove substrings in parentheses
def remove_parentheses(dialogues):
    return [re.sub(r'\(.*?\)', '', dialogue).strip() for dialogue in dialogues]
concatenated_df["Dialogues"] = concatenated_df["Dialogues"].apply(remove_parentheses)

# Filter out punctuation marks
def remove_punctuations(dialogues):
    return [d for d in dialogues if d.strip(string.punctuation)]
concatenated_df["Dialogues"] = concatenated_df["Dialogues"].apply(remove_punctuations)

# Remove characters without dialogues
concatenated_df = concatenated_df[concatenated_df['Dialogues'].map(len) > 0]

# Compute number of lines for each character
concatenated_df = concatenated_df.assign(Lines=concatenated_df["Dialogues"].apply(len))

# Compute number of sentences for each character
concatenated_df["Sentences"] = concatenated_df["Dialogues"].apply(lambda dialogues: sum(len(re.findall(r"\.{3}|\.{2}|[.!?]", dialogue)) for dialogue in dialogues))

# Compute number of words for each character
concatenated_df["Words"] = concatenated_df["Dialogues"].apply(lambda x: sum(len(dialogue.split()) for dialogue in x))

# Save the dataframe
concatenated_df.to_csv('data/all/dialogue_data.csv', index=False)
