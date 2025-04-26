# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/persona_5/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Morgana",
    "Ryuji Sakamoto",
    "Ann Takamaki",
    "Makoto Niijima",
    "Yusuke Kitagawa",
    "Futaba Sakura",
    "Joker",
    "Haru Okumura",
    "Sojiro Sakura",
    "Goro Akechi",
    "Yuuki Mishima",
    "Sae Niijima",
    "Sadayo Kawakami",
    "Chihaya Mifune",
    "Tae Takemi",
    "Ichiko Ohya",
    "Hifumi Togo",
    "Justine",
    "Munehisa Iwai",
    "Caroline",
    "Shinya Oda",
    "Toranosuke Yoshida",
    "Masayoshi Shido",
    "Igor",
    "Lala Escargot",
    "SIU Director",
    "Inui",
    "Shadow Suguru Kamoshida",
    "Shadow Junya Kaneshiro",
    "Shadow Ichiryusai Madarame",
    "Suguru Kamoshida",
    "Shadow Sae Niijima",
    "Chouno",
    "Matsushita",
    "Principal",
    "Lavenza",
    "Ushimaru",
    "Shadow Futaba Sakura",
    "Eiko Takao",
    "Usami",
    "Kaoru",
    "Hiruta",
    "Shadow Kunikazu Okumura",
    "Shiho Suzui",
    "President Tanaka",
    "Ichiryusai Madarame",
    "Alibaba",
    "Masa",
    "Mika",
    "Akiyama",
    "Takakura",
    "Scruffy Romantic",
    "Tsukasa",
    "Futaba's Uncle",
    "Tsuda",
    "Takeishi",
    "Junya Kaneshiro",
    "Iida",
    "Sugimura",
    "Kunikazu Okumura",
    "Benzo",
    "Nakaoka",
    "Shadow Masayoshi Shido",
    "Wakaba Isshiki",
    "Yuuta",
    "Shiro Asakura",
    "Ikeda",
    "Takekuma",
    "Chairman Fukurai",
    "Natsuhiko Nakanohara",
    "Hanasaki",
    "Clara",
    "Yamauchi",
    "Yokoda",
    "Shadow Yuuki Mishima",
    "Shadow Oyamada",
    "Nanami",
    "Shadow Makigami",
    "Kotaro",
    "Akitsu",
    "Shadow Nejima",
    "Shadow Kiritani",
    "Shadow Yuichi Fukurai",
    "Shadow Tsuboi",
    "Shadow Mogami",
    "Shadow Sakoda",
    "Nishiyama",
    "Shadow Shimizu",
    "Shadow Natsuhiko Nakanohara",
    "Asakura",
    "Shadow Wakasa",
    "Shadow Mrs Magario",
    "ShadowTsuda",
    "Tohru",
    "Shadow Jochi",
    "Shadow Kishi",
    "Shadow Mr Takase",
    "Shadow Takanashi",
    "Ikesugi",
    "Shadow Mr Magario",
    "Shadow Honyo",
    "Shadow Naguri",
    "Shadow Mrs Takase",
    "Yasuo Jochi",
    "Shadow Odo",
    "Futaba's Mother",
    "Shadow Uchimura",
    "Daisuke Takanashi",
    "Shinsuke Kishi",
    "Shadow Asakura",
    "Yoshimora Sakoda",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Morgana"]["gender"] = "Male"
character_info["Ryuji Sakamoto"]["gender"] = "Male"
character_info["Ann Takamaki"]["gender"] = "Female"
character_info["Makoto Niijima"]["gender"] = "Female"
character_info["Yusuke Kitagawa"]["gender"] = "Male"
character_info["Futaba Sakura"]["gender"] = "Female"
character_info["Joker"]["gender"] = "Male"
character_info["Haru Okumura"]["gender"] = "Female"
character_info["Sojiro Sakura"]["gender"] = "Male"
character_info["Goro Akechi"]["gender"] = "Male"
character_info["Yuuki Mishima"]["gender"] = "Male"
character_info["Sae Niijima"]["gender"] = "Female"
character_info["Sadayo Kawakami"]["gender"] = "Female"
character_info["Chihaya Mifune"]["gender"] = "Female"
character_info["Tae Takemi"]["gender"] = "Female"
character_info["Ichiko Ohya"]["gender"] = "Female"
character_info["Hifumi Togo"]["gender"] = "Female"
character_info["Justine"]["gender"] = "Female"
character_info["Munehisa Iwai"]["gender"] = "Male"
character_info["Caroline"]["gender"] = "Female"
character_info["Shinya Oda"]["gender"] = "Male"
character_info["Toranosuke Yoshida"]["gender"] = "Male"
character_info["Masayoshi Shido"]["gender"] = "Male"
character_info["Igor"]["gender"] = "Male"
character_info["Lala Escargot"]["gender"] = "Female"
character_info["SIU Director"]["gender"] = "Male"
character_info["Inui"]["gender"] = "Male"
character_info["Shadow Suguru Kamoshida"]["gender"] = "Male"
character_info["Shadow Junya Kaneshiro"]["gender"] = "Male"
character_info["Shadow Ichiryusai Madarame"]["gender"] = "Male"
character_info["Suguru Kamoshida"]["gender"] = "Male"
character_info["Shadow Sae Niijima"]["gender"] = "Female"
character_info["Chouno"]["gender"] = "Female"
character_info["Matsushita"]["gender"] = "Male"
character_info["Principal"]["gender"] = "Male"
character_info["Lavenza"]["gender"] = "Female"
character_info["Ushimaru"]["gender"] = "Male"
character_info["Shadow Futaba Sakura"]["gender"] = "Female"
character_info["Eiko Takao"]["gender"] = "Female"
character_info["Usami"]["gender"] = "Female"
character_info["Kaoru"]["gender"] = "Male"
character_info["Hiruta"]["gender"] = "Male"
character_info["Shadow Kunikazu Okumura"]["gender"] = "Male"
character_info["Shiho Suzui"]["gender"] = "Female"
character_info["President Tanaka"]["gender"] = "Male"
character_info["Ichiryusai Madarame"]["gender"] = "Male"
character_info["Alibaba"]["gender"] = "Female"
character_info["Masa"]["gender"] = "Male"
character_info["Mika"]["gender"] = "Female"
character_info["Akiyama"]["gender"] = "Male"
character_info["Takakura"]["gender"] = "Male"
character_info["Scruffy Romantic"]["gender"] = "Female"
character_info["Tsukasa"]["gender"] = "Male"
character_info["Futaba's Uncle"]["gender"] = "Male"
character_info["Tsuda"]["gender"] = "Male"
character_info["Takeishi"]["gender"] = "Male"
character_info["Junya Kaneshiro"]["gender"] = "Male"
character_info["Iida"]["gender"] = "Male"
character_info["Sugimura"]["gender"] = "Male"
character_info["Kunikazu Okumura"]["gender"] = "Male"
character_info["Benzo"]["gender"] = "Male"
character_info["Nakaoka"]["gender"] = "Male"
character_info["Shadow Masayoshi Shido"]["gender"] = "Male"
character_info["Wakaba Isshiki"]["gender"] = "Female"
character_info["Yuuta"]["gender"] = "Male"
character_info["Shiro Asakura"]["gender"] = "Male"
character_info["Ikeda"]["gender"] = "Male"
character_info["Takekuma"]["gender"] = "Male"
character_info["Chairman Fukurai"]["gender"] = "Male"
character_info["Natsuhiko Nakanohara"]["gender"] = "Male"
character_info["Hanasaki"]["gender"] = "Female"
character_info["Clara"]["gender"] = "Female"
character_info["Yamauchi"]["gender"] = "Male"
character_info["Yokoda"]["gender"] = "Male"
character_info["Shadow Yuuki Mishima"]["gender"] = "Male"
character_info["Shadow Oyamada"]["gender"] = "Male"
character_info["Nanami"]["gender"] = "Female"
character_info["Shadow Makigami"]["gender"] = "Male"
character_info["Kotaro"]["gender"] = "Male"
character_info["Akitsu"]["gender"] = "Male"
character_info["Shadow Nejima"]["gender"] = "Male"
character_info["Shadow Kiritani"]["gender"] = "Male"
character_info["Shadow Yuichi Fukurai"]["gender"] = "Male"
character_info["Shadow Tsuboi"]["gender"] = "Male"
character_info["Shadow Mogami"]["gender"] = "Female"
character_info["Shadow Sakoda"]["gender"] = "Male"
character_info["Nishiyama"]["gender"] = "Male"
character_info["Shadow Shimizu"]["gender"] = "Female"
character_info["Shadow Natsuhiko Nakanohara"]["gender"] = "Male"
character_info["Asakura"]["gender"] = "Male"
character_info["Shadow Wakasa"]["gender"] = "Male"
character_info["Shadow Mrs Magario"]["gender"] = "Female"
character_info["ShadowTsuda"]["gender"] = "Male"
character_info["Tohru"]["gender"] = "Male"
character_info["Shadow Jochi"]["gender"] = "Male"
character_info["Shadow Kishi"]["gender"] = "Male"
character_info["Shadow Mr Takase"]["gender"] = "Male"
character_info["Shadow Takanashi"]["gender"] = "Male"
character_info["Ikesugi"]["gender"] = "Male"
character_info["Shadow Mr Magario"]["gender"] = "Male"
character_info["Shadow Honyo"]["gender"] = "Male"
character_info["Shadow Naguri"]["gender"] = "Male"
character_info["Shadow Mrs Takase"]["gender"] = "Female"
character_info["Yasuo Jochi"]["gender"] = "Male"
character_info["Shadow Odo"]["gender"] = "Male"
character_info["Futaba's Mother"]["gender"] = "Female"
character_info["Shadow Uchimura"]["gender"] = "Male"
character_info["Daisuke Takanashi"]["gender"] = "Male"
character_info["Shinsuke Kishi"]["gender"] = "Male"
character_info["Shadow Asakura"]["gender"] = "Male"
character_info["Yoshimora Sakoda"]["gender"] = "Male"

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
            "Title": "Persona 5",
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
    "Joker": "Ren Amamiya",
    "Inui": "Mr. Inui",
    "Chouno": "Ms. Chouno",
    "Principal": "Kobayakawa",
    "Ushimaru": "Mr. Ushimaru",
    "Usami": "Ms. Usami",
    "Hiruta": "Mr. Hiruta",
    "Alibaba": "Futaba Sakura",
    "Scruffy Romantic": "Julian",
    "Tsuda": "Akimitsu Tsuda",
    "Yuuta": "Yuuta Minami",
    "Chairman Fukurai": "Fukurai",
    "Shadow Makigami": "Shadow Kazuya Makigami",
    "Asakura": "Shiro Asakura",
    "Shadow Mrs Magario": "Shadow Mrs. Magario",
    "ShadowTsuda": "Shadow Tsuda",
    "Tohru": "Tohru Adachi",
    "Shadow Mr Takase": "Shadow Mr. Takase",
    "Shadow Mr Magario": "Shadow Mr. Magario",
    "Shadow Honyo": "Shadow Honjo",
    "Shadow Mrs Takase": "Shadow Mrs. Takase",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "Ren Amamiya",
    "Ryuji Sakamoto",
    "Morgana"
    "Ann Takamaki",
    "Makoto Niijima",
    "Futaba Sakura",
    "Haru Okumura",
    "Goro Akechi",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/persona_5/data.csv", index=False)
