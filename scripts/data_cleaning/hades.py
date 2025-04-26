# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/hades/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Zagreus",
    "Hades",
    "Megaera",
    "Thanatos",
    "Theseus",
    "Skelly",
    "Dusa",
    "Alecto",
    "Sisyphus",
    "Nyx",
    "Patroclus",
    "Achilles",
    "Asterius",
    "Persephone",
    "Hypnos",
    "Orpheus",
    "Eurydice",
    "Tisiphone",
    "Hermes",
    "Poseidon",
    "Ares",
    "Demeter",
    "Artemis",
    "Athena",
    "Zeus",
    "Dionysus",
    "Aphrodite",
    "Charon",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]['dialogues'] = []

# Label gender for each character
character_info["Zagreus"]["gender"] = "Male"
character_info["Hades"]["gender"] = "Male"
character_info["Megaera"]["gender"] = "Female"
character_info["Thanatos"]["gender"] = "Male"
character_info["Theseus"]["gender"] = "Male"
character_info["Skelly"]["gender"] = "Male"
character_info["Dusa"]["gender"] = "Female"
character_info["Alecto"]["gender"] = "Female"
character_info["Sisyphus"]["gender"] = "Male"
character_info["Nyx"]["gender"] = "Female"
character_info["Patroclus"]["gender"] = "Male"
character_info["Achilles"]["gender"] = "Male"
character_info["Asterius"]["gender"] = "Male"
character_info["Persephone"]["gender"] = "Female"
character_info["Hypnos"]["gender"] = "Male"
character_info["Orpheus"]["gender"] = "Male"
character_info["Eurydice"]["gender"] = "Female"
character_info["Tisiphone"]["gender"] = "Female"
character_info["Hermes"]["gender"] = "Male"
character_info["Poseidon"]["gender"] = "Male"
character_info["Ares"]["gender"] = "Male"
character_info["Demeter"]["gender"] = "Female"
character_info["Artemis"]["gender"] = "Female"
character_info["Athena"]["gender"] = "Female"
character_info["Zeus"]["gender"] = "Male"
character_info["Dionysus"]["gender"] = "Male"
character_info["Aphrodite"]["gender"] = "Female"
character_info["Charon"]["gender"] = "Male"

# Function to extract dialogues
def extract_dialogue(data, character_info):
    def parse_entry(entry): 
        if isinstance(entry, dict): # Check for dictionary items
            if "CHOICE" in entry: # Check for choice items
                for branch in entry["CHOICE"]:
                    parse_entry(branch)
            else: # Check for non-choice items
                for key, value in entry.items():
                    if key in character_info:
                        if value.strip().endswith(('.', '?', '!')):
                            character_info[key]["dialogues"].append(value)
        elif isinstance(entry, list): # Check for list items
            for sub_entry in entry:
                parse_entry(sub_entry)
    for item in data["text"]:
        parse_entry(item)
    return character_info

# Apply the function to the dataset
character_info = extract_dialogue(data, character_info)

# Create a dataframe from character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Hades",
            "Year": "2020",
            "Country": "US",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a list to store playable characters
PC = ["Zagreus"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv('../../data/hades/data.csv', index=False)
