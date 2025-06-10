import pandas as pd
import os

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

df2 = pd.read_csv(r'C:/Users/Mariana/Documents/Python/csv/Data_0_done.csv')

df2 = df2.drop_duplicates(subset=['comment_id'], keep=False) #I'm trying to delete repeted comments from the get go

df2 = df2.drop_duplicates(subset=['self_text'], keep=False)

df2.to_csv(r'C:/Users/Mariana/Documents/Python/csv/Data_0_done.csv', index=False)

print('done')
