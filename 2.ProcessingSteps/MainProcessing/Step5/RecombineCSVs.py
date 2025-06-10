import os

# Directory containing the CSV files
directory = r'C:\Users\Mariana\Documents\Python\steps\word_embedding\TODOcsvs'
# Change theese for each step
Combine_from  = "DONE_step4"
# Directory for the output file
output_directory = r"C:\Users\Mariana\Documents\Python\results"
os.makedirs(output_directory, exist_ok=True)
outputfilename = os.path.join(output_directory, "CompleteDATA_step4_recombined.csv")

import os
import pandas as pd

files = [f for f in os.listdir(directory) if Combine_from in f]
print(f"Combining {len(files)} files")
for i, file in enumerate(files[:10]):
    print(f"{i+1}: {file}")
    
df = pd.concat([pd.read_csv(os.path.join(directory, file)) for file in files])
# save the file
DONEfile_path = os.path.join(output_directory, outputfilename)
df.to_csv(DONEfile_path, index=False, mode='w')
print(f"Combined file saved to {DONEfile_path}")
