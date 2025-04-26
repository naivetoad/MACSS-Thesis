# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_xv/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Noctis",
    "Prompto",
    "Gladiolus",
    "Ignis",
    "Ardyn",
    "Cindy",
    "Aranea",
    "Iris",
    "Cor",
    "Vyv",
    "Dino",
    "Luna",
    "Cid",
    "Camelia",
    "Talcott",
    "Takka",
    "Sania",
    "Holly",
    "Dave",
    "Navyth",
    "Wiz",
    "Ravus",
    "Loqi",
    "Shiva",
    "Gentiana",
    "Verstael",
    "Gilgamesh",
    "Randolph",
    "Biggs",
    "Monica",
    "Weskham",
    "Coctura",
    "Ezma",
    "Regis",
    "Kimya",
    "Jared",
    "Maria",
    "Wedge",
    "Caligo",
    "Iedolas",
    "Bahamut",
    "Leviathan",
    "Tony",
    "Dustin",
    "Drautos",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Noctis"]["gender"] = "Male"
character_info["Prompto"]["gender"] = "Male"
character_info["Gladiolus"]["gender"] = "Male"
character_info["Ignis"]["gender"] = "Male"
character_info["Ardyn"]["gender"] = "Male"
character_info["Cindy"]["gender"] = "Female"
character_info["Aranea"]["gender"] = "Female"
character_info["Iris"]["gender"] = "Female"
character_info["Cor"]["gender"] = "Male"
character_info["Vyv"]["gender"] = "Male"
character_info["Dino"]["gender"] = "Male"
character_info["Luna"]["gender"] = "Female"
character_info["Cid"]["gender"] = "Male"
character_info["Camelia"]["gender"] = "Female"
character_info["Talcott"]["gender"] = "Male"
character_info["Takka"]["gender"] = "Male"
character_info["Sania"]["gender"] = "Female"
character_info["Holly"]["gender"] = "Female"
character_info["Dave"]["gender"] = "Male"
character_info["Navyth"]["gender"] = "Male"
character_info["Wiz"]["gender"] = "Male"
character_info["Ravus"]["gender"] = "Male"
character_info["Loqi"]["gender"] = "Male"
character_info["Shiva"]["gender"] = "Female"
character_info["Gentiana"]["gender"] = "Female"
character_info["Verstael"]["gender"] = "Male"
character_info["Gilgamesh"]["gender"] = "Male"
character_info["Randolph"]["gender"] = "Male"
character_info["Biggs"]["gender"] = "Male"
character_info["Monica"]["gender"] = "Female"
character_info["Weskham"]["gender"] = "Male"
character_info["Coctura"]["gender"] = "Female"
character_info["Ezma"]["gender"] = "Female"
character_info["Regis"]["gender"] = "Male"
character_info["Kimya"]["gender"] = "Female"
character_info["Jared"]["gender"] = "Male"
character_info["Maria"]["gender"] = "Female"
character_info["Wedge"]["gender"] = "Male"
character_info["Caligo"]["gender"] = "Male"
character_info["Iedolas"]["gender"] = "Male"
character_info["Bahamut"]["gender"] = "Male"
character_info["Leviathan"]["gender"] = "Female"
character_info["Tony"]["gender"] = "Male"
character_info["Dustin"]["gender"] = "Male"
character_info["Drautos"]["gender"] = "Male"

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
            "Title": "Final Fantasy XV",
            "Year": "2016",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Noctis": "Noctis Lucis Caelum",
    "Prompto": "Prompto Argentum",
    "Gladiolus": "Gladiolus Amicitia",
    "Ignis": "Ignis Scientia",
    "Ardyn": "Ardyn Izunia",
    "Cindy": "Cindy Aurum",
    "Aranea": "Aranea Highwind",
    "Iris": "Iris Amicitia",
    "Cor": "Cor Leonis",
    "Vyv": "Vyv Dorden",
    "Dino": "Dino Ghiranze",
    "Luna": "Lunafreya Nox Fleuret",
    "Cid": "Cid Sophiar",
    "Camelia": "Camelia Claustra",
    "Talcott": "Talcott Hester",
    "Takka": "Takka Bradham",
    "Sania": "Sania Yeagre",
    "Holly": "Holly Teulle",
    "Dave": "David Auburnbrie",
    "Navyth": "Navyth Arlund",
    "Wiz": "Wiz Forlane",
    "Ravus": "Ravus Nox Fleuret",
    "Loqi": "Loqi Tummelt",
    "Verstael": "Verstael Besithia",
    "Monica": "Monica Elshett",
    "Weskham": "Weskham Armaugh",
    "Coctura": "Coctura Arlund",
    "Ezma": "Ezma Auburnbrie",
    "Regis": "Regis Lucis Caelum",
    "Kimya": "Kimya Auburnbrie",
    "Jared": "Jared Hester",
    "Caligo": "Caligo Ulldor",
    "Iedolas": "Iedolas Aldercapt",
    "Dustin": "Dustin Ackers",
    "Drautos": "Titus Drautos",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Noctis Lucis Caelum",
    "Gladiolus Amicitia",
    "Prompto Argentum",
    "Ignis Scientia",
    "Ardyn Izunia",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_xv/data.csv", index=False)
