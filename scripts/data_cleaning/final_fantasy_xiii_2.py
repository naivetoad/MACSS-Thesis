# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_xiii_2/data.json", "r") as file:
    data = json.load(file)

# Initiate a list to store characters
characters = [
    "Serah",
    "Noel",
    "Mog",
    "Hope",
    "Snow",
    "Caius",
    "Alyssa",
    "Lightning",
    "Yeul",
    "Maqui",
    "Gadot",
    "Chocolina",
    "Yuj",
    "Lebreau",
    "Tipur",
    "Myta",
    "Vanille",
    "Captain Cryptic",
    "Rhett",
    "Sazh",
    "Torreno",
    "Baxter",
    "Falcon",
    "Alyssa's Duplicate",
    "Raymond",
    "Lex",
    "Lester",
    "Jed",
    "Morris",
    "Pat",
    "Dr. M",
    "Brant",
    "Brenda",
    "Nell",
    "Ronan",
    "Sergeant Blitz",
    "Jonah",
    "Marlow",
    "Duncan",
    "Shannon",
    "Cole",
    "Cordelia",
    "Chester",
    "Fang",
    "Ray",
    "Arbiter of Time",
    "Bridget",
    "Uma",
    "Thurston",
    "Dajh",
    "Walter",
    "Thorne",
    "Paddra Nsu-Yeul",
    "Catlin",
    "Thunder",
    "Millie",
]

# Initialize a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Serah"]["gender"] = "Female"
character_info["Noel"]["gender"] = "Male"
character_info["Mog"]["gender"] = "Male"
character_info["Hope"]["gender"] = "Male"
character_info["Snow"]["gender"] = "Male"
character_info["Caius"]["gender"] = "Male"
character_info["Alyssa"]["gender"] = "Female"
character_info["Lightning"]["gender"] = "Female"
character_info["Yeul"]["gender"] = "Female"
character_info["Maqui"]["gender"] = "Male"
character_info["Gadot"]["gender"] = "Male"
character_info["Chocolina"]["gender"] = "Female"
character_info["Yuj"]["gender"] = "Male"
character_info["Lebreau"]["gender"] = "Female"
character_info["Tipur"]["gender"] = "Male"
character_info["Myta"]["gender"] = "Female"
character_info["Vanille"]["gender"] = "Female"
character_info["Captain Cryptic"]["gender"] = "Male"
character_info["Rhett"]["gender"] = "Male"
character_info["Sazh"]["gender"] = "Male"
character_info["Torreno"]["gender"] = "Male"
character_info["Baxter"]["gender"] = "Male"
character_info["Falcon"]["gender"] = "Male"
character_info["Alyssa's Duplicate"]["gender"] = "Female"
character_info["Raymond"]["gender"] = "Male"
character_info["Lex"]["gender"] = "Male"
character_info["Lester"]["gender"] = "Male"
character_info["Jed"]["gender"] = "Male"
character_info["Morris"]["gender"] = "Male"
character_info["Pat"]["gender"] = "Female"
character_info["Dr. M"]["gender"] = "Male"
character_info["Brant"]["gender"] = "Male"
character_info["Brenda"]["gender"] = "Female"
character_info["Nell"]["gender"] = "Female"
character_info["Ronan"]["gender"] = "Male"
character_info["Sergeant Blitz"]["gender"] = "Male"
character_info["Jonah"]["gender"] = "Male"
character_info["Marlow"]["gender"] = "Male"
character_info["Duncan"]["gender"] = "Male"
character_info["Shannon"]["gender"] = "Female"
character_info["Cole"]["gender"] = "Male"
character_info["Cordelia"]["gender"] = "Female"
character_info["Chester"]["gender"] = "Male"
character_info["Fang"]["gender"] = "Female"
character_info["Ray"]["gender"] = "Male"
character_info["Arbiter of Time"]["gender"] = "Male"
character_info["Bridget"]["gender"] = "Female"
character_info["Uma"]["gender"] = "Female"
character_info["Thurston"]["gender"] = "Male"
character_info["Dajh"]["gender"] = "Male"
character_info["Walter"]["gender"] = "Male"
character_info["Thorne"]["gender"] = "Male"
character_info["Paddra Nsu-Yeul"]["gender"] = "Female"
character_info["Catlin"]["gender"] = "Female"
character_info["Thunder"]["gender"] = "Male"
character_info["Millie"]["gender"] = "Female"

# Function to extract dialogues from data recursively
def extract_dialogue(data, character_info):
    def parse_entry(entry):
        # Check for dictionary items
        if isinstance(entry, dict):
            # Check for choice items
            if "CHOICE" in entry:
                for branch in entry["CHOICE"]:
                    parse_entry(branch)
            # Check for non-choice items
            else:
                for key, value in entry.items():
                    if key in character_info:
                        if value.strip().endswith(('.', '?', '!')):
                            character_info[key]["dialogues"].append(value)
        # Check for list items
        elif isinstance(entry, list):
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
            "Title": "Final Fantasy XIII-2",
            "Year": "2011",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Initiate a dictionary to map aliases to real names
aliases = {
    "Serah": "Serah Farron",
    "Noel": "Noel Kreiss",
    "Hope": "Hope Estheim",
    "Snow": "Snow Villiers",
    "Caius": "Caius Ballad",
    "Alyssa": "Alyssa Zaidelle",
    "Yeul": "Paddra Nsu-Yeul",
    "Vanille": "Oerba Dia Vanille",
    "Captain Cryptic": "Amodar",
    "Sazh": "Sazh Katzroy",
    "Alyssa's Duplicate": "Alyssa Zaidelle",
    "Thurston": "Thursten",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of the same character
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Initiate a list to store playable characters
PC = [
    "Serah Farron",
    "Noel Kreiss",
    "Lightning",
    "Sazh Katzroy",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_xiii_2/data.csv", index=False)
