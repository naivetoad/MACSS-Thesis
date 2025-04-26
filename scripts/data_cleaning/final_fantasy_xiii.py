# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_xiii/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Lightning",
    "Vanille",
    "Sazh",
    "Snow",
    "Hope",
    "Fang",
    "Galenth",
    "Cid",
    "Serah",
    "Yaag",
    "Jihl",
    "Gadot",
    "Yuj",
    "Maqui",
    "Nora",
    "Dajh",
    "Lebreau",
    "Amodar",
    "Titan",
    "Rygdea",
    "Barthandelus",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Lightning"]["gender"] = "Female"
character_info["Vanille"]["gender"] = "Female"
character_info["Sazh"]["gender"] = "Male"
character_info["Snow"]["gender"] = "Male"
character_info["Hope"]["gender"] = "Male"
character_info["Fang"]["gender"] = "Female"
character_info["Galenth"]["gender"] = "Male"
character_info["Cid"]["gender"] = "Male"
character_info["Serah"]["gender"] = "Female"
character_info["Yaag"]["gender"] = "Male"
character_info["Jihl"]["gender"] = "Female"
character_info["Gadot"]["gender"] = "Male"
character_info["Yuj"]["gender"] = "Male"
character_info["Maqui"]["gender"] = "Male"
character_info["Nora"]["gender"] = "Female"
character_info["Dajh"]["gender"] = "Male"
character_info["Lebreau"]["gender"] = "Female"
character_info["Amodar"]["gender"] = "Male"
character_info["Titan"]["gender"] = "Male"
character_info["Rygdea"]["gender"] = "Male"
character_info["Barthandelus"]["gender"] = "Male"

# Extract dialogues from the dataset
for item in data["text"]:
    key, value = next(iter(item.items()))
    if key in character_info:
        if value.strip().endswith(('.', '?', '!')):
            character_info[key]["dialogues"].append(value)

# Create a dataframe from character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Final Fantasy XIII",
            "Year": "2009",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Vanille": "Oerba Dia Vanille",
    "Sazh": "Sazh Katzroy",
    "Snow": "Snow Villiers",
    "Hope": "Hope Estheim",
    "Fang": "Oerba Yun Fang",
    "Galenth": "Galenth Dysley",
    "Cid": "Cid Raines",
    "Serah": "Serah Farron",
    "Yaag": "Yaag Rosch",
    "Jihl": "Jihl Nabaat",
    "Nora": "Nora Estheim",
    "Dajh": "Dajh Katzroy",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Lightning",
    "Sazh Katzroy",
    "Snow Villiers",
    "Oerba Dia Vanille",
    "Hope Estheim",
    "Oerba Yun Fang",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_xiii/data.csv", index=False)
