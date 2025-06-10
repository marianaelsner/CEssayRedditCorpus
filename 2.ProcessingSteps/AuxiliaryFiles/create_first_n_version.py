import pandas as pd

n= 10000
# Load the first 1000 rows of each CSV file
df = pd.read_csv(r'C:\Users\Mariana\Documents\Python\csv\Data_in.csv', nrows=n)
columns_to_keep = ['comment_id', 'self_text', 'subreddit', 'created_time', 'post_id', 'author_name', 'source']
df = df[columns_to_keep]
df.to_csv(f'C:/Users/Mariana/Documents/Python/csv/Data_in_first1000.csv', index=False)
