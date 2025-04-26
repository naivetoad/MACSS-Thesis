# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/persona_4/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Yu Narukami",
    "Yosuke Hanamura",
    "Chie Satonaka",
    "Naoto Shirogane",
    "Yukiko Amagi",
    "Rise Kujikawa",
    "Teddie",
    "Kanji Tatsumi",
    "Ryotaro Dojima",
    "Nanako",
    "Tohru Adachi",
    "Ai Ebihara",
    "Yumi Ozawa",
    "Hisano Kuroda",
    "Margaret",
    "Souji",
    "Kou Ichijo",
    "Daisuke Nagase",
    "Sayoko Uehara",
    "Taro Namatame",
    "Igor",
    "Shu Nakajima",
    "Mr. Kondo",
    "Kinshiro Morooka",
    "Eri",
    "Moel Gas Station Attendant",
    "Noriko Kashiwagi",
    "Kimiko Sofue",
    "Shadow Rise Kujikawa",
    "Announcer",
    "Mr. Hosoi",
    "Mr. Yamada",
    "Mrs. Nakayama",
    "Shadow Yukiko Amagi",
    "Mitsuo Kubo",
    "Shadow Kanji Tatsumi",
    "Shadow Naoto Shirogane",
    "Inoue",
    "Kanji's Mother",
    "Edogawa",
    "Shadow Mitsuo Kubo",
    "Takeshi",
    "Keita's Grandpa",
    "Saki",
    "Tanaka",
    "Shadow Teddie",
    "Yumi's Mother",
    "Yuuta",
    "Chihiro Fushimi",
    "Shadow Chie Satonaka",
    "Shu's Mother",
    "Yakushiji",
    "Kasai",
    "Shadow Yosuke",
    "Rise's Grandmother",
    "Hanako Ohtani",
    "Yumi's Father",
    "Naoki",
    "P.E. Teacher",
    "Daisuke's Ex",
    "Mayumi Yamano",
    "Daidara",
    "Saki's Dad",
    "Akio",
    "Akio's Dad",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Yu Narukami"]["gender"] = "Male"
character_info["Yosuke Hanamura"]["gender"] = "Male"
character_info["Chie Satonaka"]["gender"] = "Female"
character_info["Naoto Shirogane"]["gender"] = "Female"
character_info["Yukiko Amagi"]["gender"] = "Female"
character_info["Rise Kujikawa"]["gender"] = "Female"
character_info["Teddie"]["gender"] = "Male"
character_info["Kanji Tatsumi"]["gender"] = "Male"
character_info["Ryotaro Dojima"]["gender"] = "Male"
character_info["Nanako"]["gender"] = "Female"
character_info["Tohru Adachi"]["gender"] = "Male"
character_info["Ai Ebihara"]["gender"] = "Female"
character_info["Yumi Ozawa"]["gender"] = "Female"
character_info["Hisano Kuroda"]["gender"] = "Female"
character_info["Margaret"]["gender"] = "Female"
character_info["Souji"]["gender"] = "Male"
character_info["Kou Ichijo"]["gender"] = "Male"
character_info["Daisuke Nagase"]["gender"] = "Male"
character_info["Sayoko Uehara"]["gender"] = "Female"
character_info["Taro Namatame"]["gender"] = "Male"
character_info["Igor"]["gender"] = "Male"
character_info["Shu Nakajima"]["gender"] = "Male"
character_info["Mr. Kondo"]["gender"] = "Male"
character_info["Kinshiro Morooka"]["gender"] = "Male"
character_info["Eri"]["gender"] = "Female"
character_info["Moel Gas Station Attendant"]["gender"] = "Male"
character_info["Noriko Kashiwagi"]["gender"] = "Female"
character_info["Kimiko Sofue"]["gender"] = "Female"
character_info["Shadow Rise Kujikawa"]["gender"] = "Female"
character_info["Announcer"]["gender"] = "Female"
character_info["Mr. Hosoi"]["gender"] = "Male"
character_info["Mr. Yamada"]["gender"] = "Male"
character_info["Mrs. Nakayama"]["gender"] = "Female"
character_info["Shadow Yukiko Amagi"]["gender"] = "Female"
character_info["Mitsuo Kubo"]["gender"] = "Male"
character_info["Shadow Kanji Tatsumi"]["gender"] = "Male"
character_info["Shadow Naoto Shirogane"]["gender"] = "Female"
character_info["Inoue"]["gender"] = "Male"
character_info["Kanji's Mother"]["gender"] = "Female"
character_info["Edogawa"]["gender"] = "Male"
character_info["Shadow Mitsuo Kubo"]["gender"] = "Male"
character_info["Takeshi"]["gender"] = "Male"
character_info["Keita's Grandpa"]["gender"] = "Male"
character_info["Saki"]["gender"] = "Female"
character_info["Tanaka"]["gender"] = "Male"
character_info["Shadow Teddie"]["gender"] = "Male"
character_info["Yumi's Mother"]["gender"] = "Female"
character_info["Yuuta"]["gender"] = "Male"
character_info["Chihiro Fushimi"]["gender"] = "Female"
character_info["Shadow Chie Satonaka"]["gender"] = "Female"
character_info["Shu's Mother"]["gender"] = "Female"
character_info["Yakushiji"]["gender"] = "Male"
character_info["Kasai"]["gender"] = "Female"
character_info["Shadow Yosuke"]["gender"] = "Male"
character_info["Rise's Grandmother"]["gender"] = "Female"
character_info["Hanako Ohtani"]["gender"] = "Female"
character_info["Yumi's Father"]["gender"] = "Male"
character_info["Naoki"]["gender"] = "Male"
character_info["P.E. Teacher"]["gender"] = "Male"
character_info["Daisuke's Ex"]["gender"] = "Female"
character_info["Mayumi Yamano"]["gender"] = "Female"
character_info["Daidara"]["gender"] = "Male"
character_info["Saki's Dad"]["gender"] = "Male"
character_info["Akio"]["gender"] = "Male"
character_info["Akio's Dad"]["gender"] = "Male"

# Extract dialogues from the dataset
for item in data["text"]:
    key, value = next(iter(item.items()))
    if key in character_info:
        if value.strip().endswith(('.', '?', '!')):
            character_info[key]["dialogues"].append(value)
    elif key == "ACTION":
        if value.strip().endswith(('.', '?', '!')):
            character_info["Yu Narukami"]["dialogues"].append(value)

# Create a dataframe from character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Persona 4",
            "Year": "2008",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Nanako": "Nanako Dojima",
    "Souji": "Yu Narukami",
    "Eri": "Eri Minami",
    "Inoue": "Minoru Inoue",
    "Edogawa": "Mr. Edogawa",
    "Keita's Grandpa": "Keita's Grandfather",
    "Saki": "Saki Konishi",
    "Tanaka": "President Tanaka",
    "Yuuta": "Yuuta Minami",
    "Shadow Yosuke": "Shadow Yosuke Hanamura",
    "Naoki": "Naoki Konishi",
    "P.E. Teacher": "Mr. Kondo",
    "Daisuke's Ex": "Daisuke's Ex-girlfriend",
    "Saki's Dad": "Saki's Father",
    "Akio's Dad": "Akio's Father",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Yu Narukami",
    "Yosuke Hanamura",
    "Chie Satonaka",
    "Yukiko Amagi",
    "Kanji Tatsumi",
    "Rise Kujikawa",
    "Nanako Dojima",
    "Teddie",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/persona_4/data.csv", index=False)
