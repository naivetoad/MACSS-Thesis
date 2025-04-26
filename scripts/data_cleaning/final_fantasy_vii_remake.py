# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_vii_remake/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Cloud",
    "Barret",
    "Tifa",
    "Aerith",
    "Yuffie",
    "Jessie",
    "Biggs",
    "Wedge",
    "Johnny",
    "Sonon",
    "Madam M",
    "Red XIII",
    "Kotch",
    "Reno",
    "Leslie",
    "Heidegger",
    "Scotch",
    "Chadley",
    "Sam",
    "Marle",
    "Nayo",
    "Scarlet",
    "Elmyra",
    "Sephiroth",
    "Mireille",
    "Don Corneo",
    "Hojo",
    "Wymer",
    "President Shinra",
    "Rude",
    "Jules",
    "Roche",
    "Betty",
    "Kyrie",
    "Marlene",
    "Damon",
    "Zhijie",
    "Andrea",
    "Oates",
    "Tseng",
    "Ms. Folia",
    "Nero",
    "Jay",
    "Beck",
    "Shinra Middle Manager",
    "Domino",
    "Ronnie",
    "Old Snapper",
    "Polk",
    "Reeve",
    "Housemother",
    "Billy Bob",
    "Rufus",
    "Gwen",
    "Zack",
    "Hart",
    "Johnny's father",
    "Butch",
    "Burke",
    "Moggie",
    "Katie",
    "Weiss",
    "Jessie'S Mom",
    "Palmer",
    "Beastmaster",
    "Sarah",
    "Narjin",
    "Claudia",
    "Betty's Dad",
    "Chocobo Bill",
    "Leslie'S Fiancée",
    "Marco",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]['dialogues'] = []

# Label gender for each character
character_info["Cloud"]["gender"] = "Male"
character_info["Barret"]["gender"] = "Male"
character_info["Tifa"]["gender"] = "Female"
character_info["Aerith"]["gender"] = "Female"
character_info["Yuffie"]["gender"] = "Female"
character_info["Jessie"]["gender"] = "Female"
character_info["Biggs"]["gender"] = "Male"
character_info["Wedge"]["gender"] = "Male"
character_info["Johnny"]["gender"] = "Male"
character_info["Sonon"]["gender"] = "Male"
character_info["Madam M"]["gender"] = "Female"
character_info["Red XIII"]["gender"] = "Male"
character_info["Kotch"]["gender"] = "Male"
character_info["Reno"]["gender"] = "Male"
character_info["Leslie"]["gender"] = "Male"
character_info["Heidegger"]["gender"] = "Male"
character_info["Scotch"]["gender"] = "Male"
character_info["Chadley"]["gender"] = "Male"
character_info["Sam"]["gender"] = "Male"
character_info["Marle"]["gender"] = "Female"
character_info["Nayo"]["gender"] = "Female"
character_info["Scarlet"]["gender"] = "Female"
character_info["Elmyra"]["gender"] = "Female"
character_info["Sephiroth"]["gender"] = "Male"
character_info["Mireille"]["gender"] = "Female"
character_info["Don Corneo"]["gender"] = "Male"
character_info["Hojo"]["gender"] = "Male"
character_info["Wymer"]["gender"] = "Male"
character_info["President Shinra"]["gender"] = "Male"
character_info["Rude"]["gender"] = "Male"
character_info["Jules"]["gender"] = "Male"
character_info["Roche"]["gender"] = "Male"
character_info["Betty"]["gender"] = "Female"
character_info["Kyrie"]["gender"] = "Female"
character_info["Marlene"]["gender"] = "Female"
character_info["Damon"]["gender"] = "Male"
character_info["Zhijie"]["gender"] = "Male"
character_info["Andrea"]["gender"] = "Male"
character_info["Oates"]["gender"] = "Male"
character_info["Tseng"]["gender"] = "Male"
character_info["Ms. Folia"]["gender"] = "Female"
character_info["Nero"]["gender"] = "Male"
character_info["Jay"]["gender"] = "Male"
character_info["Beck"]["gender"] = "Male"
character_info["Shinra Middle Manager"]["gender"] = "Male"
character_info["Domino"]["gender"] = "Male"
character_info["Ronnie"]["gender"] = "Male"
character_info["Old Snapper"]["gender"] = "Male"
character_info["Polk"]["gender"] = "Male"
character_info["Reeve"]["gender"] = "Male"
character_info["Housemother"]["gender"] = "Female"
character_info["Billy Bob"]["gender"] = "Male"
character_info["Rufus"]["gender"] = "Male"
character_info["Gwen"]["gender"] = "Female"
character_info["Zack"]["gender"] = "Male"
character_info["Hart"]["gender"] = "Male"
character_info["Johnny's father"]["gender"] = "Male"
character_info["Butch"]["gender"] = "Male"
character_info["Burke"]["gender"] = "Male"
character_info["Moggie"]["gender"] = "Male"
character_info["Katie"]["gender"] = "Female"
character_info["Weiss"]["gender"] = "Male"
character_info["Jessie'S Mom"]["gender"] = "Female"
character_info["Palmer"]["gender"] = "Male"
character_info["Beastmaster"]["gender"] = "Male"
character_info["Sarah"]["gender"] = "Female"
character_info["Narjin"]["gender"] = "Male"
character_info["Claudia"]["gender"] = "Female"
character_info["Betty's Dad"]["gender"] = "Male"
character_info["Chocobo Bill"]["gender"] = "Male"
character_info["Leslie'S Fiancée"]["gender"] = "Female"
character_info["Marco"]["gender"] = "Male"

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
            "Title": "Final Fantasy VII Remake",
            "Year": "2020",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Cloud": "Cloud Strife",
    "Barret": "Barret Wallace",
    "Tifa": "Tifa Lockhart",
    "Aerith": "Aerith Gainsborough",
    "Yuffie": "Yuffie Kisaragi",
    "Jessie": "Jessie Rasberry",
    "Sonon": "Sonon Kusakabe",
    "Leslie": "Leslie Kyle",
    "Sam": "Chocobo Sam",
    "Elmyra": "Elmyra Gainsborough",
    "Mireille": "Mireille Dudley",
    "Hojo": "Professor Hojo",
    "Kyrie": "Kyrie Canaan",
    "Marlene": "Marlene Wallace",
    "Andrea": "Andrea Rhodea",
    "Nero": "Nero the Sable",
    "Reeve": "Reeve Tuesti",
    "Rufus": "Rufus Shinra",
    "Zack": "Zack Fair",
    "Johnny's father": "Johnny's Father",
    "Jessie'S Mom": "Jessie's Mother",
    "Claudia": "Claudia Strife",
    "Betty's Dad": "Betty's Father",
    "Leslie'S Fiancée": "Merle",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Cloud Strife",
    "Barret Wallace",
    "Tifa Lockhart",
    "Aerith Gainsborough",
    "Yuffie Kisaragi",
    "Sonon Kusakabe",
    "Red XIII",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv('data/final_fantasy_vii_remake/data.csv', index=False)
