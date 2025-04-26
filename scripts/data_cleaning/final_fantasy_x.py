# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_x/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Tidus",
    "Yuna",
    "Wakka",
    "Auron",
    "Rikku",
    "Lulu",
    "Jecht",
    "Kimahri",
    "Cid",
    "Seymour",
    "Belgemine",
    "Braska",
    "Luzzu",
    "Shelinda",
    "Datto",
    "Gatta",
    "O'aka",
    "Letty",
    "Rin",
    "Dona",
    "Maechen",
    "Jassu",
    "Keepa",
    "Lucil",
    "Botta",
    "Clasko",
    "Brother",
    "Tromell",
    "Elma",
    "Bobba",
    "Isaaru",
    "Biran",
    "Vilucha's son",
    "Kinoc",
    "Maroda",
    "Yenke",
    "Gramps",
    "Yunalesca",
    "Barthello",
    "Bickson",
    "Pacce",
    "Seymour's mother",
    "Mika",
    "Wantz",
    "Shaami",
    "Graav",
    "Tidus' Mom",
    "Vilucha",
    "Calli's Mother",
    "Blappa",
    "Larbeight",
    "Kelk",
    "Father Zuke",
    "Nimrook",
    "Eigaar",
    "Judda",
    "Lakkam",
    "Kyou",
    "Miyu",
    "Biggs",
    "Berrik",
    "Shuu",
    "Jumal",
    "Wedge",
    "Balgerda",
    "Doram",
    "Abus",
    "Nizarut",
    "Kulukan",
    "Kulukan's little sister",
    "Keyakku",
    "Auda Guado",
    "Yuma Guado",
    "Noy Guado",
    "Nedus",
    "Nhadala",
    "Jimma",
    "Deim",
    "Tatts",
    "Vuroja",
    "Giera Guado",
    "Nav Guado",
    "Calli",
    "Irga Ronso",
    "Kiyuri",
    "Mep",
    "Isken",
    "Linna",
    "Zazi Guado",
    "Pah Guado",
    "Zamzi Ronso",
    "Nuvy Ronso",
    "Basik Ronso",
    "Argai Ronso",
    "Gazna Ronso",
    "Borra",
    "Zalitz",
    "Zev Ronso",
    "Svanda",
    "Mifurey",
    "Jyscal",
    "Naida",
    "Ropp",
    "Zanar",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Tidus"]["gender"] = "Male"
character_info["Yuna"]["gender"] = "Female"
character_info["Wakka"]["gender"] = "Male"
character_info["Auron"]["gender"] = "Male"
character_info["Rikku"]["gender"] = "Male"
character_info["Lulu"]["gender"] = "Female"
character_info["Jecht"]["gender"] = "Male"
character_info["Kimahri"]["gender"] = "Male"
character_info["Cid"]["gender"] = "Male"
character_info["Seymour"]["gender"] = "Male"
character_info["Belgemine"]["gender"] = "Female"
character_info["Braska"]["gender"] = "Male"
character_info["Luzzu"]["gender"] = "Male"
character_info["Shelinda"]["gender"] = "Female"
character_info["Datto"]["gender"] = "Male"
character_info["Gatta"]["gender"] = "Male"
character_info["O'aka"]["gender"] = "Male"
character_info["Letty"]["gender"] = "Male"
character_info["Rin"]["gender"] = "Male"
character_info["Dona"]["gender"] = "Female"
character_info["Maechen"]["gender"] = "Male"
character_info["Jassu"]["gender"] = "Male"
character_info["Keepa"]["gender"] = "Male"
character_info["Lucil"]["gender"] = "Female"
character_info["Botta"]["gender"] = "Male"
character_info["Clasko"]["gender"] = "Male"
character_info["Brother"]["gender"] = "Male"
character_info["Tromell"]["gender"] = "Male"
character_info["Elma"]["gender"] = "Female"
character_info["Bobba"]["gender"] = "Male"
character_info["Isaaru"]["gender"] = "Male"
character_info["Biran"]["gender"] = "Male"
character_info["Vilucha's son"]["gender"] = "Male"
character_info["Kinoc"]["gender"] = "Male"
character_info["Maroda"]["gender"] = "Male"
character_info["Yenke"]["gender"] = "Male"
character_info["Gramps"]["gender"] = "Male"
character_info["Yunalesca"]["gender"] = "Female"
character_info["Barthello"]["gender"] = "Male"
character_info["Bickson"]["gender"] = "Male"
character_info["Pacce"]["gender"] = "Male"
character_info["Seymour's mother"]["gender"] = "Female"
character_info["Mika"]["gender"] = "Male"
character_info["Wantz"]["gender"] = "Male"
character_info["Shaami"]["gender"] = "Female"
character_info["Graav"]["gender"] = "Male"
character_info["Tidus' Mom"]["gender"] = "Female"
character_info["Vilucha"]["gender"] = "Female"
character_info["Calli's Mother"]["gender"] = "Female"
character_info["Blappa"]["gender"] = "Male"
character_info["Larbeight"]["gender"] = "Male"
character_info["Kelk"]["gender"] = "Male"
character_info["Father Zuke"]["gender"] = "Male"
character_info["Nimrook"]["gender"] = "Male"
character_info["Eigaar"]["gender"] = "Male"
character_info["Judda"]["gender"] = "Female"
character_info["Lakkam"]["gender"] = "Female"
character_info["Kyou"]["gender"] = "Male"
character_info["Miyu"]["gender"] = "Female"
character_info["Biggs"]["gender"] = "Male"
character_info["Berrik"]["gender"] = "Male"
character_info["Shuu"]["gender"] = "Female"
character_info["Jumal"]["gender"] = "Male"
character_info["Wedge"]["gender"] = "Male"
character_info["Balgerda"]["gender"] = "Female"
character_info["Doram"]["gender"] = "Female"
character_info["Abus"]["gender"] = "Male"
character_info["Nizarut"]["gender"] = "Male"
character_info["Kulukan"]["gender"] = "Female"
character_info["Kulukan's little sister"]["gender"] = "Female"
character_info["Keyakku"]["gender"] = "Male"
character_info["Auda Guado"]["gender"] = "Female"
character_info["Yuma Guado"]["gender"] = "Female"
character_info["Noy Guado"]["gender"] = "Male"
character_info["Nedus"]["gender"] = "Male"
character_info["Nhadala"]["gender"] = "Female"
character_info["Jimma"]["gender"] = "Male"
character_info["Deim"]["gender"] = "Female"
character_info["Tatts"]["gender"] = "Male"
character_info["Vuroja"]["gender"] = "Male"
character_info["Giera Guado"]["gender"] = "Male"
character_info["Nav Guado"]["gender"] = "Male"
character_info["Calli"]["gender"] = "Female"
character_info["Irga Ronso"]["gender"] = "Female"
character_info["Kiyuri"]["gender"] = "Female"
character_info["Mep"]["gender"] = "Male"
character_info["Isken"]["gender"] = "Male"
character_info["Linna"]["gender"] = "Female"
character_info["Zazi Guado"]["gender"] = "Male"
character_info["Pah Guado"]["gender"] = "Female"
character_info["Zamzi Ronso"]["gender"] = "Male"
character_info["Nuvy Ronso"]["gender"] = "Female"
character_info["Basik Ronso"]["gender"] = "Male"
character_info["Argai Ronso"]["gender"] = "Male"
character_info["Gazna Ronso"]["gender"] = "Male"
character_info["Borra"]["gender"] = "Male"
character_info["Zalitz"]["gender"] = "Male"
character_info["Zev Ronso"]["gender"] = "Male"
character_info["Svanda"]["gender"] = "Female"
character_info["Mifurey"]["gender"] = "Female"
character_info["Jyscal"]["gender"] = "Male"
character_info["Naida"]["gender"] = "Female"
character_info["Ropp"]["gender"] = "Male"
character_info["Zanar"]["gender"] = "Male"

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
            "Title": "Final Fantasy X",
            "Year": "2001",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Kimahri": "Kimahri Ronso",
    "Seymour": "Seymour Guado",
    "Braska": "Lord Braska",
    "Biran": "Biran Ronso",
    "Kinoc": "Wen Kinoc",
    "Yenke": "Yenke Ronso",
    "Vilucha's son": "Vilucha's Son",
    "Seymour's mother": "Seymour's Mother",
    "Mika": "Yo Mika",
    "Kelk": "Kelk Ronso",
    "Father Zuke": "Zuke",
    "Kulukan's little sister": "Kulukan's Sister",
    "Jyscal": "Jyscal Guado",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Tidus",
    "Auron",
    "Rikku",
    "Wakka",
    "Lulu",
    "Yuna",
    "Kimahri",
    "Seymour",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_x/data.csv", index=False)
