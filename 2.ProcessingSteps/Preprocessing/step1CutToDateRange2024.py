import pandas as pd
import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Define file paths
file1 = r'C:\Users\Mariana\Documents\Python\csv\reddit_opinion_democrats.csv'
file2 = r'C:\Users\Mariana\Documents\Python\csv\reddit_opinion_republican.csv'

Dev = True  # Set to False when ready to run on the full dataset

# Read the CSV files into DataFrames
print("Reading CSV files...")
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine the DataFrames
df = pd.concat([df1, df2])

# Display the combined DataFrame
print(df.head())
print(df.columns)

# Remove duplicate column names in the list
columns_to_keep = ['comment_id', 'self_text', 'subreddit', 'created_time', 'post_id', 'author_name', 'post_self_text', 'post_title']
df = df[columns_to_keep]

print(df.head())
print(df.columns)

# Convert the 'created_time' column to datetime format
df['created_time'] = pd.to_datetime(df['created_time'])

# Format the 'created_time' column to 'yyyy-mm-dd'
df['created_day'] = df['created_time'].dt.strftime('%Y-%m-%d')

# Create a column with the year of 'created_time'
df['year'] = pd.to_datetime(df['created_time']).dt.year

# Drop the 'created_time' column
df = df.drop(columns=['created_time'])

# Filter the DataFrame to include only rows where the year is 2024
df = df[df['year'] == 2024]

print(df.head())
print(df.columns)

# Save the filtered DataFrame to a CSV file
df.to_csv(f'C:/Users/Mariana/Documents/Python/csv/Data_0_done.csv', index=False)
