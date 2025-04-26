# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_xii/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Vaan",
    "Balthier",
    "Ashe",
    "Basch",
    "Penelo",
    "Fran",
    "Larsa",
    "Ondore",
    "Vossler",
    "Vayne",
    "Tchigri",
    "Masyua",
    "Judge Ghis",
    "Jules",
    "Mjrn",
    "Gabranth",
    "Old Dalan",
    "Tomaj",
    "Jinn",
    "Kytes",
    "War-chief Supinelu",
    "Cid",
    "Migelo",
    "Al-Cid",
    "Dantro's Wife",
    "Reddas",
    "Drace",
    "Gramis",
    "Jote",
    "Burrogh",
    "Stok",
    "Blok",
    "Atak",
    "Dyce",
    "Reks",
    "Rimzat",
    "Ba'Gamnan",
    "Terra",
    "Chief Steward Ann",
    "Camina",
    "Ktjn",
    "Rikken",
    "Anastasis",
    "Bergan",
    "Great Chief Uball-Ka",
    "Cotze",
    "Chit",
    "Sassan",
    "Elder Brunoa",
    "Rasler",
    "Deweg",
    "Ruksel",
    "Rande",
    "Gurdy",
    "High-chief Zayalu",
    "Arjie",
    "Agytha",
    "July",
    "Gibbs",
    "Asdalu",
    "Lulucce",
    "Northon",
    "Tott",
    "Bucco",
    "Renn",
    "Torrie",
    "Geomancer Yugelu",
    "Dilah",
    "Havharo",
    "Balzac",
    "Filo",
    "Roaklo",
    "Dantro",
    "Montblanc",
    "Zargabaath",
    "Warrior Guromu",
    "Nutsy",
    "Riby",
    "Sherral",
    "Johm",
    "Moomer",
    "Alja",
    "Rael",
    "Kjrs",
    "Rena",
    "Nera",
    "Warrior Hsemu",
    "Old War-chief Kadalu",
    "Lohen",
    "Melisa",
    "Rithil",
    "Dania",
    "Lesina",
    "Nanau",
    "Panamis",
    "Raz",
    "Elza",
    "Docent",
    "Beasley",
    "Shifty-eyed Man",
    "Relj",
    "Hala",
    "Queen of the Urutan",
    "Nono",
    "Niray",
    "Aekom",
    "Chief Steward Chezelle",
    "Bwagi",
    "Fidget",
    "Samal",
    "Ada",
    "Yamoora",
    "Lord Vain",
    "Yugri",
    "Raminas",
    "Shurry",
    "Fermon",
    "Va'Kansa",
    "Adair",
    "Judge Hausen",
    "Low-chief Sugumu",
    "Sadeen",
    "Clio",
    "Rinok",
    "Gijuk",
    "Milha",
    "Jovy",
    "Arryl",
    "Krjn",
    "Ma'kenroh",
    "Bansat",
    "Monid",
    "Gatsly",
    "Ma'kleou",
    "Chief Steward Liddy",
    "Lirschell",
    "Koqmihn",
    "Popol",
    "Beruny",
    "Emma",
    "Cabbie",
    "Lebleu's Daughter",
    "Granch",
    "Malloud",
    "Mummer",
    "Otto",
    "Ieeha",
    "Ivaness",
    "Hymms",
    "Kait",
    "Pilika",
    "Yrlon",
    "Mait",
    "Targe",
    "Horne",
    "Hurdy",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Vaan"]["gender"] = "Male"
character_info["Balthier"]["gender"] = "Male"
character_info["Ashe"]["gender"] = "Female"
character_info["Basch"]["gender"] = "Male"
character_info["Penelo"]["gender"] = "Female"
character_info["Fran"]["gender"] = "Female"
character_info["Larsa"]["gender"] = "Female"
character_info["Ondore"]["gender"] = "Male"
character_info["Vossler"]["gender"] = "Male"
character_info["Vayne"]["gender"] = "Female"
character_info["Tchigri"]["gender"] = "Male"
character_info["Masyua"]["gender"] = "Female"
character_info["Judge Ghis"]["gender"] = "Male"
character_info["Jules"]["gender"] = "Male"
character_info["Mjrn"]["gender"] = "Female"
character_info["Gabranth"]["gender"] = "Male"
character_info["Old Dalan"]["gender"] = "Male"
character_info["Tomaj"]["gender"] = "Male"
character_info["Jinn"]["gender"] = "Male"
character_info["Kytes"]["gender"] = "Male"
character_info["War-chief Supinelu"]["gender"] = "Male"
character_info["Cid"]["gender"] = "Male"
character_info["Migelo"]["gender"] = "Male"
character_info["Al-Cid"]["gender"] = "Male"
character_info["Dantro's Wife"]["gender"] = "Female"
character_info["Reddas"]["gender"] = "Male"
character_info["Drace"]["gender"] = "Female"
character_info["Gramis"]["gender"] = "Male"
character_info["Jote"]["gender"] = "Female"
character_info["Burrogh"]["gender"] = "Male"
character_info["Stok"]["gender"] = "Male"
character_info["Blok"]["gender"] = "Male"
character_info["Atak"]["gender"] = "Male"
character_info["Dyce"]["gender"] = "Male"
character_info["Reks"]["gender"] = "Male"
character_info["Rimzat"]["gender"] = "Male"
character_info["Ba'Gamnan"]["gender"] = "Male"
character_info["Terra"]["gender"] = "Female"
character_info["Chief Steward Ann"]["gender"] = "Female"
character_info["Camina"]["gender"] = "Female"
character_info["Ktjn"]["gender"] = "Female"
character_info["Rikken"]["gender"] = "Male"
character_info["Anastasis"]["gender"] = "Male"
character_info["Bergan"]["gender"] = "Male"
character_info["Great Chief Uball-Ka"]["gender"] = "Male"
character_info["Cotze"]["gender"] = "Male"
character_info["Chit"]["gender"] = "Male"
character_info["Sassan"]["gender"] = "Female"
character_info["Elder Brunoa"]["gender"] = "Female"
character_info["Rasler"]["gender"] = "Female"
character_info["Deweg"]["gender"] = "Male"
character_info["Ruksel"]["gender"] = "Male"
character_info["Rande"]["gender"] = "Male"
character_info["Gurdy"]["gender"] = "Female"
character_info["High-chief Zayalu"]["gender"] = "Male"
character_info["Arjie"]["gender"] = "Female"
character_info["Agytha"]["gender"] = "Female"
character_info["July"]["gender"] = "Female"
character_info["Gibbs"]["gender"] = "Male"
character_info["Asdalu"]["gender"] = "Male"
character_info["Lulucce"]["gender"] = "Male"
character_info["Northon"]["gender"] = "Male"
character_info["Tott"]["gender"] = "Male"
character_info["Bucco"]["gender"] = "Male"
character_info["Renn"]["gender"] = "Male"
character_info["Torrie"]["gender"] = "Female"
character_info["Geomancer Yugelu"]["gender"] = "Male"
character_info["Dilah"]["gender"] = "Female"
character_info["Havharo"]["gender"] = "Male"
character_info["Balzac"]["gender"] = "Male"
character_info["Filo"]["gender"] = "Female"
character_info["Roaklo"]["gender"] = "Male"
character_info["Dantro"]["gender"] = "Male"
character_info["Montblanc"]["gender"] = "Male"
character_info["Zargabaath"]["gender"] = "Female"
character_info["Warrior Guromu"]["gender"] = "Male"
character_info["Nutsy"]["gender"] = "Male"
character_info["Riby"]["gender"] = "Male"
character_info["Sherral"]["gender"] = "Male"
character_info["Johm"]["gender"] = "Male"
character_info["Moomer"]["gender"] = "Male"
character_info["Alja"]["gender"] = "Female"
character_info["Rael"]["gender"] = "Female"
character_info["Kjrs"]["gender"] = "Female"
character_info["Rena"]["gender"] = "Female"
character_info["Nera"]["gender"] = "Female"
character_info["Warrior Hsemu"]["gender"] = "Male"
character_info["Old War-chief Kadalu"]["gender"] = "Male"
character_info["Lohen"]["gender"] = "Male"
character_info["Melisa"]["gender"] = "Female"
character_info["Rithil"]["gender"] = "Male"
character_info["Dania"]["gender"] = "Female"
character_info["Lesina"]["gender"] = "Female"
character_info["Nanau"]["gender"] = "Female"
character_info["Panamis"]["gender"] = "Male"
character_info["Raz"]["gender"] = "Male"
character_info["Elza"]["gender"] = "Female"
character_info["Docent"]["gender"] = "Female"
character_info["Beasley"]["gender"] = "Male"
character_info["Shifty-eyed Man"]["gender"] = "Male"
character_info["Relj"]["gender"] = "Female"
character_info["Hala"]["gender"] = "Female"
character_info["Queen of the Urutan"]["gender"] = "Female"
character_info["Nono"]["gender"] = "Male"
character_info["Niray"]["gender"] = "Female"
character_info["Aekom"]["gender"] = "Female"
character_info["Chief Steward Chezelle"]["gender"] = "Female"
character_info["Bwagi"]["gender"] = "Male"
character_info["Fidget"]["gender"] = "Male"
character_info["Samal"]["gender"] = "Male"
character_info["Ada"]["gender"] = "Female"
character_info["Yamoora"]["gender"] = "Female"
character_info["Lord Vain"]["gender"] = "Male"
character_info["Yugri"]["gender"] = "Female"
character_info["Raminas"]["gender"] = "Male"
character_info["Shurry"]["gender"] = "Female"
character_info["Fermon"]["gender"] = "Male"
character_info["Va'Kansa"]["gender"] = "Male"
character_info["Adair"]["gender"] = "Female"
character_info["Judge Hausen"]["gender"] = "Male"
character_info["Low-chief Sugumu"]["gender"] = "Male"
character_info["Sadeen"]["gender"] = "Male"
character_info["Clio"]["gender"] = "Male"
character_info["Rinok"]["gender"] = "Female"
character_info["Gijuk"]["gender"] = "Male"
character_info["Milha"]["gender"] = "Female"
character_info["Jovy"]["gender"] = "Male"
character_info["Arryl"]["gender"] = "Male"
character_info["Krjn"]["gender"] = "Female"
character_info["Ma'kenroh"]["gender"] = "Male"
character_info["Bansat"]["gender"] = "Male"
character_info["Monid"]["gender"] = "Male"
character_info["Gatsly"]["gender"] = "Male"
character_info["Ma'kleou"]["gender"] = "Male"
character_info["Chief Steward Liddy"]["gender"] = "Female"
character_info["Lirschell"]["gender"] = "Male"
character_info["Koqmihn"]["gender"] = "Male"
character_info["Popol"]["gender"] = "Male"
character_info["Beruny"]["gender"] = "Male"
character_info["Emma"]["gender"] = "Female"
character_info["Cabbie"]["gender"] = "Male"
character_info["Lebleu's Daughter"]["gender"] = "Female"
character_info["Granch"]["gender"] = "Male"
character_info["Malloud"]["gender"] = "Female"
character_info["Mummer"]["gender"] = "Male"
character_info["Otto"]["gender"] = "Male"
character_info["Ieeha"]["gender"] = "Female"
character_info["Ivaness"]["gender"] = "Male"
character_info["Hymms"]["gender"] = "Male"
character_info["Kait"]["gender"] = "Female"
character_info["Pilika"]["gender"] = "Female"
character_info["Yrlon"]["gender"] = "Male"
character_info["Mait"]["gender"] = "Female"
character_info["Targe"]["gender"] = "Male"
character_info["Horne"]["gender"] = "Male"
character_info["Hurdy"]["gender"] = "Male"

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
            "Title": "Final Fantasy XII",
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
    "Ashe": "Ashelia B'nargin Dalmasca",
    "Basch": "Basch fon Ronsenburg",
    "Larsa": "Larsa Ferrinas Solidor",
    "Ondore": "Marquis Halim Ondore IV",
    "Vossler": "Vossler York Azelas",
    "Vayne": "Vayne Carudas Solidor",
    "Gabranth": "Judge Gabranth",
    "War-chief Supinelu": "Supinelu",
    "Cid": "Cidolfus Demen Bunansa",
    "Al-Cid": "Al-Cid Margrace",
    "Drace": "Judge Drace",
    "Gramis": "Gramis Gana Solidor",
    "Chief Steward Ann": "Ann",
    "Bergan": "Judge Bergan",
    "Great Chief Uball-Ka": "Uball-Ka",
    "Elder Brunoa": "Brunoa",
    "Rasler Heios Nabradia": "Rasler",
    "High-chief Zayalu": "Zayalu",
    "Geomancer Yugelu": "Yugelu",
    "Warrior Guromu": "Guromu",
    "Warrior Hsemu": "Hsemu",
    "Old War-chief Kadalu": "Kadalu",
    "Shifty-eyed Man": "Shifty-Eyed Man",
    "Chief Steward Chezelle": "Chezelle",
    "Raminas": "Raminas B'nargin Dalmasca",
    "Low-chief Sugumu": "Sugumu",
    "Chief Steward Liddy": "Liddy",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Vaan",
    "Balthier",
    "Fran",
    "Basch fon Ronsenburg",
    "Ashelia B'nargin Dalmasca",
    "Penelo",
    "Reks",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_xii/data.csv", index=False)
