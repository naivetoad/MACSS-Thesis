# Load required libraries
import ast
import json
import pandas as pd
from tqdm import tqdm
from transformers import pipeline
from transformers import set_seed
from transformers import utils

# Load the dataset
df = pd.read_csv("data/dialogue_data.csv",converters={"Dialogues": ast.literal_eval})

# Set the seed for reproducibility
set_seed(42)

# Load the classifier
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None, truncation=True)

# Disable warnings
utils.logging.set_verbosity_error()

# Classify emotions
for index, row in tqdm(df.iterrows(), total=len(df)):
    dialogues = row["Dialogues"]
    emotion_scores = []
    for line in dialogues:
        predictions = classifier(line)
        scores = {emotion["label"]: emotion["score"] for emotion in predictions[0]} # Extract emotion labels and confidence scores
        emotion_scores.append(scores)
    df.at[index, "Emotions"] = json.dumps(emotion_scores)

# Save the dataframe
df.to_csv('data/emotion_data.csv', index=False)
