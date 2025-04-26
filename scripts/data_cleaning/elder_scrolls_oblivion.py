# Load required libraries
import json
import pandas as pd

# Load the dataset
file_path = "data/elder_scrolls_oblivion/data.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Create a list to store characters
characters = [
    "Generic Imperial Male",
    "Generic Imperial Female",
    "Generic Nord Male",
    "Generic Breton Female",
    "Generic DarkElf Male",
    "Generic Breton Male",
    "Generic WoodElf Male",
    "Generic DarkElf Female",
    "Generic HighElf Male",
    "Generic Orc Male",
    "Generic WoodElf Female",
    "Generic Redguard Male",
    "Generic Argonian Male",
    "Generic Khajiit Male",
    "Generic Argonian Female",
    "Generic HighElf Female",
    "Generic Nord Female",
    "Generic Orc Female",
    "Generic Redguard Female",
    "Generic Khajiit Female",
    "Martin",
    "SEHaskill",
    "ModrynOreyn",
    "SESheogorath",
    "SERelmynaVerenim",
    "Jauffre",
    "Baurus",
    "SEHalion",
    "TarMeena",
    "Ocheeva",
    "RaminusPolus",
    "SEDumagGraBonk",
    "SEEaril",
    "SEAmiableFanriene",
    "SEKithlan",
    "MazogatheOrc",
    "SEBruscusDannus",
    "SESontaire",
    "ArmandChristophe",
    "Neville",
    "SEThaedil",
    "Emfrid",
    "HannibalTraven",
    "SEAhjazda",
    "SEUshnarGroShadborgob",
    "GrayFox",
    "YsabelAndronicus",
    "Skrivva",
    "LucienLachance",
    "NelsTheNaughty",
    "SEUnaArmina",
    "SECindanwe",
    "VicenteValtieri",
    "SEMuurine",
    "Owyn",
    "JanusHassildor",
    "Umbacano",
    "TheNightMother",
    "DovesiDran",
    "Jskar",
    "MatildePetit",
    "PrimoAntonius",
    "SETilseAreleth",
    "KudEi",
    "Srathad",
    "SavlianMatius",
    "Talasma",
    "Teinaava",
    "NarinaCarvain",
    "UrielSeptim",
    "Tamika",
    "Shameer",
    "BumphgraGash",
    "Roliand",
    "SEKilibanNyrandil",
    "Jena",
    "SEOrinthal",
    "SEHerdir",
    "SECutter",
    "SEThadon",
    "Cirroc",
    "SEDyus",
    "SERendilDrarara",
    "GogrongroBolmog",
    "Arquen",
    "Sinderion",
    "Azzan",
    "BurzGroKhash",
    "Glarthir",
    "SEDervenin",
    "Cyrus",
    "SE11Rakheran",
    "AlvalUvani",
    "SEMiriliUlven",
    "Telaendril",
    "Caroline",
    "SEArctus",
    "MankarCamoran",
    "SEJzidzoMania",
    "Karinnarre",
    "Vigdis",
    "GuilbertJemane",
    "VelwynBenirus",
    "AndelIndarys",
    "CariusRunellius",
    "Jearl",
    "VilenaDonton",
    "SEAtrabhiDementia",
    "SEWideEye",
    "SEAtrabhiMania",
    "SESyl",
    "SESicklyBernice",
    "RightWind",
    "SEErverDevani",
    "SEHirrusClutumnus",
    "Sdrassa",
    "SEShelden",
    "Rellian",
    "Jensine",
    "ArrianaValga",
    "SEBeelei",
    "ArenaMouth",
    "Seridur",
    "Earana",
    "Shelley",
    "Amusei",
    "SE08GoldenSaintAurigDesha",
    "SE08DarkSeducerGrakendoUdico",
    "GarrusDarelliun",
    "Teekeeus",
    "MQ15Eldamil",
    "SEJayredIceVeins",
    "MariusCaro",
    "AgronakGroMalog",
    "Jorundr",
    "BeggarLeyawiinRancidRadirsha",
    "ErlineLirrian",
    "BeggarLeyawiinDeehTheScalawag",
    "Raqanar",
    "QuillWeave",
    "SEKaneh",
    "Ormil",
    "LlevanaNedaren",
    "Thoronir",
    "ArnoraAuria",
    "Melisande",
    "RolandJenseric",
    "FarwilIndarys",
    "SERanarrJo",
    "Fafnir",
    "FathisUles",
    "Carahil",
    "Methredhel",
    "Larthjar",
    "Sherina",
    "SECaldanaMonrius",
    "SEAnyaHerrick",
    "Burd",
    "SENanetteDon",
    "Maelona",
    "RosentiaGallenus",
    "RytheLythandas",
    "AlvesUvenim",
    "ReynaldJemane",
    "Sshani",
    "Glenroy",
    "AmminusGregori",
    "SERavenBiter",
    "SEKishashi",
    "MQ15Kathutet",
    "BremmanSenyan",
    "SEGrommokgroBarak",
    "Dagail",
    "Deetsan",
    "Maglir",
    "Chanel",
    "SEPyke",
    "Ocato",
    "TivelaLythandas",
    "SEHorkvirBearArmMania",
    "ValenDreth",
    "ValusOdiil",
    "SEBrithaur",
    "SEHorkvirBearArmDementia",
    "SEMazaddha",
    "SulinusVassinus",
    "SE11Ciirta",
    "Volanaro",
    "JulienneFanis",
    "Phintias",
    "Gwinas",
    "ClaudeMaric",
    "SEToveTheUnrestful",
    "SERunsInCircles",
    "SEBigHead",
    "HalLiurz",
    "Caranya",
    "SEMirel",
    "JeanneFrasoric",
    "HerminiaCinna",
    "Hundolin",
    "SEDylora",
    "Eridor",
    "Falcar",
    "Witseidutsei",
    "SEUlfri",
    "GramangroMarad",
    "AdrienneBerene",
    "Ancotar",
    "SEStaada",
    "LucienLachanceHunted",
    "AntoinettaMarie",
    "DarJee",
    "VantusPrelius",
    "Denel",
    "AelwinMerowald",
    "SEDredhwen",
    "SEZoeMalene",
    "Nerussa",
    "BrotherPiner",
    "MercatorHosidus",
    "RallusOdiil",
    "FaustinaCartia",
    "Skaleel",
    "SEFelasSarandas",
    "SabineLaul",
    "Thalfin",
    "Mirisa",
    "UrsanneLoche",
    "GreyThroat",
    "SEBeggarBolwing",
    "SEJastiraNanusDementia",
    "ArvenaThelas",
    "Ribassa",
    "Agata",
    "Olav",
    "HieronymusLex",
    "GilenNorvalo",
    "SEUrulGoAgamphMania",
    "SEUrulGoAgamphDementia",
    "LucianaGalena",
    "WeebumNa",
    "DynariAmnis",
    "TrayvondtheRedguard",
    "SEJzidzoDementia",
    "PriorMaborel",
    "SESyndeliusGatharian",
    "OngartheWorldWeary",
    "Delmar",
    "KurdangroDragol",
    "SEBeggarBhisha",
    "AntusOdiil",
    "BarthelGernand",
    "SEJastiraNanusMania",
    "Renote",
    "Jollring",
    "Eyja",
    "SERelan",
    "Margarte",
    "UlrichLeland",
    "BerichInian",
    "DubokgroShagk",
    "Erthor",
    "OrgnolfHairyLegs",
    "LaytheWavrick",
    "MillonaUmbranox",
    "ArielleJurard",
    "SEGundlar",
    "Ruma",
    "SENelrene",
    "Athrelor",
    "SE32CountCirion",
    "MyvrynaArano",
    "AncusAfranius",
    "DarMa",
    "Malene",
    "ElseGodHater",
    "ChristopheMarane",
    "IlendVonius",
    "Ruslan",
    "Gogan",
    "BragGroBharg",
    "IrroketheWide",
    "Ahdarji",
    "Elidor",
    "RalsaNorvalo",
    "VaronVamori",
    "BieneAmelion",
    "RavenCamoran",
    "FrancoisMotierre",
    "BatulgraSharob",
    "Sigrid",
    "GuilbertSelone",
    "WeedumJa",
    "Tolgan",
    "GrayFoxStranger",
    "Faelian",
    "DiramSerethi",
    "LuronkgroGlurzog",
    "Selene",
    "ShumgroYarug",
    "Srazirr",
    "Boldon",
    "LenkaValus",
    "Kalthar",
    "ArenaICBlueTeamGladiator",
    "CorrickNorthwode",
    "AleronLoche",
    "HenantierDream",
    "AjumKajin",
    "SEIssmi",
    "SEAdeo",
    "JeetumZe",
    "ManheimMaulhand",
    "Sjirra",
    "JivHiriel",
    "LordRugdumph",
    "SEDulphumphGroUrgash",
    "BittneldtheCurseBringer",
    "Maiqtheliar",
    "Engorm",
    "MoggraMogakh",
    "MraajDar",
    "Enilroth",
    "Rienna",
    "ViranusDonton",
    "Lithnilian",
    "ThorleyAethelred",
    "MorGraGamorn",
    "SESheerMeedish",
    "RegulusTerentius",
    "Eronor",
    "MaevatheBuxom",
    "Harrow",
    "Druja",
    "SELewinTilwald",
    "OgierGeorick",
    "Gilgondorin",
    "SeedNeeus",
    "SignyHomeWrecker",
    "SE01GaiusPrentus",
    "SE32HlovalDreth",
    "AldosOthran",
    "SorisArenim",
    "NorbertLelles",
    "BrusciusLongus",
    "BeggarBravilWretchedAia",
    "BeggarBravilCosmusTheCheat",
    "Agarmir",
    "IrlavJarol",
    "ElanteofAlinor",
    "HlidaraMothril",
    "MS93Varulae",
    "SETallTreesFalling",
    "Umbra",
    "MargueriteDiel",
    "Orrin",
    "HjolfroditheHarrier",
    "Maraska",
    "SE32DesideratusAnnius",
    "LerexusCallidus",
    "PinarusInventius",
    "Aryarie",
    "FerulRavel",
    "JharedStrongblade",
    "SEPadEi",
    "ViggetheCautious",
    "HelviusCecia",
    "OlynSeran",
    "SelenaOrania",
    "FalanuHlaalu",
    "SEBeggarUungor",
    "NewheimthePortly",
    "PerenniaDraconis",
    "Atraena",
    "DraranaThelis",
    "CalliaBincal",
    "SEBeggarGloorolros",
    "GemellusAxius",
    "CaeliaDraconis",
    "Pranal",
    "Jbaana",
    "ToothintheSea",
    "ClaudettePerrick",
    "SE32Althel",
    "Minerva",
    "Amir",
    "AloysBincal",
    "Caminalda",
    "Honditar",
    "Bothiel",
    "VlanhonderMoslin",
    "Shuravi",
    "Hirtel",
    "Mannimarco",
    "Bejeen",
    "ValenDrethDark04",
    "SEBeggarFimmion",
    "MarentheSeal",
    "Vajhira",
    "AndreasDraconis",
    "LordDrad",
    "Ortis",
    "Tsavi",
    "MathieuBellamont",
    "Tierra",
    "JakbenImbel",
    "Andragil",
    "GinWulm",
    "UgakgraMogakh",
    "Petrine",
    "EtiraMoslin",
    "UlfgarFogEye",
    "AugustaCalidia",
    "ArenaICYellowTeamChampion",
    "IlavDralgoner",
    "Haekwon",
    "Kewan",
    "MenienGoneld",
    "Mirie",
    "IlvelRomayn",
    "ErTeeus",
    "SE14Juggler",
    "AlessiaCaro",
    "Palonirya",
    "OrokgroGhoth",
    "ShobobgroRugdush",
    "ToutiusSextius",
    "ErinaJeranus",
    "TertullianVerus",
    "Eilonwy",
    "Angalmo",
    "Bongond",
    "ItiusHayn",
    "Uurwen",
    "Mishaxhi",
    "Mahei",
    "RusiaBradus",
    "Foroch",
    "IsabeauBienne",
    "BeggarCheydinhalLucklessLucina",
    "BeggarCheydinhalBrucciusTheOrphan",
    "UmoggraMarad",
    "Dion",
    "Ardaline",
    "DerveraRomalen",
    "CylbenDolovas",
    "MelsMaryon",
    "ScarTail",
    "Ganredhel",
    "Iver",
    "Anedhel",
    "GulGroBurbog",
    "MelusPetilius",
    "DredenaHlavel",
    "LadyDrad",
    "AlbericLitte",
    "Fithragaer",
    "Dairihill",
    "MartinaFloria",
    "FelenRelas",
    "SEBrevi",
    "Athragar",
    "Clesa",
    "Lynch",
    "Wrath",
    "Sthasa",
    "ViniciaMelissaeia",
    "MQ06MythicDawnDoorkeeper",
    "TovasSelvani",
    "BernadettePeneles",
    "Jeelius",
    "Holger",
    "HidesHisHeart",
    "GoganGuard",
    "SE32BatGroOrkul",
    "Yushi",
    "Rijirr",
    "MatthiasDraconis",
    "BasilErnarde",
    "Eitar",
    "AudensAvidius",
    "RonaHassildor",
    "Merandil",
    "MaranaRian",
    "Tandilwe",
    "BralsaAndaren",
    "IreneMetrick",
    "AlixLencolia",
    "BugakgroBol",
    "DelosFandas",
    "CatFace",
    "MachNa",
    "LorgrenBenirusNPC",
    "Wilbur",
    "Merete",
    "DecentiusOpsius",
    "VieraLerus",
    "Orintur",
    "RaynilDralas",
    "DelphineJend",
    "MarcGulitte",
    "Marz",
    "Aengvir",
    "Rona",
    "LadyRogbut",
    "Ksharr",
    "Smirra",
    "Henantier",
    "AymarDouar",
    "NorasaAdus",
    "Pajeen",
    "DeetumJa",
    "OraggraBargol",
    "Baenlin",
    "Gromm",
    "Alawen",
    "Torbern",
    "TorbaltheSufficient",
    "Astante",
    "Merildor",
    "Maenlorn",
    "Willet",
    "ItaRienus",
    "LutherBroad",
    "Minx",
    "CitySwimmer",
    "Steffan",
    "SE32Anglor",
    "Faurinthil",
    "Degil",
    "Ciindil",
    "SEYngvar",
    "JGhasta",
    "Ashni",
    "TolvasaSendas",
    "Rufio",
    "BlancheMastien",
    "BronsilaKvinchal",
    "UravasaOthrelas",
    "BorbagraUzgash",
    "FathisAren",
    "Varnado",
    "Abhuki",
    "DavelaHlaren",
    "BogrumGroGalash",
    "MagubgraOrum",
    "HafidHollowleg",
    "Tsrava",
    "Droshanji",
    "ArentusFalvius",
    "LeyMarillin",
    "RemanBroder",
    "FadusCalidius",
    "GruiandGarrana",
    "AdamusPhillida",
    "PistaMarillin",
    "UleneHlervu",
    "HaulsRopesFaster",
    "Sakeepa",
    "Othrelos",
    "MarcelAmelion",
    "Boroneth",
    "Dhola",
    "TyrelliusLogellus",
    "DranasLlethro",
    "FrancineVelain",
    "HuntingTail",
    "BurMeema",
    "Thamriel",
    "Trevaia",
    "OlavatheFair",
    "HiltheTall",
    "ContumeliorusFlorius",
    "UndenaOrethi",
    "DraloraAthram",
    "BoderiFarano",
    "Oleta",
    "Jbari",
    "UurastheShepherd",
    "Parwen",
    "Thaurron",
    "Caenlorn",
    "Shafaye",
    "ShagolgroBumph",
    "JaFazir",
    "Jmhad",
    "BrotchCalus",
    "OntusVanin",
    "ServatiusQuintilius",
    "JesanRilian",
    "SchlerusSestius",
    "CamillaLollia",
    "ErissareArenim",
    "SEStela",
    "AdosiSerethi",
    "AmbroiseCanne",
    "LazareMilvan",
    "MirabelleMonet",
    "CandiceCorgine",
    "MarietteRielle",
    "Ernest",
    "HumilisNonius",
    "MalintusAncrus",
    "MQ15Orthe",
    "MivrynaArano",
    "AntoineBranck",
    "GastonTussaud",
    "Tenville",
    "Demetrius",
    "SESfara",
    "AvieraNirol",
    "JavoliaMaborel",
    "BanusAlor",
    "SEBelmyneDreleth",
    "GranthamBlakeley",
    "EduardRetiene",
    "Baeralorn",
    "HeinrichOakenHull",
    "TadroseHelas",
    "EstelleRenoit",
    "TunZeeus",
    "SEGrommokgroBarakGhosted",
    "Neesha",
    "UlmuggroCromgog",
    "VelusHosidius",
    "Cingor",
    "Brodras",
    "Elragail",
    "Mandil",
    "Rasheda",
    "Rhano",
    "SnakgraBura",
    "DulfishgroOrum",
    "LumgroBaroth",
    "HansBlackNail",
    "Alga",
    "DroNahrah",
    "SuriusAfranius",
    "MarianaAncharia",
    "CaulaAllectus",
    "AmantiusAllectus",
    "Ohtesse",
    "DrelsTheran",
    "UrnsiSerethi",
    "GanLuseph",
    "DavideSurilie",
    "Otumeel",
    "AhMalz",
    "Shamar",
    "Carsten",
    "BelisariusArius",
    "RoliandHanus",
    "VontusIdolus",
    "GregoryArne",
    "Beewos",
    "HomrazgraMorgrump",
    "Nardhil",
    "Aenvir",
    "StorntheBurly",
    "LordLovidicus",
    "DranasLerano",
    "AgnetethePickled",
    "Skjorta",
    "TertiaViducia",
    "VarelMorvayn",
    "UlrikaUlfgar",
    "Beirir",
    "HrolUlfgar",
    "TG03ChapelUnderCroftGuard",
    "Gundalas",
    "Tavia",
    "IsleifTheOpenHanded",
    "Jair",
    "Rohssan",
    "Borissean",
    "Wallace",
    "Isolde",
    "Winson",
    "UrbulgroOrkulg",
    "OghashgraMagul",
    "GaturngroGonk",
    "Regner",
    "KeldoftheIsles",
    "MogensWindShifter",
    "Rizakar",
    "Shamada",
    "Nahsi",
    "Hassiri",
    "JulittaPlotius",
    "BettoPlotius",
    "RomanaFaleria",
    "OtiusLoran",
    "CastaScribonia",
    "TyrelliusLogellusOffDuty",
    "WormAnchorite",
    "Ungarion",
    "Voranil",
    "Ohtimbar",
    "Errandil",
    "AvrusAdas",
    "UlenAthram",
    "YvaraChannitte",
    "SalomonGeonette",
    "HastrelOttus",
    "ErnestManis",
    "GastonSurilie",
    "DidierAumilie",
    "TimotheeLaRouche",
    "ElisaPierrane",
    "RodericPierrane",
    "OnStayaSundew",
    "Usheeja",
    "GeemJasaiin",
    "Wumeek",
    "KewanSOUL",
    "MarentheSealSOUL",
    "Atahba",
    "Tilmo",
    "MirieSOUL",
    "IlvelRomaynSOUL",
    "ErTeeusSOUL",
    "Ungolim",
    "GraklakgroBuglump",
    "Angalsama",
    "ForlornWatchmanPre",
    "ShadySam",
    "Curtis",
    "GelliusTerentius",
    "Ranaline",
    "Ashanta",
    "Hlofgar",
    "Enrion",
    "BeatriceGene",
    "ColinStedrine",
    "DreetLai",
    "Suurootan",
    "NatchPinder",
    "MarlenaBrussiner",
    "NivanDalvilu",
    "SisterAngrond",
    "Daenlin",
    "Nilawen",
    "Carwen",
    "Adanrel",
    "Hagaer",
    "Gelephor",
    "Rindir",
    "Hasathil",
    "Thurindil",
    "Anguilon",
    "Huurwen",
    "Laralthir",
    "Caenlin",
    "HillodTheOutlaw",
    "Dorian",
    "Angelie",
    "CarmenLitte",
    "BrokilgroShatur",
    "UzulGroGrulam",
    "DulgroShug",
    "BazurgroGharz",
    "MaknokgroCoblug",
    "RogmeshgraCoblug",
    "GorgogroShura",
    "KrognakgroBrok",
    "KurzgroBaroth",
    "ReistrtheRotted",
    "EdlaDarkHeart",
    "Honmund",
    "Fjotreid",
    "Olfand",
    "SnartheCook",
    "Logvaar",
    "AlgottheNortherner",
    "Gunder",
    "StentheUgly",
    "WilhelmtheWorm",
    "Rigmor",
    "Shomara",
    "Rvanni",
    "JzinDar",
    "RaJhan",
    "Rajiradh",
    "Urjabhi",
    "KantavCheynoslin",
    "SilanaBlandia",
    "JanoniaAurunceia",
    "JanuariusAurunceia",
    "JantusBrolus",
    "GerichSenarel",
    "IsaRaman",
    "BrielusGawey",
    "RestitaStatlilia",
    "KastavKvinchal",
    "VlanarusKvinchal",
    "VelanAndus",
    "PennusMallius",
    "PraxedesAfranius",
    "ReneeGeonette",
    "StantusVarrid",
    "TrenusDuronius",
    "IdaOttus",
    "AlessiaOttus",
    "AstiniaAtius",
    "LurioMaenius",
    "HelvoAtius",
    "SevariusAtius",
    "JenaSintav",
    "JastiaSintav",
    "VontanSintav",
    "TertiusFavonius",
    "MarinusCatiotus",
    "IdaVlinorman",
    "CarmanaSintav",
    "CyroninSintav",
    "InielSintav",
    "MaroRufus",
    "CiceroVerus",
    "SergiusVerus",
    "ViatorAccius",
    "DanusArtellian",
    "ValandrusAbor",
    "NaspiaCosma",
    "RimalusBruiant",
    "RenaBruiant",
    "JesanSextius",
    "AstiaInventius",
    "RufriusVinicius",
    "Langley",
    "DumaniaJirich",
    "CastaFlavus",
    "Carandial",
    "Areldil",
    "Calindil",
    "Salmo",
    "Tumindil",
    "DovynAren",
    "TanasaArano",
    "TolisiGirith",
    "GureryneSelvilo",
    "Glistel",
    "LlensiLlaram",
    "BolorSavel",
    "NoveniOthran",
    "SisterPhebeJeanard",
    "RoxanneBrigette",
    "ChanaMona",
    "DamianMagius",
    "RochelleBantien",
    "SamuelBantien",
    "BeranSintav",
    "KastusSintav",
    "EdgarVautrine",
    "RenaldViernis",
    "MariePalielle",
    "EugalBelette",
    "BrucetusFestinius",
    "Numeen",
    "OleedEi",
    "Geel",
    "Rana",
    "Elsynia",
    "TG06PaleLadyVampire",
    "RisFralmoton",
    "Baurion",
    "Belisarius",
    "Arterion",
    "MondrarHenim",
    "Hridi",
    "Hjar",
    "AzaniBlackheart",
    "Kiara",
    "Eletta",
    "MuggraMurgak",
    "GhorubgroUgdub",
    "Styrbjorn",
    "Ayisha",
    "JBaasha",
    "Zahrasha",
    "GrayFoxCorvus",
    "ClaudiusArcadia",
    "MensaSelas",
    "RalsaNethan",
    "GasparStegine",
    "MQ05AstavWirich",
    "Arkved",
    "MagragroNaybek",
]

# Create a dictionary to store character information
character_info = {}
for character in characters:
    character_info[character] = {}
    character_info[character]["dialogues"] = []

# Label gender for each character
character_info["Generic Imperial Male"]["gender"] = "Male"
character_info["Generic Imperial Female"]["gender"] = "Female"
character_info["Generic Nord Male"]["gender"] = "Male"
character_info["Generic Breton Female"]["gender"] = "Female"
character_info["Generic DarkElf Male"]["gender"] = "Male"
character_info["Generic Breton Male"]["gender"] = "Male"
character_info["Generic WoodElf Male"]["gender"] = "Male"
character_info["Generic DarkElf Female"]["gender"] = "Female"
character_info["Generic HighElf Male"]["gender"] = "Male"
character_info["Generic Orc Male"]["gender"] = "Male"
character_info["Generic WoodElf Female"]["gender"] = "Female"
character_info["Generic Redguard Male"]["gender"] = "Male"
character_info["Generic Argonian Male"]["gender"] = "Male"
character_info["Generic Khajiit Male"]["gender"] = "Male"
character_info["Generic Argonian Female"]["gender"] = "Female"
character_info["Generic HighElf Female"]["gender"] = "Female"
character_info["Generic Nord Female"]["gender"] = "Female"
character_info["Generic Orc Female"]["gender"] = "Female"
character_info["Generic Redguard Female"]["gender"] = "Female"
character_info["Generic Khajiit Female"]["gender"] = "Female"
character_info["Martin"]["gender"] = "Male"
character_info["SEHaskill"]["gender"] = "Male"
character_info["ModrynOreyn"]["gender"] = "Male"
character_info["SESheogorath"]["gender"] = "Male"
character_info["SERelmynaVerenim"]["gender"] = "Female"
character_info["Jauffre"]["gender"] = "Male"
character_info["Baurus"]["gender"] = "Male"
character_info["SEHalion"]["gender"] = "Male"
character_info["TarMeena"]["gender"] = "Female"
character_info["Ocheeva"]["gender"] = "Female"
character_info["RaminusPolus"]["gender"] = "Male"
character_info["SEDumagGraBonk"]["gender"] = "Male"
character_info["SEEaril"]["gender"] = "Male"
character_info["SEAmiableFanriene"]["gender"] = "Male"
character_info["SEKithlan"]["gender"] = "Male"
character_info["MazogatheOrc"]["gender"] = "Female"
character_info["SEBruscusDannus"]["gender"] = "Male"
character_info["SESontaire"]["gender"] = "Female"
character_info["ArmandChristophe"]["gender"] = "Male"
character_info["Neville"]["gender"] = "Male"
character_info["SEThaedil"]["gender"] = "Female"
character_info["Emfrid"]["gender"] = "Female"
character_info["HannibalTraven"]["gender"] = "Male"
character_info["SEAhjazda"]["gender"] = "Female"
character_info["SEUshnarGroShadborgob"]["gender"] = "Male"
character_info["GrayFox"]["gender"] = "Male"
character_info["YsabelAndronicus"]["gender"] = "Female"
character_info["Skrivva"]["gender"] = "Female"
character_info["LucienLachance"]["gender"] = "Male"
character_info["NelsTheNaughty"]["gender"] = "Male"
character_info["SEUnaArmina"]["gender"] = "Male"
character_info["SECindanwe"]["gender"] = "Female"
character_info["VicenteValtieri"]["gender"] = "Male"
character_info["SEMuurine"]["gender"] = "Female"
character_info["Owyn"]["gender"] = "Male"
character_info["JanusHassildor"]["gender"] = "Male"
character_info["Umbacano"]["gender"] = "Male"
character_info["TheNightMother"]["gender"] = "Female"
character_info["DovesiDran"]["gender"] = "Female"
character_info["Jskar"]["gender"] = "Male"
character_info["MatildePetit"]["gender"] = "Female"
character_info["PrimoAntonius"]["gender"] = "Male"
character_info["SETilseAreleth"]["gender"] = "Female"
character_info["KudEi"]["gender"] = "Female"
character_info["Srathad"]["gender"] = "Male"
character_info["SavlianMatius"]["gender"] = "Male"
character_info["Talasma"]["gender"] = "Female"
character_info["Teinaava"]["gender"] = "Male"
character_info["NarinaCarvain"]["gender"] = "Female"
character_info["UrielSeptim"]["gender"] = "Male"
character_info["Tamika"]["gender"] = "Female"
character_info["Shameer"]["gender"] = "Male"
character_info["BumphgraGash"]["gender"] = "Female"
character_info["Roliand"]["gender"] = "Male"
character_info["SEKilibanNyrandil"]["gender"] = "Male"
character_info["Jena"]["gender"] = "Female"
character_info["SEOrinthal"]["gender"] = "Male"
character_info["SEHerdir"]["gender"] = "Male"
character_info["SECutter"]["gender"] = "Female"
character_info["SEThadon"]["gender"] = "Male"
character_info["Cirroc"]["gender"] = "Male"
character_info["SEDyus"]["gender"] = "Male"
character_info["SERendilDrarara"]["gender"] = "Male"
character_info["GogrongroBolmog"]["gender"] = "Male"
character_info["Arquen"]["gender"] = "Female"
character_info["Sinderion"]["gender"] = "Male"
character_info["Azzan"]["gender"] = "Male"
character_info["BurzGroKhash"]["gender"] = "Male"
character_info["Glarthir"]["gender"] = "Male"
character_info["SEDervenin"]["gender"] = "Male"
character_info["Cyrus"]["gender"] = "Male"
character_info["SE11Rakheran"]["gender"] = "Male"
character_info["AlvalUvani"]["gender"] = "Male"
character_info["SEMiriliUlven"]["gender"] = "Female"
character_info["Telaendril"]["gender"] = "Female"
character_info["Caroline"]["gender"] = "Female"
character_info["SEArctus"]["gender"] = "Male"
character_info["MankarCamoran"]["gender"] = "Male"
character_info["SEJzidzoMania"]["gender"] = "Male"
character_info["Karinnarre"]["gender"] = "Female"
character_info["Vigdis"]["gender"] = "Female"
character_info["GuilbertJemane"]["gender"] = "Male"
character_info["VelwynBenirus"]["gender"] = "Male"
character_info["AndelIndarys"]["gender"] = "Male"
character_info["CariusRunellius"]["gender"] = "Male"
character_info["Jearl"]["gender"] = "Female"
character_info["VilenaDonton"]["gender"] = "Female"
character_info["SEAtrabhiDementia"]["gender"] = "Female"
character_info["SEWideEye"]["gender"] = "Female"
character_info["SEAtrabhiMania"]["gender"] = "Female"
character_info["SESyl"]["gender"] = "Female"
character_info["SESicklyBernice"]["gender"] = "Female"
character_info["RightWind"]["gender"] = "Male"
character_info["SEErverDevani"]["gender"] = "Male"
character_info["SEHirrusClutumnus"]["gender"] = "Male"
character_info["Sdrassa"]["gender"] = "Male"
character_info["SEShelden"]["gender"] = "Male"
character_info["Rellian"]["gender"] = "Male"
character_info["Jensine"]["gender"] = "Female"
character_info["ArrianaValga"]["gender"] = "Female"
character_info["SEBeelei"]["gender"] = "Female"
character_info["ArenaMouth"]["gender"] = "Male"
character_info["Seridur"]["gender"] = "Male"
character_info["Earana"]["gender"] = "Female"
character_info["Shelley"]["gender"] = "Female"
character_info["Amusei"]["gender"] = "Male"
character_info["SE08GoldenSaintAurigDesha"]["gender"] = "Female"
character_info["SE08DarkSeducerGrakendoUdico"]["gender"] = "Female"
character_info["GarrusDarelliun"]["gender"] = "Male"
character_info["Teekeeus"]["gender"] = "Male"
character_info["MQ15Eldamil"]["gender"] = "Male"
character_info["SEJayredIceVeins"]["gender"] = "Male"
character_info["MariusCaro"]["gender"] = "Male"
character_info["AgronakGroMalog"]["gender"] = "Male"
character_info["Jorundr"]["gender"] = "Male"
character_info["BeggarLeyawiinRancidRadirsha"]["gender"] = "Female"
character_info["ErlineLirrian"]["gender"] = "Female"
character_info["BeggarLeyawiinDeehTheScalawag"]["gender"] = "Male"
character_info["Raqanar"]["gender"] = "Male"
character_info["QuillWeave"]["gender"] = "Female"
character_info["SEKaneh"]["gender"] = "Female"
character_info["Ormil"]["gender"] = "Male"
character_info["LlevanaNedaren"]["gender"] = "Female"
character_info["Thoronir"]["gender"] = "Male"
character_info["ArnoraAuria"]["gender"] = "Female"
character_info["Melisande"]["gender"] = "Female"
character_info["RolandJenseric"]["gender"] = "Male"
character_info["FarwilIndarys"]["gender"] = "Male"
character_info["SERanarrJo"]["gender"] = "Male"
character_info["Fafnir"]["gender"] = "Male"
character_info["FathisUles"]["gender"] = "Male"
character_info["Carahil"]["gender"] = "Female"
character_info["Methredhel"]["gender"] = "Female"
character_info["Larthjar"]["gender"] = "Male"
character_info["Sherina"]["gender"] = "Female"
character_info["SECaldanaMonrius"]["gender"] = "Female"
character_info["SEAnyaHerrick"]["gender"] = "Female"
character_info["Burd"]["gender"] = "Male"
character_info["SENanetteDon"]["gender"] = "Female"
character_info["Maelona"]["gender"] = "Female"
character_info["RosentiaGallenus"]["gender"] = "Female"
character_info["RytheLythandas"]["gender"] = "Male"
character_info["AlvesUvenim"]["gender"] = "Female"
character_info["ReynaldJemane"]["gender"] = "Male"
character_info["Sshani"]["gender"] = "Male"
character_info["Glenroy"]["gender"] = "Male"
character_info["AmminusGregori"]["gender"] = "Male"
character_info["SERavenBiter"]["gender"] = "Male"
character_info["SEKishashi"]["gender"] = "Female"
character_info["MQ15Kathutet"]["gender"] = "Male"
character_info["BremmanSenyan"]["gender"] = "Male"
character_info["SEGrommokgroBarak"]["gender"] = "Male"
character_info["Dagail"]["gender"] = "Female"
character_info["Deetsan"]["gender"] = "Female"
character_info["Maglir"]["gender"] = "Male"
character_info["Chanel"]["gender"] = "Female"
character_info["SEPyke"]["gender"] = "Male"
character_info["Ocato"]["gender"] = "Male"
character_info["TivelaLythandas"]["gender"] = "Female"
character_info["SEHorkvirBearArmMania"]["gender"] = "Male"
character_info["ValenDreth"]["gender"] = "Male"
character_info["ValusOdiil"]["gender"] = "Male"
character_info["SEBrithaur"]["gender"] = "Male"
character_info["SEHorkvirBearArmDementia"]["gender"] = "Male"
character_info["SEMazaddha"]["gender"] = "Male"
character_info["SulinusVassinus"]["gender"] = "Male"
character_info["SE11Ciirta"]["gender"] = "Female"
character_info["Volanaro"]["gender"] = "Male"
character_info["JulienneFanis"]["gender"] = "Female"
character_info["Phintias"]["gender"] = "Male"
character_info["Gwinas"]["gender"] = "Male"
character_info["ClaudeMaric"]["gender"] = "Male"
character_info["SEToveTheUnrestful"]["gender"] = "Male"
character_info["SERunsInCircles"]["gender"] = "Female"
character_info["SEBigHead"]["gender"] = "Male"
character_info["HalLiurz"]["gender"] = "Female"
character_info["Caranya"]["gender"] = "Female"
character_info["SEMirel"]["gender"] = "Male"
character_info["JeanneFrasoric"]["gender"] = "Female"
character_info["HerminiaCinna"]["gender"] = "Female"
character_info["Hundolin"]["gender"] = "Male"
character_info["SEDylora"]["gender"] = "Female"
character_info["Eridor"]["gender"] = "Male"
character_info["Falcar"]["gender"] = "Male"
character_info["Witseidutsei"]["gender"] = "Female"
character_info["SEUlfri"]["gender"] = "Female"
character_info["GramangroMarad"]["gender"] = "Male"
character_info["AdrienneBerene"]["gender"] = "Female"
character_info["Ancotar"]["gender"] = "Male"
character_info["SEStaada"]["gender"] = "Female"
character_info["LucienLachanceHunted"]["gender"] = "Male"
character_info["AntoinettaMarie"]["gender"] = "Female"
character_info["DarJee"]["gender"] = "Male"
character_info["VantusPrelius"]["gender"] = "Male"
character_info["Denel"]["gender"] = "Male"
character_info["AelwinMerowald"]["gender"] = "Male"
character_info["SEDredhwen"]["gender"] = "Female"
character_info["SEZoeMalene"]["gender"] = "Female"
character_info["Nerussa"]["gender"] = "Female"
character_info["BrotherPiner"]["gender"] = "Male"
character_info["MercatorHosidus"]["gender"] = "Male"
character_info["RallusOdiil"]["gender"] = "Male"
character_info["FaustinaCartia"]["gender"] = "Female"
character_info["Skaleel"]["gender"] = "Female"
character_info["SEFelasSarandas"]["gender"] = "Male"
character_info["SabineLaul"]["gender"] = "Female"
character_info["Thalfin"]["gender"] = "Female"
character_info["Mirisa"]["gender"] = "Female"
character_info["UrsanneLoche"]["gender"] = "Female"
character_info["GreyThroat"]["gender"] = "Male"
character_info["SEBeggarBolwing"]["gender"] = "Male"
character_info["SEJastiraNanusDementia"]["gender"] = "Female"
character_info["ArvenaThelas"]["gender"] = "Female"
character_info["Ribassa"]["gender"] = "Male"
character_info["Agata"]["gender"] = "Female"
character_info["Olav"]["gender"] = "Male"
character_info["HieronymusLex"]["gender"] = "Male"
character_info["GilenNorvalo"]["gender"] = "Male"
character_info["SEUrulGoAgamphMania"]["gender"] = "Male"
character_info["SEUrulGoAgamphDementia"]["gender"] = "Male"
character_info["LucianaGalena"]["gender"] = "Female"
character_info["WeebumNa"]["gender"] = "Male"
character_info["DynariAmnis"]["gender"] = "Female"
character_info["TrayvondtheRedguard"]["gender"] = "Male"
character_info["SEJzidzoDementia"]["gender"] = "Male"
character_info["PriorMaborel"]["gender"] = "Male"
character_info["SESyndeliusGatharian"]["gender"] = "Male"
character_info["OngartheWorldWeary"]["gender"] = "Male"
character_info["Delmar"]["gender"] = "Male"
character_info["KurdangroDragol"]["gender"] = "Male"
character_info["SEBeggarBhisha"]["gender"] = "Male"
character_info["AntusOdiil"]["gender"] = "Male"
character_info["BarthelGernand"]["gender"] = "Male"
character_info["SEJastiraNanusMania"]["gender"] = "Male"
character_info["Renote"]["gender"] = "Female"
character_info["Jollring"]["gender"] = "Male"
character_info["Eyja"]["gender"] = "Female"
character_info["SERelan"]["gender"] = "Male"
character_info["Margarte"]["gender"] = "Female"
character_info["UlrichLeland"]["gender"] = "Male"
character_info["BerichInian"]["gender"] = "Male"
character_info["DubokgroShagk"]["gender"] = "Male"
character_info["Erthor"]["gender"] = "Male"
character_info["OrgnolfHairyLegs"]["gender"] = "Male"
character_info["LaytheWavrick"]["gender"] = "Male"
character_info["MillonaUmbranox"]["gender"] = "Female"
character_info["ArielleJurard"]["gender"] = "Female"
character_info["SEGundlar"]["gender"] = "Male"
character_info["Ruma"]["gender"] = "Female"
character_info["SENelrene"]["gender"] = "Female"
character_info["Athrelor"]["gender"] = "Male"
character_info["SE32CountCirion"]["gender"] = "Male"
character_info["MyvrynaArano"]["gender"] = "Female"
character_info["AncusAfranius"]["gender"] = "Male"
character_info["DarMa"]["gender"] = "Female"
character_info["Malene"]["gender"] = "Female"
character_info["ElseGodHater"]["gender"] = "Female"
character_info["ChristopheMarane"]["gender"] = "Male"
character_info["IlendVonius"]["gender"] = "Male"
character_info["Ruslan"]["gender"] = "Male"
character_info["Gogan"]["gender"] = "Male"
character_info["BragGroBharg"]["gender"] = "Male"
character_info["IrroketheWide"]["gender"] = "Male"
character_info["Ahdarji"]["gender"] = "Female"
character_info["Elidor"]["gender"] = "Male"
character_info["RalsaNorvalo"]["gender"] = "Female"
character_info["VaronVamori"]["gender"] = "Male"
character_info["BieneAmelion"]["gender"] = "Female"
character_info["RavenCamoran"]["gender"] = "Male"
character_info["FrancoisMotierre"]["gender"] = "Male"
character_info["BatulgraSharob"]["gender"] = "Female"
character_info["Sigrid"]["gender"] = "Female"
character_info["GuilbertSelone"]["gender"] = "Male"
character_info["WeedumJa"]["gender"] = "Female"
character_info["Tolgan"]["gender"] = "Male"
character_info["GrayFoxStranger"]["gender"] = "Male"
character_info["Faelian"]["gender"] = "Male"
character_info["DiramSerethi"]["gender"] = "Male"
character_info["LuronkgroGlurzog"]["gender"] = "Male"
character_info["Selene"]["gender"] = "Female"
character_info["ShumgroYarug"]["gender"] = "Male"
character_info["Srazirr"]["gender"] = "Male"
character_info["Boldon"]["gender"] = "Male"
character_info["LenkaValus"]["gender"] = "Female"
character_info["Kalthar"]["gender"] = "Male"
character_info["ArenaICBlueTeamGladiator"]["gender"] = "Male"
character_info["CorrickNorthwode"]["gender"] = "Male"
character_info["AleronLoche"]["gender"] = "Male"
character_info["HenantierDream"]["gender"] = "Male"
character_info["AjumKajin"]["gender"] = "Male"
character_info["SEIssmi"]["gender"] = "Female"
character_info["SEAdeo"]["gender"] = "Female"
character_info["JeetumZe"]["gender"] = "Male"
character_info["ManheimMaulhand"]["gender"] = "Male"
character_info["Sjirra"]["gender"] = "Female"
character_info["JivHiriel"]["gender"] = "Male"
character_info["LordRugdumph"]["gender"] = "Male"
character_info["SEDulphumphGroUrgash"]["gender"] = "Male"
character_info["BittneldtheCurseBringer"]["gender"] = "Male"
character_info["Maiqtheliar"]["gender"] = "Male"
character_info["Engorm"]["gender"] = "Male"
character_info["MoggraMogakh"]["gender"] = "Female"
character_info["MraajDar"]["gender"] = "Male"
character_info["Enilroth"]["gender"] = "Male"
character_info["Rienna"]["gender"] = "Female"
character_info["ViranusDonton"]["gender"] = "Male"
character_info["Lithnilian"]["gender"] = "Male"
character_info["ThorleyAethelred"]["gender"] = "Male"
character_info["MorGraGamorn"]["gender"] = "Female"
character_info["SESheerMeedish"]["gender"] = "Female"
character_info["RegulusTerentius"]["gender"] = "Male"
character_info["Eronor"]["gender"] = "Male"
character_info["MaevatheBuxom"]["gender"] = "Female"
character_info["Harrow"]["gender"] = "Male"
character_info["Druja"]["gender"] = "Female"
character_info["SELewinTilwald"]["gender"] = "Male"
character_info["OgierGeorick"]["gender"] = "Male"
character_info["Gilgondorin"]["gender"] = "Male"
character_info["SeedNeeus"]["gender"] = "Female"
character_info["SignyHomeWrecker"]["gender"] = "Female"
character_info["SE01GaiusPrentus"]["gender"] = "Male"
character_info["SE32HlovalDreth"]["gender"] = "Male"
character_info["AldosOthran"]["gender"] = "Male"
character_info["SorisArenim"]["gender"] = "Male"
character_info["NorbertLelles"]["gender"] = "Male"
character_info["BrusciusLongus"]["gender"] = "Male"
character_info["BeggarBravilWretchedAia"]["gender"] = "Female"
character_info["BeggarBravilCosmusTheCheat"]["gender"] = "Male"
character_info["Agarmir"]["gender"] = "Male"
character_info["IrlavJarol"]["gender"] = "Male"
character_info["ElanteofAlinor"]["gender"] = "Female"
character_info["HlidaraMothril"]["gender"] = "Female"
character_info["MS93Varulae"]["gender"] = "Female"
character_info["SETallTreesFalling"]["gender"] = "Female"
character_info["Umbra"]["gender"] = "Female"
character_info["MargueriteDiel"]["gender"] = "Female"
character_info["Orrin"]["gender"] = "Male"
character_info["HjolfroditheHarrier"]["gender"] = "Female"
character_info["Maraska"]["gender"] = "Male"
character_info["SE32DesideratusAnnius"]["gender"] = "Male"
character_info["LerexusCallidus"]["gender"] = "Male"
character_info["PinarusInventius"]["gender"] = "Male"
character_info["Aryarie"]["gender"] = "Female"
character_info["FerulRavel"]["gender"] = "Male"
character_info["JharedStrongblade"]["gender"] = "Male"
character_info["SEPadEi"]["gender"] = "Male"
character_info["ViggetheCautious"]["gender"] = "Male"
character_info["HelviusCecia"]["gender"] = "Male"
character_info["OlynSeran"]["gender"] = "Male"
character_info["SelenaOrania"]["gender"] = "Female"
character_info["FalanuHlaalu"]["gender"] = "Female"
character_info["SEBeggarUungor"]["gender"] = "Male"
character_info["NewheimthePortly"]["gender"] = "Male"
character_info["PerenniaDraconis"]["gender"] = "Female"
character_info["Atraena"]["gender"] = "Female"
character_info["DraranaThelis"]["gender"] = "Female"
character_info["CalliaBincal"]["gender"] = "Female"
character_info["SEBeggarGloorolros"]["gender"] = "Male"
character_info["GemellusAxius"]["gender"] = "Male"
character_info["CaeliaDraconis"]["gender"] = "Female"
character_info["Pranal"]["gender"] = "Male"
character_info["Jbaana"]["gender"] = "Male"
character_info["ToothintheSea"]["gender"] = "Male"
character_info["ClaudettePerrick"]["gender"] = "Female"
character_info["SE32Althel"]["gender"] = "Female"
character_info["Minerva"]["gender"] = "Female"
character_info["Amir"]["gender"] = "Male"
character_info["AloysBincal"]["gender"] = "Male"
character_info["Caminalda"]["gender"] = "Female"
character_info["Honditar"]["gender"] = "Male"
character_info["Bothiel"]["gender"] = "Female"
character_info["VlanhonderMoslin"]["gender"] = "Male"
character_info["Shuravi"]["gender"] = "Female"
character_info["Hirtel"]["gender"] = "Male"
character_info["Mannimarco"]["gender"] = "Male"
character_info["Bejeen"]["gender"] = "Female"
character_info["ValenDrethDark04"]["gender"] = "Male"
character_info["SEBeggarFimmion"]["gender"] = "Male"
character_info["MarentheSeal"]["gender"] = "Female"
character_info["Vajhira"]["gender"] = "Female"
character_info["AndreasDraconis"]["gender"] = "Male"
character_info["LordDrad"]["gender"] = "Male"
character_info["Ortis"]["gender"] = "Male"
character_info["Tsavi"]["gender"] = "Female"
character_info["MathieuBellamont"]["gender"] = "Male"
character_info["Tierra"]["gender"] = "Female"
character_info["JakbenImbel"]["gender"] = "Male"
character_info["Andragil"]["gender"] = "Female"
character_info["GinWulm"]["gender"] = "Male"
character_info["UgakgraMogakh"]["gender"] = "Female"
character_info["Petrine"]["gender"] = "Female"
character_info["EtiraMoslin"]["gender"] = "Female"
character_info["UlfgarFogEye"]["gender"] = "Male"
character_info["AugustaCalidia"]["gender"] = "Female"
character_info["ArenaICYellowTeamChampion"]["gender"] = "Female"
character_info["IlavDralgoner"]["gender"] = "Male"
character_info["Haekwon"]["gender"] = "Male"
character_info["Kewan"]["gender"] = "Male"
character_info["MenienGoneld"]["gender"] = "Male"
character_info["Mirie"]["gender"] = "Female"
character_info["IlvelRomayn"]["gender"] = "Male"
character_info["ErTeeus"]["gender"] = "Male"
character_info["SE14Juggler"]["gender"] = "Female"
character_info["AlessiaCaro"]["gender"] = "Female"
character_info["Palonirya"]["gender"] = "Female"
character_info["OrokgroGhoth"]["gender"] = "Male"
character_info["ShobobgroRugdush"]["gender"] = "Male"
character_info["ToutiusSextius"]["gender"] = "Male"
character_info["ErinaJeranus"]["gender"] = "Female"
character_info["TertullianVerus"]["gender"] = "Male"
character_info["Eilonwy"]["gender"] = "Female"
character_info["Angalmo"]["gender"] = "Male"
character_info["Bongond"]["gender"] = "Male"
character_info["ItiusHayn"]["gender"] = "Male"
character_info["Uurwen"]["gender"] = "Female"
character_info["Mishaxhi"]["gender"] = "Male"
character_info["Mahei"]["gender"] = "Male"
character_info["RusiaBradus"]["gender"] = "Female"
character_info["Foroch"]["gender"] = "Male"
character_info["IsabeauBienne"]["gender"] = "Female"
character_info["BeggarCheydinhalLucklessLucina"]["gender"] = "Female"
character_info["BeggarCheydinhalBrucciusTheOrphan"]["gender"] = "Male"
character_info["UmoggraMarad"]["gender"] = "Female"
character_info["Dion"]["gender"] = "Male"
character_info["Ardaline"]["gender"] = "Female"
character_info["DerveraRomalen"]["gender"] = "Female"
character_info["CylbenDolovas"]["gender"] = "Male"
character_info["MelsMaryon"]["gender"] = "Male"
character_info["ScarTail"]["gender"] = "Male"
character_info["Ganredhel"]["gender"] = "Female"
character_info["Iver"]["gender"] = "Male"
character_info["Anedhel"]["gender"] = "Female"
character_info["GulGroBurbog"]["gender"] = "Male"
character_info["MelusPetilius"]["gender"] = "Male"
character_info["DredenaHlavel"]["gender"] = "Female"
character_info["LadyDrad"]["gender"] = "Female"
character_info["AlbericLitte"]["gender"] = "Male"
character_info["Fithragaer"]["gender"] = "Male"
character_info["Dairihill"]["gender"] = "Female"
character_info["MartinaFloria"]["gender"] = "Female"
character_info["FelenRelas"]["gender"] = "Male"
character_info["SEBrevi"]["gender"] = "Female"
character_info["Athragar"]["gender"] = "Male"
character_info["Clesa"]["gender"] = "Female"
character_info["Lynch"]["gender"] = "Male"
character_info["Wrath"]["gender"] = "Male"
character_info["Sthasa"]["gender"] = "Female"
character_info["ViniciaMelissaeia"]["gender"] = "Female"
character_info["MQ06MythicDawnDoorkeeper"]["gender"] = "Male"
character_info["TovasSelvani"]["gender"] = "Male"
character_info["BernadettePeneles"]["gender"] = "Female"
character_info["Jeelius"]["gender"] = "Male"
character_info["Holger"]["gender"] = "Male"
character_info["HidesHisHeart"]["gender"] = "Male"
character_info["GoganGuard"]["gender"] = "Male"
character_info["SE32BatGroOrkul"]["gender"] = "Male"
character_info["Yushi"]["gender"] = "Female"
character_info["Rijirr"]["gender"] = "Male"
character_info["MatthiasDraconis"]["gender"] = "Male"
character_info["BasilErnarde"]["gender"] = "Male"
character_info["Eitar"]["gender"] = "Male"
character_info["AudensAvidius"]["gender"] = "Male"
character_info["RonaHassildor"]["gender"] = "Female"
character_info["Merandil"]["gender"] = "Male"
character_info["MaranaRian"]["gender"] = "Female"
character_info["Tandilwe"]["gender"] = "Female"
character_info["BralsaAndaren"]["gender"] = "Female"
character_info["IreneMetrick"]["gender"] = "Female"
character_info["AlixLencolia"]["gender"] = "Male"
character_info["BugakgroBol"]["gender"] = "Male"
character_info["DelosFandas"]["gender"] = "Male"
character_info["CatFace"]["gender"] = "Male"
character_info["MachNa"]["gender"] = "Female"
character_info["LorgrenBenirusNPC"]["gender"] = "Male"
character_info["Wilbur"]["gender"] = "Male"
character_info["Merete"]["gender"] = "Female"
character_info["DecentiusOpsius"]["gender"] = "Male"
character_info["VieraLerus"]["gender"] = "Female"
character_info["Orintur"]["gender"] = "Male"
character_info["RaynilDralas"]["gender"] = "Male"
character_info["DelphineJend"]["gender"] = "Female"
character_info["MarcGulitte"]["gender"] = "Male"
character_info["Marz"]["gender"] = "Female"
character_info["Aengvir"]["gender"] = "Male"
character_info["Rona"]["gender"] = "Female"
character_info["LadyRogbut"]["gender"] = "Female"
character_info["Ksharr"]["gender"] = "Male"
character_info["Smirra"]["gender"] = "Female"
character_info["Henantier"]["gender"] = "Male"
character_info["AymarDouar"]["gender"] = "Male"
character_info["NorasaAdus"]["gender"] = "Female"
character_info["Pajeen"]["gender"] = "Male"
character_info["DeetumJa"]["gender"] = "Male"
character_info["OraggraBargol"]["gender"] = "Female"
character_info["Baenlin"]["gender"] = "Male"
character_info["Gromm"]["gender"] = "Male"
character_info["Alawen"]["gender"] = "Female"
character_info["Torbern"]["gender"] = "Male"
character_info["TorbaltheSufficient"]["gender"] = "Male"
character_info["Astante"]["gender"] = "Female"
character_info["Merildor"]["gender"] = "Male"
character_info["Maenlorn"]["gender"] = "Male"
character_info["Willet"]["gender"] = "Male"
character_info["ItaRienus"]["gender"] = "Female"
character_info["LutherBroad"]["gender"] = "Male"
character_info["Minx"]["gender"] = "Female"
character_info["CitySwimmer"]["gender"] = "Female"
character_info["Steffan"]["gender"] = "Male"
character_info["SE32Anglor"]["gender"] = "Male"
character_info["Faurinthil"]["gender"] = "Female"
character_info["Degil"]["gender"] = "Female"
character_info["Ciindil"]["gender"] = "Female"
character_info["SEYngvar"]["gender"] = "Male"
character_info["JGhasta"]["gender"] = "Male"
character_info["Ashni"]["gender"] = "Female"
character_info["TolvasaSendas"]["gender"] = "Female"
character_info["Rufio"]["gender"] = "Male"
character_info["BlancheMastien"]["gender"] = "Female"
character_info["BronsilaKvinchal"]["gender"] = "Female"
character_info["UravasaOthrelas"]["gender"] = "Female"
character_info["BorbagraUzgash"]["gender"] = "Female"
character_info["FathisAren"]["gender"] = "Male"
character_info["Varnado"]["gender"] = "Male"
character_info["Abhuki"]["gender"] = "Female"
character_info["DavelaHlaren"]["gender"] = "Female"
character_info["BogrumGroGalash"]["gender"] = "Male"
character_info["MagubgraOrum"]["gender"] = "Male"
character_info["HafidHollowleg"]["gender"] = "Male"
character_info["Tsrava"]["gender"] = "Female"
character_info["Droshanji"]["gender"] = "Male"
character_info["ArentusFalvius"]["gender"] = "Male"
character_info["LeyMarillin"]["gender"] = "Male"
character_info["RemanBroder"]["gender"] = "Male"
character_info["FadusCalidius"]["gender"] = "Male"
character_info["GruiandGarrana"]["gender"] = "Female"
character_info["AdamusPhillida"]["gender"] = "Male"
character_info["PistaMarillin"]["gender"] = "Female"
character_info["UleneHlervu"]["gender"] = "Female"
character_info["HaulsRopesFaster"]["gender"] = "Male"
character_info["Sakeepa"]["gender"] = "Male"
character_info["Othrelos"]["gender"] = "Male"
character_info["MarcelAmelion"]["gender"] = "Male"
character_info["Boroneth"]["gender"] = "Female"
character_info["Dhola"]["gender"] = "Female"
character_info["TyrelliusLogellus"]["gender"] = "Male"
character_info["DranasLlethro"]["gender"] = "Male"
character_info["FrancineVelain"]["gender"] = "Female"
character_info["HuntingTail"]["gender"] = "Male"
character_info["BurMeema"]["gender"] = "Female"
character_info["Thamriel"]["gender"] = "Female"
character_info["Trevaia"]["gender"] = "Female"
character_info["OlavatheFair"]["gender"] = "Female"
character_info["HiltheTall"]["gender"] = "Male"
character_info["ContumeliorusFlorius"]["gender"] = "Male"
character_info["UndenaOrethi"]["gender"] = "Female"
character_info["DraloraAthram"]["gender"] = "Female"
character_info["BoderiFarano"]["gender"] = "Female"
character_info["Oleta"]["gender"] = "Female"
character_info["Jbari"]["gender"] = "Male"
character_info["UurastheShepherd"]["gender"] = "Male"
character_info["Parwen"]["gender"] = "Female"
character_info["Thaurron"]["gender"] = "Male"
character_info["Caenlorn"]["gender"] = "Male"
character_info["Shafaye"]["gender"] = "Female"
character_info["ShagolgroBumph"]["gender"] = "Male"
character_info["JaFazir"]["gender"] = "Male"
character_info["Jmhad"]["gender"] = "Male"
character_info["BrotchCalus"]["gender"] = "Male"
character_info["OntusVanin"]["gender"] = "Male"
character_info["ServatiusQuintilius"]["gender"] = "Male"
character_info["JesanRilian"]["gender"] = "Male"
character_info["SchlerusSestius"]["gender"] = "Female"
character_info["CamillaLollia"]["gender"] = "Female"
character_info["ErissareArenim"]["gender"] = "Female"
character_info["SEStela"]["gender"] = "Female"
character_info["AdosiSerethi"]["gender"] = "Female"
character_info["AmbroiseCanne"]["gender"] = "Male"
character_info["LazareMilvan"]["gender"] = "Male"
character_info["MirabelleMonet"]["gender"] = "Female"
character_info["CandiceCorgine"]["gender"] = "Female"
character_info["MarietteRielle"]["gender"] = "Female"
character_info["Ernest"]["gender"] = "Male"
character_info["HumilisNonius"]["gender"] = "Male"
character_info["MalintusAncrus"]["gender"] = "Male"
character_info["MQ15Orthe"]["gender"] = "Male"
character_info["MivrynaArano"]["gender"] = "Female"
character_info["AntoineBranck"]["gender"] = "Male"
character_info["GastonTussaud"]["gender"] = "Male"
character_info["Tenville"]["gender"] = "Female"
character_info["Demetrius"]["gender"] = "Male"
character_info["SESfara"]["gender"] = "Female"
character_info["AvieraNirol"]["gender"] = "Female"
character_info["JavoliaMaborel"]["gender"] = "Female"
character_info["BanusAlor"]["gender"] = "Male"
character_info["SEBelmyneDreleth"]["gender"] = "Male"
character_info["GranthamBlakeley"]["gender"] = "Male"
character_info["EduardRetiene"]["gender"] = "Male"
character_info["Baeralorn"]["gender"] = "Male"
character_info["HeinrichOakenHull"]["gender"] = "Male"
character_info["TadroseHelas"]["gender"] = "Female"
character_info["EstelleRenoit"]["gender"] = "Female"
character_info["TunZeeus"]["gender"] = "Male"
character_info["SEGrommokgroBarakGhosted"]["gender"] = "Male"
character_info["Neesha"]["gender"] = "Female"
character_info["UlmuggroCromgog"]["gender"] = "Male"
character_info["VelusHosidius"]["gender"] = "Male"
character_info["Cingor"]["gender"] = "Male"
character_info["Brodras"]["gender"] = "Male"
character_info["Elragail"]["gender"] = "Female"
character_info["Mandil"]["gender"] = "Female"
character_info["Rasheda"]["gender"] = "Female"
character_info["Rhano"]["gender"] = "Male"
character_info["SnakgraBura"]["gender"] = "Female"
character_info["DulfishgroOrum"]["gender"] = "Male"
character_info["LumgroBaroth"]["gender"] = "Male"
character_info["HansBlackNail"]["gender"] = "Male"
character_info["Alga"]["gender"] = "Female"
character_info["DroNahrah"]["gender"] = "Female"
character_info["SuriusAfranius"]["gender"] = "Male"
character_info["MarianaAncharia"]["gender"] = "Female"
character_info["CaulaAllectus"]["gender"] = "Female"
character_info["AmantiusAllectus"]["gender"] = "Male"
character_info["Ohtesse"]["gender"] = "Female"
character_info["DrelsTheran"]["gender"] = "Male"
character_info["UrnsiSerethi"]["gender"] = "Female"
character_info["GanLuseph"]["gender"] = "Male"
character_info["DavideSurilie"]["gender"] = "Male"
character_info["Otumeel"]["gender"] = "Male"
character_info["AhMalz"]["gender"] = "Male"
character_info["Shamar"]["gender"] = "Male"
character_info["Carsten"]["gender"] = "Male"
character_info["BelisariusArius"]["gender"] = "Male"
character_info["RoliandHanus"]["gender"] = "Male"
character_info["VontusIdolus"]["gender"] = "Male"
character_info["GregoryArne"]["gender"] = "Male"
character_info["Beewos"]["gender"] = "Female"
character_info["HomrazgraMorgrump"]["gender"] = "Female"
character_info["Nardhil"]["gender"] = "Female"
character_info["Aenvir"]["gender"] = "Male"
character_info["StorntheBurly"]["gender"] = "Male"
character_info["LordLovidicus"]["gender"] = "Male"
character_info["DranasLerano"]["gender"] = "Male"
character_info["AgnetethePickled"]["gender"] = "Female"
character_info["Skjorta"]["gender"] = "Female"
character_info["TertiaViducia"]["gender"] = "Female"
character_info["VarelMorvayn"]["gender"] = "Male"
character_info["UlrikaUlfgar"]["gender"] = "Female"
character_info["Beirir"]["gender"] = "Male"
character_info["HrolUlfgar"]["gender"] = "Male"
character_info["TG03ChapelUnderCroftGuard"]["gender"] = "Female"
character_info["Gundalas"]["gender"] = "Male"
character_info["Tavia"]["gender"] = "Female"
character_info["IsleifTheOpenHanded"]["gender"] = "Male"
character_info["Jair"]["gender"] = "Male"
character_info["Rohssan"]["gender"] = "Female"
character_info["Borissean"]["gender"] = "Male"
character_info["Wallace"]["gender"] = "Male"
character_info["Isolde"]["gender"] = "Female"
character_info["Winson"]["gender"] = "Male"
character_info["UrbulgroOrkulg"]["gender"] = "Male"
character_info["OghashgraMagul"]["gender"] = "Female"
character_info["GaturngroGonk"]["gender"] = "Male"
character_info["Regner"]["gender"] = "Male"
character_info["KeldoftheIsles"]["gender"] = "Male"
character_info["MogensWindShifter"]["gender"] = "Male"
character_info["Rizakar"]["gender"] = "Male"
character_info["Shamada"]["gender"] = "Female"
character_info["Nahsi"]["gender"] = "Female"
character_info["Hassiri"]["gender"] = "Male"
character_info["JulittaPlotius"]["gender"] = "Female"
character_info["BettoPlotius"]["gender"] = "Male"
character_info["RomanaFaleria"]["gender"] = "Female"
character_info["OtiusLoran"]["gender"] = "Male"
character_info["CastaScribonia"]["gender"] = "Female"
character_info["TyrelliusLogellusOffDuty"]["gender"] = "Male"
character_info["WormAnchorite"]["gender"] = "Male"
character_info["Ungarion"]["gender"] = "Male"
character_info["Voranil"]["gender"] = "Male"
character_info["Ohtimbar"]["gender"] = "Male"
character_info["Errandil"]["gender"] = "Male"
character_info["AvrusAdas"]["gender"] = "Male"
character_info["UlenAthram"]["gender"] = "Male"
character_info["YvaraChannitte"]["gender"] = "Female"
character_info["SalomonGeonette"]["gender"] = "Male"
character_info["HastrelOttus"]["gender"] = "Male"
character_info["ErnestManis"]["gender"] = "Male"
character_info["GastonSurilie"]["gender"] = "Male"
character_info["DidierAumilie"]["gender"] = "Male"
character_info["TimotheeLaRouche"]["gender"] = "Male"
character_info["ElisaPierrane"]["gender"] = "Female"
character_info["RodericPierrane"]["gender"] = "Male"
character_info["OnStayaSundew"]["gender"] = "Female"
character_info["Usheeja"]["gender"] = "Male"
character_info["GeemJasaiin"]["gender"] = "Male"
character_info["Wumeek"]["gender"] = "Male"
character_info["KewanSOUL"]["gender"] = "Male"
character_info["MarentheSealSOUL"]["gender"] = "Female"
character_info["Atahba"]["gender"] = "Female"
character_info["Tilmo"]["gender"] = "Male"
character_info["MirieSOUL"]["gender"] = "Female"
character_info["IlvelRomaynSOUL"]["gender"] = "Male"
character_info["ErTeeusSOUL"]["gender"] = "Male"
character_info["Ungolim"]["gender"] = "Male"
character_info["GraklakgroBuglump"]["gender"] = "Male"
character_info["Angalsama"]["gender"] = "Female"
character_info["ForlornWatchmanPre"]["gender"] = "Male"
character_info["ShadySam"]["gender"] = "Male"
character_info["Curtis"]["gender"] = "Male"
character_info["GelliusTerentius"]["gender"] = "Male"
character_info["Ranaline"]["gender"] = "Female"
character_info["Ashanta"]["gender"] = "Female"
character_info["Hlofgar"]["gender"] = "Male"
character_info["Enrion"]["gender"] = "Male"
character_info["BeatriceGene"]["gender"] = "Female"
character_info["ColinStedrine"]["gender"] = "Male"
character_info["DreetLai"]["gender"] = "Male"
character_info["Suurootan"]["gender"] = "Male"
character_info["NatchPinder"]["gender"] = "Male"
character_info["MarlenaBrussiner"]["gender"] = "Female"
character_info["NivanDalvilu"]["gender"] = "Male"
character_info["SisterAngrond"]["gender"] = "Female"
character_info["Daenlin"]["gender"] = "Male"
character_info["Nilawen"]["gender"] = "Female"
character_info["Carwen"]["gender"] = "Female"
character_info["Adanrel"]["gender"] = "Female"
character_info["Hagaer"]["gender"] = "Male"
character_info["Gelephor"]["gender"] = "Male"
character_info["Rindir"]["gender"] = "Male"
character_info["Hasathil"]["gender"] = "Female"
character_info["Thurindil"]["gender"] = "Male"
character_info["Anguilon"]["gender"] = "Male"
character_info["Huurwen"]["gender"] = "Female"
character_info["Laralthir"]["gender"] = "Female"
character_info["Caenlin"]["gender"] = "Male"
character_info["HillodTheOutlaw"]["gender"] = "Male"
character_info["Dorian"]["gender"] = "Male"
character_info["Angelie"]["gender"] = "Female"
character_info["CarmenLitte"]["gender"] = "Female"
character_info["BrokilgroShatur"]["gender"] = "Male"
character_info["UzulGroGrulam"]["gender"] = "Male"
character_info["DulgroShug"]["gender"] = "Male"
character_info["BazurgroGharz"]["gender"] = "Male"
character_info["MaknokgroCoblug"]["gender"] = "Male"
character_info["RogmeshgraCoblug"]["gender"] = "Female"
character_info["GorgogroShura"]["gender"] = "Male"
character_info["KrognakgroBrok"]["gender"] = "Male"
character_info["KurzgroBaroth"]["gender"] = "Male"
character_info["ReistrtheRotted"]["gender"] = "Male"
character_info["EdlaDarkHeart"]["gender"] = "Female"
character_info["Honmund"]["gender"] = "Male"
character_info["Fjotreid"]["gender"] = "Male"
character_info["Olfand"]["gender"] = "Male"
character_info["SnartheCook"]["gender"] = "Male"
character_info["Logvaar"]["gender"] = "Male"
character_info["AlgottheNortherner"]["gender"] = "Male"
character_info["Gunder"]["gender"] = "Male"
character_info["StentheUgly"]["gender"] = "Male"
character_info["WilhelmtheWorm"]["gender"] = "Male"
character_info["Rigmor"]["gender"] = "Female"
character_info["Shomara"]["gender"] = "Female"
character_info["Rvanni"]["gender"] = "Male"
character_info["JzinDar"]["gender"] = "Male"
character_info["RaJhan"]["gender"] = "Male"
character_info["Rajiradh"]["gender"] = "Male"
character_info["Urjabhi"]["gender"] = "Male"
character_info["KantavCheynoslin"]["gender"] = "Male"
character_info["SilanaBlandia"]["gender"] = "Female"
character_info["JanoniaAurunceia"]["gender"] = "Female"
character_info["JanuariusAurunceia"]["gender"] = "Male"
character_info["JantusBrolus"]["gender"] = "Female"
character_info["GerichSenarel"]["gender"] = "Male"
character_info["IsaRaman"]["gender"] = "Female"
character_info["BrielusGawey"]["gender"] = "Male"
character_info["RestitaStatlilia"]["gender"] = "Female"
character_info["KastavKvinchal"]["gender"] = "Male"
character_info["VlanarusKvinchal"]["gender"] = "Male"
character_info["VelanAndus"]["gender"] = "Male"
character_info["PennusMallius"]["gender"] = "Male"
character_info["PraxedesAfranius"]["gender"] = "Female"
character_info["ReneeGeonette"]["gender"] = "Female"
character_info["StantusVarrid"]["gender"] = "Male"
character_info["TrenusDuronius"]["gender"] = "Male"
character_info["IdaOttus"]["gender"] = "Female"
character_info["AlessiaOttus"]["gender"] = "Female"
character_info["AstiniaAtius"]["gender"] = "Female"
character_info["LurioMaenius"]["gender"] = "Male"
character_info["HelvoAtius"]["gender"] = "Male"
character_info["SevariusAtius"]["gender"] = "Male"
character_info["JenaSintav"]["gender"] = "Female"
character_info["JastiaSintav"]["gender"] = "Female"
character_info["VontanSintav"]["gender"] = "Male"
character_info["TertiusFavonius"]["gender"] = "Male"
character_info["MarinusCatiotus"]["gender"] = "Male"
character_info["IdaVlinorman"]["gender"] = "Female"
character_info["CarmanaSintav"]["gender"] = "Female"
character_info["CyroninSintav"]["gender"] = "Male"
character_info["InielSintav"]["gender"] = "Male"
character_info["MaroRufus"]["gender"] = "Male"
character_info["CiceroVerus"]["gender"] = "Male"
character_info["SergiusVerus"]["gender"] = "Male"
character_info["ViatorAccius"]["gender"] = "Male"
character_info["DanusArtellian"]["gender"] = "Male"
character_info["ValandrusAbor"]["gender"] = "Male"
character_info["NaspiaCosma"]["gender"] = "Female"
character_info["RimalusBruiant"]["gender"] = "Male"
character_info["RenaBruiant"]["gender"] = "Female"
character_info["JesanSextius"]["gender"] = "Male"
character_info["AstiaInventius"]["gender"] = "Female"
character_info["RufriusVinicius"]["gender"] = "Male"
character_info["Langley"]["gender"] = "Male"
character_info["DumaniaJirich"]["gender"] = "Female"
character_info["CastaFlavus"]["gender"] = "Male"
character_info["Carandial"]["gender"] = "Male"
character_info["Areldil"]["gender"] = "Male"
character_info["Calindil"]["gender"] = "Male"
character_info["Salmo"]["gender"] = "Male"
character_info["Tumindil"]["gender"] = "Male"
character_info["DovynAren"]["gender"] = "Male"
character_info["TanasaArano"]["gender"] = "Female"
character_info["TolisiGirith"]["gender"] = "Female"
character_info["GureryneSelvilo"]["gender"] = "Male"
character_info["Glistel"]["gender"] = "Female"
character_info["LlensiLlaram"]["gender"] = "Female"
character_info["BolorSavel"]["gender"] = "Male"
character_info["NoveniOthran"]["gender"] = "Female"
character_info["SisterPhebeJeanard"]["gender"] = "Female"
character_info["RoxanneBrigette"]["gender"] = "Female"
character_info["ChanaMona"]["gender"] = "Female"
character_info["DamianMagius"]["gender"] = "Male"
character_info["RochelleBantien"]["gender"] = "Female"
character_info["SamuelBantien"]["gender"] = "Male"
character_info["BeranSintav"]["gender"] = "Male"
character_info["KastusSintav"]["gender"] = "Male"
character_info["EdgarVautrine"]["gender"] = "Male"
character_info["RenaldViernis"]["gender"] = "Male"
character_info["MariePalielle"]["gender"] = "Female"
character_info["EugalBelette"]["gender"] = "Male"
character_info["BrucetusFestinius"]["gender"] = "Male"
character_info["Numeen"]["gender"] = "Female"
character_info["OleedEi"]["gender"] = "Male"
character_info["Geel"]["gender"] = "Male"
character_info["Rana"]["gender"] = "Female"
character_info["Elsynia"]["gender"] = "Female"
character_info["TG06PaleLadyVampire"]["gender"] = "Female"
character_info["RisFralmoton"]["gender"] = "Male"
character_info["Baurion"]["gender"] = "Male"
character_info["Belisarius"]["gender"] = "Male"
character_info["Arterion"]["gender"] = "Male"
character_info["MondrarHenim"]["gender"] = "Male"
character_info["Hridi"]["gender"] = "Male"
character_info["Hjar"]["gender"] = "Male"
character_info["AzaniBlackheart"]["gender"] = "Male"
character_info["Kiara"]["gender"] = "Female"
character_info["Eletta"]["gender"] = "Female"
character_info["MuggraMurgak"]["gender"] = "Male"
character_info["GhorubgroUgdub"]["gender"] = "Male"
character_info["Styrbjorn"]["gender"] = "Male"
character_info["Ayisha"]["gender"] = "Female"
character_info["JBaasha"]["gender"] = "Male"
character_info["Zahrasha"]["gender"] = "Female"
character_info["GrayFoxCorvus"]["gender"] = "Male"
character_info["ClaudiusArcadia"]["gender"] = "Male"
character_info["MensaSelas"]["gender"] = "Female"
character_info["RalsaNethan"]["gender"] = "Male"
character_info["GasparStegine"]["gender"] = "Male"
character_info["MQ05AstavWirich"]["gender"] = "Male"
character_info["Arkved"]["gender"] = "Male"
character_info["MagragroNaybek"]["gender"] = "Male"

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
            "Title": "Elder Scrolls Oblivion",
            "Year": "2006",
            "Country": "US",
            "Characters": character,
            "Gender": info["gender"],
            "Dialogues": info["dialogues"],
        }
    )
df = pd.DataFrame(dataframe)

# Create a dictionary to map aliases to real names
aliases = {
    "Generic DarkElf Male": "Generic Dark Elf Male",
    "Generic WoodElf Male": "Generic Wood Elf Male",
    "Generic DarkElf Female": "Generic Dark Elf Female",
    "Generic HighElf Male": "Generic High Elf Male",
    "Generic WoodElf Female": "Generic Wood Elf Female",
    "Generic HighElf Female": "Generic High Elf Female",
    "Martin": "Martin Septim",
    "SEHaskill": "Haskill",
    "ModrynOreyn": "Modryn Oreyn",
    "SESheogorath": "Sheogorath",
    "SERelmynaVerenim": "Relmyna Verenim",
    "SEHalion": "Halion",
    "TarMeena": "Tar-Meena",
    "RaminusPolus": "Raminus Polus",
    "SEDumagGraBonk": "Dumag gro-Bonk",
    "SEEaril": "Earil",
    "SEAmiableFanriene": "Amiable Fanriene",
    "SEKithlan": "Kithlan",
    "MazogatheOrc": "Mazoga the Orc",
    "SEBruscusDannus": "Bruscus Dannus",
    "SESontaire": "Sontaire",
    "ArmandChristophe": "Armand Christophe",
    "SEThaedil": "Thaedil",
    "HannibalTraven": "Hannibal Traven",
    "SEAhjazda": "Ahjazda",
    "SEUshnarGroShadborgob": "Ushnar gro-Shadborgob",
    "GrayFox": "Gray Fox",
    "YsabelAndronicus": "Ysabel Andronicus",
    "Skrivva": "S'Krivva",
    "LucienLachance": "Lucien Lachance",
    "NelsTheNaughty": "Nels the Naughty",
    "SEUnaArmina": "Una Armina",
    "SECindanwe": "Cindanwe",
    "VicenteValtieri": "Vicente Valtieri",
    "SEMuurine": "Muurine",
    "JanusHassildor": "Janus Hassildor",
    "TheNightMother": "The Night Mother",
    "DovesiDran": "Dovesi Dran",
    "Jskar": "J'skar",
    "MatildePetit": "Matilde Petit",
    "PrimoAntonius": "Primo Antonius",
    "SETilseAreleth": "Tilse Areleth",
    "KudEi": "Kud-Ei",
    "Srathad": "S'rathad",
    "SavlianMatius": "Savlian Matius",
    "NarinaCarvain": "Countess Narina Carvain",
    "UrielSeptim": "Emperor Uriel Septim",
    "BumphgraGash": "Bumph gra-Gash",
    "Roliand": "Roliand Hanus",
    "SEKilibanNyrandil": "Kiliban Nyrandil",
    "SEOrinthal": "Orinthal",
    "SEHerdir": "Herdir",
    "SECutter": "Cutter",
    "SEThadon": "Thadon",
    "SEDyus": "Dyus",
    "SERendilDrarara": "Rendil Drarara",
    "GogrongroBolmog": "Gogron gro-Bolmog",
    "BurzGroKhash": "Burz gro-Khash",
    "SEDervenin": "Dervenin",
    "SE11Rakheran": "Ra'kheran",
    "AlvalUvani": "Alval Uvani",
    "SEMiriliUlven": "Mirili Ulven",
    "SEArctus": "Arctus",
    "MankarCamoran": "Mankar Camoran",
    "SEJzidzoMania": "J'zidzo Mania",
    "GuilbertJemane": "Guilbert Jemane",
    "VelwynBenirus": "Velwyn Benirus",
    "AndelIndarys": "Count Andel Indarys",
    "CariusRunellius": "Carius Runellius",
    "VilenaDonton": "Vilena Donton",
    "SEAtrabhiDementia": "Atrabhi Dementia",
    "SEWideEye": "Wide-Eye",
    "SEAtrabhiMania": "Atrabhi Mania",
    "SESyl": "Syl",
    "SESicklyBernice": "Sickly Bernice",
    "RightWind": "Right-Wind",
    "SEErverDevani": "Erver Devani",
    "SEHirrusClutumnus": "Hirrus Clutumnus",
    "Sdrassa": "S'drassa",
    "SEShelden": "Shelden",
    "ArrianaValga": "Countess Arriana Valga",
    "SEBeelei": "Beelei",
    "ArenaMouth": "Arena Mouth",
    "SE08GoldenSaintAurigDesha": "Aurig Desha",
    "SE08DarkSeducerGrakendoUdico": "Grakendo Udico",
    "GarrusDarelliun": "Garrus Darelliun",
    "MQ15Eldamil": "Eldamil",
    "SEJayredIceVeins": "Jayred Ice-Veins",
    "MariusCaro": "Count Marius Caro",
    "AgronakGroMalog": "Agronak gro-Malog",
    "BeggarLeyawiinRancidRadirsha": "Rancid Ra'dirsha",
    "ErlineLirrian": "Erline Lirrian",
    "BeggarLeyawiinDeehTheScalawag": "Deeh the Scalawag",
    "Raqanar": "Ra'qanar",
    "QuillWeave": "Quill-Weave",
    "SEKaneh": "Aurmazl Kaneh",
    "LlevanaNedaren": "Llevana Nedaren",
    "ArnoraAuria": "Arnora Auria",
    "RolandJenseric": "Roland Jenseric",
    "FarwilIndarys": "Farwil Indarys",
    "SERanarrJo": "Ranarr-Jo",
    "FathisUles": "Fathis Ules",
    "Larthjar": "Larthjar the Laggard",
    "SECaldanaMonrius": "Caldana Monrius",
    "SEAnyaHerrick": "Anya Herrick",
    "SENanetteDon": "Nanette Don",
    "RosentiaGallenus": "Rosentia Gallenus",
    "RytheLythandas": "Rythe Lythandas",
    "AlvesUvenim": "Alves Uvenim",
    "ReynaldJemane": "Reynald Jemane",
    "Sshani": "S'shani",
    "AmminusGregori": "Amminus Gregori",
    "SERavenBiter": "Raven Biter",
    "SEKishashi": "Kishashi",
    "MQ15Kathutet": "Kathutet",
    "BremmanSenyan": "Bremman Senyan",
    "SEGrommokgroBarak": "Grommok gro-Barak",
    "SEPyke": "Pyke",
    "Ocato": "High Chancellor Ocato",
    "TivelaLythandas": "Tivela Lythandas",
    "SEHorkvirBearArmMania": "Horkvir Bear-Arm Mania",
    "ValenDreth": "Valen Dreth",
    "ValusOdiil": "Valus Odiil",
    "SEBrithaur": "Brithaur",
    "SEHorkvirBearArmDementia": "Horkvir Bear-Arm Dementia",
    "SEMazaddha": "Ma'zaddha",
    "SulinusVassinus": "Sulinus Vassinus",
    "SE11Ciirta": "Ciirta",
    "JulienneFanis": "Julienne Fanis",
    "ClaudeMaric": "Claude Maric",
    "SEToveTheUnrestful": "Tove the Unrestful",
    "SERunsInCircles": "Runs-in-Circles",
    "SEBigHead": "Big Head",
    "HalLiurz": "Hal-Liurz",
    "SEMirel": "Mirel",
    "JeanneFrasoric": "Jeanne Frasoric",
    "HerminiaCinna": "Herminia Cinna",
    "SEDylora": "Dylora",
    "SEUlfri": "Grakedrig Ulfri",
    "GramangroMarad": "Graman gro-Marad",
    "AdrienneBerene": "Adrienne Berene",
    "SEStaada": "Staada",
    "LucienLachanceHunted": "Lucien Lachance",
    "AntoinettaMarie": "Antoinetta Marie",
    "DarJee": "Dar Jee",
    "VantusPrelius": "Vantus Prelius",
    "AelwinMerowald": "Aelwin Merowald",
    "SEDredhwen": "Dredhwen",
    "SEZoeMalene": "Zoe Malene",
    "BrotherPiner": "Brother Piner",
    "MercatorHosidus": "Mercator Hosidus",
    "RallusOdiil": "Rallus Odiil",
    "FaustinaCartia": "Faustina Cartia",
    "SEFelasSarandas": "Felas Sarandas",
    "SabineLaul": "Sabine Laul",
    "UrsanneLoche": "Ursanne Loche",
    "GreyThroat": "Grey-Throat",
    "SEBeggarBolwing": "Bolwing",
    "SEJastiraNanusDementia": "Jastira Nanus Dementia",
    "ArvenaThelas": "Arvena Thelas",
    "Ribassa": "Ri'Bassa",
    "HieronymusLex": "Hieronymus Lex",
    "GilenNorvalo": "Gilen Norvalo",
    "SEUrulGoAgamphMania": "Urul gro-Agamph Mania",
    "SEUrulGoAgamphDementia": "Urul gro-Agamph Dementia",
    "LucianaGalena": "Luciana Galena",
    "WeebumNa": "Weebam-Na",
    "DynariAmnis": "Dynari Amnis",
    "TrayvondtheRedguard": "Trayvond the Redguard",
    "SEJzidzoDementia": "J'zidzo Dementia",
    "PriorMaborel": "Prior Maborel",
    "SESyndeliusGatharian": "Syndelius Gatharian",
    "OngartheWorldWeary": "Ongar the World-Weary",
    "KurdangroDragol": "Kurdan gro-Dragol",
    "SEBeggarBhisha": "Bhisha",
    "AntusOdiil": "Antus Odiil",
    "BarthelGernand": "Barthel Gernand",
    "SEJastiraNanusMania": "Jastira Nanus Mania",
    "Renote": "Captain Renault",
    "SERelan": "Relan",
    "UlrichLeland": "Ulrich Leland",
    "BerichInian": "Berich Inian",
    "DubokgroShagk": "Dubok gro-Shagk",
    "OrgnolfHairyLegs": "Orgnolf Hairy-Legs",
    "LaytheWavrick": "Laythe Wavrick",
    "MillonaUmbranox": "Countess Millona Umbranox",
    "ArielleJurard": "Arielle Jurard",
    "SEGundlar": "Gundlar",
    "Ruma": "Ruma Camoran",
    "SENelrene": "Nelrene",
    "Athrelor": "Athrelor",
    "SE32CountCirion": "Count Cirion",
    "MyvrynaArano": "Myvryna Arano",
    "AncusAfranius": "Ancus Afranius",
    "DarMa": "Dar-Ma",
    "ElseGodHater": "Else God-Hater",
    "ChristopheMarane": "Christophe Marane",
    "IlendVonius": "Ilend Vonius",
    "BragGroBharg": "Brag gro-Bharg",
    "IrroketheWide": "Irroke the Wide",
    "RalsaNorvalo": "Ralsa Norvalo",
    "VaronVamori": "Varon Vamori",
    "BieneAmelion": "Biene Amelion",
    "RavenCamoran": "Raven Camoran",
    "FrancoisMotierre": "Francois Motierre",
    "BatulgraSharob": "Batul gra-Sharob",
    "GuilbertSelone": "Guilbert Selone",
    "WeedumJa": "Weedum-Ja",
    "GrayFoxStranger": "Gray Fox",
    "DiramSerethi": "Diram Serethi",
    "LuronkgroGlurzog": "Luronk gro-Glurzog",
    "ShumgroYarug": "Shum gro-Yarug",
    "Srazirr": "S'razirr",
    "LenkaValus": "Lenka Valus",
    "ArenaICBlueTeamGladiator": "Blue Team Gladiator",
    "CorrickNorthwode": "Corrick Northwode",
    "AleronLoche": "Aleron Loche",
    "HenantierDream": "Henantier",
    "AjumKajin": "Ajum-Kajin",
    "SEIssmi": "Issmi",
    "SEAdeo": "Adeo",
    "JeetumZe": "Jeetum-Ze",
    "ManheimMaulhand": "Manheim Maulhand",
    "Sjirra": "S'jirra",
    "JivHiriel": "Jiv Hiriel",
    "LordRugdumph": "Lord Rugdumph gro-Shurgak",
    "SEDulphumphGroUrgash": "Dulphumph gro-Urgash",
    "BittneldtheCurseBringer": "Bittneld the Curse-Bringer",
    "Maiqtheliar": "M'aiq the Liar",
    "MoggraMogakh": "Mog gra-Mogakh",
    "MraajDar": "M'raaj-Dar",
    "ViranusDonton": "Viranus Donton",
    "ThorleyAethelred": "Thorley Aethelred",
    "MorGraGamorn": "Mor gra-Gamorn",
    "SESheerMeedish": "Sheer Meedish",
    "RegulusTerentius": "Count Regulus Terentius",
    "MaevatheBuxom": "Maeva the Buxom",
    "SELewinTilwald": "Lewin Tilwald",
    "OgierGeorick": "Ogier Georick",
    "SeedNeeus": "Seed-Neeus",
    "SignyHomeWrecker": "Signy Home-Wrecker",
    "SE01GaiusPrentus": "Gaius Prentus",
    "SE32HlovalDreth": "Hloval Dreth",
    "AldosOthran": "Aldos Othran",
    "SorisArenim": "Soris Arenim",
    "NorbertLelles": "Norbert Lelles",
    "BrusciusLongus": "Bruscius Longus",
    "BeggarBravilWretchedAia": "Wretched Aia",
    "BeggarBravilCosmusTheCheat": "Cosmus the Cheat",
    "IrlavJarol": "Irlav Jarol",
    "ElanteofAlinor": "Elante of Alinor",
    "HlidaraMothril": "Hlidara Mothril",
    "MS93Varulae": "Varulae",
    "SETallTreesFalling": "Tall-Trees-Falling",
    "MargueriteDiel": "Marguerite Diel",
    "HjolfroditheHarrier": "Hjolfrodi the Harrier",
    "Maraska": "Ma'Raska",
    "SE32DesideratusAnnius": "Desideratus Annius",
    "LerexusCallidus": "Lerexus Callidus",
    "PinarusInventius": "Pinarus Inventius",
    "FerulRavel": "Ferul Ravel",
    "JharedStrongblade": "Jhared Strongblade",
    "SEPadEi": "Pad-Ei",
    "ViggetheCautious": "Vigge the Cautious",
    "HelviusCecia": "Helvius Cecia",
    "OlynSeran": "Olyn Seran",
    "SelenaOrania": "Selena Orania",
    "FalanuHlaalu": "Falanu Hlaalu",
    "SEBeggarUungor": "Uungor",
    "NewheimthePortly": "Newheim the Portly",
    "PerenniaDraconis": "Perennia Draconis",
    "DraranaThelis": "Drarana Thelis",
    "CalliaBincal": "Callia Bincal",
    "SEBeggarGloorolros": "Gloorolros",
    "GemellusAxius": "Gemellus Axius",
    "CaeliaDraconis": "Caelia Draconis",
    "Jbaana": "J'baana",
    "ToothintheSea": "Tooth-in-the-Sea",
    "ClaudettePerrick": "Claudette Perrick",
    "SE32Althel": "Althel",
    "AloysBincal": "Aloys Bincal",
    "VlanhonderMoslin": "Vlanhonder Moslin",
    "ValenDrethDark04": "Valen Dreth",
    "SEBeggarFimmion": "Fimmion",
    "MarentheSeal": "Maren the Seal",
    "AndreasDraconis": "Andreas Draconis",
    "LordDrad": "Lord Drad",
    "MathieuBellamont": "Mathieu Bellamont",
    "JakbenImbel": "Jakben, Earl of Imbel",
    "GinWulm": "Gin-Wulm",
    "UgakgraMogakh": "Ugak gra-Mogakh",
    "EtiraMoslin": "Etira Moslin",
    "UlfgarFogEye": "Ulfgar Fog-Eye",
    "AugustaCalidia": "Augusta Calidia",
    "ArenaICYellowTeamChampion": "Yellow Team Champion",
    "IlavDralgoner": "Ilav Dralgoner",
    "MenienGoneld": "Menien Goneld",
    "IlvelRomayn": "Ilvel Romayn",
    "ErTeeus": "Er-Teeus",
    "SE14Juggler": "Juggler",
    "AlessiaCaro": "Countess Alessia Caro",
    "OrokgroGhoth": "Orok gro-Ghoth",
    "ShobobgroRugdush": "Shobob gro-Rugdush",
    "ToutiusSextius": "Toutius Sextius",
    "ErinaJeranus": "Erina Jeranus",
    "TertullianVerus": "Tertullian Verus",
    "ItiusHayn": "Itius Hayn",
    "Mishaxhi": "Akaviri Commander Mishaxhi",
    "RusiaBradus": "Rusia Bradus",
    "IsabeauBienne": "Isabeau Bienne",
    "BeggarCheydinhalLucklessLucina": "Luckless Lucina",
    "BeggarCheydinhalBrucciusTheOrphan": "Bruccius the Orphan",
    "UmoggraMarad": "Umog gra-Marad",
    "DerveraRomalen": "Dervera Romalen",
    "CylbenDolovas": "Cylben Dolovas",
    "MelsMaryon": "Mels Maryon",
    "ScarTail": "Scar-Tail",
    "GulGroBurbog": "Gul gro-Burbog",
    "MelusPetilius": "Melus Petilius",
    "DredenaHlavel": "Dredena Hlavel",
    "LadyDrad": "Lady Drad",
    "AlbericLitte": "Alberic Litte",
    "MartinaFloria": "Martina Floria",
    "FelenRelas": "Felen Relas",
    "SEBrevi": "Brevi",
    "Sthasa": "S'thasa",
    "ViniciaMelissaeia": "Vinicia Melissaeia",
    "MQ06MythicDawnDoorkeeper": "Doorkeeper",
    "TovasSelvani": "Tovas Selvani",
    "BernadettePeneles": "Bernadette Peneles",
    "Holger": "Brother Holger",
    "HidesHisHeart": "Hides-His-Heart",
    "GoganGuard": "Gogan",
    "SE32BatGroOrkul": "Bat gro-Orkul",
    "Rijirr": "Ri'Jirr",
    "MatthiasDraconis": "Matthias Draconis",
    "BasilErnarde": "Basil Ernarde",
    "AudensAvidius": "Audens Avidius",
    "RonaHassildor": "Rona Hassildor",
    "MaranaRian": "Marana Rian",
    "BralsaAndaren": "Bralsa Andaren",
    "IreneMetrick": "Irene Metrick",
    "AlixLencolia": "Alix Lencolia",
    "BugakgroBol": "Bugak gro-Bol",
    "DelosFandas": "Delos Fandas",
    "CatFace": "Cat-Face",
    "MachNa": "Mach-Na",
    "LorgrenBenirusNPC": "Lorgren Benirus",
    "DecentiusOpsius": "Decentius Opsius",
    "VieraLerus": "Viera Lerus",
    "RaynilDralas": "Raynil Dralas",
    "DelphineJend": "Delphine Jend",
    "MarcGulitte": "Marc Gulitte",
    "LadyRogbut": "Lady Rogbut gra-Shurgak",
    "Ksharr": "K'Sharr",
    "Smirra": "S'mirra",
    "AymarDouar": "Aymar Douar",
    "NorasaAdus": "Norasa Adus",
    "DeetumJa": "Deetum-Ja",
    "OraggraBargol": "Orag gra-Bargol",
    "TorbaltheSufficient": "Torbal the Sufficient",
    "ItaRienus": "Ita Rienus",
    "LutherBroad": "Luther Broad",
    "CitySwimmer": "City-Swimmer",
    "Steffan": "Captain Steffan",
    "SE32Anglor": "Anglor",
    "SEYngvar": "Yngvar Doom-Sayer",
    "JGhasta": "J'Ghasta",
    "TolvasaSendas": "Tolvasa Sendas",
    "BlancheMastien": "Blanche Mastien",
    "BronsilaKvinchal": "Bronsila Kvinchal",
    "UravasaOthrelas": "Uravasa Othrelas",
    "BorbagraUzgash": "Borba gra-Uzgash",
    "FathisAren": "Fathis Aren",
    "DavelaHlaren": "Davela Hlaren",
    "BogrumGroGalash": "Bogrum gro-Galash",
    "MagubgraOrum": "Magub gra-Orum",
    "HafidHollowleg": "Hafid Hollowleg",
    "Droshanji": "Dro'shanji",
    "ArentusFalvius": "Arentus Falvius",
    "LeyMarillin": "Ley Marillin",
    "RemanBroder": "Reman Broder",
    "FadusCalidius": "Fadus Calidius",
    "GruiandGarrana": "Gruiand Garrana",
    "AdamusPhillida": "Adamus Phillida",
    "PistaMarillin": "Pista Marillin",
    "UleneHlervu": "Ulene Hlervu",
    "HaulsRopesFaster": "Hauls-Ropes-Faster",
    "MarcelAmelion": "Marcel Amelion",
    "TyrelliusLogellus": "Tyrellius Logellus",
    "DranasLlethro": "Dranas Llethro",
    "FrancineVelain": "Francine Velain",
    "HuntingTail": "Hunting Tail",
    "BurMeema": "Bur-Meema",
    "OlavatheFair": "Olava the Fair",
    "HiltheTall": "Hil the Tall",
    "ContumeliorusFlorius": "Contumeliorus Florius",
    "UndenaOrethi": "Undena Orethi",
    "DraloraAthram": "Dralora Athram",
    "BoderiFarano": "Boderi Farano",
    "Jbari": "J'bari",
    "UurastheShepherd": "Uuras the Shepherd",
    "ShagolgroBumph": "Shagol gro-Bumph",
    "JaFazir": "Ja'Fazir",
    "Jmhad": "J'mhad",
    "BrotchCalus": "Brotch Calus",
    "OntusVanin": "Ontus Vanin",
    "ServatiusQuintilius": "Servatius Quintilius",
    "JesanRilian": "Jesan Rilian",
    "SchlerusSestius": "Schlerus Sestius",
    "CamillaLollia": "Camilla Lollia",
    "ErissareArenim": "Erissare Arenim",
    "SEStela": "Stela",
    "AdosiSerethi": "Adosi Serethi",
    "AmbroiseCanne": "Ambroise Canne",
    "LazareMilvan": "Lazare Milvan",
    "MirabelleMonet": "Mirabelle Monet",
    "CandiceCorgine": "Candice Corgine",
    "MarietteRielle": "Mariette Rielle",
    "HumilisNonius": "Humilis Nonius",
    "MalintusAncrus": "Malintus Ancrus",
    "MQ15Orthe": "Orthe",
    "MivrynaArano": "Mivryna Arano",
    "AntoineBranck": "Antoine Branck",
    "GastonTussaud": "Gaston Tussaud",
    "SESfara": "S'fara",
    "AvieraNirol": "Aviera Nirol",
    "JavoliaMaborel": "Javolia Maborel",
    "BanusAlor": "Banus Alor",
    "SEBelmyneDreleth": "Belmyne Dreleth",
    "GranthamBlakeley": "Grantham Blakeley",
    "EduardRetiene": "Eduard Retiene",
    "HeinrichOakenHull": "Heinrich Oaken-Hull",
    "TadroseHelas": "Tadrose Helas",
    "EstelleRenoit": "Estelle Renoit",
    "TunZeeus": "Tun-Zeeus",
    "SEGrommokgroBarakGhosted": "Grommok gro-Barak",
    "UlmuggroCromgog": "Ulmug gro-Cromgog",
    "VelusHosidius": "Velus Hosidius",
    "SnakgraBura": "Snak gra-Bura",
    "DulfishgroOrum": "Dulfish gro-Orum",
    "LumgroBaroth": "Lum gro-Baroth",
    "HansBlackNail": "Hans Black-Nail",
    "DroNahrah": "Dro'Nahrahe",
    "SuriusAfranius": "Surius Afranius",
    "MarianaAncharia": "Mariana Ancharia",
    "CaulaAllectus": "Caula Allectus",
    "AmantiusAllectus": "Amantius Allectus",
    "DrelsTheran": "Drels Theran",
    "UrnsiSerethi": "Urnsi Serethi",
    "GanLuseph": "Gan Luseph",
    "DavideSurilie": "Davide Surilie",
    "AhMalz": "Ah-Malz",
    "BelisariusArius": "Belisarius Arius",
    "RoliandHanus": "Roliand Hanus",
    "VontusIdolus": "Vontus Idolus",
    "GregoryArne": "Gregory Arne",
    "HomrazgraMorgrump": "Homraz gra-Morgrump",
    "StorntheBurly": "Storn the Burly",
    "LordLovidicus": "Lord Lovidicus",
    "DranasLerano": "Dranas Lerano",
    "AgnetethePickled": "Agnete the Pickled",
    "TertiaViducia": "Tertia Viducia",
    "VarelMorvayn": "Varel Morvayn",
    "UlrikaUlfgar": "Ulrika Ulfgar",
    "HrolUlfgar": "Hrol Ulfgar",
    "TG03ChapelUnderCroftGuard": "Chapel Guard",
    "IsleifTheOpenHanded": "Isleif the Open Handed",
    "UrbulgroOrkulg": "Urbul gro-Orkulg",
    "OghashgraMagul": "Oghash gra-Magul",
    "GaturngroGonk": "Gaturn gro-Gonk",
    "KeldoftheIsles": "Keld of the Isles",
    "MogensWindShifter": "Mogens Wind-Shifter",
    "Rizakar": "Ri'Zakar",
    "JulittaPlotius": "Julitta Plotius",
    "BettoPlotius": "Betto Plotius",
    "RomanaFaleria": "Romana Faleria",
    "OtiusLoran": "Otius Loran",
    "CastaScribonia": "Casta Scribonia",
    "TyrelliusLogellusOffDuty": "Tyrellius Logellus",
    "WormAnchorite": "Worm Anchorite",
    "AvrusAdas": "Avrus Adas",
    "UlenAthram": "Ulen Athram",
    "YvaraChannitte": "Yvara Channitte",
    "SalomonGeonette": "Salomon Geonette",
    "HastrelOttus": "Hastrel Ottus",
    "ErnestManis": "Ernest Manis",
    "GastonSurilie": "Gaston Surilie",
    "DidierAumilie": "Didier Aumilie",
    "TimotheeLaRouche": "Timothee LaRouche",
    "ElisaPierrane": "Elisa Pierrane",
    "RodericPierrane": "Roderic Pierrane",
    "OnStayaSundew": "On-Staya Sundew",
    "GeemJasaiin": "Geem Jasaiin",
    "KewanSOUL": "Kewan",
    "MarentheSealSOUL": "Maren the Seal",
    "MirieSOUL": "Mirie",
    "IlvelRomaynSOUL": "Ilvel Romayn",
    "ErTeeusSOUL": "Er-Teeus",
    "GraklakgroBuglump": "Graklak gro-Buglump",
    "ForlornWatchmanPre": "The Forlorn Watchman",
    "ShadySam": "Shady Sam",
    "GelliusTerentius": "Gellius Terentius",
    "BeatriceGene": "Beatrice Gene",
    "ColinStedrine": "Colin Stedrine",
    "DreetLai": "Dreet-Lai",
    "NatchPinder": "Natch Pinder",
    "MarlenaBrussiner": "Marlena Brussiner",
    "NivanDalvilu": "Nivan Dalvilu",
    "SisterAngrond": "Sister Angrond",
    "HillodTheOutlaw": "Hillod the Outlaw",
    "CarmenLitte": "Carmen Litte",
    "BrokilgroShatur": "Brokil gro-Shatur",
    "UzulGroGrulam": "Uzul gro-Grulam",
    "DulgroShug": "Dul gro-Shug",
    "BazurgroGharz": "Bazur gro-Gharz",
    "MaknokgroCoblug": "Maknok gro-Coblug",
    "RogmeshgraCoblug": "Rogmesh gra-Coblug",
    "GorgogroShura": "Gorgo gro-Shura",
    "KrognakgroBrok": "Krognak gro-Brok",
    "KurzgroBaroth": "Kurz gro-Baroth",
    "ReistrtheRotted": "Reistr the Rotted",
    "EdlaDarkHeart": "Edla Dark-Heart",
    "SnartheCook": "Snar the Cook",
    "AlgottheNortherner": "Algot the Northerner",
    "StentheUgly": "Sten the Ugly",
    "WilhelmtheWorm": "Wilhelm the Worm",
    "Rvanni": "R'vanni",
    "JzinDar": "J'zin-Dar",
    "RaJhan": "Ra'Jhan",
    "Rajiradh": "Ra'jiradh",
    "KantavCheynoslin": "Kantav Cheynoslin",
    "SilanaBlandia": "Silana Blandia",
    "JanoniaAurunceia": "Janonia Aurunceia",
    "JanuariusAurunceia": "Januarius Aurunceia",
    "JantusBrolus": "Jantus Brolus",
    "GerichSenarel": "Gerich Senarel",
    "IsaRaman": "Isa Raman",
    "BrielusGawey": "Brielus Gawey",
    "RestitaStatlilia": "Restita Statlilia",
    "KastavKvinchal": "Kastav Kvinchal",
    "VlanarusKvinchal": "Vlanarus Kvinchal",
    "VelanAndus": "Velan Andus",
    "PennusMallius": "Pennus Mallius",
    "PraxedesAfranius": "Praxedes Afranius",
    "ReneeGeonette": "Renee Geonette",
    "StantusVarrid": "Stantus Varrid",
    "TrenusDuronius": "Trenus Duronius",
    "IdaOttus": "Ida Ottus",
    "AlessiaOttus": "Alessia Ottus",
    "AstiniaAtius": "Astinia Atius",
    "LurioMaenius": "Lurio Maenius",
    "HelvoAtius": "Helvo Atius",
    "SevariusAtius": "Sevarius Atius",
    "JenaSintav": "Jena Sintav",
    "JastiaSintav": "Jastia Sintav",
    "VontanSintav": "Vontan Sintav",
    "TertiusFavonius": "Tertius Favonius",
    "MarinusCatiotus": "Marinus Catiotus",
    "IdaVlinorman": "Ida Vlinorman",
    "CarmanaSintav": "Carmana Sintav",
    "CyroninSintav": "Cyronin Sintav",
    "InielSintav": "Iniel Sintav",
    "MaroRufus": "Maro Rufus",
    "CiceroVerus": "Cicero Verus",
    "SergiusVerus": "Sergius Verus",
    "ViatorAccius": "Viator Accius",
    "DanusArtellian": "Danus Artellian",
    "ValandrusAbor": "Valandrus Abor",
    "NaspiaCosma": "Naspia Cosma",
    "RimalusBruiant": "Rimalus Bruiant",
    "RenaBruiant": "Rena Bruiant",
    "JesanSextius": "Jesan Sextius",
    "AstiaInventius": "Astia Inventius",
    "RufriusVinicius": "Rufrius Vinicius",
    "DumaniaJirich": "Dumania Jirich",
    "CastaFlavus": "Casta Flavus",
    "DovynAren": "Dovyn Aren",
    "TanasaArano": "Tanasa Arano",
    "TolisiGirith": "Tolisi Girith",
    "GureryneSelvilo": "Gureryne Selvilo",
    "LlensiLlaram": "Llensi Llaram",
    "BolorSavel": "Bolor Savel",
    "NoveniOthran": "Noveni Othran",
    "SisterPhebeJeanard": "Sister Phebe Jeanard",
    "RoxanneBrigette": "Roxanne Brigette",
    "ChanaMona": "Chana Mona",
    "DamianMagius": "Damian Magius",
    "RochelleBantien": "Rochelle Bantien",
    "SamuelBantien": "Samuel Bantien",
    "BeranSintav": "Beran Sintav",
    "KastusSintav": "Kastus Sintav",
    "EdgarVautrine": "Edgar Vautrine",
    "RenaldViernis": "Renald Viernis",
    "MariePalielle": "Marie Palielle",
    "EugalBelette": "Eugal Belette",
    "BrucetusFestinius": "Brucetus Festinius",
    "OleedEi": "Oleed-Ei",
    "TG06PaleLadyVampire": "Pale Lady",
    "RisFralmoton": "Ris Fralmoton",
    "MondrarHenim": "Mondrar Henim",
    "Hridi": "Brother Hridi",
    "Hjar": "Brother Hjar",
    "AzaniBlackheart": "Azani Blackheart",
    "MuggraMurgak": "Mug gra-Murgak",
    "GhorubgroUgdub": "Ghorub gro-Ugdub",
    "JBaasha": "J'Baasha",
    "GrayFoxCorvus": "Gray Fox",
    "ClaudiusArcadia": "Claudius Arcadia",
    "MensaSelas": "Mensa Selas",
    "RalsaNethan": "Ralsa Nethan",
    "GasparStegine": "Gaspar Stegine",
    "MQ05AstavWirich": "Astav Wirich",
    "MagragroNaybek": "Magra gro-Naybek",
}

# Replace aliases with real names
df["Characters"] = df["Characters"].replace(aliases)

# Combine dialogues of same characters
df = df.groupby(["Title", "Year", "Country", "Characters", "Gender"], as_index=False).agg({"Dialogues": lambda series: sum(series, [])})

# Create a list to store playable charaters
PC = [
    "Generic Imperial Male",
    "Generic Imperial Female",
    "Generic Nord Male",
    "Generic Breton Female",
    "Generic Dark Elf Male",
    "Generic Breton Male",
    "Generic Wood Elf Male",
    "Generic Dark Elf Female",
    "Generic High Elf Male",
    "Generic Orc Male",
    "Generic Wood Elf Female",
    "Generic Redguard Male",
    "Generic Argonian Male",
    "Generic Khajiit Male",
    "Generic Argonian Female",
    "Generic High Elf Female",
    "Generic Nord Female",
    "Generic Orc Female",
    "Generic Redguard Female",
    "Generic Khajiit Female",
]

# Assign playability to each character
df['Playability'] = df['Characters'].apply(lambda x: 'PC' if x in PC else 'NPC')

# Save the dataframe
df.to_csv("data/elder_scrolls_oblivion/data.csv", index=False)
