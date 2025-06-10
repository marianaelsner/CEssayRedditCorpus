folder = r'C:\Users\Mariana\Documents\Python\steps\TODOcsvs'

import os
import numpy as np
import json
import pickle

StepFileout = "step1".lower() # What is the name of the step when it is "Done" that we want to eliminate from run
ThreadCount = 30
WeAreInFolder = r"C:\Users\Mariana\Documents\Python\steps\step1"

#################### CHANGE ABOVE ########################### 
files = [f for f in os.listdir(folder) if StepFileout in f]

DoneSet = set()
AllChunksSet = set(range(1, 5482))

for file in files:
    if file.endswith('.csv'):
        chunk = file.split('_')[-1].split('.')[0]
        DoneSet.add(int(chunk))

remaining_chunks = AllChunksSet - DoneSet
remaining_chunks = sorted(remaining_chunks)
print(F"""{len(remaining_chunks)} chunks remaining""")
remaining_chunks = sorted(remaining_chunks)
remaining_chunks_split = np.array_split(remaining_chunks, ThreadCount)
remaining_chunks_split = [list(part) for part in remaining_chunks_split]

print(remaining_chunks_split)

thread_chunks = {}
for i, part in enumerate(remaining_chunks_split):
    print(f"Thread {i} will process {len(part)} chunks: {part}")
    workitems = {}
    for j, chunk in enumerate(part, start=1):
        workitems[j] = chunk
    thread_chunks[i] = workitems    

print(thread_chunks)

with open(os.path.join(WeAreInFolder, 'workitems.pickle'), 'wb') as f:
    pickle.dump(thread_chunks, f)
    
print("threadSpread.json created ready for startThreads.ps1")
