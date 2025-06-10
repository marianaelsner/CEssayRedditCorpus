# preprocess_data.py
import pandas as pd
import ast
import re
import string
import pickle
from collections import Counter
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords

# Download stopwords if needed
nltk.download("stopwords")

# Initialize
stopword_set = set(stopwords.words("english"))
punctuation_set = set(string.punctuation)
tqdm.pandas()

# File paths
input_path = r"C:\Users\Mariana\Documents\Python\results\CompleteDATA_recombined.csv"
preprocessed_output_path = "preprocessed_data_noun.pkl"

# Function to safely parse pos_word_tuples
def safe_literal_eval(value):
    try:
        return ast.literal_eval(value) if isinstance(value, str) else value
    except (ValueError, SyntaxError):
        return []

# Function to filter tokens
def filter_tokens(pos_list):
    filtered_tokens = []
    for word, tag in pos_list:
        if word not in punctuation_set and word.lower() not in stopword_set and not word.isdigit():
            if not re.search(r'\w*\d\w*', word):
                filtered_tokens.append((word.lower(), tag))
    return filtered_tokens

# Load and process data
print("📥 Loading dataset...")
df = pd.read_csv(input_path, usecols=["pos_word_tuples"], low_memory=False).dropna(subset=["pos_word_tuples"])
df["pos_word_tuples"] = df["pos_word_tuples"].apply(safe_literal_eval)
df["filtered_pos_word_tuples"] = df["pos_word_tuples"].progress_apply(filter_tokens)

# Extract woke-containing sentences (CORRECTED check for 'woke' as NOUN)
woke_sentences = [
    pos_list for pos_list in df["filtered_pos_word_tuples"]
    if ("woke", "NOUN") in pos_list or ("wokes", "NOUN") in pos_list
]

# Flatten into words and pos_tuples
woke_words = [word for sentence in woke_sentences for word, _ in sentence]
woke_pos_tuples = [token for sentence in woke_sentences for token in sentence]

# Save preprocessed data
with open(preprocessed_output_path, "wb") as f:
    pickle.dump({
        "woke_sentences": woke_sentences,
        "woke_words": woke_words,
        "woke_pos_tuples": woke_pos_tuples
    }, f)

print("✅ Preprocessing complete. Saved to:", preprocessed_output_path)
print(f"📊 Sentences containing 'woke' as NOUN: {len(woke_sentences)}")
