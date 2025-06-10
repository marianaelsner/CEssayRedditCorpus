import os
import pandas as pd
# Load the CSV file into a DataFrame
file_path = r'C:\Users\Mariana\Documents\Python\csv\Data_1_done.csv'
TargetTODOFolder = r"C:\Users\Mariana\Documents\Python\steps\TODOcsvs"

df = pd.read_csv(file_path)
if not os.path.exists(TargetTODOFolder):
    os.makedirs(TargetTODOFolder)
    
chunk_size = 1000
for i, chunk in enumerate(range(0, len(df), chunk_size)):
    chunk_df = df.iloc[chunk:chunk + chunk_size]
    chunk_df.to_csv(os.path.join(TargetTODOFolder, f'DONE_step0_{i + 1}.csv'), index=False)
