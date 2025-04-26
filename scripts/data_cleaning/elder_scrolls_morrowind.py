# Load required libraries
import json
import pandas as pd

# Load the dataset
with open("data/elder_scrolls_morrowind/data.json", "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "PC",
    "Eno Hlaalu",
    "Aryon (Morrowind)",
    "Crassius Curio",
    "Eydis Fire-Eye",
    "Nibani Maesa",
    "Caius Cosades (Morrowind)",
    "Edwinna Elbert",
    "Darius (Morrowind)",
    "Gentleman Jim Stacey (Morrowind)",
    "Athyn Sarethi",
    "Nileno Dorvayn",
    "Baladas Demnevanni (Character)",
    "Lalatia Varian",
    "Sul-Matuul",
    "Neminda",
    "Ajira",
    "Savile Imayn",
    "Duke Vedam Dren (Morrowind)",
    "Vivec (Morrowind)",
    "Divayth Fyr (Morrowind)",
    "Edryno Arethi",
    "Dagoth Ur (Character)",
    "Sugar-Lips Habasi",
    "Sinnammu Mirpal",
    "Skink-in-Tree's-Shade",
    "Kaye",
    "Garothmuk gro-Muzgub",
    "Aengoth the Jeweler",
    "Ranis Athrys",
    "Odral Helvi",
    "Iulus Truptor",
    "Faral Retheran",
    "Tholer Saryoni",
    "Han-Ammu",
    "Theldyn Virith",
    "Llunela Hleran",
    "Lloros Sarano",
    "Dondos Driler",
    "Synnolian Tunifus",
    "Big Helende",
    "Tuls Valen",
    "Manirai",
    "Uvoo Llaren",
    "Therana (Morrowind)",
    "Radd Hard-Heart",
    "Galsa Gindu",
    "Mistress Dratha (Morrowind)",
    "Kaushad",
    "Fast Eddie",
    "Trebonius Artorius",
    "Sharn gra-Muzgob",
    "Gilvas Barelo",
    "Endryn Llethan",
    "Dram Bero",
    "Hasphat Antabolis",
    "Frald the White",
    "Garisa Llethri",
    "Huleeya",
    "Hassour Zainsubani",
    "Ilmeni Dren",
    "Canctunian Ponius",
    "Mehra Milo",
    "Galos Mathendis",
    "Cunius Pelelius",
    "Tharer Rotheloth",
    "Larrius Varro",
    "Addhiranirr",
    "Varvur Sarethi",
    "Raven Omayn",
    "Imsin the Dreamer",
    "Gadayn Andarys",
    "Felisa Ulessen",
    "Varus Vantinius",
    "Neloth (Morrowind)",
    "Salyn Sarethi",
    "Orvas Dren",
    "Hlaren Ramoran",
    "Angoril",
    "Sonummu Zabamat",
    "Sellus Gravius",
    "Nevena Ules",
    "Din",
    "Ra'Gruzgob",
    "Peakstar",
    "Mallam Ryon",
    "Falura Llervu",
    "Ethasi Rilvayn",
    "Arara Uvulas",
    "Teris Raledran",
    "Urshamusa Rapli",
    "Paur Maston",
    "Bolvyn Venim (Morrowind)",
    "Yngling Half-Troll",
    "Yagrum Bagarn (Morrowind)",
    "Widow Vabdas",
    "Eleedal-Lei",
    "Drulene Falen",
    "Baren Alen",
    "Tuveso Beleth",
    "M'aiq the Liar (Morrowind)",
    "Athanden Girith",
    "Assaba-Bentus",
    "Hlireni Indavel",
    "Hides-His-Foot",
    "Drinar Varyon",
    "Botrir",
    "Velanda Omani",
    "Taros Dral",
    "Sadal Doren",
    "Hlormar Wine-Sot",
    "Garyn Girith",
    "Elam Andas",
    "Danso Indules",
    "Anes Hlaren",
    "Turedus Talanian",
    "Saprius Entius",
    "Manat Shimmabadas",
    "Hannat Zainsubani (Character)",
    "Frelene Acques",
    "Delyna Mandas",
    "Bolrin",
    "Yenammu",
    "Uupse Fyr (Morrowind)",
    "Tussurradad",
    "Rasha (Morrowind)",
    "Mistress Brara Morvayn",
    "Gothren (Morrowind)",
    "Duvianus Platorius",
    "Berwen",
    "Wulf",
    "Ughash gro-Batul",
    "Tinos Drothan",
    "Tarvyn Faren",
    "Senilias Cadiusus",
    "Nels Llendo (Character)",
    "Miun-Gei",
    "Miner Arobar",
    "Mathis Dalobar",
    "Lette",
    "Hrisskar Flat-Foot",
    "Giras Indaram",
    "Cassius Olcinius",
    "Assantus Hansar",
    "Ama Nin",
    "Alarvyne Indalas",
    "Zabamund",
    "Vistha-Kai",
    "Vanjirra",
    "Vala Catraso",
    "Socucius Ergalla",
    "Rothis Nethan",
    "Moroni Uvelas",
    "Mevure Hlen",
    "Llovyn Andus",
    "Kausi",
    "Jobasha",
    "Hul",
    "Hort Ledd",
    "Ganciele Douar",
    "Ethys Savil",
    "Erur-Dan",
    "Dutadalk",
    "Drores Arvel",
    "Domalen",
    "Bulfim gra-Shugarz",
    "Arielle Phiencel",
    "Arethan Mandas",
    "Ane Teria",
    "Urven Davor",
    "Umbra (Morrowind)",
    "Tralas Rendas",
    "Tivam Sadri",
    "Tarer Braryn",
    "Tanusea Veloth",
    "Segunivus Mantedius",
    "Ranabi (Morrowind)",
    "Ondres Nerano",
    "Nedhelas",
    "Nartise Arobar",
    "Mossanon",
    "Llaalam Dredil",
    "Itermerel",
    "Ienas Sarandas (Character)",
    "Idrenie Nerothan",
    "Hisin Deep-Raed",
    "Favel Gobor",
    "Deval Beleth",
    "Conoon Chodala (Morrowind)",
    "Bacola Closcius",
    "Azura (Morrowind)",
    "Audenian Valius",
    "Ashu-Ahhe",
    "Ashibaal",
    "Uryne Nirith",
    "Tidros Indaram",
    "Thavere Vedrano",
    "Tenyeminwe",
    "Percius Mercius",
    "Pania Cadiusus",
    "Oritius Maro",
    "Marcel Maurard",
    "Mansilamat Vabdas",
    "Hetman Guls",
    "Galyn Arvel",
    "Fjorgeir",
    "Fathusa Girethi",
    "Ertius Fulbenus",
    "Elvil Vidron",
    "Daynes Redothril",
    "Dandsa",
    "Braynas Hlervu",
    "Vedelea Othril",
    "Ulath-Pal",
    "Tsrazami",
    "Tiram Gadar",
    "Tashpi Ashibael",
    "Sinyaramen",
    "Silm-Dar",
    "Sendus Sathis",
    "Ragash gra-Shuzgub",
    "Raesa Pullia",
    "Piernette Beluelle",
    "Ordinator (Morrowind)",
    "Okur",
    "Nevrasa Dralor",
    "Murudius Flaeus",
    "Lucretinaus Olcinius",
    "Kjeld (Morrowind)",
    "J'Saddha",
    "Helviane Desele",
    "Gindrala Hleran",
    "Garding the Bold",
    "Fargoth",
    "Eraldil",
    "Chaplain Ogrul",
    "Blatta Hateria",
    "Bethes Sarothril",
    "Benunius Agrudilius",
    "Balur Salvu",
    "Arrille",
    "Alvis Teri",
    "Zennammu",
    "Shadbak gra-Burbug",
    "Pilus Amatius",
    "Only-He-Stands-There",
    "On-Wan",
    "Llerar Mandas",
    "Listien Bierles",
    "Jon Hawker",
    "Indrele Rathryon",
    "Fjol",
    "Fevyn Ralen",
    "Fedris Tharen",
    "Delte Fyr (Morrowind)",
    "Dahleena",
    "Codus Callonus",
    "Brallion",
    "Bivale Teneran",
    "Beyte Fyr (Morrowind)",
    "Banor Seran",
    "Anhaedra (Morrowind)",
    "Albecius Colollius",
    "Ahdni",
    "Ahaz",
    "Abassel Asserbassalit",
    "Vevrana Aryon",
    "Varona Nelas (Morrowind)",
    "Tenisi Lladri",
    "Sosia Caristiana",
    "New-Shoes Bragor",
    "Movis Darys",
    "Minabibi Assardarainat",
    "Milyn Faram",
    "Meril Hlaano",
    "Mehrunes Dagon (Morrowind)",
    "Manwe (Morrowind)",
    "Madura Seran",
    "Kund Assarnibani",
    "Ilasour Tansumiran",
    "Foryn Gilnith",
    "Flaenia Amiulusus",
    "Dulnea Ralaal",
    "Beden Giladren",
    "Aurane Frernis",
    "Aryni Orethi",
    "Artisa Arelas",
    "Andil",
    "Alfe Fyr (Morrowind)",
    "Vodunius Nuccius",
    "Vobend Dulfass",
    "Vatollia Apo",
    "Tusamircil",
    "Thanelen Velas",
    "Tappius Esdrecus",
    "Sondryn Irathi",
    "Somutis Vunnis",
    "Sirilonwe",
    "Rufinus Alleius",
    "Remasa Othril",
    "Ra'Zahr",
    "Phane Rielle",
    "Olumba gro-Boglar",
    "Manat Varnan-Adda",
    "Ilden Mirel",
    "Hyna Dorn'ke",
    "Glathel",
    "Galuro Belan",
    "Frizkav Brutya",
    "Fara (Morrowind)",
    "Falanaamo",
    "Elmussa Damori",
    "Daglin Selarar",
    "Crulius Pontanian",
    "Bugdul gro-Kharbush",
    "Brerama Selas",
    "Berel Sala",
    "Arius Rulician",
    "Alven Salas",
    "Alvela Saram",
    "Yantus",
    "Temis Romavel",
    "Sheogorath (Morrowind)",
    "Ra'Virr",
    "Optio Bologra",
    "Okan-Shei",
    "Ohibaal Assintashiran",
    "Nine-Toes",
    "Mollimo of Cloudrest",
    "Mimanu Zeba-Adad",
    "Llirala Sendas",
    "Llevena Sendas",
    "Jocien Ancois",
    "J'Zhirr",
    "Im-Kilaya",
    "Hetman Abelmawia",
    "Hanarai Assutlanipal",
    "Grand Inquisitor (Morrowind)",
    "Galtis Guvron",
    "Fieryra",
    "Carecalmo",
    "Birer Indaram",
    "Big Head (Morrowind)",
    "Bashuk gra-Bat",
    "Addut-Lamanu",
    "Volmyni Dral",
    "Suryn Athones",
    "Shazgob gra-Luzgan",
    "Omesu Hlarys",
    "Kashtes Ilabael",
    "Iniel",
    "Hecerinde",
    "Gashnakh gra-Mughol",
    "Flacassia Fauseius",
    "Esar-Don Dunsamsi",
    "Endase Avel",
    "Emul-Ran",
    "Drerel Indaren",
    "Cavortius Albuttian",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["PC"]["gender"] = "Neutral"
character_info["Eno Hlaalu"]["gender"] = "Male"
character_info["Aryon (Morrowind)"]["gender"] = "Male"
character_info["Crassius Curio"]["gender"] = "Male"
character_info["Eydis Fire-Eye"]["gender"] = "Female"
character_info["Nibani Maesa"]["gender"] = "Female"
character_info["Caius Cosades (Morrowind)"]["gender"] = "Male"
character_info["Edwinna Elbert"]["gender"] = "Female"
character_info["Darius (Morrowind)"]["gender"] = "Male"
character_info["Gentleman Jim Stacey (Morrowind)"]["gender"] = "Male"
character_info["Athyn Sarethi"]["gender"] = "Male"
character_info["Nileno Dorvayn"]["gender"] = "Female"
character_info["Baladas Demnevanni (Character)"]["gender"] = "Male"
character_info["Lalatia Varian"]["gender"] = "Female"
character_info["Sul-Matuul"]["gender"] = "Male"
character_info["Neminda"]["gender"] = "Female"
character_info["Ajira"]["gender"] = "Female"
character_info["Savile Imayn"]["gender"] = "Female"
character_info["Duke Vedam Dren (Morrowind)"]["gender"] = "Male"
character_info["Vivec (Morrowind)"]["gender"] = "Male"
character_info["Divayth Fyr (Morrowind)"]["gender"] = "Male"
character_info["Dagoth Ur (Character)"]["gender"] = "Male"
character_info["Edryno Arethi"]["gender"] = "Female"
character_info["Sugar-Lips Habasi"]["gender"] = "Female"
character_info["Sinnammu Mirpal"]["gender"] = "Female"
character_info["Skink-in-Tree's-Shade"]["gender"] = "Male"
character_info["Kaye"]["gender"] = "Male"
character_info["Garothmuk gro-Muzgub"]["gender"] = "Male"
character_info["Aengoth the Jeweler"]["gender"] = "Male"
character_info["Ranis Athrys"]["gender"] = "Female"
character_info["Odral Helvi"]["gender"] = "Male"
character_info["Iulus Truptor"]["gender"] = "Male"
character_info["Faral Retheran"]["gender"] = "Female"
character_info["Tholer Saryoni"]["gender"] = "Male"
character_info["Han-Ammu"]["gender"] = "Male"
character_info["Theldyn Virith"]["gender"] = "Male"
character_info["Llunela Hleran"]["gender"] = "Female"
character_info["Lloros Sarano"]["gender"] = "Male"
character_info["Dondos Driler"]["gender"] = "Male"
character_info["Synnolian Tunifus"]["gender"] = "Male"
character_info["Big Helende"]["gender"] = "Female"
character_info["Tuls Valen"]["gender"] = "Male"
character_info["Manirai"]["gender"] = "Female"
character_info["Uvoo Llaren"]["gender"] = "Female"
character_info["Therana (Morrowind)"]["gender"] = "Female"
character_info["Radd Hard-Heart"]["gender"] = "Male"
character_info["Galsa Gindu"]["gender"] = "Female"
character_info["Mistress Dratha (Morrowind)"]["gender"] = "Female"
character_info["Kaushad"]["gender"] = "Male"
character_info["Fast Eddie"]["gender"] = "Male"
character_info["Trebonius Artorius"]["gender"] = "Male"
character_info["Sharn gra-Muzgob"]["gender"] = "Female"
character_info["Gilvas Barelo"]["gender"] = "Male"
character_info["Endryn Llethan"]["gender"] = "Male"
character_info["Dram Bero"]["gender"] = "Male"
character_info["Hasphat Antabolis"]["gender"] = "Male"
character_info["Frald the White"]["gender"] = "Male"
character_info["Garisa Llethri"]["gender"] = "Male"
character_info["Huleeya"]["gender"] = "Male"
character_info["Hassour Zainsubani"]["gender"] = "Male"
character_info["Ilmeni Dren"]["gender"] = "Female"
character_info["Canctunian Ponius"]["gender"] = "Male"
character_info["Mehra Milo"]["gender"] = "Female"
character_info["Galos Mathendis"]["gender"] = "Male"
character_info["Cunius Pelelius"]["gender"] = "Male"
character_info["Tharer Rotheloth"]["gender"] = "Male"
character_info["Larrius Varro"]["gender"] = "Male"
character_info["Addhiranirr"]["gender"] = "Female"
character_info["Varvur Sarethi"]["gender"] = "Male"
character_info["Raven Omayn"]["gender"] = "Female"
character_info["Imsin the Dreamer"]["gender"] = "Female"
character_info["Gadayn Andarys"]["gender"] = "Male"
character_info["Felisa Ulessen"]["gender"] = "Female"
character_info["Varus Vantinius"]["gender"] = "Male"
character_info["Neloth (Morrowind)"]["gender"] = "Male"
character_info["Salyn Sarethi"]["gender"] = "Male"
character_info["Orvas Dren"]["gender"] = "Male"
character_info["Hlaren Ramoran"]["gender"] = "Male"
character_info["Angoril"]["gender"] = "Male"
character_info["Sonummu Zabamat"]["gender"] = "Female"
character_info["Sellus Gravius"]["gender"] = "Male"
character_info["Nevena Ules"]["gender"] = "Female"
character_info["Din"]["gender"] = "Male"
character_info["Ra'Gruzgob"]["gender"] = "Male"
character_info["Peakstar"]["gender"] = "Female"
character_info["Mallam Ryon"]["gender"] = "Male"
character_info["Falura Llervu"]["gender"] = "Female"
character_info["Ethasi Rilvayn"]["gender"] = "Female"
character_info["Arara Uvulas"]["gender"] = "Female"
character_info["Teris Raledran"]["gender"] = "Male"
character_info["Urshamusa Rapli"]["gender"] = "Female"
character_info["Paur Maston"]["gender"] = "Male"
character_info["Bolvyn Venim (Morrowind)"]["gender"] = "Male"
character_info["Yngling Half-Troll"]["gender"] = "Male"
character_info["Yagrum Bagarn (Morrowind)"]["gender"] = "Male"
character_info["Widow Vabdas"]["gender"] = "Female"
character_info["Eleedal-Lei"]["gender"] = "Male"
character_info["Drulene Falen"]["gender"] = "Female"
character_info["Baren Alen"]["gender"] = "Male"
character_info["Tuveso Beleth"]["gender"] = "Female"
character_info["M'aiq the Liar (Morrowind)"]["gender"] = "Male"
character_info["Athanden Girith"]["gender"] = "Male"
character_info["Assaba-Bentus"]["gender"] = "Male"
character_info["Hlireni Indavel"]["gender"] = "Female"
character_info["Hides-His-Foot"]["gender"] = "Male"
character_info["Drinar Varyon"]["gender"] = "Male"
character_info["Botrir"]["gender"] = "Male"
character_info["Velanda Omani"]["gender"] = "Female"
character_info["Taros Dral"]["gender"] = "Male"
character_info["Sadal Doren"]["gender"] = "Female"
character_info["Hlormar Wine-Sot"]["gender"] = "Male"
character_info["Garyn Girith"]["gender"] = "Male"
character_info["Elam Andas"]["gender"] = "Male"
character_info["Danso Indules"]["gender"] = "Female"
character_info["Anes Hlaren"]["gender"] = "Male"
character_info["Turedus Talanian"]["gender"] = "Male"
character_info["Saprius Entius"]["gender"] = "Male"
character_info["Manat Shimmabadas"]["gender"] = "Male"
character_info["Hannat Zainsubani (Character)"]["gender"] = "Male"
character_info["Frelene Acques"]["gender"] = "Female"
character_info["Delyna Mandas"]["gender"] = "Female"
character_info["Bolrin"]["gender"] = "Male"
character_info["Yenammu"]["gender"] = "Male"
character_info["Uupse Fyr (Morrowind)"]["gender"] = "Female"
character_info["Tussurradad"]["gender"] = "Male"
character_info["Rasha (Morrowind)"]["gender"] = "Male"
character_info["Mistress Brara Morvayn"]["gender"] = "Female"
character_info["Gothren (Morrowind)"]["gender"] = "Male"
character_info["Duvianus Platorius"]["gender"] = "Male"
character_info["Berwen"]["gender"] = "Female"
character_info["Wulf"]["gender"] = "Male"
character_info["Ughash gro-Batul"]["gender"] = "Male"
character_info["Tinos Drothan"]["gender"] = "Male"
character_info["Tarvyn Faren"]["gender"] = "Male"
character_info["Senilias Cadiusus"]["gender"] = "Male"
character_info["Nels Llendo (Character)"]["gender"] = "Male"
character_info["Miun-Gei"]["gender"] = "Male"
character_info["Miner Arobar"]["gender"] = "Male"
character_info["Mathis Dalobar"]["gender"] = "Male"
character_info["Lette"]["gender"] = "Female"
character_info["Hrisskar Flat-Foot"]["gender"] = "Male"
character_info["Giras Indaram"]["gender"] = "Male"
character_info["Cassius Olcinius"]["gender"] = "Male"
character_info["Assantus Hansar"]["gender"] = "Male"
character_info["Ama Nin"]["gender"] = "Female"
character_info["Alarvyne Indalas"]["gender"] = "Female"
character_info["Zabamund"]["gender"] = "Male"
character_info["Vistha-Kai"]["gender"] = "Male"
character_info["Vanjirra"]["gender"] = "Female"
character_info["Vala Catraso"]["gender"] = "Female"
character_info["Socucius Ergalla"]["gender"] = "Male"
character_info["Rothis Nethan"]["gender"] = "Male"
character_info["Moroni Uvelas"]["gender"] = "Female"
character_info["Mevure Hlen"]["gender"] = "Male"
character_info["Llovyn Andus"]["gender"] = "Male"
character_info["Kausi"]["gender"] = "Male"
character_info["Jobasha"]["gender"] = "Male"
character_info["Hul"]["gender"] = "Female"
character_info["Hort Ledd"]["gender"] = "Male"
character_info["Ganciele Douar"]["gender"] = "Male"
character_info["Ethys Savil"]["gender"] = "Male"
character_info["Erur-Dan"]["gender"] = "Male"
character_info["Dutadalk"]["gender"] = "Male"
character_info["Drores Arvel"]["gender"] = "Male"
character_info["Domalen"]["gender"] = "Male"
character_info["Bulfim gra-Shugarz"]["gender"] = "Female"
character_info["Arielle Phiencel"]["gender"] = "Female"
character_info["Arethan Mandas"]["gender"] = "Male"
character_info["Ane Teria"]["gender"] = "Female"
character_info["Urven Davor"]["gender"] = "Male"
character_info["Umbra (Morrowind)"]["gender"] = "Male"
character_info["Tralas Rendas"]["gender"] = "Male"
character_info["Tivam Sadri"]["gender"] = "Male"
character_info["Tarer Braryn"]["gender"] = "Male"
character_info["Tanusea Veloth"]["gender"] = "Female"
character_info["Segunivus Mantedius"]["gender"] = "Male"
character_info["Ranabi (Morrowind)"]["gender"] = "Male"
character_info["Ondres Nerano"]["gender"] = "Male"
character_info["Nedhelas"]["gender"] = "Male"
character_info["Nartise Arobar"]["gender"] = "Female"
character_info["Mossanon"]["gender"] = "Male"
character_info["Llaalam Dredil"]["gender"] = "Male"
character_info["Itermerel"]["gender"] = "Male"
character_info["Ienas Sarandas (Character)"]["gender"] = "Male"
character_info["Idrenie Nerothan"]["gender"] = "Female"
character_info["Hisin Deep-Raed"]["gender"] = "Female"
character_info["Favel Gobor"]["gender"] = "Male"
character_info["Deval Beleth"]["gender"] = "Male"
character_info["Conoon Chodala (Morrowind)"]["gender"] = "Male"
character_info["Bacola Closcius"]["gender"] = "Male"
character_info["Azura (Morrowind)"]["gender"] = "Female"
character_info["Audenian Valius"]["gender"] = "Male"
character_info["Ashu-Ahhe"]["gender"] = "Male"
character_info["Ashibaal"]["gender"] = "Male"
character_info["Uryne Nirith"]["gender"] = "Male"
character_info["Tidros Indaram"]["gender"] = "Female"
character_info["Thavere Vedrano"]["gender"] = "Male"
character_info["Tenyeminwe"]["gender"] = "Female"
character_info["Percius Mercius"]["gender"] = "Male"
character_info["Pania Cadiusus"]["gender"] = "Female"
character_info["Oritius Maro"]["gender"] = "Male"
character_info["Marcel Maurard"]["gender"] = "Male"
character_info["Mansilamat Vabdas"]["gender"] = "Female"
character_info["Hetman Guls"]["gender"] = "Male"
character_info["Galyn Arvel"]["gender"] = "Female"
character_info["Fjorgeir"]["gender"] = "Male"
character_info["Fathusa Girethi"]["gender"] = "Female"
character_info["Ertius Fulbenus"]["gender"] = "Male"
character_info["Elvil Vidron"]["gender"] = "Male"
character_info["Daynes Redothril"]["gender"] = "Male"
character_info["Dandsa"]["gender"] = "Female"
character_info["Braynas Hlervu"]["gender"] = "Male"
character_info["Vedelea Othril"]["gender"] = "Female"
character_info["Ulath-Pal"]["gender"] = "Male"
character_info["Tsrazami"]["gender"] = "Female"
character_info["Tiram Gadar"]["gender"] = "Male"
character_info["Tashpi Ashibael"]["gender"] = "Female"
character_info["Sinyaramen"]["gender"] = "Male"
character_info["Silm-Dar"]["gender"] = "Male"
character_info["Sendus Sathis"]["gender"] = "Male"
character_info["Ragash gra-Shuzgub"]["gender"] = "Female"
character_info["Raesa Pullia"]["gender"] = "Female"
character_info["Piernette Beluelle"]["gender"] = "Female"
character_info["Ordinator (Morrowind)"]["gender"] = "Male"
character_info["Okur"]["gender"] = "Female"
character_info["Nevrasa Dralor"]["gender"] = "Female"
character_info["Murudius Flaeus"]["gender"] = "Male"
character_info["Lucretinaus Olcinius"]["gender"] = "Male"
character_info["Kjeld (Morrowind)"]["gender"] = "Male"
character_info["J'Saddha"]["gender"] = "Male"
character_info["Helviane Desele"]["gender"] = "Female"
character_info["Gindrala Hleran"]["gender"] = "Female"
character_info["Garding the Bold"]["gender"] = "Male"
character_info["Fargoth"]["gender"] = "Male"
character_info["Eraldil"]["gender"] = "Female"
character_info["Chaplain Ogrul"]["gender"] = "Male"
character_info["Blatta Hateria"]["gender"] = "Female"
character_info["Bethes Sarothril"]["gender"] = "Male"
character_info["Benunius Agrudilius"]["gender"] = "Male"
character_info["Balur Salvu"]["gender"] = "Male"
character_info["Arrille"]["gender"] = "Male"
character_info["Alvis Teri"]["gender"] = "Male"
character_info["Zennammu"]["gender"] = "Female"
character_info["Shadbak gra-Burbug"]["gender"] = "Female"
character_info["Pilus Amatius"]["gender"] = "Male"
character_info["Only-He-Stands-There"]["gender"] = "Male"
character_info["On-Wan"]["gender"] = "Female"
character_info["Llerar Mandas"]["gender"] = "Male"
character_info["Listien Bierles"]["gender"] = "Male"
character_info["Jon Hawker"]["gender"] = "Male"
character_info["Indrele Rathryon"]["gender"] = "Female"
character_info["Fjol"]["gender"] = "Male"
character_info["Fevyn Ralen"]["gender"] = "Male"
character_info["Fedris Tharen"]["gender"] = "Male"
character_info["Delte Fyr (Morrowind)"]["gender"] = "Female"
character_info["Dahleena"]["gender"] = "Female"
character_info["Codus Callonus"]["gender"] = "Male"
character_info["Brallion"]["gender"] = "Male"
character_info["Bivale Teneran"]["gender"] = "Female"
character_info["Beyte Fyr (Morrowind)"]["gender"] = "Female"
character_info["Banor Seran"]["gender"] = "Male"
character_info["Anhaedra (Morrowind)"]["gender"] = "Male"
character_info["Albecius Colollius"]["gender"] = "Male"
character_info["Ahdni"]["gender"] = "Female"
character_info["Ahaz"]["gender"] = "Male"
character_info["Abassel Asserbassalit"]["gender"] = "Male"
character_info["Vevrana Aryon"]["gender"] = "Female"
character_info["Varona Nelas (Morrowind)"]["gender"] = "Female"
character_info["Tenisi Lladri"]["gender"] = "Female"
character_info["Sosia Caristiana"]["gender"] = "Female"
character_info["New-Shoes Bragor"]["gender"] = "Male"
character_info["Movis Darys"]["gender"] = "Male"
character_info["Minabibi Assardarainat"]["gender"] = "Female"
character_info["Milyn Faram"]["gender"] = "Male"
character_info["Meril Hlaano"]["gender"] = "Male"
character_info["Mehrunes Dagon (Morrowind)"]["gender"] = "Male"
character_info["Manwe (Morrowind)"]["gender"] = "Female"
character_info["Madura Seran"]["gender"] = "Female"
character_info["Kund Assarnibani"]["gender"] = "Male"
character_info["Ilasour Tansumiran"]["gender"] = "Male"
character_info["Foryn Gilnith"]["gender"] = "Male"
character_info["Flaenia Amiulusus"]["gender"] = "Female"
character_info["Dulnea Ralaal"]["gender"] = "Female"
character_info["Beden Giladren"]["gender"] = "Male"
character_info["Aurane Frernis"]["gender"] = "Female"
character_info["Aryni Orethi"]["gender"] = "Female"
character_info["Artisa Arelas"]["gender"] = "Female"
character_info["Andil"]["gender"] = "Male"
character_info["Alfe Fyr (Morrowind)"]["gender"] = "Female"
character_info["Vodunius Nuccius"]["gender"] = "Male"
character_info["Vobend Dulfass"]["gender"] = "Male"
character_info["Vatollia Apo"]["gender"] = "Male"
character_info["Tusamircil"]["gender"] = "Male"
character_info["Thanelen Velas"]["gender"] = "Male"
character_info["Tappius Esdrecus"]["gender"] = "Male"
character_info["Sondryn Irathi"]["gender"] = "Female"
character_info["Somutis Vunnis"]["gender"] = "Male"
character_info["Sirilonwe"]["gender"] = "Female"
character_info["Rufinus Alleius"]["gender"] = "Male"
character_info["Remasa Othril"]["gender"] = "Female"
character_info["Ra'Zahr"]["gender"] = "Male"
character_info["Phane Rielle"]["gender"] = "Male"
character_info["Olumba gro-Boglar"]["gender"] = "Male"
character_info["Manat Varnan-Adda"]["gender"] = "Male"
character_info["Ilden Mirel"]["gender"] = "Male"
character_info["Hyna Dorn'ke"]["gender"] = "Female"
character_info["Glathel"]["gender"] = "Female"
character_info["Galuro Belan"]["gender"] = "Female"
character_info["Frizkav Brutya"]["gender"] = "Male"
character_info["Fara (Morrowind)"]["gender"] = "Female"
character_info["Falanaamo"]["gender"] = "Male"
character_info["Elmussa Damori"]["gender"] = "Female"
character_info["Daglin Selarar"]["gender"] = "Male"
character_info["Crulius Pontanian"]["gender"] = "Male"
character_info["Bugdul gro-Kharbush"]["gender"] = "Male"
character_info["Brerama Selas"]["gender"] = "Male"
character_info["Berel Sala"]["gender"] = "Male"
character_info["Arius Rulician"]["gender"] = "Male"
character_info["Alven Salas"]["gender"] = "Male"
character_info["Alvela Saram"]["gender"] = "Female"
character_info["Yantus"]["gender"] = "Male"
character_info["Temis Romavel"]["gender"] = "Male"
character_info["Sheogorath (Morrowind)"]["gender"] = "Male"
character_info["Ra'Virr"]["gender"] = "Male"
character_info["Optio Bologra"]["gender"] = "Male"
character_info["Okan-Shei"]["gender"] = "Male"
character_info["Ohibaal Assintashiran"]["gender"] = "Male"
character_info["Nine-Toes"]["gender"] = "Male"
character_info["Mollimo of Cloudrest"]["gender"] = "Male"
character_info["Mimanu Zeba-Adad"]["gender"] = "Female"
character_info["Llirala Sendas"]["gender"] = "Female"
character_info["Llevena Sendas"]["gender"] = "Female"
character_info["Jocien Ancois"]["gender"] = "Male"
character_info["J'Zhirr"]["gender"] = "Male"
character_info["Im-Kilaya"]["gender"] = "Male"
character_info["Hetman Abelmawia"]["gender"] = "Male"
character_info["Hanarai Assutlanipal"]["gender"] = "Female"
character_info["Grand Inquisitor (Morrowind)"]["gender"] = "Male"
character_info["Galtis Guvron"]["gender"] = "Male"
character_info["Fieryra"]["gender"] = "Female"
character_info["Carecalmo"]["gender"] = "Male"
character_info["Birer Indaram"]["gender"] = "Male"
character_info["Big Head (Morrowind)"]["gender"] = "Male"
character_info["Bashuk gra-Bat"]["gender"] = "Female"
character_info["Addut-Lamanu"]["gender"] = "Female"
character_info["Volmyni Dral"]["gender"] = "Female"
character_info["Suryn Athones"]["gender"] = "Male"
character_info["Shazgob gra-Luzgan"]["gender"] = "Male"
character_info["Omesu Hlarys"]["gender"] = "Female"
character_info["Kashtes Ilabael"]["gender"] = "Male"
character_info["Iniel"]["gender"] = "Female"
character_info["Hecerinde"]["gender"] = "Male"
character_info["Gashnakh gra-Mughol"]["gender"] = "Female"
character_info["Flacassia Fauseius"]["gender"] = "Female"
character_info["Esar-Don Dunsamsi"]["gender"] = "Male"
character_info["Endase Avel"]["gender"] = "Female"
character_info["Emul-Ran"]["gender"] = "Male"
character_info["Drerel Indaren"]["gender"] = "Male"
character_info["Cavortius Albuttian"]["gender"] = "Male"

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
            "Title": "Elder Scrolls Morrowind",
            "Year": "2002",
            "Country": "US",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "PC": "Nerevarine",
    "Aryon (Morrowind)": "Aryon",
    "Caius Cosades (Morrowind)": "Caius Cosades",
    "Darius (Morrowind)": "Darius",
    "Gentleman Jim Stacey (Morrowind)": "Gentleman Jim Stacey",
    "Baladas Demnevanni (Character)": "Baladas Demnevanni",
    "Duke Vedam Dren (Morrowind)": "Duke Vedam Dren",
    "Vivec (Morrowind)": "Vivec",
    "Divayth Fyr (Morrowind)": "Divayth Fyr",
    "Dagoth Ur (Character)": "Dagoth Ur",
    "Therana (Morrowind)": "Therana",
    "Mistress Dratha (Morrowind)": "Mistress Dratha",
    "Neloth (Morrowind)": "Neloth",
    "Bolvyn Venim (Morrowind)": "Bolvyn Venim",
    "Yagrum Bagarn (Morrowind)": "Yagrum Bagarn",
    "M'aiq the Liar (Morrowind)": "M'aiq the Liar",
    "Hannat Zainsubani (Character)": "Hannat Zainsubani",
    "Uupse Fyr (Morrowind)": "Uupse Fyr",
    "Rasha (Morrowind)": "Rasha",
    "Gothren (Morrowind)": "Gothren",
    "Nels Llendo (Character)": "Nels Llendo",
    "Umbra (Morrowind)": "Umbra",
    "Ranabi (Morrowind)": "Ranabi",
    "Ienas Sarandas (Character)": "Ienas Sarandas",
    "Conoon Chodala (Morrowind)": "Conoon Chodala",
    "Azura (Morrowind)": "Azura",
    "Ordinator (Morrowind)": "Ordinator",
    "Kjeld (Morrowind)": "Kjeld",
    "Delte Fyr (Morrowind)": "Delte Fyr",
    "Beyte Fyr (Morrowind)": "Beyte Fyr",
    "Anhaedra (Morrowind)": "Anhaedra",
    "Mehrunes Dagon (Morrowind)": "Mehrunes Dagon",
    "Manwe (Morrowind)": "Manwe",
    "Alfe Fyr (Morrowind)": "Alfe Fyr",
    "Fara (Morrowind)": "Fara",
    "Sheogorath (Morrowind)": "Sheogorath",
    "Grand Inquisitor (Morrowind)": "Grand Inquisitor",
    "Big Head (Morrowind)": "Big Head",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable charaters
PC = ["Nerevarine"]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/elder_scrolls_morrowind/data.csv", index=False)
