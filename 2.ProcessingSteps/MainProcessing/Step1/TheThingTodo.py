import re
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

# Download necessary resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize spell checker and lemmatizer
spell = SpellChecker()
lemmatizer = WordNetLemmatizer()

exception_words = {"woke", "pelosi", "Reddit", "covid", "AI", "Python", "cliche", "elon", "maga", "mag", "harvy", "bs", "conover", "tldr", "tbh",
                   "lmao", "lol","wokeness", "wokeism", "wokism"}

def get_wordnet_pos(nltk_tag):
    """Convert NLTK POS tags to WordNet POS tags."""
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):  # Verbs
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Function to correct spelling and lemmatize
def correct_spelling(text):
    if pd.isna(text) or not isinstance(text, str):
        return ""  # Handle missing or non-string values safely

    # Tokenize words while keeping punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    pos_tags = nltk.pos_tag(tokens)  # Get POS tags
    corrected_tokens = []

    for token, pos in pos_tags:
        if (
            token.lower() in exception_words  # Skip exception words
            or not token.isalpha()  # Keep punctuation/numbers unchanged
            or pos in {"NNP", "NNPS"}  # Leave proper nouns unchanged
        ):
            corrected_tokens.append(token)
            continue

        corrected_token = spell.correction(token)  # Spell correction
        if corrected_token is None:  # If spellchecker returns None, keep original token
            corrected_token = token

        wordnet_pos = get_wordnet_pos(pos)  # Get correct POS for lemmatization
        lemma = lemmatizer.lemmatize(corrected_token, pos=wordnet_pos)  # Lemmatize properly

        if wordnet.synsets(lemma):  # Keep lemmatized form if it exists in WordNet
            corrected_tokens.append(lemma)
        else:
            corrected_tokens.append(corrected_token)  # Otherwise, keep corrected word

    # Join words and punctuation correctly (no spaces before punctuation)
    return ''.join(
        [corrected_tokens[i] if corrected_tokens[i] in ",.!?;:" 
         else (' ' + corrected_tokens[i]) for i in range(len(corrected_tokens))]
    ).strip()

def DOThis(df)->pd.DataFrame:
    df["self_text_corrected"] = df["self_text"].apply(correct_spelling)
    return df
