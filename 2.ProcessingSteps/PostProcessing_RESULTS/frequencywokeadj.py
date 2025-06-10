import pandas as pd
import ast  # To safely convert string representation of tuples back to lists
import string  # For punctuation filtering
from tqdm import tqdm  # For progress bar

# Enable tqdm for pandas
tqdm.pandas()

# File paths
input_path = r"C:\Users\Mariana\Documents\Python\csv\CompleteDATA_recombined.csv"
output_path = r"C:\\Users\\Mariana\\Documents\\Python\\results\\Woke_ADJ_Frequency_2.csv"

# Read only necessary columns
df = pd.read_csv(input_path, usecols=["pos_word_tuples"], low_memory=False).dropna(subset=["pos_word_tuples"])

# Convert "self_text_pos" from string representation to a list of tuples
df["pos_word_tuples"] = df["pos_word_tuples"].apply(ast.literal_eval)

# Define a set of punctuation characters to exclude
punctuation_set = set(string.punctuation)

# Function to filter out punctuation tokens while retaining their POS tags
def filter_non_punct_tokens(pos_list):
    return [(word, tag) for word, tag in pos_list if word not in punctuation_set]

# Apply function to remove punctuation tokens and retain POS tags, with a progress bar
df["filtered_pos_word_tuples"] = df["pos_word_tuples"].progress_apply(filter_non_punct_tokens)

# Count occurrences of ('woke', 'ADJ') with progress bar (using generator expression for efficiency)
woke_adj_count = df["filtered_pos_word_tuples"].progress_apply(lambda pos_list: sum(1 for word, tag in pos_list if word == 'woke' and tag == 'ADJ')).sum()

# Hardcoded total token count (for scaling purposes)
total_token_count = df["filtered_pos_word_tuples"].progress_apply(len).sum()

# Calculate relative frequency
relative_frequency = woke_adj_count / total_token_count if total_token_count > 0 else 0

# Scale the relative frequency to occurrences per 1,000,000 words
relative_frequency_scaled = (woke_adj_count / total_token_count) * 1_000_000 if total_token_count > 0 else 0

# Save results to CSV
output_df = pd.DataFrame({
    "Metric": ["Woke as ADJ Count", "Total Token Count (Excl. Punctuation)", "Relative Frequency", "Relative Frequency Scaled (per 1M words)"],
    "Value": [woke_adj_count, total_token_count, relative_frequency, relative_frequency_scaled]
})
output_df.to_csv(output_path, index=False)

# Print confirmation
print("✅ Results saved to", output_path)
print(f"📊 'woke' as ADJ Count: {woke_adj_count}")
print(f"🔢 Total Token Count (Excl. Punctuation): {total_token_count}")
print(f"📈 Relative Frequency of 'woke' as ADJ: {relative_frequency:.6f}")
print(f"📈 Relative Frequency of 'woke' as ADJ per 1,000,000 words: {relative_frequency_scaled:.4f}")
