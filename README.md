# MACCS Thesis: Gender Differences in Psychological States in Role-Playing Video Game Dialogue

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
│   │   ├── dialogue_data.csv                   # dialogue data from all games
│   │   ├── emotion_data.csv                    # data from emotion classifcaiton on dialogue data
│   │   └── liwc_data.csv                       # data from liwc analysis on dialogue data
│   ├── death_stranding
│   │   ├── data.csv                            # cleaned dialogue data from Death Stranding
│   │   └── data.json                           # raw dialogue data from Death Stranding
│   ├── disco_elysium
│   │   ├── data.csv                            # cleaned dialogue data from Disco Elysium
│   │   └── data.json                           # raw dialogue data from Disco Elysium
│   ├── elder_scrolls_morrowind
│   │   ├── data.csv                            # cleaned dialogue data from Elder Scrolls Morrowind
│   │   └── data.json                           # raw dialogue data from Elder Scrolls Morrowind
│   ├── elder_scrolls_oblivion
│   │   ├── data.csv                            # cleaned dialogue data from Elder Scrolls Oblivion
│   │   └── data.json
│   ├── elder_scrolls_skyrim
│   │   ├── data.csv                            # cleaned dialogue data from Elder Scrolls Skyrim
│   │   └── data.json
│   ├── final_fantasy_vii_remake
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy VII Remake
│   │   └── data.json
│   ├── final_fantasy_x
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy X
│   │   └── data.json
│   ├── final_fantasy_xii
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy XII
│   │   └── data.json
│   ├── final_fantasy_xiii
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy XIII
│   │   └── data.json
│   ├── final_fantasy_xiii_2
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy XIII-2
│   │   └── data.json
│   ├── final_fantasy_xiv
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy XIV
│   │   └── data.json
│   ├── final_fantasy_xv
│   │   ├── data.csv                            # cleaned dialogue data from Final Fantasy XV
│   │   └── data.json
│   ├── hades
│   │   ├── data.csv                            # cleaned dialogue data from Hades
│   │   └── data.json
│   ├── horizon_forbidden_west
│   │   ├── data.csv                            # cleaned dialogue data from Horizon Forbidden West
│   │   └── data.json
│   ├── horizon_zero_dawn
│   │   ├── data.csv                            # cleaned dialogue data from Horizon Zero Dawn
│   │   └── data.json
│   ├── persona_3
│   │   ├── data.csv                            # cleaned dialogue data from Persona 3
│   │   └── data.json
│   ├── persona_4
│   │   ├── data.csv                            # cleaned dialogue data from Persona 4
│   │   └── data.json
│   └── persona_5
│       ├── data.csv                            # cleaned dialogue data from Persona 5
│       └── data.json
├── figures
│   ├── emotion_distribution.pdf                # figure on the distribution of emotions
│   ├── emotion_frequency.pdf                   # figure on the frequency of emotions
│   ├── female_percentage.pdf                   # figure on the percetage of female words
│   └── pca.pdf                                 # figure on the principal component analysis
└── scripts
    ├── data_analysis
    │   ├── emotion_analysis.R                  # script for analyzing emotion variables
    │   ├── exploratory_data_analysis.R         # script for exploratory data analysis
    │   ├── liwc_analysis.R                     # script for analyzing liwc variables
    │   └── pca_analysis.R                      # script for principal component analysis
    └── data_cleaning
        ├── death_stranding.py                  # script for cleaning dialogue data of Death Stranding
        ├── disco_elysium.py                    # script for cleaning dialogue data of Disco Elysium  
        ├── elder_scrolls_morrowind.py
        ├── elder_scrolls_oblivion.py
        ├── elder_scrolls_skyrim.py
        ├── emotion_classification.py
        ├── final_fantasy_vii_remake.py
        ├── final_fantasy_x.py
        ├── final_fantasy_xii.py
        ├── final_fantasy_xiii_2.py
        ├── final_fantasy_xiii.py
        ├── final_fantasy_xiv.py
        ├── final_fantasy_xv.py
        ├── hades.py
        ├── horizon_forbidden_west.py
        ├── horizon_zero_dawn.py
        ├── merge.py
        ├── persona_3.py
        ├── persona_4.py
        └── persona_5.py
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