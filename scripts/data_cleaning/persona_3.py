# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/persona_3/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Makoto Yuki",
    "Junpei",
    "Yukari",
    "Mitsuru",
    "Akihiko",
    "Fuuka",
    "Ikutsuki",
    "Shinjiro",
    "Aigis",
    "Ken",
    "Chidori",
    "Maya",
    "Takaya",
    "Akinari",
    "Yuko",
    "Chihiro",
    "Bunkichi",
    "Tanaka",
    "Mutatsu",
    "Pharos",
    "Mamoru",
    "Bebe",
    "Kenji",
    "Maiko",
    "Natsuki",
    "Ryoji",
    "Jin",
    "Mr. Edogawa",
    "Nozomi",
    "Takeharu",
    "Mitsuko",
    "Kazushi",
    "Igor",
    "Ms. Toriumi",
    "Eiichiro",
    "Monk",
    "Nobuko",
    "Keisuke",
    "Mr. Ekoda",
    "Maiko's Dad",
    "Maiko's Mom",
    "Hidetoshi",
    "Elizabeth",
    "Kouetsu Kirijo",
    "Kurosawa",
    "Ms. Kanou",
    "Koromaru",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Makoto Yuki"]["gender"] = "Male"
character_info["Junpei"]["gender"] = "Male"
character_info["Yukari"]["gender"] = "Female"
character_info["Mitsuru"]["gender"] = "Female"
character_info["Akihiko"]["gender"] = "Male"
character_info["Fuuka"]["gender"] = "Female"
character_info["Ikutsuki"]["gender"] = "Male"
character_info["Shinjiro"]["gender"] = "Male"
character_info["Aigis"]["gender"] = "Female"
character_info["Ken"]["gender"] = "Male"
character_info["Chidori"]["gender"] = "Female"
character_info["Maya"]["gender"] = "Female"
character_info["Takaya"]["gender"] = "Male"
character_info["Akinari"]["gender"] = "Male"
character_info["Yuko"]["gender"] = "Female"
character_info["Chihiro"]["gender"] = "Female"
character_info["Bunkichi"]["gender"] = "Male"
character_info["Tanaka"]["gender"] = "Male"
character_info["Mutatsu"]["gender"] = "Male"
character_info["Pharos"]["gender"] = "Male"
character_info["Mamoru"]["gender"] = "Male"
character_info["Bebe"]["gender"] = "Male"
character_info["Kenji"]["gender"] = "Male"
character_info["Maiko"]["gender"] = "Female"
character_info["Natsuki"]["gender"] = "Female"
character_info["Ryoji"]["gender"] = "Male"
character_info["Jin"]["gender"] = "Male"
character_info["Mr. Edogawa"]["gender"] = "Male"
character_info["Nozomi"]["gender"] = "Male"
character_info["Takeharu"]["gender"] = "Male"
character_info["Mitsuko"]["gender"] = "Female"
character_info["Kazushi"]["gender"] = "Male"
character_info["Igor"]["gender"] = "Male"
character_info["Ms. Toriumi"]["gender"] = "Female"
character_info["Eiichiro"]["gender"] = "Male"
character_info["Monk"]["gender"] = "Male"
character_info["Nobuko"]["gender"] = "Female"
character_info["Keisuke"]["gender"] = "Male"
character_info["Mr. Ekoda"]["gender"] = "Male"
character_info["Maiko's Dad"]["gender"] = "Male"
character_info["Maiko's Mom"]["gender"] = "Female"
character_info["Hidetoshi"]["gender"] = "Male"
character_info["Elizabeth"]["gender"] = "Female"
character_info["Kouetsu Kirijo"]["gender"] = "Male"
character_info["Kurosawa"]["gender"] = "Male"
character_info["Ms. Kanou"]["gender"] = "Female"
character_info["Koromaru"]["gender"] = "Male"

# Extract dialogues from the dataset
for item in data["text"]:
    key, value = next(iter(item.items()))
    if key in character_info:
        if value.strip().endswith(('.', '?', '!')):
            character_info[key]["dialogues"].append(value)
    elif key == "ACTION":
        if value.strip().endswith(('.', '?', '!')):
            character_info["Makoto Yuki"]["dialogues"].append(value)

# Create a dataframe from character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Persona 3",
            "Year": "2006",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Junpei": "Junpei Iori",
    "Yukari": "Yukari Takeba",
    "Mitsuru": "Mitsuru Kirijo",
    "Akihiko": "Akihiko Sanada",
    "Fuuka": "Fuuka Yamagishi",
    "Ikutsuki": "Shuji Ikutsuki",
    "Shinjiro": "Shinjiro Aragaki",
    "Ken": "Ken Amada",
    "Chidori": "Chidori Yoshino",
    "Maya": "Isako Toriumi",
    "Takaya": "Takaya Sakaki",
    "Akinari": "Akinari Kamiki",
    "Yuko": "Yuko Nishiwaki",
    "Chihiro": "Chihiro Fushimi",
    "Tanaka": "President Tanaka",
    "Mamoru": "Mamoru Hayase",
    "Bebe": "Andre Laurent Jean Geraux",
    "Kenji": "Kenji Tomochika",
    "Maiko": "Maiko Oohashi",
    "Natsuki": "Natsuki Moriyama",
    "Ryoji": "Ryoji Mochizuki",
    "Jin": "Jin Shirato",
    "Nozomi": "Nozomi Suemitsu",
    "Takeharu": "Takeharu Kirijo",
    "Kazushi": "Kazushi Miyamoto",
    "Ms. Toriumi": "Isako Toriumi",
    "Eiichiro": "Eiichiro Takeba",
    "Monk": "Mutatsu",
    "Keisuke": "Keisuke Hiraga",
    "Maiko's Dad": "Maiko's Father",
    "Maiko's Mom": "Maiko's Mother",
    "Hidetoshi": "Hidetoshi Odagiri",
    "Ms. Kanou": "Emiri Kanou",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Makoto Yuki",
    "Yukari Takeba",
    "Junpei Iori",
    "Mitsuru Kirijo",
    "Akihiko Sanada",
    "Fuuka Yamagishi",
    "Aigis",
    "Koromaru",
    "Ken Amada",
    "Shinjiro Aragaki",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/persona_3/data.csv", index=False)
