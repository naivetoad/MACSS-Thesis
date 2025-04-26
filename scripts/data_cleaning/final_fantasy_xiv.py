# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/final_fantasy_xiv/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Alphinaud",
    "Alisaie",
    "Y'shtola",
    "Thancred",
    "Lyse",
    "Urianger",
    "G'raha Tia",
    "The Adventurer",
    "Ryne",
    "Tataru",
    "Estinien",
    "Yugiri",
    "Hien",
    "Raubahn",
    "Aymeric",
    "Minfilia Warde",
    "Cid",
    "Krile",
    "Lucia",
    "Chai-Nuzz",
    "Gosetsu",
    "Ysayle",
    "Papalymo",
    "Pipin",
    "Lyna",
    "Almet",
    "Emmanellain",
    "Kan-E-Senna",
    "Elidibus",
    "Arenvald",
    "Haurchefant",
    "Dulia-Chai",
    "M'naago",
    "Runar",
    "Emet-Selch",
    "Cirina",
    "Artoirel",
    "Merlwyb",
    "Ardbert",
    "Ran'jit",
    "Count Edmont de Fortemps",
    "Jeryk",
    "Ilberd",
    "Wedge",
    "Honoroit",
    "Kai-Shirr",
    "Hilda",
    "Conrad",
    "Meffrid",
    "Hancock",
    "Nanamo Ul Namo",
    "Thaffe",
    "Magnus",
    "Uimet",
    "Moren",
    "Cymet",
    "Zenos Galvus",
    "Soroban",
    "Hoary Boulder",
    "Matoya",
    "Hraesvelgr",
    "Vidofnir",
    "Biggs",
    "Riol",
    "Momodi",
    "Tansui",
    "Wiscar",
    "Manager of Suites",
    "Korutt",
    "Baderon",
    "Alianne",
    "Gaius",
    "Wrenden",
    "Yozan",
    "Kuplo Kopp",
    "Coultenet",
    "Tristol",
    "Seto",
    "Mother Miounne",
    "Ga Bu",
    "Rasho",
    "Tista-Bie",
    "Slafborn",
    "Redwald",
    "Drillemont",
    "Theyler",
    "Papashan",
    "Isse",
    "Tesleen",
    "Maxima",
    "Xamott",
    "Chessamile",
    "F'lhaminn",
    "Archbishop Thordan VII",
    "Fufulupa",
    "Szem Djenmai",
    "Magnai",
    "Bartholomew",
    "Zanthael",
    "Cassard",
    "Riqi-Tio",
    "Glynard",
    "Nero",
    "Sadu",
    "Guthjon",
    "Moghan",
    "Komuxio",
    "Midgardsormr",
    "Shamani Lohmani",
    "Nidhogg",
    "Buscarron",
    "Wheiskaet",
    "Asahi",
    "Hozan",
    "Dorbei",
    "Staelwyrn",
    "Bragi",
    "V'mah Tia",
    "Temulun",
    "Hakuro",
    "Eirwel",
    "Eynzahr Slafyrsyn",
    "Katliss",
    "Baatu",
    "Gundobald",
    "Lahabrea",
    "Lonu Vanu",
    "Yuyuhase",
    "Vorsaile Heuloix",
    "Brayflox Alltalks",
    "Handeloup",
    "J'moldva",
    "Halric",
    "Carvallain",
    "Arkil",
    "Koharu",
    "Azami",
    "Lionnellais",
    "Ephemie",
    "Laniaitte",
    "Ceana",
    "Gibrillont",
    "Raganfrid",
    "Wilred",
    "Moglin",
    "Ravana",
    "Trachtoum",
    "Eline Roaille",
    "Tsuranuki",
    "Edelstein",
    "Owyne",
    "Lewin",
    "Sevrin",
    "Fordola",
    "Portelaine",
    "Moenbryda",
    "Slowfix",
    "L'nophlo",
    "Irvithe",
    "U'odh Nunh",
    "Gods' Quiver Bow",
    "Ungust",
    "Skaenrael",
    "Homei",
    "Glaumunt",
    "Cyella",
    "Rothe",
    "Kaidate",
    "Haname",
    "Laurentius",
    "Isembard",
    "Marques",
    "Grithil",
    "Mutamix",
    "Marcechamp",
    "Leofric",
    "Galfrid",
    "Bloeidin",
    "Isildaure",
    "Theva",
    "Zephirin",
    "Hythlodaeus",
    "Dewlala",
    "Higiri",
    "Watt",
    "Grenoldt",
    "Ele",
    "Fourchenault",
    "Yotsuyu",
    "Luquelot",
    "Frixio",
    "Daidukul",
    "Marcelain",
    "Atharn",
    "Regula van Hydrus",
    "Varis",
    "Thoarich",
    "Falkbryda",
    "Baldewyn",
    "Keitha",
    "Udutai",
    "Tiamat",
    "Elyenora",
    "Igeyorhm",
    "Eudestand",
    "Symme",
    "Clemence",
    "Aenor",
    "Ocher Boulder",
    "Kikyo",
    "Kasasagi",
    "Landenel",
    "Sonu Vanu",
    "Aideen",
    "Motojiro",
    "Mimidoa",
    "Raya-O-Senna",
    "Reyner",
    "Ihanashi",
    "Parsemontret",
    "The Griffin",
    "Bismarck",
    "Todden",
    "Pawnil",
    "Lolorito",
    "Wystan",
    "Medrod",
    "Willfort",
    "Marielle",
    "Rammbroes",
    "Venat",
    "Drest",
    "Vonard",
    "Voyne",
    "Eybor",
    "Chaunollet",
    "Loanne",
    "Ourcen",
    "Lamberteint",
    "Charibert",
    "Vauthry",
    "Julia quo Soranus",
    "Forlemort",
    "Francel",
    "Glagg",
    "Ivaurault",
    "Sylvetrel de Dzemael",
    "Ihanami",
    "Davyd",
    "Shiosai",
    "Rolfe Hawthorne",
    "Garibald",
    "Swift",
    "Yaelle",
    "Keeper of the Entwined Serpents",
    "Prunilla",
    "Godbert",
    "Griseldis",
    "Ahelissa",
    "Master of Shofuku Shichiten",
    "Narengawa",
    "Ucugen",
    "Grey Fleet Miller",
    "Chigusa",
    "Gogg Dwarf",
    "Wercrata",
    "Hahasako",
    "Ursandel",
    "Teledji Adeledji",
    "Cotan",
    "Mogwin",
    "Yunagi",
    "Dolorous Bear",
    "Haustefort",
    "Sozai Rarzai",
    "Eyrimhus",
    "Seseroga",
    "Nenebaru",
    "Nicia",
    "Swozblaet",
    "Sundhimal",
    "Quentenain",
    "S'dhodjbi",
    "Eluned",
    "Bertliana",
    "Hedyn",
    "Maelie",
    "Knolexia",
    "Jakys Ryder",
    "Ersabel",
    "Miraudont the Madder",
    "Lue-Reeq",
    "Granson",
    "Cerigg",
    "Giott",
    "Astidien",
    "Kajika",
    "Fyrilsmyd",
    "Warin",
    "Bujeg",
    "Myrcant",
    "Roseline",
    "Talebot",
    "Hihibaru",
    "Aethelmaer",
    "Beves",
    "Thierremont",
    "Edda",
    "Cenota",
    "Sark Malark",
    "Wymond",
    "Orella",
    "Bluomwyda",
    "Thubyrgeim",
    "Byrglaent",
    "Hirase",
    "Kotokaze",
    "Vath Fleetfoot",
    "Afumi",
    "Sicard",
    "Chambui",
    "Miyama",
    "Aranami",
    "Guillaime",
    "Estaine",
    "Khanswys",
    "Ahtbyrm",
    "Mogmug",
    "Y'mhitra",
    "Pfrewahl",
    "Janremi Blackheart",
    "Flavien de Fortemps",
    "E-Sumi-Yan",
    "Doware",
    "Ingaret",
    "Noirterel",
    "Emerissel",
    "Auriaune",
    "Tourcenet",
    "Ermegarde",
    "Aylmer",
    "Zazawaka",
    "Fandaniel",
    "Yuyutazi",
    "Bubukkuli",
    "Tutumoko",
    "Ryssfloh",
    "Ludovoix",
    "Pierriquet",
    "Jantellot",
    "Joellaut",
    "Aergmhus",
    "Masgud",
    "Hathenbet",
    "Serendipity",
    "Cracked Fist",
    "Midnight Dew",
    "Karaku",
    "Mosha-Moa",
    "Kupta Kapa",
    "Annia quo Soranus",
    "Qoyar",
    "Koko",
    "Mergen",
    "Honami",
    "Baidur",
    "Yesui",
    "Sifrid",
    "Lyulf",
    "Cassana",
    "Skyfryn",
    "Ceinguled",
    "Rhoswen",
    "Roger",
    "Begrimed Bloke",
    "Yagoro",
    "Eylgar",
    "Jocea",
    "Swynbroes",
    "Haldrath",
    "Painted Mesa",
    "Grimold",
    "Loupard",
    "Yusui",
    "Hiun",
    "Elaisse",
    "Gallien",
    "Albreda",
    "Shiun",
    "Rokka",
    "R'ashaht Rhiki",
    "Josseloux",
    "Liavinne",
    "Kikina",
    "E'manafa",
    "Beatin",
    "Theophilain",
    "Iliud",
    "Chadden",
    "Monranguin",
    "Adelstan",
    "Aurildis",
    "Swaenhylt",
    "Knerl",
    "Eginolf",
    "Ghimthota",
    "Paulecrain",
    "Grinnaux",
    "Ghen Gen",
    "Kunu Vali",
    "Pauline",
    "Cornenne",
    "J'nasshym",
    "Armelle",
    "Gilow",
    "Dalmascan Fusilier",
    "Asgeir",
    "Kupli Kipp",
    "Haldbroda",
    "Keiten",
    "Otelin",
    "Wauter",
    "Edmelle",
    "Ninne",
    "Aokumo",
    "M'hahtoa",
    "M'rahz Nunh",
    "Carrilaut",
    "Hida",
    "Brunadier",
    "Nimbus",
    "Ernold",
    "Hardyss",
    "Angry River",
    "Yayazuku",
    "Osric",
    "Gisilbehrt",
    "Dadanen",
    "Raffe",
    "Alestan",
    "Louistiaux of the First Line",
    "Tristechambel",
    "Adelphel",
    "Bernadette",
    "Fromelaut",
    "Yellow Moon",
    "H'naanza",
    "Monne",
    "Adalbert",
    "Sekiseigumi Blade",
    "Merilda",
    "Hierytha",
    "Baensyng",
    "Gegeruju",
    "Rowena",
    "Styrnlona",
    "Adala",
    "Shiva",
    "Kokosamu",
    "F'hobas",
    "Ewmond",
    "Bernard",
    "Junghbhar",
    "Avere",
    "Firkmann",
    "L'khonebb",
    "Bloisirant",
    "Alboise",
    "Gracine",
    "Faramund",
    "Ysaudore",
    "Ghon Gon",
    "Imedia",
    "Hastelot",
    "Abelie",
    "Rickeman",
    "Amelain",
    "Paiyo Reiyo",
    "Ignemortel",
    "Ombeline",
    "Pierremons",
    "Bricelt",
    "Ossine",
    "Theodore",
    "C'nangho",
    "Jeantremont",
    "Nawashiro",
    "Grehfarr",
    "F'zhumii",
    "Abylfarr",
    "Ahldskyf",
    "Vortefaurt",
    "Blauthota",
    "Shinobi",
    "Rhesh Polaali",
    "Beltardois",
    "Mowen",
    "Leonnie",
    "Tebbe",
    "Gerraldieux",
    "Kupqu Kogi",
    "Goudernoux",
    "Latgar",
    "Hremfing",
    "Ourdilic",
    "Lancefer",
    "Emmerololth",
    "Nabriales",
    "Mitainie",
    "Zuzumeda",
    "Urswyrst",
    "Shoina",
    "Loymet",
    "Nymet",
    "Korille",
    "Fyrbryda",
    "Elmar",
    "Ozun Nazun",
    "Cravellin",
    "Ume",
    "Katherine",
    "Fridurih",
    "Oroniri Spearson",
    "Eo An",
    "Rispa",
    "Aenc Thon",
    "Ghun Gun",
    "Adalind",
    "Waldhar",
    "Geva",
    "Blaisette",
    "Ysabel Hawthorne",
    "Ahlduwil",
    "Louis",
    "Erapi Taropi",
    "Nunuzofu",
    "Gagari",
    "Cicidoa",
    "Giah Molkoh",
    "Wyrkrhit",
    "Owen",
    "Fraeloef",
    "Landebert",
    "Syntgoht",
    "Victor",
    "Nathaxio",
    "Pelixia",
    "Hihira",
    "Baron Von Quiveron IV",
    "Ignace",
    "Ahldfoet",
    "Wineburg",
    "Lothaire",
    "Haribehrt",
    "Rhotwyda",
    "Leodaire",
    "Seseli",
    "Charline",
    "Grynewyda",
    "Durim Falurim",
    "V'mellpa",
    "Q'ahnebb",
    "Alza Gamilza",
    "Patrick",
    "Hourlinet",
    "Brigie",
    "Nathelain",
    "Shar",
    "Rhitskylt",
    "Hughoc",
    "Hrotmar",
    "Totoruna",
    "Rosa Hawthorne",
    "Glazrael",
    "Osha Jaab",
    "Amalberga",
    "Dellexia",
    "Ameexia",
    "Bertennant",
    "Yayake",
    "Gagaruna",
    "Jillian",
    "Lulutsu",
    "Madelle",
    "Athelyna",
    "Murie",
    "Luciae",
    "Claxio",
    "Simeonard of the Holiest Flame",
    "Alys",
    "Notrelchamps",
    "Tescelingeon",
    "Vaincannet",
    "Gondelimbaud",
    "Quomonrentin",
    "Tsubh Khamazom",
    "Chief Honu Vanu",
    "Cibleroit",
    "Meriel",
    "Kikipu",
    "Danyell",
    "Vondia",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Alphinaud"]["gender"] = "Male"
character_info["Alisaie"]["gender"] = "Female"
character_info["Y'shtola"]["gender"] = "Female"
character_info["Thancred"]["gender"] = "Male"
character_info["Lyse"]["gender"] = "Female"
character_info["Urianger"]["gender"] = "Male"
character_info["G'raha Tia"]["gender"] = "Male"
character_info["The Adventurer"]["gender"] = "Neutral"
character_info["Ryne"]["gender"] = "Female"
character_info["Tataru"]["gender"] = "Female"
character_info["Estinien"]["gender"] = "Male"
character_info["Yugiri"]["gender"] = "Female"
character_info["Hien"]["gender"] = "Male"
character_info["Raubahn"]["gender"] = "Male"
character_info["Aymeric"]["gender"] = "Male"
character_info["Minfilia Warde"]["gender"] = "Female"
character_info["Cid"]["gender"] = "Male"
character_info["Krile"]["gender"] = "Female"
character_info["Lucia"]["gender"] = "Female"
character_info["Chai-Nuzz"]["gender"] = "Male"
character_info["Gosetsu"]["gender"] = "Male"
character_info["Ysayle"]["gender"] = "Female"
character_info["Papalymo"]["gender"] = "Male"
character_info["Pipin"]["gender"] = "Male"
character_info["Lyna"]["gender"] = "Female"
character_info["Almet"]["gender"] = "Female"
character_info["Emmanellain"]["gender"] = "Male"
character_info["Kan-E-Senna"]["gender"] = "Female"
character_info["Elidibus"]["gender"] = "Male"
character_info["Arenvald"]["gender"] = "Male"
character_info["Haurchefant"]["gender"] = "Male"
character_info["Dulia-Chai"]["gender"] = "Female"
character_info["M'naago"]["gender"] = "Female"
character_info["Runar"]["gender"] = "Male"
character_info["Emet-Selch"]["gender"] = "Male"
character_info["Cirina"]["gender"] = "Female"
character_info["Artoirel"]["gender"] = "Male"
character_info["Merlwyb"]["gender"] = "Female"
character_info["Ardbert"]["gender"] = "Male"
character_info["Ran'jit"]["gender"] = "Male"
character_info["Count Edmont de Fortemps"]["gender"] = "Male"
character_info["Jeryk"]["gender"] = "Male"
character_info["Ilberd"]["gender"] = "Male"
character_info["Wedge"]["gender"] = "Male"
character_info["Honoroit"]["gender"] = "Male"
character_info["Kai-Shirr"]["gender"] = "Male"
character_info["Hilda"]["gender"] = "Female"
character_info["Conrad"]["gender"] = "Male"
character_info["Meffrid"]["gender"] = "Male"
character_info["Hancock"]["gender"] = "Male"
character_info["Nanamo Ul Namo"]["gender"] = "Female"
character_info["Thaffe"]["gender"] = "Male"
character_info["Magnus"]["gender"] = "Male"
character_info["Uimet"]["gender"] = "Female"
character_info["Moren"]["gender"] = "Male"
character_info["Cymet"]["gender"] = "Female"
character_info["Zenos Galvus"]["gender"] = "Male"
character_info["Soroban"]["gender"] = "Male"
character_info["Hoary Boulder"]["gender"] = "Male"
character_info["Matoya"]["gender"] = "Male"
character_info["Hraesvelgr"]["gender"] = "Male"
character_info["Vidofnir"]["gender"] = "Female"
character_info["Biggs"]["gender"] = "Male"
character_info["Riol"]["gender"] = "Male"
character_info["Momodi"]["gender"] = "Female"
character_info["Tansui"]["gender"] = "Male"
character_info["Wiscar"]["gender"] = "Male"
character_info["Manager of Suites"]["gender"] = "Male"
character_info["Korutt"]["gender"] = "Male"
character_info["Baderon"]["gender"] = "Male"
character_info["Alianne"]["gender"] = "Female"
character_info["Gaius"]["gender"] = "Male"
character_info["Wrenden"]["gender"] = "Male"
character_info["Yozan"]["gender"] = "Male"
character_info["Kuplo Kopp"]["gender"] = "Male"
character_info["Coultenet"]["gender"] = "Male"
character_info["Tristol"]["gender"] = "Male"
character_info["Seto"]["gender"] = "Male"
character_info["Mother Miounne"]["gender"] = "Female"
character_info["Ga Bu"]["gender"] = "Male"
character_info["Rasho"]["gender"] = "Male"
character_info["Tista-Bie"]["gender"] = "Female"
character_info["Slafborn"]["gender"] = "Male"
character_info["Redwald"]["gender"] = "Male"
character_info["Drillemont"]["gender"] = "Male"
character_info["Theyler"]["gender"] = "Male"
character_info["Papashan"]["gender"] = "Male"
character_info["Isse"]["gender"] = "Male"
character_info["Tesleen"]["gender"] = "Female"
character_info["Maxima"]["gender"] = "Male"
character_info["Xamott"]["gender"] = "Male"
character_info["Chessamile"]["gender"] = "Female"
character_info["F'lhaminn"]["gender"] = "Female"
character_info["Archbishop Thordan VII"]["gender"] = "Male"
character_info["Fufulupa"]["gender"] = "Male"
character_info["Szem Djenmai"]["gender"] = "Male"
character_info["Magnai"]["gender"] = "Male"
character_info["Bartholomew"]["gender"] = "Male"
character_info["Zanthael"]["gender"] = "Male"
character_info["Cassard"]["gender"] = "Male"
character_info["Riqi-Tio"]["gender"] = "Female"
character_info["Glynard"]["gender"] = "Male"
character_info["Nero"]["gender"] = "Male"
character_info["Sadu"]["gender"] = "Female"
character_info["Guthjon"]["gender"] = "Male"
character_info["Moghan"]["gender"] = "Male"
character_info["Komuxio"]["gender"] = "Male"
character_info["Midgardsormr"]["gender"] = "Male"
character_info["Shamani Lohmani"]["gender"] = "Male"
character_info["Nidhogg"]["gender"] = "Male"
character_info["Buscarron"]["gender"] = "Male"
character_info["Wheiskaet"]["gender"] = "Male"
character_info["Asahi"]["gender"] = "Male"
character_info["Hozan"]["gender"] = "Male"
character_info["Dorbei"]["gender"] = "Male"
character_info["Staelwyrn"]["gender"] = "Male"
character_info["Bragi"]["gender"] = "Male"
character_info["V'mah Tia"]["gender"] = "Male"
character_info["Temulun"]["gender"] = "Female"
character_info["Hakuro"]["gender"] = "Male"
character_info["Eirwel"]["gender"] = "Male"
character_info["Eynzahr Slafyrsyn"]["gender"] = "Male"
character_info["Katliss"]["gender"] = "Female"
character_info["Baatu"]["gender"] = "Male"
character_info["Gundobald"]["gender"] = "Male"
character_info["Lahabrea"]["gender"] = "Male"
character_info["Lonu Vanu"]["gender"] = "Male"
character_info["Yuyuhase"]["gender"] = "Male"
character_info["Vorsaile Heuloix"]["gender"] = "Male"
character_info["Brayflox Alltalks"]["gender"] = "Female"
character_info["Handeloup"]["gender"] = "Female"
character_info["J'moldva"]["gender"] = "Female"
character_info["Halric"]["gender"] = "Male"
character_info["Carvallain"]["gender"] = "Male"
character_info["Arkil"]["gender"] = "Male"
character_info["Koharu"]["gender"] = "Female"
character_info["Azami"]["gender"] = "Female"
character_info["Lionnellais"]["gender"] = "Male"
character_info["Ephemie"]["gender"] = "Female"
character_info["Laniaitte"]["gender"] = "Female"
character_info["Ceana"]["gender"] = "Female"
character_info["Gibrillont"]["gender"] = "Male"
character_info["Raganfrid"]["gender"] = "Male"
character_info["Wilred"]["gender"] = "Male"
character_info["Moglin"]["gender"] = "Male"
character_info["Ravana"]["gender"] = "Male"
character_info["Trachtoum"]["gender"] = "Male"
character_info["Eline Roaille"]["gender"] = "Female"
character_info["Tsuranuki"]["gender"] = "Male"
character_info["Edelstein"]["gender"] = "Male"
character_info["Owyne"]["gender"] = "Male"
character_info["Lewin"]["gender"] = "Male"
character_info["Sevrin"]["gender"] = "Male"
character_info["Fordola"]["gender"] = "Female"
character_info["Portelaine"]["gender"] = "Male"
character_info["Moenbryda"]["gender"] = "Female"
character_info["Slowfix"]["gender"] = "Male"
character_info["L'nophlo"]["gender"] = "Female"
character_info["Irvithe"]["gender"] = "Male"
character_info["U'odh Nunh"]["gender"] = "Male"
character_info["Gods' Quiver Bow"]["gender"] = "Male"
character_info["Ungust"]["gender"] = "Male"
character_info["Skaenrael"]["gender"] = "Female"
character_info["Homei"]["gender"] = "Male"
character_info["Glaumunt"]["gender"] = "Male"
character_info["Cyella"]["gender"] = "Female"
character_info["Rothe"]["gender"] = "Male"
character_info["Kaidate"]["gender"] = "Male"
character_info["Haname"]["gender"] = "Female"
character_info["Laurentius"]["gender"] = "Male"
character_info["Isembard"]["gender"] = "Male"
character_info["Marques"]["gender"] = "Male"
character_info["Grithil"]["gender"] = "Male"
character_info["Mutamix"]["gender"] = "Male"
character_info["Marcechamp"]["gender"] = "Male"
character_info["Leofric"]["gender"] = "Male"
character_info["Galfrid"]["gender"] = "Male"
character_info["Bloeidin"]["gender"] = "Male"
character_info["Isildaure"]["gender"] = "Male"
character_info["Theva"]["gender"] = "Female"
character_info["Zephirin"]["gender"] = "Male"
character_info["Hythlodaeus"]["gender"] = "Male"
character_info["Dewlala"]["gender"] = "Female"
character_info["Higiri"]["gender"] = "Female"
character_info["Watt"]["gender"] = "Male"
character_info["Grenoldt"]["gender"] = "Male"
character_info["Ele"]["gender"] = "Female"
character_info["Fourchenault"]["gender"] = "Male"
character_info["Yotsuyu"]["gender"] = "Female"
character_info["Luquelot"]["gender"] = "Male"
character_info["Frixio"]["gender"] = "Male"
character_info["Daidukul"]["gender"] = "Male"
character_info["Marcelain"]["gender"] = "Male"
character_info["Atharn"]["gender"] = "Male"
character_info["Regula van Hydrus"]["gender"] = "Male"
character_info["Varis"]["gender"] = "Male"
character_info["Thoarich"]["gender"] = "Male"
character_info["Falkbryda"]["gender"] = "Female"
character_info["Baldewyn"]["gender"] = "Male"
character_info["Keitha"]["gender"] = "Female"
character_info["Udutai"]["gender"] = "Male"
character_info["Tiamat"]["gender"] = "Female"
character_info["Elyenora"]["gender"] = "Female"
character_info["Igeyorhm"]["gender"] = "Female"
character_info["Eudestand"]["gender"] = "Male"
character_info["Symme"]["gender"] = "Male"
character_info["Clemence"]["gender"] = "Female"
character_info["Aenor"]["gender"] = "Female"
character_info["Ocher Boulder"]["gender"] = "Male"
character_info["Kikyo"]["gender"] = "Female"
character_info["Kasasagi"]["gender"] = "Male"
character_info["Landenel"]["gender"] = "Male"
character_info["Sonu Vanu"]["gender"] = "Male"
character_info["Aideen"]["gender"] = "Female"
character_info["Motojiro"]["gender"] = "Male"
character_info["Motojiro"]["gender"] = "Male"
character_info["Mimidoa"]["gender"] = "Male"
character_info["Raya-O-Senna"]["gender"] = "Female"
character_info["Reyner"]["gender"] = "Male"
character_info["Ihanashi"]["gender"] = "Male"
character_info["Parsemontret"]["gender"] = "Male"
character_info["The Griffin"]["gender"] = "Male"
character_info["Bismarck"]["gender"] = "Male"
character_info["Todden"]["gender"] = "Male"
character_info["Pawnil"]["gender"] = "Male"
character_info["Lolorito"]["gender"] = "Male"
character_info["Wystan"]["gender"] = "Male"
character_info["Medrod"]["gender"] = "Male"
character_info["Willfort"]["gender"] = "Male"
character_info["Marielle"]["gender"] = "Female"
character_info["Rammbroes"]["gender"] = "Male"
character_info["Venat"]["gender"] = "Female"
character_info["Drest"]["gender"] = "Male"
character_info["Vonard"]["gender"] = "Male"
character_info["Voyne"]["gender"] = "Male"
character_info["Eybor"]["gender"] = "Male"
character_info["Chaunollet"]["gender"] = "Male"
character_info["Loanne"]["gender"] = "Female"
character_info["Ourcen"]["gender"] = "Female"
character_info["Lamberteint"]["gender"] = "Male"
character_info["Charibert"]["gender"] = "Male"
character_info["Vauthry"]["gender"] = "Male"
character_info["Julia quo Soranus"]["gender"] = "Female"
character_info["Forlemort"]["gender"] = "Male"
character_info["Francel"]["gender"] = "Male"
character_info["Glagg"]["gender"] = "Male"
character_info["Ivaurault"]["gender"] = "Male"
character_info["Sylvetrel de Dzemael"]["gender"] = "Male"
character_info["Ihanami"]["gender"] = "Male"
character_info["Davyd"]["gender"] = "Male"
character_info["Shiosai"]["gender"] = "Male"
character_info["Rolfe Hawthorne"]["gender"] = "Male"
character_info["Garibald"]["gender"] = "Male"
character_info["Swift"]["gender"] = "Male"
character_info["Yaelle"]["gender"] = "Female"
character_info["Keeper of the Entwined Serpents"]["gender"] = "Male"
character_info["Prunilla"]["gender"] = "Female"
character_info["Godbert"]["gender"] = "Male"
character_info["Griseldis"]["gender"] = "Female"
character_info["Ahelissa"]["gender"] = "Female"
character_info["Master of Shofuku Shichiten"]["gender"] = "Male"
character_info["Narengawa"]["gender"] = "Female"
character_info["Ucugen"]["gender"] = "Female"
character_info["Grey Fleet Miller"]["gender"] = "Male"
character_info["Chigusa"]["gender"] = "Female"
character_info["Gogg Dwarf"]["gender"] = "Male"
character_info["Wercrata"]["gender"] = "Male"
character_info["Hahasako"]["gender"] = "Male"
character_info["Ursandel"]["gender"] = "Male"
character_info["Teledji Adeledji"]["gender"] = "Male"
character_info["Cotan"]["gender"] = "Female"
character_info["Mogwin"]["gender"] = "Male"
character_info["Yunagi"]["gender"] = "Female"
character_info["Dolorous Bear"]["gender"] = "Male"
character_info["Haustefort"]["gender"] = "Male"
character_info["Sozai Rarzai"]["gender"] = "Male"
character_info["Eyrimhus"]["gender"] = "Male"
character_info["Seseroga"]["gender"] = "Male"
character_info["Nenebaru"]["gender"] = "Male"
character_info["Nicia"]["gender"] = "Female"
character_info["Swozblaet"]["gender"] = "Male"
character_info["Sundhimal"]["gender"] = "Male"
character_info["Quentenain"]["gender"] = "Male"
character_info["S'dhodjbi"]["gender"] = "Female"
character_info["Eluned"]["gender"] = "Female"
character_info["Bertliana"]["gender"] = "Female"
character_info["Hedyn"]["gender"] = "Male"
character_info["Maelie"]["gender"] = "Female"
character_info["Knolexia"]["gender"] = "Female"
character_info["Jakys Ryder"]["gender"] = "Male"
character_info["Ersabel"]["gender"] = "Female"
character_info["Miraudont the Madder"]["gender"] = "Male"
character_info["Lue-Reeq"]["gender"] = "Male"
character_info["Granson"]["gender"] = "Male"
character_info["Cerigg"]["gender"] = "Male"
character_info["Giott"]["gender"] = "Female"
character_info["Astidien"]["gender"] = "Male"
character_info["Kajika"]["gender"] = "Male"
character_info["Fyrilsmyd"]["gender"] = "Male"
character_info["Warin"]["gender"] = "Male"
character_info["Bujeg"]["gender"] = "Male"
character_info["Myrcant"]["gender"] = "Male"
character_info["Roseline"]["gender"] = "Female"
character_info["Talebot"]["gender"] = "Male"
character_info["Hihibaru"]["gender"] = "Male"
character_info["Aethelmaer"]["gender"] = "Male"
character_info["Beves"]["gender"] = "Male"
character_info["Thierremont"]["gender"] = "Male"
character_info["Edda"]["gender"] = "Female"
character_info["Cenota"]["gender"] = "Female"
character_info["Sark Malark"]["gender"] = "Male"
character_info["Wymond"]["gender"] = "Male"
character_info["Orella"]["gender"] = "Female"
character_info["Bluomwyda"]["gender"] = "Female"
character_info["Thubyrgeim"]["gender"] = "Female"
character_info["Byrglaent"]["gender"] = "Male"
character_info["Hirase"]["gender"] = "Male"
character_info["Kotokaze"]["gender"] = "Female"
character_info["Vath Fleetfoot"]["gender"] = "Male"
character_info["Afumi"]["gender"] = "Female"
character_info["Sicard"]["gender"] = "Male"
character_info["Chambui"]["gender"] = "Female"
character_info["Miyama"]["gender"] = "Male"
character_info["Aranami"]["gender"] = "Male"
character_info["Guillaime"]["gender"] = "Male"
character_info["Estaine"]["gender"] = "Female"
character_info["Khanswys"]["gender"] = "Female"
character_info["Ahtbyrm"]["gender"] = "Male"
character_info["Mogmug"]["gender"] = "Male"
character_info["Y'mhitra"]["gender"] = "Female"
character_info["Pfrewahl"]["gender"] = "Male"
character_info["Janremi Blackheart"]["gender"] = "Male"
character_info["Flavien de Fortemps"]["gender"] = "Male"
character_info["E-Sumi-Yan"]["gender"] = "Male"
character_info["Doware"]["gender"] = "Male"
character_info["Ingaret"]["gender"] = "Female"
character_info["Noirterel"]["gender"] = "Male"
character_info["Emerissel"]["gender"] = "Male"
character_info["Auriaune"]["gender"] = "Female"
character_info["Tourcenet"]["gender"] = "Male"
character_info["Ermegarde"]["gender"] = "Female"
character_info["Aylmer"]["gender"] = "Male"
character_info["Zazawaka"]["gender"] = "Male"
character_info["Fandaniel"]["gender"] = "Male"
character_info["Yuyutazi"]["gender"] = "Male"
character_info["Bubukkuli"]["gender"] = "Male"
character_info["Tutumoko"]["gender"] = "Male"
character_info["Ryssfloh"]["gender"] = "Male"
character_info["Ludovoix"]["gender"] = "Male"
character_info["Pierriquet"]["gender"] = "Male"
character_info["Jantellot"]["gender"] = "Male"
character_info["Joellaut"]["gender"] = "Male"
character_info["Aergmhus"]["gender"] = "Male"
character_info["Masgud"]["gender"] = "Male"
character_info["Hathenbet"]["gender"] = "Male"
character_info["Serendipity"]["gender"] = "Female"
character_info["Cracked Fist"]["gender"] = "Male"
character_info["Midnight Dew"]["gender"] = "Female"
character_info["Karaku"]["gender"] = "Male"
character_info["Mosha-Moa"]["gender"] = "Female"
character_info["Kupta Kapa"]["gender"] = "Male"
character_info["Annia quo Soranus"]["gender"] = "Female"
character_info["Qoyar"]["gender"] = "Female"
character_info["Koko"]["gender"] = "Male"
character_info["Mergen"]["gender"] = "Female"
character_info["Honami"]["gender"] = "Female"
character_info["Baidur"]["gender"] = "Male"
character_info["Yesui"]["gender"] = "Female"
character_info["Sifrid"]["gender"] = "Male"
character_info["Lyulf"]["gender"] = "Male"
character_info["Cassana"]["gender"] = "Female"
character_info["Skyfryn"]["gender"] = "Male"
character_info["Ceinguled"]["gender"] = "Female"
character_info["Rhoswen"]["gender"] = "Female"
character_info["Roger"]["gender"] = "Male"
character_info["Begrimed Bloke"]["gender"] = "Male"
character_info["Yagoro"]["gender"] = "Male"
character_info["Eylgar"]["gender"] = "Male"
character_info["Jocea"]["gender"] = "Female"
character_info["Swynbroes"]["gender"] = "Male"
character_info["Haldrath"]["gender"] = "Male"
character_info["Painted Mesa"]["gender"] = "Male"
character_info["Grimold"]["gender"] = "Male"
character_info["Loupard"]["gender"] = "Male"
character_info["Yusui"]["gender"] = "Male"
character_info["Hiun"]["gender"] = "Male"
character_info["Elaisse"]["gender"] = "Female"
character_info["Gallien"]["gender"] = "Male"
character_info["Albreda"]["gender"] = "Female"
character_info["Shiun"]["gender"] = "Male"
character_info["Rokka"]["gender"] = "Female"
character_info["R'ashaht Rhiki"]["gender"] = "Female"
character_info["Josseloux"]["gender"] = "Male"
character_info["Liavinne"]["gender"] = "Female"
character_info["Kikina"]["gender"] = "Female"
character_info["E'manafa"]["gender"] = "Female"
character_info["Beatin"]["gender"] = "Male"
character_info["Theophilain"]["gender"] = "Male"
character_info["Iliud"]["gender"] = "Male"
character_info["Chadden"]["gender"] = "Male"
character_info["Monranguin"]["gender"] = "Male"
character_info["Adelstan"]["gender"] = "Male"
character_info["Aurildis"]["gender"] = "Female"
character_info["Swaenhylt"]["gender"] = "Male"
character_info["Knerl"]["gender"] = "Male"
character_info["Eginolf"]["gender"] = "Male"
character_info["Ghimthota"]["gender"] = "Female"
character_info["Paulecrain"]["gender"] = "Male"
character_info["Grinnaux"]["gender"] = "Male"
character_info["Ghen Gen"]["gender"] = "Male"
character_info["Kunu Vali"]["gender"] = "Female"
character_info["Pauline"]["gender"] = "Female"
character_info["Cornenne"]["gender"] = "Male"
character_info["J'nasshym"]["gender"] = "Female"
character_info["Armelle"]["gender"] = "Female"
character_info["Gilow"]["gender"] = "Male"
character_info["Dalmascan Fusilier"]["gender"] = "Male"
character_info["Asgeir"]["gender"] = "Male"
character_info["Kupli Kipp"]["gender"] = "Male"
character_info["Haldbroda"]["gender"] = "Male"
character_info["Keiten"]["gender"] = "Male"
character_info["Otelin"]["gender"] = "Male"
character_info["Wauter"]["gender"] = "Male"
character_info["Edmelle"]["gender"] = "Female"
character_info["Ninne"]["gender"] = "Female"
character_info["Aokumo"]["gender"] = "Male"
character_info["M'hahtoa"]["gender"] = "Female"
character_info["M'rahz Nunh"]["gender"] = "Male"
character_info["Carrilaut"]["gender"] = "Male"
character_info["Hida"]["gender"] = "Female"
character_info["Brunadier"]["gender"] = "Male"
character_info["Nimbus"]["gender"] = "Male"
character_info["Ernold"]["gender"] = "Male"
character_info["Hardyss"]["gender"] = "Female"
character_info["Angry River"]["gender"] = "Male"
character_info["Yayazuku"]["gender"] = "Male"
character_info["Osric"]["gender"] = "Male"
character_info["Gisilbehrt"]["gender"] = "Male"
character_info["Dadanen"]["gender"] = "Male"
character_info["Raffe"]["gender"] = "Male"
character_info["Alestan"]["gender"] = "Male"
character_info["Louistiaux of the First Line"]["gender"] = "Female"
character_info["Tristechambel"]["gender"] = "Male"
character_info["Adelphel"]["gender"] = "Male"
character_info["Bernadette"]["gender"] = "Female"
character_info["Fromelaut"]["gender"] = "Male"
character_info["Yellow Moon"]["gender"] = "Female"
character_info["H'naanza"]["gender"] = "Female"
character_info["Monne"]["gender"] = "Female"
character_info["Adalbert"]["gender"] = "Male"
character_info["Sekiseigumi Blade"]["gender"] = "Male"
character_info["Merilda"]["gender"] = "Female"
character_info["Hierytha"]["gender"] = "Female"
character_info["Baensyng"]["gender"] = "Male"
character_info["Gegeruju"]["gender"] = "Male"
character_info["Rowena"]["gender"] = "Female"
character_info["Styrnlona"]["gender"] = "Female"
character_info["Adala"]["gender"] = "Female"
character_info["Shiva"]["gender"] = "Female"
character_info["Shiva"]["gender"] = "Female"
character_info["Kokosamu"]["gender"] = "Male"
character_info["F'hobas"]["gender"] = "Male"
character_info["Ewmond"]["gender"] = "Male"
character_info["Bernard"]["gender"] = "Male"
character_info["Junghbhar"]["gender"] = "Male"
character_info["Avere"]["gender"] = "Male"
character_info["Firkmann"]["gender"] = "Male"
character_info["L'khonebb"]["gender"] = "Female"
character_info["Bloisirant"]["gender"] = "Male"
character_info["Alboise"]["gender"] = "Female"
character_info["Gracine"]["gender"] = "Female"
character_info["Faramund"]["gender"] = "Male"
character_info["Ysaudore"]["gender"] = "Female"
character_info["Ghon Gon"]["gender"] = "Male"
character_info["Imedia"]["gender"] = "Female"
character_info["Hastelot"]["gender"] = "Male"
character_info["Abelie"]["gender"] = "Female"
character_info["Rickeman"]["gender"] = "Male"
character_info["Amelain"]["gender"] = "Male"
character_info["Paiyo Reiyo"]["gender"] = "Male"
character_info["Ignemortel"]["gender"] = "Male"
character_info["Ombeline"]["gender"] = "Female"
character_info["Pierremons"]["gender"] = "Male"
character_info["Bricelt"]["gender"] = "Male"
character_info["Ossine"]["gender"] = "Male"
character_info["Theodore"]["gender"] = "Male"
character_info["C'nangho"]["gender"] = "Female"
character_info["Jeantremont"]["gender"] = "Male"
character_info["Nawashiro"]["gender"] = "Male"
character_info["Grehfarr"]["gender"] = "Male"
character_info["F'zhumii"]["gender"] = "Female"
character_info["Abylfarr"]["gender"] = "Male"
character_info["Ahldskyf"]["gender"] = "Male"
character_info["Vortefaurt"]["gender"] = "Male"
character_info["Blauthota"]["gender"] = "Female"
character_info["Shinobi"]["gender"] = "Male"
character_info["Rhesh Polaali"]["gender"] = "Female"
character_info["Beltardois"]["gender"] = "Male"
character_info["Mowen"]["gender"] = "Female"
character_info["Leonnie"]["gender"] = "Female"
character_info["Tebbe"]["gender"] = "Male"
character_info["Gerraldieux"]["gender"] = "Male"
character_info["Kupqu Kogi"]["gender"] = "Male"
character_info["Goudernoux"]["gender"] = "Male"
character_info["Latgar"]["gender"] = "Male"
character_info["Hremfing"]["gender"] = "Male"
character_info["Ourdilic"]["gender"] = "Female"
character_info["Lancefer"]["gender"] = "Male"
character_info["Emmerololth"]["gender"] = "Female"
character_info["Nabriales"]["gender"] = "Male"
character_info["Mitainie"]["gender"] = "Female"
character_info["Zuzumeda"]["gender"] = "Male"
character_info["Urswyrst"]["gender"] = "Male"
character_info["Shoina"]["gender"] = "Female"
character_info["Loymet"]["gender"] = "Female"
character_info["Nymet"]["gender"] = "Female"
character_info["Korille"]["gender"] = "Female"
character_info["Fyrbryda"]["gender"] = "Female"
character_info["Elmar"]["gender"] = "Male"
character_info["Ozun Nazun"]["gender"] = "Male"
character_info["Cravellin"]["gender"] = "Male"
character_info["Ume"]["gender"] = "Male"
character_info["Katherine"]["gender"] = "Female"
character_info["Fridurih"]["gender"] = "Male"
character_info["Oroniri Spearson"]["gender"] = "Male"
character_info["Eo An"]["gender"] = "Female"
character_info["Rispa"]["gender"] = "Male"
character_info["Aenc Thon"]["gender"] = "Male"
character_info["Ghun Gun"]["gender"] = "Male"
character_info["Adalind"]["gender"] = "Female"
character_info["Waldhar"]["gender"] = "Male"
character_info["Geva"]["gender"] = "Female"
character_info["Blaisette"]["gender"] = "Female"
character_info["Ysabel Hawthorne"]["gender"] = "Female"
character_info["Ahlduwil"]["gender"] = "Male"
character_info["Louis"]["gender"] = "Male"
character_info["Erapi Taropi"]["gender"] = "Male"
character_info["Nunuzofu"]["gender"] = "Male"
character_info["Gagari"]["gender"] = "Female"
character_info["Cicidoa"]["gender"] = "Male"
character_info["Giah Molkoh"]["gender"] = "Female"
character_info["Wyrkrhit"]["gender"] = "Male"
character_info["Owen"]["gender"] = "Male"
character_info["Fraeloef"]["gender"] = "Male"
character_info["Landebert"]["gender"] = "Male"
character_info["Syntgoht"]["gender"] = "Male"
character_info["Victor"]["gender"] = "Male"
character_info["Nathaxio"]["gender"] = "Male"
character_info["Pelixia"]["gender"] = "Female"
character_info["Hihira"]["gender"] = "Female"
character_info["Baron Von Quiveron IV"]["gender"] = "Male"
character_info["Ignace"]["gender"] = "Male"
character_info["Ahldfoet"]["gender"] = "Male"
character_info["Wineburg"]["gender"] = "Male"
character_info["Lothaire"]["gender"] = "Male"
character_info["Haribehrt"]["gender"] = "Male"
character_info["Rhotwyda"]["gender"] = "Female"
character_info["Leodaire"]["gender"] = "Male"
character_info["Seseli"]["gender"] = "Female"
character_info["Charline"]["gender"] = "Female"
character_info["Grynewyda"]["gender"] = "Female"
character_info["Durim Falurim"]["gender"] = "Male"
character_info["V'mellpa"]["gender"] = "Female"
character_info["Q'ahnebb"]["gender"] = "Female"
character_info["Alza Gamilza"]["gender"] = "Male"
character_info["Patrick"]["gender"] = "Male"
character_info["Hourlinet"]["gender"] = "Male"
character_info["Brigie"]["gender"] = "Female"
character_info["Nathelain"]["gender"] = "Male"
character_info["Shar"]["gender"] = "Female"
character_info["Rhitskylt"]["gender"] = "Male"
character_info["Hughoc"]["gender"] = "Male"
character_info["Hrotmar"]["gender"] = "Male"
character_info["Totoruna"]["gender"] = "Male"
character_info["Rosa Hawthorne"]["gender"] = "Female"
character_info["Glazrael"]["gender"] = "Female"
character_info["Osha Jaab"]["gender"] = "Female"
character_info["Amalberga"]["gender"] = "Female"
character_info["Dellexia"]["gender"] = "Female"
character_info["Ameexia"]["gender"] = "Female"
character_info["Bertennant"]["gender"] = "Male"
character_info["Yayake"]["gender"] = "Female"
character_info["Gagaruna"]["gender"] = "Male"
character_info["Jillian"]["gender"] = "Female"
character_info["Lulutsu"]["gender"] = "Female"
character_info["Madelle"]["gender"] = "Female"
character_info["Athelyna"]["gender"] = "Female"
character_info["Murie"]["gender"] = "Female"
character_info["Luciae"]["gender"] = "Female"
character_info["Claxio"]["gender"] = "Male"
character_info["Simeonard of the Holiest Flame"]["gender"] = "Male"
character_info["Alys"]["gender"] = "Female"
character_info["Notrelchamps"]["gender"] = "Male"
character_info["Tescelingeon"]["gender"] = "Male"
character_info["Vaincannet"]["gender"] = "Male"
character_info["Gondelimbaud"]["gender"] = "Male"
character_info["Quomonrentin"]["gender"] = "Male"
character_info["Tsubh Khamazom"]["gender"] = "Male"
character_info["Chief Honu Vanu"]["gender"] = "Male"
character_info["Cibleroit"]["gender"] = "Male"
character_info["Meriel"]["gender"] = "Female"
character_info["Kikipu"]["gender"] = "Female"
character_info["Danyell"]["gender"] = "Male"
character_info["Vondia"]["gender"] = "Female"

# Function to extract dialogues
def extract_dialogue(data, character_info):
    def parse_entry(entry):
        if isinstance(entry, dict): # Check for dictionary items
            if "CHOICE" in entry: # Check for choice items
                for branch in entry["CHOICE"]:
                    parse_entry(branch)
            elif "ACTION" in entry: # Check for action items
                text = entry["ACTION"]
                for character in character_info:
                    if text.startswith(character):
                        text = text.removeprefix(character)
                        if text.strip().endswith(('.', '?', '!')):
                            character_info[character]["dialogues"].append(text)
            else: # Check for non-choice and non-action items
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
            "Title": "Final Fantasy XIV",
            "Year": "2013",
            "Country": "Japan",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Alphinaud": "Alphinaud Leveilleur",
    "Alisaie": "Alisaie Leveilleur",
    "Y'shtola": "Y'shtola Rhul",
    "Thancred": "Thancred Waters",
    "Lyse": "Lyse Hext",
    "Urianger": "Urianger Augurelt",
    "Ryne": "Ryne Waters",
    "Tataru": "Tataru Taru",
    "Estinien": "Estinien Varlineau",
    "Yugiri": "Yugiri Mistwalker",
    "Hien": "Hien Rijin",
    "Raubahn": "Raubahn Aldynn",
    "Aymeric": "Aymeric de Borel",
    "Cid": "Cid Garlond",
    "Krile": "Krile Maya Baldesion",
    "Lucia": "Lucia Junius",
    "Chai-Nuzz": "Chai-Nuzz Mewlah",
    "Gosetsu": "Gosetsu Daito",
    "Ysayle": "Ysayle Dangoulain",
    "Papalymo": "Papalymo Totolymo",
    "Pipin": "Pipin Tarupin",
    "Emmanellain": "Emmanellain de Fortemps",
    "Arenvald": "Arenvald Lentinus",
    "Haurchefant": "Haurchefant Greystone",
    "Dulia-Chai": "Dulia-Chai Mewlah",
    "M'naago": "M'naago Rahz",
    "Cirina": "Cirina Mol",
    "Artoirel": "Artoirel de Fortemps",
    "Merlwyb": "Merlwyb Bloefhiswyn",
    "Ardbert": "Ardbert Hylfyst",
    "Count Edmont de Fortemps": "Edmont de Fortemps",
    "Ilberd": "Ilberd Feare",
    "Honoroit": "Honoroit Banlardois",
    "Kai-Shirr": "Kai-Shirr Olkoh",
    "Hilda": "Hilda Ware",
    "Conrad": "Conrad Kemp",
    "Meffrid": "Meffrid Noward",
    "Hancock": "Hancock Fitzgerald",
    "Riol": "Riol Forrest",
    "Momodi": "Momodi Modi",
    "Wiscar": "Wiscar Marshe",
    "Baderon": "Baderon Tenfingers",
    "Alianne": "Alianne Vellegrance",
    "Gaius": "Gaius Baelsar",
    "Yozan": "Yozan Nagae",
    "Coultenet": "Coultenet Dailebaure",
    "Tristol": "Tristol Horpurse",
    "Mother Miounne": "Miounne",
    "Rasho": "Rasho Mastbreaker",
    "Tista-Bie": "Tista-Bie Amari",
    "Redwald": "Redwald Younge",
    "Drillemont": "Drillemont de Lasserrant",
    "Papashan": "Papashan Nonoshan",
    "Isse": "Isse Shibunuri",
    "Tesleen": "Tesleen Stoneplowe",
    "Maxima": "Maxima Priscus",
    "F'lhaminn": "F'lhaminn Qesh",
    "Archbishop Thordan VII": "Thordan VII",
    "Magnai": "Magnai Oronir",
    "Nero": "Nero Scaeva",
    "Sadu": "Sadu Dotharl",
    "Buscarron": "Buscarron Stacks",
    "Wheiskaet": "Wheiskaet Rysswoerdsyn",
    "Asahi": "Asahi Brutus",
    "Hakuro": "Hakuro Gunji",
    "Yuyuhase": "Yuyuhase Luluhase",
    "Handeloup": "Handeloup de Daimbaux",
    "Carvallain": "Carvallain de Gorgagne",
    "Azami": "Azami Shibunuri",
    "Ephemie": "Ephemie Giphelmont",
    "Laniaitte": "Laniaitte de Haillenarte",
    "Wilred": "Wilred Glasse",
    "Lewin": "Lewin Hunte",
    "Fordola": "Fordola Lupis",
    "Moenbryda": "Moenbryda Wilfsunnwyn",
    "Slowfix": "Slowfix Cointoss",
    "Cyella": "Cyella Valthane",
    "Laurentius": "Laurentius Daye",
    "Mutamix": "Mutamix Bubblypots",
    "Isildaure": "Isildaure Vellegrance",
    "Zephirin": "Zephirin de Valhourdin",
    "Dewlala": "Dewlala Dewla",
    "Fourchenault": "Fourchenault Leveilleur",
    "Yotsuyu": "Yotsuyu Brutus",
    "Regula van Hydrus": "Regula Hydrus",
    "Varis": "Varis zos Galvus",
    "Aenor": "Aenor Cockburne",
    "Landenel": "Landenel Peaumasquier",
    "Reyner": "Reyner Hansred",
    "Lolorito": "Lolorito Nanarito",
    "Charibert": "Charibert de Leusignac",
    "Francel": "Joacin Charlemend Francel de Haillenarte",
    "Shiosai": "Shiosai Sui",
    "Godbert": "Godbert Manderville",
    "Lue-Reeq": "Lue-Reeq Chalah",
    "Granson": "Granson Ketchthane",
    "Cerigg": "Cerigg Morpurse",
    "Orella": "Orella Rushton",
    "Thubyrgeim": "Thubyrgeim Guldweitzwyn",
    "Kotokaze": "Kotokaze Benitoki",
    "Sicard": "Sicard Spence",
    "Chambui": "Chambui Dazkar",
    "Miyama": "Kongo Miyama",
    "Y'mhitra": "Y'mhitra Rhul",
    "Yuyutazi": "Yuyutazi Luluhase",
    "Jantellot": "Jantellot de Thelomaire",
    "Aergmhus": "Aergmhus Saehstymmsyn",
    "Rhoswen": "Rhoswen Leach",
    "Liavinne": "Liavinne Painefort",
    "Beatin": "Beatin Mainrocquat",
    "Paulecrain": "Paulecrain de Fanouilley",
    "Grinnaux": "Grinnaux de Dzemael",
    "Adelphel": "Adelphel de Chevraudan",
    "H'naanza": "H'naanza Esi",
    "F'hobas": "F'hobhas",
    "Geva": "Geva Storke",
    "Kikipu": "Kikipu Kipu",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable characters
PC = [
    "The Adventurer",
    "Alphinaud Leveilleur",
    "Y'shtola Rhul",
    "Hien Rijin",
    "Thancred Waters",
    "Estinien Varlineau",
    "Alisaie Leveilleur",
    "Urianger Augurelt",
    "G'raha Tia",
    "Godbert Manderville",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/final_fantasy_xiv/data.csv", index=False)
