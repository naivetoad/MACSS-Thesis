# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/horizon_forbidden_west/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Aloy",
    "Varl",
    "Zo",
    "Erend",
    "Alva",
    "GAIA",
    "Kotallo",
    "Tilda van der Meer",
    "Beta",
    "Sylens",
    "Talanah",
    "Dekka",
    "Morlund",
    "Hekarro",
    "Ceo",
    "Lawan",
    "Bohai",
    "Amadis",
    "Ulvund",
    "Petra",
    "Javad the Willing",
    "Abadund",
    "Kue",
    "Silga",
    "Natikka",
    "Ivvira",
    "Marshal Fashav",
    "Lokasha",
    "HADES",
    "Arokkeh",
    "Penttoh",
    "Stemmur",
    "Avad",
    "Kavvoh",
    "Regalla",
    "Studious Vuadis",
    "Ritakka",
    "Porguf",
    "Erik",
    "Larend",
    "Delah",
    "Wekatta",
    "Tekotteh",
    "Vanasha",
    "Ragurt",
    "Untalla",
    "Nozar",
    "Thurlis",
    "Milduf",
    "Karhn",
    "Kivva",
    "Gerard",
    "Keruf",
    "Tolland Cleanbroker",
    "Belna",
    "Joruf",
    "Vetteh",
    "Hataktto",
    "Kitakka",
    "Hakund",
    "Uthid",
    "Littay",
    "Jekkah",
    "Ivinna",
    "Blameless Marad",
    "Travis Tate",
    "Rokko",
    "Savohar",
    "Boomer",
    "Telga",
    "Arnuf",
    "Kenalla",
    "Kentokk",
    "Zokkah",
    "Luf",
    "Salma",
    "Odurg",
    "Nirik",
    "Lirokkeh",
    "Erayyo",
    "Corend",
    "Mian",
    "Aldur",
    "Nakalla",
    "Isabel",
    "Verbena",
    "Gerrah",
    "Fane",
    "Lel",
    "Milu",
    "Elisabet Sobeck",
    "Fendur",
    "Volma",
    "Itamen",
    "Eileen Sasaki",
    "Nakko",
    "Ziverra",
    "Lunda",
    "Minda",
    "Rukka",
    "Nasadi",
    "Yivekka",
    "Aquino",
    "Litakka",
    "Terakka",
    "Jorund",
    "Osvald Dalgaard",
    "Kenzo Sasaki",
    "Urekka",
    "Ted Faro",
    "Sonkai",
    "Uvveh",
    "Kel",
    "Lora",
    "Grudda",
    "Regalla Rebel",
    "Dr. Somptow",
    "Isabet",
    "Zikka",
    "Faraday",
    "Arorro",
    "Kin",
    "Gilvarn",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Aloy"]["gender"] = "Female"
character_info["Varl"]["gender"] = "Male"
character_info["Zo"]["gender"] = "Female"
character_info["Erend"]["gender"] = "Male"
character_info["Alva"]["gender"] = "Female"
character_info["GAIA"]["gender"] = "Female"
character_info["Kotallo"]["gender"] = "Male"
character_info["Tilda van der Meer"]["gender"] = "Female"
character_info["Beta"]["gender"] = "Female"
character_info["Sylens"]["gender"] = "Male"
character_info["Talanah"]["gender"] = "Female"
character_info["Dekka"]["gender"] = "Female"
character_info["Morlund"]["gender"] = "Male"
character_info["Hekarro"]["gender"] = "Male"
character_info["Ceo"]["gender"] = "Male"
character_info["Lawan"]["gender"] = "Male"
character_info["Bohai"]["gender"] = "Male"
character_info["Amadis"]["gender"] = "Male"
character_info["Ulvund"]["gender"] = "Male"
character_info["Petra"]["gender"] = "Female"
character_info["Javad the Willing"]["gender"] = "Male"
character_info["Abadund"]["gender"] = "Male"
character_info["Kue"]["gender"] = "Male"
character_info["Silga"]["gender"] = "Female"
character_info["Natikka"]["gender"] = "Female"
character_info["Ivvira"]["gender"] = "Female"
character_info["Marshal Fashav"]["gender"] = "Male"
character_info["Lokasha"]["gender"] = "Female"
character_info["HADES"]["gender"] = "Male"
character_info["Arokkeh"]["gender"] = "Male"
character_info["Penttoh"]["gender"] = "Male"
character_info["Stemmur"]["gender"] = "Male"
character_info["Avad"]["gender"] = "Male"
character_info["Kavvoh"]["gender"] = "Male"
character_info["Regalla"]["gender"] = "Female"
character_info["Studious Vuadis"]["gender"] = "Male"
character_info["Ritakka"]["gender"] = "Female"
character_info["Porguf"]["gender"] = "Male"
character_info["Erik"]["gender"] = "Male"
character_info["Larend"]["gender"] = "Male"
character_info["Delah"]["gender"] = "Male"
character_info["Wekatta"]["gender"] = "Female"
character_info["Tekotteh"]["gender"] = "Female"
character_info["Vanasha"]["gender"] = "Female"
character_info["Ragurt"]["gender"] = "Male"
character_info["Untalla"]["gender"] = "Female"
character_info["Nozar"]["gender"] = "Male"
character_info["Thurlis"]["gender"] = "Male"
character_info["Milduf"]["gender"] = "Male"
character_info["Karhn"]["gender"] = "Male"
character_info["Kivva"]["gender"] = "Female"
character_info["Gerard"]["gender"] = "Male"
character_info["Keruf"]["gender"] = "Male"
character_info["Tolland Cleanbroker"]["gender"] = "Male"
character_info["Belna"]["gender"] = "Female"
character_info["Joruf"]["gender"] = "Male"
character_info["Vetteh"]["gender"] = "Male"
character_info["Hataktto"]["gender"] = "Male"
character_info["Kitakka"]["gender"] = "Female"
character_info["Hakund"]["gender"] = "Male"
character_info["Uthid"]["gender"] = "Male"
character_info["Littay"]["gender"] = "Female"
character_info["Jekkah"]["gender"] = "Female"
character_info["Ivinna"]["gender"] = "Female"
character_info["Blameless Marad"]["gender"] = "Male"
character_info["Travis Tate"]["gender"] = "Male"
character_info["Rokko"]["gender"] = "Male"
character_info["Savohar"]["gender"] = "Male"
character_info["Boomer"]["gender"] = "Female"
character_info["Telga"]["gender"] = "Female"
character_info["Arnuf"]["gender"] = "Male"
character_info["Kenalla"]["gender"] = "Female"
character_info["Kentokk"]["gender"] = "Male"
character_info["Zokkah"]["gender"] = "Male"
character_info["Luf"]["gender"] = "Male"
character_info["Salma"]["gender"] = "Female"
character_info["Odurg"]["gender"] = "Male"
character_info["Nirik"]["gender"] = "Male"
character_info["Lirokkeh"]["gender"] = "Male"
character_info["Erayyo"]["gender"] = "Male"
character_info["Corend"]["gender"] = "Male"
character_info["Mian"]["gender"] = "Female"
character_info["Aldur"]["gender"] = "Male"
character_info["Nakalla"]["gender"] = "Female"
character_info["Isabel"]["gender"] = "Female"
character_info["Verbena"]["gender"] = "Female"
character_info["Gerrah"]["gender"] = "Female"
character_info["Fane"]["gender"] = "Male"
character_info["Lel"]["gender"] = "Male"
character_info["Milu"]["gender"] = "Female"
character_info["Elisabet Sobeck"]["gender"] = "Female"
character_info["Fendur"]["gender"] = "Male"
character_info["Volma"]["gender"] = "Female"
character_info["Itamen"]["gender"] = "Male"
character_info["Eileen Sasaki"]["gender"] = "Female"
character_info["Nakko"]["gender"] = "Male"
character_info["Ziverra"]["gender"] = "Female"
character_info["Lunda"]["gender"] = "Female"
character_info["Minda"]["gender"] = "Female"
character_info["Rukka"]["gender"] = "Female"
character_info["Nasadi"]["gender"] = "Female"
character_info["Yivekka"]["gender"] = "Female"
character_info["Aquino"]["gender"] = "Female"
character_info["Litakka"]["gender"] = "Female"
character_info["Terakka"]["gender"] = "Female"
character_info["Jorund"]["gender"] = "Male"
character_info["Osvald Dalgaard"]["gender"] = "Male"
character_info["Kenzo Sasaki"]["gender"] = "Male"
character_info["Urekka"]["gender"] = "Female"
character_info["Ted Faro"]["gender"] = "Male"
character_info["Sonkai"]["gender"] = "Female"
character_info["Uvveh"]["gender"] = "Male"
character_info["Kel"]["gender"] = "Female"
character_info["Lora"]["gender"] = "Female"
character_info["Grudda"]["gender"] = "Male"
character_info["Regalla Rebel"]["gender"] = "Female"
character_info["Dr. Somptow"]["gender"] = "Male"
character_info["Isabet"]["gender"] = "Female"
character_info["Zikka"]["gender"] = "Female"
character_info["Faraday"]["gender"] = "Female"
character_info["Arorro"]["gender"] = "Male"
character_info["Kin"]["gender"] = "Female"
character_info["Gilvarn"]["gender"] = "Male"

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
            "Title": "Horizon Forbidden West",
            "Year": "2022",
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
    "Talanah": "Talanah Khane Padish",
    "Morlund": "Morlund Showman",
    "Amadis": "Amadis Beit Raveesh",
    "Ulvund": "Ulvund Freeholder",
    "Petra": "Petra Forgewoman",
    "Javad the Willing": "Javad",
    "Abadund": "Abadund Shardcounter",
    "Marshal Fashav": "Fashav",
    "Stemmur": "Stemmur Wordsmith",
    "Studious Vuadis": "Vuadis",
    "Porguf": "Porguf Delvesman",
    "Erik": "Erik Visser",
    "Nozar": "Nozar Arin Khuvaman",
    "Milduf": "Milduf Boarbroiler",
    "Gerard": "Gerard Bieri",
    "Blameless Marad": "Marad",
    "Verbena": "Verbena Sutter",
    "Aquino": "Tala Aquino",
    "Regalla Rebel": "Regalla",
    "Dr. Somptow": "Narong Somptow",
    "Isabet": "Elisabet Sobeck",
    "Faraday": "Anne Faraday",
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
df.to_csv("data/horizon_forbidden_west/data.csv", index=False)
