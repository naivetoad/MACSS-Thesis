# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/disco_elysium/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "You",
    "Kim Kitsuragi",
    "Cuno",
    "Klaasje (Miss Oranje Disco Dancer)",
    "The Deserter",
    "Joyce Messier",
    "Claire",
    "Garte, the Cafeteria Manager",
    "Lena, the Cryptozoologist's wife",
    "Soona, the Programmer",
    "Idiot Doom Spiral",
    "Jean Vicquemare",
    "Noid",
    "Titus Hardie",
    "Acele",
    "Andre",
    "Plaisance",
    "Bird's Nest Roy",
    "Lilienne, the Net Picker",
    "Steban, the Student Communist",
    "Novelty Dicemaker",
    "Gary, the Cryptofascist",
    "Egg Head",
    "Measurehead",
    "Sunday Friend",
    "Call Me Mañana",
    "René Arnoux",
    "Annette",
    "Working Class Woman",
    "Dolores Dei",
    "Cindy the SKULL",
    "Washerwoman",
    "Trant Heidelstam",
    "Gaston Martin",
    "Cunoesse",
    "Racist lorry driver",
    "Tommy Le Homme",
    "Siileng",
    "Mega Rich Light-Bending Guy",
    "Morell, the Cryptozoologist",
    "Smoker on the Balcony",
    "Ruby, the Instigator",
    "Man with Sunglasses",
    "Paledriver",
    "Frittte clerk",
    "Scab Leader",
    "Easy Leo",
    "Alice",
    "Tiago",
    "The Hanged Man",
    "Elizabeth",
    "Jules Pidieu",
    "Judit Minot",
    "Echo Maker",
    "Rosemary",
    "Sylvie",
    "Alain",
    "The Gardener",
    "Eugene",
    "Little Lily",
    "Cleaning Lady",
    "Horse-Faced Woman",
    "East-Insulindian Repeater Station",
    "Pissf****t",
    "Lilienne's Twin",
    "Fuck the World",
    "Measurehead's Babe",
    "The Pigs",
    "Shanky",
    "Lilienne's Other Twin",
    "DJ Mesh",
    "Sleeping Dockworker",
    "Glen",
    "Don't Call Abigail",
    "Nix Gottlieb",
    "Mack Torson",
    "Kortenaer",
    "Man on water lock",
    "Chester McLaine",
    "Real Estate Agent",
    "Gorący Kubek",
    "Bloated Corpse of a Drunk",
    "Theo",
    "Cuno's Dad",
    "Working Class Corpse",
    "Moneyman",
    "Fat Angus",
    "Mikael Heidelstam",
    "Ruud Hoenkloewen",
    "DJ Flacio",
    "Netpicker's Twins",
    "De Paule",
    "Tare Drunk",
    "Barry the Butcher",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["You"]["gender"] = "Male"
character_info["Kim Kitsuragi"]["gender"] = "Female"
character_info["Cuno"]["gender"] = "Male"
character_info["Klaasje (Miss Oranje Disco Dancer)"]["gender"] = "Female"
character_info["The Deserter"]["gender"] = "Male"
character_info["Joyce Messier"]["gender"] = "Female"
character_info["Claire"]["gender"] = "Male"
character_info["Garte, the Cafeteria Manager"]["gender"] = "Male"
character_info["Lena, the Cryptozoologist's wife"]["gender"] = "Female"
character_info["Soona, the Programmer"]["gender"] = "Female"
character_info["Idiot Doom Spiral"]["gender"] = "Male"
character_info["Jean Vicquemare"]["gender"] = "Male"
character_info["Noid"]["gender"] = "Male"
character_info["Titus Hardie"]["gender"] = "Male"
character_info["Acele"]["gender"] = "Female"
character_info["Andre"]["gender"] = "Male"
character_info["Plaisance"]["gender"] = "Female"
character_info["Bird's Nest Roy"]["gender"] = "Male"
character_info["Lilienne, the Net Picker"]["gender"] = "Female"
character_info["Steban, the Student Communist"]["gender"] = "Male"
character_info["Novelty Dicemaker"]["gender"] = "Female"
character_info["Gary, the Cryptofascist"]["gender"] = "Male"
character_info["Egg Head"]["gender"] = "Male"
character_info["Measurehead"]["gender"] = "Male"
character_info["Sunday Friend"]["gender"] = "Male"
character_info["Call Me Mañana"]["gender"] = "Male"
character_info["René Arnoux"]["gender"] = "Male"
character_info["Annette"]["gender"] = "Female"
character_info["Working Class Woman"]["gender"] = "Female"
character_info["Dolores Dei"]["gender"] = "Female"
character_info["Cindy the SKULL"]["gender"] = "Female"
character_info["Washerwoman"]["gender"] = "Female"
character_info["Trant Heidelstam"]["gender"] = "Male"
character_info["Gaston Martin"]["gender"] = "Male"
character_info["Cunoesse"]["gender"] = "Female"
character_info["Racist lorry driver"]["gender"] = "Male"
character_info["Tommy Le Homme"]["gender"] = "Male"
character_info["Siileng"]["gender"] = "Male"
character_info["Mega Rich Light-Bending Guy"]["gender"] = "Male"
character_info["Morell, the Cryptozoologist"]["gender"] = "Male"
character_info["Smoker on the Balcony"]["gender"] = "Male"
character_info["Ruby, the Instigator"]["gender"] = "Female"
character_info["Man with Sunglasses"]["gender"] = "Male"
character_info["Paledriver"]["gender"] = "Female"
character_info["Frittte clerk"]["gender"] = "Female"
character_info["Scab Leader"]["gender"] = "Male"
character_info["Easy Leo"]["gender"] = "Male"
character_info["Alice"]["gender"] = "Female"
character_info["Tiago"]["gender"] = "Male"
character_info["The Hanged Man"]["gender"] = "Male"
character_info["Elizabeth"]["gender"] = "Female"
character_info["Jules Pidieu"]["gender"] = "Male"
character_info["Judit Minot"]["gender"] = "Female"
character_info["Echo Maker"]["gender"] = "Male"
character_info["Rosemary"]["gender"] = "Male"
character_info["Sylvie"]["gender"] = "Female"
character_info["Alain"]["gender"] = "Male"
character_info["The Gardener"]["gender"] = "Female"
character_info["Eugene"]["gender"] = "Male"
character_info["Little Lily"]["gender"] = "Female"
character_info["Cleaning Lady"]["gender"] = "Female"
character_info["Horse-Faced Woman"]["gender"] = "Female"
character_info["East-Insulindian Repeater Station"]["gender"] = "Female"
character_info["Pissf****t"]["gender"] = "Male"
character_info["Lilienne's Twin"]["gender"] = "Male"
character_info["Fuck the World"]["gender"] = "Male"
character_info["Measurehead's Babe"]["gender"] = "Female"
character_info["The Pigs"]["gender"] = "Male"
character_info["Shanky"]["gender"] = "Male"
character_info["Lilienne's Other Twin"]["gender"] = "Male"
character_info["DJ Mesh"]["gender"] = "Male"
character_info["Sleeping Dockworker"]["gender"] = "Male"
character_info["Glen"]["gender"] = "Male"
character_info["Don't Call Abigail"]["gender"] = "Male"
character_info["Nix Gottlieb"]["gender"] = "Male"
character_info["Mack Torson"]["gender"] = "Male"
character_info["Kortenaer"]["gender"] = "Male"
character_info["Man on water lock"]["gender"] = "Male"
character_info["Chester McLaine"]["gender"] = "Male"
character_info["Real Estate Agent"]["gender"] = "Female"
character_info["Gorący Kubek"]["gender"] = "Male"
character_info["Bloated Corpse of a Drunk"]["gender"] = "Male"
character_info["Theo"]["gender"] = "Male"
character_info["Cuno's Dad"]["gender"] = "Male"
character_info["Working Class Corpse"]["gender"] = "Male"
character_info["Moneyman"]["gender"] = "Male"
character_info["Fat Angus"]["gender"] = "Male"
character_info["Mikael Heidelstam"]["gender"] = "Male"
character_info["Ruud Hoenkloewen"]["gender"] = "Male"
character_info["DJ Flacio"]["gender"] = "Male"
character_info["Netpicker's Twins"]["gender"] = "Male"
character_info["De Paule"]["gender"] = "Female"
character_info["Tare Drunk"]["gender"] = "Male"
character_info["Barry the Butcher"]["gender"] = "Male"

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
            "Title": "Disco Elysium",
            "Year": "2019",
            "Country": "UK",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "You": "Harrier Du Bois",
    "Klaasje (Miss Oranje Disco Dancer)": "Klaasje Amandou",
    "Claire": "Evrart Claire",
    "Garte": "Lawrence Garte",
    "Soona, the Programmer": "Soona Luukanen-Kilde",
    "Acele": "Acele Berger",
    "Andre": "Pete Andre",
    "Lilienne, the Net Picker": "Lilienne Carter",
    "Sunday Friend": "Charles Villedrouin",
    "Working Class Woman": "Billie Méjean",
    "Cunoesse": "Cunoesse Vittulainen",
    "Racist lorry driver": "Racist Lorry Driver",
    "Man with Sunglasses": "Jean Vicquemare",
    "Frittte clerk": "Frittte Clerk",
    "Scab Leader": "Raul Kortenaer",
    "Alice": "Alice DeMettrie",
    "The Hanged Man": "Ellis Kortenaer",
    "Elizabeth": "Elizabeth Beaufort",
    "Sylvie": "Sylvie Malaìika",
    "The Gardener": "Elizabeth Beaufort",
    "Little Lily": "Lily Carter",
    "Horse-Faced Woman": "Judit Minot",
    "East-Insulindian Repeater Station": "Yvonne",
    "Pissf****t": "Eric",
    "Lilienne's Twin": "Lilienne's Twins",
    "Lilienne's Other Twin": "Lilienne's Twins",
    "Sleeping Dockworker": "Santiago S. John",
    "Kortenaer": "Raul Kortenaer",
    "Man on water lock": "Man on Water Lock",
    "Real Estate Agent": "Marielle Charpentier",
    "Bloated Corpse of a Drunk": "Harrier Du Bois",
    "Cuno's Dad": "Uuno de Ruyter",
    "Working Class Corpse": "Victor Méjean",
    "Moneyman": "Mega Rich Light-Bending Guy",
    "Netpicker's Twins": "Lilienne's Twins",
    "De Paule": "Phillis de Paule",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable charaters
PC = ["Harrier Du Bois"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/disco_elysium/data.csv", index=False)
