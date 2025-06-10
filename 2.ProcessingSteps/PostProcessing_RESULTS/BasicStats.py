import pandas as pd
import ast
import string
from tqdm import tqdm

tqdm.pandas()

# File paths
input_path = r"C:\Users\Mariana\Documents\Python\results\CompleteDATA_recombined.csv"
combined_output_path = r"C:\Users\Mariana\Documents\Python\results\subreddit_token_counts_combined.csv"

# Read necessary columns
df = pd.read_csv(input_path, usecols=["subreddit", "self_text_pos"], low_memory=False).dropna(subset=["self_text_pos"])

# Convert string of tuples to list of tuples
df['self_text_pos'] = df['self_text_pos'].progress_apply(ast.literal_eval)

# Count non-punctuation tokens in each row
df['token_count'] = df['self_text_pos'].progress_apply(
    lambda tokens: sum(1 for token in tokens if token[0] not in string.punctuation)
)

# Total token count per subreddit
total_counts = df.groupby('subreddit')['token_count'].sum().reset_index()
total_counts.rename(columns={'token_count': 'total_token_count'}, inplace=True)

# Average token count per row per subreddit
average_counts = df.groupby('subreddit')['token_count'].mean().reset_index()
average_counts.rename(columns={'token_count': 'average_token_count'}, inplace=True)

# Merge total and average counts
combined_counts = pd.merge(total_counts, average_counts, on='subreddit')

# Save to single file
combined_counts.to_csv(combined_output_path, index=False)

print("✅ Combined token counts saved to:", combined_output_path)
