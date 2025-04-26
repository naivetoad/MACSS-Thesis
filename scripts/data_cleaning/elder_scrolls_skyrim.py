# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/elder_scrolls_skyrim/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Dragonborn",
    "Serana",
    "Brynjolf",
    "Ulfric",
    "Galmar",
    "Karliah",
    "Tullius",
    "Delphine",
    "Rikke",
    "Astrid",
    "Balgruuf",
    "Arngeir",
    "Ralof",
    "Esbern",
    "Valerica",
    "Isran",
    "Paarthurnax",
    "Hadvar",
    "Erandur",
    "Tolfdir",
    "Harkon",
    "Nazir",
    "Neloth",
    "Gelebor",
    "Mercer",
    "Dexion",
    "Irileth",
    "Cicero",
    "Frea",
    "Kodlak",
    "Savos",
    "Silus",
    "Aela",
    "Urag",
    "Festus",
    "Hermaeus",
    "Nelacar",
    "Mirabelle",
    "Paratus",
    "Maven",
    "Storn",
    "Farkas",
    "Gallus",
    "Amaund",
    "Elenwen",
    "Sheogorath",
    "Eorlund",
    "Proventus",
    "Gianna",
    "Babette",
    "Ancano",
    "Faralda",
    "Razelan",
    "Gulum-Ei",
    "Vilkas",
    "Farengar",
    "Garan",
    "Enthir",
    "Delvin",
    "Gabriella",
    "Verulus",
    "Gormlaith",
    "Arnbjorn",
    "Eola",
    "Orthorn",
    "Septimus",
    "Odahviing",
    "Etienne",
    "Veezara",
    "Alduin",
    "Logrolf",
    "Quaranir",
    "Erikur",
    "Durnehviir",
    "Mallus",
    "Aranea",
    "Skjor",
    "Hakon",
    "Malborn",
    "Sabjorn",
    "Aventus",
    "Molag Bal",
    "Yamarz",
    "Atub",
    "Tsun",
    "Felldir",
    "Vekel",
    "Gjalund",
    "Bersi",
    "Titus Mede II",
    "Boethiah",
    "Vyrthur",
    "Sorine",
    "Clavicus",
    "Sinding",
    "Ennis",
    "Sam",
    "The Caller",
    "Adril",
    "Vex",
    "Cipius",
    "Muiri",
    "Peryite",
    "Hircine",
    "Meridia",
    "Barbas",
    "Gerdur",
    "Lokir",
    "Miraak",
    "Tyranus",
    "Ysolda",
    "Senna",
    "Elisif",
    "Rulindil",
    "Brelas",
    "Haelga",
    "Grelod",
    "Atmah",
    "Idgrod",
    "Ondolemar",
    "Gunmar",
    "Calcelmo",
    "Keerava",
    "Raerek",
    "Anuriel",
    "Gaius Maro",
    "Mephala",
    "Veren",
    "Varona",
    "Hadring",
    "Gaius",
    "Night Mother",
    "Mehrunes Dagon",
    "Kesh",
    "Dervenin",
    "Augur",
    "Dirge",
    "Orthus",
    "Alvor",
    "Corpulus",
    "Vingalmo",
    "Agmaer",
    "Durak",
    "Vald",
    "Caius",
    "Mralki",
    "Anton",
    "Nelkir",
    "Azura",
    "Morokei",
    "Hafnar",
    "Gissur",
    "Arvel",
    "Nocturnal",
    "Jorgen",
    "Malacath",
    "Lod",
    "Torturer",
    "Tolan",
    "Aringoth",
    "Brand-Shei",
    "Vittoria",
    "Fultheim",
    "Alea",
    "Vasha",
    "Sanguine",
    "Takes-In-Light",
    "Arniel",
    "Orthjolf",
    "Madesi",
    "Vignar",
    "Balagog",
    "Hern",
    "Lurbuk",
    "Nilsine",
    "Beitild",
    "Ennodius",
    "Narfi",
    "Thorek",
    "Mathies",
    "Orgnar",
    "Borri",
    "Hod",
    "Talvas Fathryon",
    "Hestla",
    "Rargal",
    "Vanik",
    "Ronthil",
    "Malkus",
    "Stalf",
    "Lokil",
    "Celann",
    "Garthar",
    "Aicantar",
    "Irgnir",
    "Namira",
    "Pelagius",
    "Erdi",
    "Una",
    "Malyn",
    "Estormo",
    "Onmund",
    "J'zargo",
    "Brelyna",
    "Tsavani",
    "Sahloknir",
    "Iddra",
    "Wulfgar",
    "Einarth",
    "Hrongar",
    "Sigrid",
    "Frodnar",
    "Sahrotaar",
    "Fura",
    "Feran",
    "Edhelbor",
    "Nirilor",
    "Celegriath",
    "Athring",
    "Sidanyis",
    "Salonia",
    "Tonilia",
    "Vipir",
    "Sapphire",
    "Thrynn",
    "Niruin",
    "Ravyn",
    "Cynric",
    "Commander Maro",
    "Fruki",
    "Hogni Red-Arm",
    "Banning",
    "Lisbet",
    "Thongvor",
    "Madena",
    "J'Kier",
    "Moira",
    "Elvali",
    "Vilod",
    "Priestess of Arkay",
    "Torolf",
    "Haming",
    "Tharstan",
    "Morwen",
    "Wulf Wild-Blood",
    "Nikulas",
    "Finna",
    "Aeta",
    "Deor",
    "Edla",
    "Fanari Strong-Voice",
    "Krosulhah",
    "Salonia Caelia",
    "Adalvald",
    "Rune",
    "Aquilius",
    "Drifa",
    "Duilis",
    "Frorkmar",
    "Faida",
    "Pantea",
    "Alexia",
    "Nura Snow-Shod",
    "Asgeir Snow-Shod",
    "Rexus",
    "Alain",
    "Francois",
    "Samuel",
    "Runa",
    "Hroar",
    "Hulda",
    "Vaermina",
    "Thoring",
    "Sanyon",
    "Nimphaneth",
    "Falk",
    "Rissing",
    "Runil",
    "Sulla",
    "Umana",
    "Lob",
    "Ugor",
    "Dagur",
    "Athis",
    "Njada",
    "Brill",
    "Girduin",
    "Phinis Gestor",
    "Sergius",
    "Gavros",
    "Jyrik Gaulderson",
    "Nerien",
    "Ysgramor",
    "Torygg",
    "Mirmulnir",
    "Dorthe",
    "Gunnar",
    "Headsman",
    "Ingrid",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Dragonborn"]["gender"] = "Neutral"
character_info["Serana"]["gender"] = "Female"
character_info["Brynjolf"]["gender"] = "Male"
character_info["Ulfric"]["gender"] = "Male"
character_info["Galmar"]["gender"] = "Male"
character_info["Karliah"]["gender"] = "Female"
character_info["Tullius"]["gender"] = "Male"
character_info["Delphine"]["gender"] = "Female"
character_info["Rikke"]["gender"] = "Female"
character_info["Astrid"]["gender"] = "Female"
character_info["Balgruuf"]["gender"] = "Male"
character_info["Arngeir"]["gender"] = "Male"
character_info["Ralof"]["gender"] = "Male"
character_info["Esbern"]["gender"] = "Male"
character_info["Valerica"]["gender"] = "Female"
character_info["Isran"]["gender"] = "Male"
character_info["Paarthurnax"]["gender"] = "Male"
character_info["Hadvar"]["gender"] = "Male"
character_info["Erandur"]["gender"] = "Male"
character_info["Tolfdir"]["gender"] = "Male"
character_info["Harkon"]["gender"] = "Male"
character_info["Nazir"]["gender"] = "Male"
character_info["Neloth"]["gender"] = "Male"
character_info["Gelebor"]["gender"] = "Male"
character_info["Mercer"]["gender"] = "Male"
character_info["Dexion"]["gender"] = "Male"
character_info["Irileth"]["gender"] = "Female"
character_info["Cicero"]["gender"] = "Male"
character_info["Frea"]["gender"] = "Female"
character_info["Kodlak"]["gender"] = "Male"
character_info["Savos"]["gender"] = "Male"
character_info["Silus"]["gender"] = "Male"
character_info["Aela"]["gender"] = "Female"
character_info["Urag"]["gender"] = "Male"
character_info["Festus"]["gender"] = "Male"
character_info["Hermaeus"]["gender"] = "Male"
character_info["Nelacar"]["gender"] = "Male"
character_info["Mirabelle"]["gender"] = "Female"
character_info["Paratus"]["gender"] = "Male"
character_info["Maven"]["gender"] = "Female"
character_info["Storn"]["gender"] = "Male"
character_info["Farkas"]["gender"] = "Male"
character_info["Gallus"]["gender"] = "Male"
character_info["Amaund"]["gender"] = "Male"
character_info["Elenwen"]["gender"] = "Female"
character_info["Sheogorath"]["gender"] = "Male"
character_info["Eorlund"]["gender"] = "Male"
character_info["Proventus"]["gender"] = "Male"
character_info["Gianna"]["gender"] = "Female"
character_info["Babette"]["gender"] = "Female"
character_info["Ancano"]["gender"] = "Male"
character_info["Faralda"]["gender"] = "Female"
character_info["Razelan"]["gender"] = "Male"
character_info["Gulum-Ei"]["gender"] = "Male"
character_info["Vilkas"]["gender"] = "Male"
character_info["Farengar"]["gender"] = "Male"
character_info["Garan"]["gender"] = "Male"
character_info["Enthir"]["gender"] = "Male"
character_info["Delvin"]["gender"] = "Male"
character_info["Gabriella"]["gender"] = "Female"
character_info["Verulus"]["gender"] = "Male"
character_info["Gormlaith"]["gender"] = "Female"
character_info["Arnbjorn"]["gender"] = "Male"
character_info["Eola"]["gender"] = "Female"
character_info["Orthorn"]["gender"] = "Male"
character_info["Septimus"]["gender"] = "Male"
character_info["Odahviing"]["gender"] = "Male"
character_info["Etienne"]["gender"] = "Male"
character_info["Veezara"]["gender"] = "Male"
character_info["Alduin"]["gender"] = "Male"
character_info["Logrolf"]["gender"] = "Male"
character_info["Quaranir"]["gender"] = "Male"
character_info["Erikur"]["gender"] = "Male"
character_info["Durnehviir"]["gender"] = "Male"
character_info["Mallus"]["gender"] = "Male"
character_info["Aranea"]["gender"] = "Female"
character_info["Skjor"]["gender"] = "Male"
character_info["Hakon"]["gender"] = "Male"
character_info["Malborn"]["gender"] = "Male"
character_info["Sabjorn"]["gender"] = "Male"
character_info["Aventus"]["gender"] = "Male"
character_info["Molag Bal"]["gender"] = "Male"
character_info["Yamarz"]["gender"] = "Male"
character_info["Atub"]["gender"] = "Female"
character_info["Tsun"]["gender"] = "Male"
character_info["Felldir"]["gender"] = "Male"
character_info["Vekel"]["gender"] = "Male"
character_info["Gjalund"]["gender"] = "Male"
character_info["Bersi"]["gender"] = "Male"
character_info["Titus Mede II"]["gender"] = "Male"
character_info["Boethiah"]["gender"] = "Female"
character_info["Vyrthur"]["gender"] = "Male"
character_info["Sorine"]["gender"] = "Female"
character_info["Clavicus"]["gender"] = "Male"
character_info["Sinding"]["gender"] = "Male"
character_info["Ennis"]["gender"] = "Male"
character_info["Sam"]["gender"] = "Male"
character_info["The Caller"]["gender"] = "Male"
character_info["Adril"]["gender"] = "Male"
character_info["Vex"]["gender"] = "Female"
character_info["Cipius"]["gender"] = "Male"
character_info["Muiri"]["gender"] = "Female"
character_info["Peryite"]["gender"] = "Male"
character_info["Hircine"]["gender"] = "Male"
character_info["Meridia"]["gender"] = "Female"
character_info["Barbas"]["gender"] = "Male"
character_info["Gerdur"]["gender"] = "Female"
character_info["Lokir"]["gender"] = "Male"
character_info["Miraak"]["gender"] = "Male"
character_info["Tyranus"]["gender"] = "Male"
character_info["Ysolda"]["gender"] = "Female"
character_info["Senna"]["gender"] = "Female"
character_info["Elisif"]["gender"] = "Female"
character_info["Rulindil"]["gender"] = "Male"
character_info["Brelas"]["gender"] = "Female"
character_info["Haelga"]["gender"] = "Female"
character_info["Grelod"]["gender"] = "Female"
character_info["Atmah"]["gender"] = "Female"
character_info["Idgrod"]["gender"] = "Female"
character_info["Ondolemar"]["gender"] = "Male"
character_info["Gunmar"]["gender"] = "Male"
character_info["Calcelmo"]["gender"] = "Male"
character_info["Keerava"]["gender"] = "Female"
character_info["Raerek"]["gender"] = "Male"
character_info["Anuriel"]["gender"] = "Female"
character_info["Gaius Maro"]["gender"] = "Male"
character_info["Mephala"]["gender"] = "Female"
character_info["Veren"]["gender"] = "Male"
character_info["Varona"]["gender"] = "Female"
character_info["Hadring"]["gender"] = "Male"
character_info["Gaius"]["gender"] = "Male"
character_info["Night Mother"]["gender"] = "Female"
character_info["Mehrunes Dagon"]["gender"] = "Male"
character_info["Kesh"]["gender"] = "Male"
character_info["Dervenin"]["gender"] = "Male"
character_info["Augur"]["gender"] = "Male"
character_info["Dirge"]["gender"] = "Male"
character_info["Orthus"]["gender"] = "Male"
character_info["Alvor"]["gender"] = "Male"
character_info["Corpulus"]["gender"] = "Male"
character_info["Vingalmo"]["gender"] = "Male"
character_info["Agmaer"]["gender"] = "Male"
character_info["Durak"]["gender"] = "Male"
character_info["Vald"]["gender"] = "Male"
character_info["Caius"]["gender"] = "Male"
character_info["Mralki"]["gender"] = "Male"
character_info["Anton"]["gender"] = "Male"
character_info["Nelkir"]["gender"] = "Male"
character_info["Azura"]["gender"] = "Female"
character_info["Morokei"]["gender"] = "Male"
character_info["Hafnar"]["gender"] = "Male"
character_info["Gissur"]["gender"] = "Male"
character_info["Arvel"]["gender"] = "Male"
character_info["Nocturnal"]["gender"] = "Female"
character_info["Jorgen"]["gender"] = "Male"
character_info["Malacath"]["gender"] = "Male"
character_info["Lod"]["gender"] = "Male"
character_info["Torturer"]["gender"] = "Male"
character_info["Tolan"]["gender"] = "Male"
character_info["Aringoth"]["gender"] = "Male"
character_info["Brand-Shei"]["gender"] = "Male"
character_info["Vittoria"]["gender"] = "Female"
character_info["Fultheim"]["gender"] = "Male"
character_info["Alea"]["gender"] = "Female"
character_info["Vasha"]["gender"] = "Male"
character_info["Sanguine"]["gender"] = "Female"
character_info["Takes-In-Light"]["gender"] = "Female"
character_info["Arniel"]["gender"] = "Male"
character_info["Orthjolf"]["gender"] = "Male"
character_info["Madesi"]["gender"] = "Male"
character_info["Vignar"]["gender"] = "Male"
character_info["Balagog"]["gender"] = "Male"
character_info["Hern"]["gender"] = "Male"
character_info["Lurbuk"]["gender"] = "Male"
character_info["Nilsine"]["gender"] = "Female"
character_info["Beitild"]["gender"] = "Female"
character_info["Ennodius"]["gender"] = "Male"
character_info["Narfi"]["gender"] = "Male"
character_info["Thorek"]["gender"] = "Male"
character_info["Mathies"]["gender"] = "Male"
character_info["Orgnar"]["gender"] = "Male"
character_info["Borri"]["gender"] = "Male"
character_info["Hod"]["gender"] = "Male"
character_info["Talvas Fathryon"]["gender"] = "Male"
character_info["Hestla"]["gender"] = "Female"
character_info["Rargal"]["gender"] = "Male"
character_info["Vanik"]["gender"] = "Male"
character_info["Ronthil"]["gender"] = "Male"
character_info["Malkus"]["gender"] = "Male"
character_info["Stalf"]["gender"] = "Male"
character_info["Lokil"]["gender"] = "Male"
character_info["Celann"]["gender"] = "Male"
character_info["Garthar"]["gender"] = "Male"
character_info["Aicantar"]["gender"] = "Male"
character_info["Irgnir"]["gender"] = "Female"
character_info["Namira"]["gender"] = "Female"
character_info["Pelagius"]["gender"] = "Male"
character_info["Erdi"]["gender"] = "Female"
character_info["Una"]["gender"] = "Female"
character_info["Malyn"]["gender"] = "Male"
character_info["Estormo"]["gender"] = "Male"
character_info["Onmund"]["gender"] = "Male"
character_info["J'zargo"]["gender"] = "Male"
character_info["Brelyna"]["gender"] = "Female"
character_info["Tsavani"]["gender"] = "Female"
character_info["Sahloknir"]["gender"] = "Male"
character_info["Iddra"]["gender"] = "Female"
character_info["Wulfgar"]["gender"] = "Male"
character_info["Einarth"]["gender"] = "Male"
character_info["Hrongar"]["gender"] = "Male"
character_info["Sigrid"]["gender"] = "Female"
character_info["Frodnar"]["gender"] = "Male"
character_info["Sahrotaar"]["gender"] = "Male"
character_info["Fura"]["gender"] = "Female"
character_info["Feran"]["gender"] = "Male"
character_info["Edhelbor"]["gender"] = "Male"
character_info["Nirilor"]["gender"] = "Male"
character_info["Celegriath"]["gender"] = "Male"
character_info["Athring"]["gender"] = "Male"
character_info["Sidanyis"]["gender"] = "Male"
character_info["Salonia"]["gender"] = "Female"
character_info["Tonilia"]["gender"] = "Female"
character_info["Vipir"]["gender"] = "Male"
character_info["Sapphire"]["gender"] = "Female"
character_info["Thrynn"]["gender"] = "Male"
character_info["Niruin"]["gender"] = "Male"
character_info["Ravyn"]["gender"] = "Male"
character_info["Cynric"]["gender"] = "Male"
character_info["Commander Maro"]["gender"] = "Male"
character_info["Fruki"]["gender"] = "Female"
character_info["Hogni Red-Arm"]["gender"] = "Male"
character_info["Banning"]["gender"] = "Male"
character_info["Lisbet"]["gender"] = "Female"
character_info["Thongvor"]["gender"] = "Male"
character_info["Madena"]["gender"] = "Female"
character_info["J'Kier"]["gender"] = "Male"
character_info["Moira"]["gender"] = "Female"
character_info["Elvali"]["gender"] = "Female"
character_info["Vilod"]["gender"] = "Male"
character_info["Priestess of Arkay"]["gender"] = "Female"
character_info["Torolf"]["gender"] = "Male"
character_info["Haming"]["gender"] = "Male"
character_info["Tharstan"]["gender"] = "Male"
character_info["Morwen"]["gender"] = "Female"
character_info["Wulf Wild-Blood"]["gender"] = "Male"
character_info["Nikulas"]["gender"] = "Male"
character_info["Finna"]["gender"] = "Female"
character_info["Aeta"]["gender"] = "Female"
character_info["Deor"]["gender"] = "Male"
character_info["Edla"]["gender"] = "Female"
character_info["Fanari Strong-Voice"]["gender"] = "Female"
character_info["Krosulhah"]["gender"] = "Male"
character_info["Salonia Caelia"]["gender"] = "Female"
character_info["Adalvald"]["gender"] = "Male"
character_info["Rune"]["gender"] = "Male"
character_info["Aquilius"]["gender"] = "Male"
character_info["Drifa"]["gender"] = "Female"
character_info["Duilis"]["gender"] = "Male"
character_info["Frorkmar"]["gender"] = "Male"
character_info["Faida"]["gender"] = "Female"
character_info["Pantea"]["gender"] = "Female"
character_info["Alexia"]["gender"] = "Female"
character_info["Nura Snow-Shod"]["gender"] = "Female"
character_info["Asgeir Snow-Shod"]["gender"] = "Male"
character_info["Rexus"]["gender"] = "Male"
character_info["Alain"]["gender"] = "Male"
character_info["Francois"]["gender"] = "Male"
character_info["Samuel"]["gender"] = "Male"
character_info["Runa"]["gender"] = "Female"
character_info["Hroar"]["gender"] = "Male"
character_info["Hulda"]["gender"] = "Female"
character_info["Vaermina"]["gender"] = "Female"
character_info["Thoring"]["gender"] = "Male"
character_info["Sanyon"]["gender"] = "Male"
character_info["Nimphaneth"]["gender"] = "Female"
character_info["Falk"]["gender"] = "Male"
character_info["Rissing"]["gender"] = "Male"
character_info["Runil"]["gender"] = "Male"
character_info["Sulla"]["gender"] = "Male"
character_info["Umana"]["gender"] = "Female"
character_info["Lob"]["gender"] = "Male"
character_info["Ugor"]["gender"] = "Female"
character_info["Dagur"]["gender"] = "Male"
character_info["Athis"]["gender"] = "Male"
character_info["Njada"]["gender"] = "Female"
character_info["Brill"]["gender"] = "Male"
character_info["Girduin"]["gender"] = "Male"
character_info["Phinis Gestor"]["gender"] = "Male"
character_info["Sergius"]["gender"] = "Male"
character_info["Gavros"]["gender"] = "Male"
character_info["Jyrik Gaulderson"]["gender"] = "Male"
character_info["Nerien"]["gender"] = "Male"
character_info["Ysgramor"]["gender"] = "Male"
character_info["Torygg"]["gender"] = "Male"
character_info["Mirmulnir"]["gender"] = "Male"
character_info["Dorthe"]["gender"] = "Female"
character_info["Gunnar"]["gender"] = "Male"
character_info["Headsman"]["gender"] = "Male"
character_info["Ingrid"]["gender"] = "Female"

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

# Create a dataframe to store character information
dataframe = []
for character, info in character_info.items():
    dataframe.append(
        {
            "Title": "Elder Scrolls Skyrim",
            "Year": "2011",
            "Country": "US",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Ulfric": "Ulfric Stormcloak",
    "Galmar": "Galmar Stone-Fist",
    "Tullius": "General Tullius",
    "Rikke": "Legate Rikke",
    "Balgruuf": "Balgruuf the Greater",
    "Harkon": "Lord Harkon",
    "Gelebor": "Knight-Paladin Gelebor",
    "Mercer": "Mercer Frey",
    "Dexion": "Dexion Evicus",
    "Kodlak": "Kodlak Whitemane",
    "Savos": "Savos Aren",
    "Silus": "Silus Vesuius",
    "Aela": "Aela the Huntress",
    "Urag": "Urag gro-Shub",
    "Festus": "Festus Krex",
    "Hermaeus": "Hermaeus Mora",
    "Mirabelle": "Mirabelle Ervine",
    "Paratus": "Paratus Decimius",
    "Maven": "Maven Black-Briar",
    "Storn": "Storn Crag-Strider",
    "Gallus": "Gallus Desidenius",
    "Amaund": "Amaund Motierre",
    "Eorlund": "Eorlund Gray-Mane",
    "Proventus": "Proventus Avenicci",
    "Farengar": "Farengar Secret-Fire",
    "Garan": "Garan Marethi",
    "Delvin": "Delvin Mallory",
    "Verulus": "Brother Verulus",
    "Gormlaith": "Gormlaith Golden-Hilt",
    "Septimus": "Septimus Signus",
    "Etienne": "Etienne Rarnis",
    "Logrolf": "Logrolf the Willful",
    "Mallus": "Mallus Maccius",
    "Aranea": "Aranea Ienith",
    "Hakon": "Hakon One-Eye",
    "Aventus": "Aventus Aretino",
    "Yamarz": "Chief Yamarz",
    "Felldir": "Felldir the Old",
    "Vekel": "Vekel the Man",
    "Gjalund": "Gjalund Salt-Sage",
    "Bersi": "Bersi Honey-Hand",
    "Vyrthur": "Arch-Curate Vyrthur",
    "Sorine": "Sorine Jurard",
    "Clavicus": "Clavicus Vile",
    "Sam": "Sam Guevenne",
    "Adril": "Adril Arano",
    "Cipius": "Legate Quentin Cipius",
    "Tyranus": "Vigilant Tyranus",
    "Elisif": "Elisif the Fair",
    "Grelod": "Grelod the Kind",
    "Idgrod": "Idgrod Ravencrone",
    "Veren": "Veren Duleri",
    "Varona": "Varona Nelas",
    "Gaius": "Gaius Maro",
    "Kesh": "Kesh the Clean",
    "Augur": "Augur of Dunlain",
    "Orthus": "Orthus Endario",
    "Corpulus": "Corpulus Vinius",
    "Caius": "Commander Caius",
    "Anton": "Anton Virane",
    "Hafnar": "Hafnar Ice-Fist",
    "Arvel": "Arvel the Swift",
    "Tolan": "Vigilant Tolan",
    "Vittoria": "Vittoria Vici",
    "Alea": "Aela the Huntress",
    "Arniel": "Arniel Gane",
    "Vignar": "Vignar Gray-Mane",
    "Balagog": "Balagog gro-Nolob",
    "Nilsine": "Nilsine Shatter-Shield",
    "Ennodius": "Ennodius Papius",
    "Rargal": "Rargal Thrallmaster",
    "Pelagius": "Pelagius the Mad",
    "Malyn": "Malyn Varen",
    "Brelyna": "Brelyna Maryon",
    "Fura": "Fura Bloodmouth",
    "Feran": "Feran Sadri",
    "Edhelbor": "Prelate Edhelbor",
    "Nirilor": "Prelate Nirilor",
    "Celegriath": "Prelate Celegriath",
    "Athring": "Prelate Athring",
    "Sidanyis": "Prelate Sidanyis",
    "Salonia": "Salonia Carvain",
    "Vipir": "Vipir the Fleet",
    "Ravyn": "Ravyn Imyan",
    "Cynric": "Cynric Endell",
    "Thongvor": "Thongvor Silver-Blood",
    "Elvali": "Elvali Veren",
    "Deor": "Deor Woodcutter",
    "Adalvald": " Vigilant Adalvald",
    "Aquilius": "Aquillius Aeresius",
    "Duilis": "Legate Taurinus Duilis",
    "Frorkmar": "Frorkmar Banner-Torn",
    "Pantea": "Pantea Ateia",
    "Alexia": "Alexia Vici",
    "Alain": "Alain Dufont",
    "Francois": "Francois Beaufort",
    "Runa": "Runa Fair-Shield",
    "Falk": "Falk Firebeard",
    "Sulla": "Sulla Trebatius",
    "Njada": "Njada Stonearm",
    "Sergius": "Sergius Turrianus",
    "Gavros": "Gavros Plinius",
    "Jyrik Gaulderson": "Jyrik Gauldurson",
    "Gunnar": "Gunnar Stone-Eye",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable charaters
PC = ["Dragonborn"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/elder_scrolls_skyrim/data.csv", index=False)
