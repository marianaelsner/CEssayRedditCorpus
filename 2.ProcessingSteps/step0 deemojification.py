import pandas as pd
import emoji

#df1 = pd.read_csv('C:/Users/Mariana/Documents/Python/csv/Data_0_done_first1000.csv')
df2 = pd.read_csv('C:/Users/Mariana/Documents/Python/csv/Data_0_done.csv')


#df1['self_text'] = df1['self_text'].apply(lambda x: emoji.demojize(x) if isinstance(x, str) else x) # remove emojis
df2['self_text'] = df2['self_text'].apply(lambda x: emoji.demojize(x) if isinstance(x, str) else x) # remove emojis

#df1.to_csv('C:/Users/Mariana/Documents/Python/csv/Data_0_done_first1000.csv', index=False)
df2.to_csv('C:/Users/Mariana/Documents/Python/csv/Data_0_done.csv', index=False)
