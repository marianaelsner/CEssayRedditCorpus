import pandas as pd
from helperfn import extract_first_numeric
from concurrent.futures import ThreadPoolExecutor


print("*" * 150)
print("Starting Step 2")

csv_file = r'C:/Users/Mariana/Documents/Python/csv/Data_0_Done.csv'

print(F"Reading CSV {csv_file}")

df = pd.read_csv(csv_file)

print(df.head())
print(df.columns)
## We do stuff here

df['wordcount'] = df['self_text'].str.split().str.len()

print("\nWord count statistics by subreddit:")
stats = df.groupby('subreddit')['wordcount'].describe()
print("\nWord count statistics by subreddit:")
print(stats)
stats.to_csv(r'steps\Step2WordCount.csv')

## We save the stuff here
df_output_file = r'C:/Users/Mariana/Documents/Python/csv/Data_0_Done.csv'

df.to_csv(df_output_file, encoding='utf-8', index=False)
print(f"Combined DataFrame saved to {df_output_file}")
