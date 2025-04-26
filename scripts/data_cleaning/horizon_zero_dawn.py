# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/horizon_zero_dawn/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Aloy",
    "Sylens",
    "Erend",
    "Rost",
    "Elisabet Sobeck",
    "Teersa",
    "Varl",
    "Ted Faro",
    "Olin",
    "Avad",
    "Teb",
    "Vanasha",
    "Sona",
    "GAIA",
    "Helis",
    "Uthid",
    "Karst",
    "General Herres",
    "HADES",
    "Resh",
    "Nora Keeper",
    "Marea",
    "Travis Tate",
    "Janeva",
    "Lansra",
    "Blameless Marad",
    "Balahn",
    "Vala",
    "Bast",
    "Charles Ronson",
    "Dervahl",
    "Margo Shěn",
    "Jezza",
    "Bahavas",
    "Christina Hsu-Vhey",
    "Guliyev",
    "Patrick Brochard-Klein",
    "Three-Toed Huadiv",
    "Murell",
    "Ron Felder",
    "Susanne Alpert",
    "Brad Andac",
    "Aidaba",
    "Samina Ebadji",
    "Tom Paech",
    "Ligan",
    "Cren",
    "Acosta",
    "Dran",
    "Nil",
    "Petra Forgewoman",
    "Ayomide Okilo",
    "Walid",
    "Mills",
    "Odund",
    "Ersa",
    "Mrs. Guliyev",
    "Connor Chasson",
    "Skylar Rivera",
    "Mia Sayied",
    "Wandari",
    "Kikuk",
    "Elkend",
    "Itamen",
    "Kam",
    "Bashar Mati",
    "Lut",
    "Ella Pontes",
    "Jackson Frye",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]['dialogues'] = []

# Label gender for each character
character_info["Aloy"]["gender"] = "Female"
character_info["Sylens"]["gender"] = "Male"
character_info["Erend"]["gender"] = "Male"
character_info["Rost"]["gender"] = "Male"
character_info["Elisabet Sobeck"]["gender"] = "Female"
character_info["Teersa"]["gender"] = "Female"
character_info["Varl"]["gender"] = "Male"
character_info["Ted Faro"]["gender"] = "Male"
character_info["Olin"]["gender"] = "Male"
character_info["Avad"]["gender"] = "Male"
character_info["Teb"]["gender"] = "Male"
character_info["Vanasha"]["gender"] = "Female"
character_info["Sona"]["gender"] = "Female"
character_info["GAIA"]["gender"] = "Female"
character_info["Helis"]["gender"] = "Male"
character_info["Uthid"]["gender"] = "Male"
character_info["Karst"]["gender"] = "Male"
character_info["General Herres"]["gender"] = "Male"
character_info["HADES"]["gender"] = "Male"
character_info["Resh"]["gender"] = "Male"
character_info["Nora Keeper"]["gender"] = "Male"
character_info["Marea"]["gender"] = "Female"
character_info["Travis Tate"]["gender"] = "Male"
character_info["Janeva"]["gender"] = "Male"
character_info["Lansra"]["gender"] = "Female"
character_info["Blameless Marad"]["gender"] = "Male"
character_info["Balahn"]["gender"] = "Male"
character_info["Vala"]["gender"] = "Female"
character_info["Bast"]["gender"] = "Male"
character_info["Charles Ronson"]["gender"] = "Male"
character_info["Dervahl"]["gender"] = "Male"
character_info["Margo Shěn"]["gender"] = "Female"
character_info["Jezza"]["gender"] = "Female"
character_info["Bahavas"]["gender"] = "Male"
character_info["Christina Hsu-Vhey"]["gender"] = "Female"
character_info["Guliyev"]["gender"] = "Male"
character_info["Patrick Brochard-Klein"]["gender"] = "Male"
character_info["Three-Toed Huadiv"]["gender"] = "Male"
character_info["Murell"]["gender"] = "Male"
character_info["Ron Felder"]["gender"] = "Male"
character_info["Susanne Alpert"]["gender"] = "Female"
character_info["Brad Andac"]["gender"] = "Male"
character_info["Aidaba"]["gender"] = "Female"
character_info["Samina Ebadji"]["gender"] = "Female"
character_info["Tom Paech"]["gender"] = "Male"
character_info["Ligan"]["gender"] = "Male"
character_info["Cren"]["gender"] = "Male"
character_info["Acosta"]["gender"] = "Female"
character_info["Dran"]["gender"] = "Male"
character_info["Nil"]["gender"] = "Male"
character_info["Petra Forgewoman"]["gender"] = "Female"
character_info["Ayomide Okilo"]["gender"] = "Female"
character_info["Walid"]["gender"] = "Male"
character_info["Mills"]["gender"] = "Male"
character_info["Odund"]["gender"] = "Male"
character_info["Ersa"]["gender"] = "Female"
character_info["Mrs. Guliyev"]["gender"] = "Female"
character_info["Connor Chasson"]["gender"] = "Male"
character_info["Skylar Rivera"]["gender"] = "Female"
character_info["Mia Sayied"]["gender"] = "Female"
character_info["Wandari"]["gender"] = "Male"
character_info["Kikuk"]["gender"] = "Male"
character_info["Elkend"]["gender"] = "Male"
character_info["Itamen"]["gender"] = "Male"
character_info["Kam"]["gender"] = "Female"
character_info["Bashar Mati"]["gender"] = "Male"
character_info["Lut"]["gender"] = "Male"
character_info["Ella Pontes"]["gender"] = "Female"
character_info["Jackson Frye"]["gender"] = "Male"

# Extract dialogues from the dataset
for item in data["text"]:
    key, value = next(iter(item.items()))
    if key in character_info:
        if value.strip().endswith(('.', '?', '!')):
            character_info[key]["dialogues"].append(value)

# Create a dataframe to store character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Horizon Zero Dawn",
            "Year": "2017",
            "Country": "Netherlands",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Erend": "Erend Vanguardsman",
    "Olin": "Olin Delverson",
    "General Herres": "Aaron Herres",
    "Blameless Marad": "Marad",
    "Guliyev": "Ames Guliyev",
    "Murell": "Fiona Murell",
    "Acosta": "Lana Acosta",
    "Mills": "Yana Mills",
    "Mrs. Guliyev": "Roshana Guliyev",
    "Wandari": "Usizo Wandari",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = ["Aloy"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/horizon_zero_dawn/data.csv", index=False)
