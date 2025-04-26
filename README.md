# Gender Differences in Psychological States in Role-Playing Video Game Dialogue

## Project Overview

This repository contains the full project for my MA thesis at the University of 
Chicago's Computational Social Science program. The thesis examines how gender 
differences are psychologically constructed in character dialogue from 
role-playing video games, using computational methods such as psycholinguistic 
analysis, transformer-based emotion classification, and dimensionality reduction.

## Repository Structure

```
├── data
│   ├── all
│   │   ├── dialogue_data.csv               # merged dialogue data
│   │   ├── emotion_data.csv                # data from emotion classifcaiton
│   │   └── liwc_data.csv                   # data from liwc analysis
│   ├── death_stranding
│   │   ├── data.csv                        # cleaned dialogue data from Death Stranding
│   │   └── data.json                       # raw dialogue data from Death Stranding
│   ├── disco_elysium
│   │   ├── data.csv                        # cleaned dialogue data from Disco Elysium
│   │   └── data.json                       # raw dialogue data from Disco Elysium
│   ├── elder_scrolls_morrowind
│   │   ├── data.csv                        # cleaned dialogue data from Elder Scrolls Morrowind
│   │   └── data.json                       # raw dialogue data from Elder Scrolls Morrowind
│   ├── elder_scrolls_oblivion
│   │   ├── data.csv                        # cleaned dialogue data from Elder Scrolls Oblivion
│   │   └── data.json                       # raw dialogue data from Elder Scrolls Oblivion
│   ├── elder_scrolls_skyrim
│   │   ├── data.csv                        # cleaned dialogue data from Elder Scrolls Skyrim
│   │   └── data.json                       # raw dialogue data from Elder Scrolls SKyrim
│   ├── final_fantasy_vii_remake
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy VII Remake
│   │   └── data.json                       # raw dialogue data from Final Fantasy VII Remake
│   ├── final_fantasy_x
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy X
│   │   └── data.json                       # raw dialogue data from Final Fantasy X
│   ├── final_fantasy_xii
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy XII
│   │   └── data.json                       # raw dialogue data from Final Fantasy XII
│   ├── final_fantasy_xiii
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy XIII
│   │   └── data.json                       # raw dialogue data from Final Fantasy XIII
│   ├── final_fantasy_xiii_2
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy XIII-2
│   │   └── data.json                       # raw dialogue data from Final Fantasy XIII-2
│   ├── final_fantasy_xiv
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy XIV
│   │   └── data.json                       # raw dialogue data from
│   ├── final_fantasy_xv
│   │   ├── data.csv                        # cleaned dialogue data from Final Fantasy XV
│   │   └── data.json                       # raw dialogue data from Final Fantasy XV
│   ├── hades
│   │   ├── data.csv                        # cleaned dialogue data from Hades
│   │   └── data.json                       # raw dialogue data from Hades
│   ├── horizon_forbidden_west
│   │   ├── data.csv                        # cleaned dialogue data from Horizon Forbidden West
│   │   └── data.json                       # raw dialogue data from Horizon Forbidden West
│   ├── horizon_zero_dawn
│   │   ├── data.csv                        # cleaned dialogue data from Horizon Zero Dawn
│   │   └── data.json                       # raw dialogue data from Horizon Zero Dawn
│   ├── persona_3
│   │   ├── data.csv                        # cleaned dialogue data from Persona 3
│   │   └── data.json                       # raw dialogue data from Persona 3
│   ├── persona_4
│   │   ├── data.csv                        # cleaned dialogue data from Persona 4
│   │   └── data.json                       # raw dialogue data from Persona 4
│   └── persona_5
│       ├── data.csv                        # cleaned dialogue data from Persona 5
│       └── data.json                       # raw dialogue data from Persona 5
├── figures 
│   ├── emotion_distribution.pdf            # figure on the distribution of emotions
│   ├── emotion_frequency.pdf               # figure on the frequency of emotions
│   ├── female_percentage.pdf               # figure on the percetage of female words
│   └── pca.pdf                             # figure on the principal component analysis
└── scripts
    ├── data_analysis
    │   ├── emotion_analysis.R              # script for analyzing emotion variables
    │   ├── exploratory_data_analysis.R     # script for exploratory data analysis
    │   ├── liwc_analysis.R                 # script for analyzing liwc variables
    │   └── pca_analysis.R                  # script for principal component analysis
    └── data_cleaning
        ├── death_stranding.py              # script for cleaning dialogue data from Death Stranding
        ├── disco_elysium.py                # script for cleaning dialogue data from Disco Elysium  
        ├── elder_scrolls_morrowind.py      # script for cleaning dialogue data from Elder Scrolls Morrowind
        ├── elder_scrolls_oblivion.py       # script for cleaning dialogue data from Elder Scrolls Oblivion
        ├── elder_scrolls_skyrim.py         # script for cleaning dialogue data from Elder Scrolls Skyrim
        ├── emotion_classification.py       # script for classifying emotions
        ├── final_fantasy_vii_remake.py     # script for cleaning dialogue data from Final Fantasy VII Remake
        ├── final_fantasy_x.py              # script for cleaning dialogue data from Final Fantasy X
        ├── final_fantasy_xii.py            # script for cleaning dialogue data from Final Fantasy XII
        ├── final_fantasy_xiii_2.py         # script for cleaning dialogue data from Final Fantasy XIII-2
        ├── final_fantasy_xiii.py           # script for cleaning dialogue data from Final Fantasy XIII
        ├── final_fantasy_xiv.py            # script for cleaning dialogue data from Final Fantasy XIV
        ├── final_fantasy_xv.py             # script for cleaning dialogue data from Final Fantasy XV
        ├── hades.py                        # script for cleaning dialogue data from Hades
        ├── horizon_forbidden_west.py       # script for cleaning dialogue data from Horizon Forbidden West
        ├── horizon_zero_dawn.py            # script for cleaning dialogue data from Horizon Zero Dawn
        ├── merge.py                        # script for mergeing cleaned data
        ├── persona_3.py                    # script for cleaning dialogue data from Persona 3
        ├── persona_4.py                    # script for cleaning dialogue data from Persona 4
        └── persona_5.py                    # script for cleaning dialogue data from Persona 5
 ```
 
## How to Run

1. Clone the repository.
```bash
git clone https://github.com/naivetoad/MACSS-Thesis.git
```
2. Change the working directory.
```bash
cd MACSS-Thesis
```
3. Download and install the latest release of Python 3.10 from the official [website](https://www.python.org/downloads/).
4. Install Python libraries
```bash
pip install pandas tqdm transformers
```
5. Clean data for each game (replace {game_title} with a specific game's folder name).
```bash
python3 scripts/data_cleaning/{game_title}.py
```
6. Merge cleaned data from all games.
```bash
python3 scripts/data_cleaning/merge.py
```
7. Perform emotion classification on merged data.
```bash
python3 scripts/data_cleaning/emotion_classification.py
```
8. Download and install the latest releases of R and RStudio from the official [website](https://posit.co/download/rstudio-desktop/).
9. Install R libraries.
```r
install.packages(c(
  "broom",
  "fmsb",
  "jsonlite",
  "MASS",
  "proxy",
  "reshape2",
  "tidyverse"
))
```
9. Change the working directory (replace {file_path} with the path to the folder where you cloned the repository).
```r
setwd("{file_path}/MACSS-Thesis")
```
10. Perform exploratory data analysis by running ```exploratory_data_analysis.R```.
11. Perform analysis on emotion variables by running ```emotion_analysis.R```.
12. Perform analysis on LIWC variables by running ```liwc_analysis.R```.
13. Perform PCA on emotion and LIWC variables by running ```pca_analysis.R```.