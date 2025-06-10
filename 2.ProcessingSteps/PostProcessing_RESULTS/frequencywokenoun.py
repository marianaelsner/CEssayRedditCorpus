import pandas as pd
import ast  # To safely convert string representation of tuples back to lists
import string  # For punctuation filtering

# File paths
input_path = r"C:\Users\Mariana\Documents\Python\csv\CompleteDATA_recombined.csv"
output_path = r"C:\\Users\\Mariana\\Documents\\Python\\results\\Woke_NOUN_Frequency_2.csv"

# Read only necessary columns
df = pd.read_csv(input_path, usecols=["pos_word_tuples"], low_memory=False).dropna(subset=["pos_word_tuples"])

# Convert "pos_word_tuples" from string representation to a list of tuples
df["pos_word_tuples"] = df["pos_word_tuples"].apply(ast.literal_eval)

# Define a set of punctuation characters to exclude
punctuation_set = set(string.punctuation)

# Function to filter out punctuation tokens while retaining their POS tags
def filter_non_punct_tokens(pos_list):
    return [(word, tag) for word, tag in pos_list if word not in punctuation_set]

# Apply function to remove punctuation tokens and retain POS tags
df["filtered_pos_word_tuples"] = df["pos_word_tuples"].apply(filter_non_punct_tokens)

# Count occurrences of ('woke', 'NOUN') and ('wokes', 'NOUN') in each filtered pos_word_tuples list
woke_noun_count = df["filtered_pos_word_tuples"].apply(
    lambda pos_list: sum(1 for word, tag in pos_list if (word == 'woke' and tag == 'NOUN') or (word == 'wokes' and tag == 'NOUN'))
).sum()

# Hardcoded total token count
total_token_count = 191402374

# Calculate relative frequency
relative_frequency = woke_noun_count / total_token_count if total_token_count > 0 else 0

# Scale the relative frequency to occurrences per 1,000,000 words
relative_frequency_scaled = (woke_noun_count / total_token_count) * 1_000_000 if total_token_count > 0 else 0

# Save results to CSV
output_df = pd.DataFrame({
    "Metric": ["Woke as NOUN Count", "Total Token Count (Excl. Punctuation)", "Relative Frequency", "Relative Frequency Scaled (per 1M words)"],
    "Value": [woke_noun_count, total_token_count, relative_frequency, relative_frequency_scaled]
})
output_df.to_csv(output_path, index=False)

# Print confirmation
print("✅ Results saved to", output_path)
print(f"📊 'woke' as NOUN Count: {woke_noun_count}")
print(f"🔢 Total Token Count (Excl. Punctuation): {total_token_count}")
print(f"📈 Relative Frequency of 'woke' as NOUN: {relative_frequency:.6f}")
print(f"📈 Relative Frequency of 'woke' as NOUN per 1,000,000 words: {relative_frequency_scaled:.4f}")
