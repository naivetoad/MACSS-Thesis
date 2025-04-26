# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/death_stranding/data.json", "r") as file:
    data = json.load(file)

# Create a list to store character names
characters = [
    "Sam",
    "Deadman",
    "Die-Hardman",
    "Fragile",
    "Mama",
    "Heartman",
    "Amelie",
    "Bridget",
    "Higgs",
    "Clifford Unger",
    "Lockne",
    "John",
    "Igor",
    "Junk Dealer",
    "Junk Dealer's Girlfriend",
    "Mountaineer",
    "Combat Veteran",
    "Paleontologist",
    "Doctor",
    "Young Sam",
    "Old Bridget",
    "Photographer",
    "Roboticist",
    "Evo-devo Biologist",
    "Spiritualist",
    "Young Bridget",
    "Lisa",
    "Geologist",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Sam"]["gender"] = "Male"
character_info["Deadman"]["gender"] = "Male"
character_info["Die-Hardman"]["gender"] = "Male"
character_info["Fragile"]["gender"] = "Female"
character_info["Mama"]["gender"] = "Female"
character_info["Heartman"]["gender"] = "Male"
character_info["Amelie"]["gender"] = "Female"
character_info["Bridget"]["gender"] = "Female"
character_info["Higgs"]["gender"] = "Male"
character_info["Clifford Unger"]["gender"] = "Male"
character_info["Lockne"]["gender"] = "Female"
character_info["John"]["gender"] = "Male"
character_info["Igor"]["gender"] = "Male"
character_info["Junk Dealer"]["gender"] = "Male"
character_info["Junk Dealer's Girlfriend"]["gender"] = "Female"
character_info["Mountaineer"]["gender"] = "Male"
character_info["Combat Veteran"]["gender"] = "Male"
character_info["Paleontologist"]["gender"] = "Male"
character_info["Doctor"]["gender"] = "Male"
character_info["Young Sam"]["gender"] = "Male"
character_info["Old Bridget"]["gender"] = "Female"
character_info["Photographer"]["gender"] = "Female"
character_info["Roboticist"]["gender"] = "Female"
character_info["Evo-devo Biologist"]["gender"] = "Female"
character_info["Spiritualist"]["gender"] = "Female"
character_info["Young Bridget"]["gender"] = "Female"
character_info["Lisa"]["gender"] = "Female"
character_info["Geologist"]["gender"] = "Male"

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
            "Title": "Death Stranding",
            "Year": "2019",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Bridget": "Bridget Strand",
    "Higgs": "Higgs Monaghan",
    "Clifford Unger": "Cliff Unger",
    "John": "Die-Hardman",
    "Igor": "Igor Frank",
    "Junk Dealer's Girlfriend": "Chiral Artist",
    "Combat Veteran": "Cliff Unger",
    "Paleontologist": "Edward Wallace",
    "Young Sam": "Sam",
    "Old Bridget": "Bridget Strand",
    "Evo-devo Biologist": "Mary Dickens",
    "Young Bridget": "Bridget Strand",
    "Lisa": "Lisa Unger",
    "Geologist": "Thomas Hucksley",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable charaters
PC = ["Sam"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/death_stranding/data.csv", index=False)
