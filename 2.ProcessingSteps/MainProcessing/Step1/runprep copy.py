folder = r'C:\Users\Mariana\Documents\Python\steps\TODOcsvs'

import os
import numpy as np
import pickle

StepINfileNAME = "step0".lower() # What is the name of the that we will take as input
StepFileout = "step1".lower() # What is the name of the step when it is "Done" that we want to eliminate from run
ThreadCount = 30
WeAreInFolder = r"C:\Users\Mariana\Documents\Python\steps\step1"

#################### CHANGE ABOVE ########################### 
files = [f for f in os.listdir(folder)]

DoneSet = set()
AllChunksSet = set(range(1, 5482))
sizes = []
for file in files:
    if file.endswith('.csv'):
        chunk = file.split('_')[-1].split('.')[0]
        if StepFileout in file:
            DoneSet.add(int(chunk))
        if StepINfileNAME in file:
            file_path = os.path.join(folder, file)
            file_size = os.path.getsize(file_path)
            sizes.append((int(chunk), file_size))


remaining_chunks = AllChunksSet - DoneSet
sizes.sort(key=lambda x: x[1], reverse=True)
print("pint")


print(F"""{len(remaining_chunks)} chunks remaining""")
# Sort remaining chunks by file size
remaining_chunks_with_sizes = [(chunk, size) for chunk, size in sizes if chunk in remaining_chunks]
remaining_chunks_with_sizes.sort(key=lambda x: x[1], reverse=True)

# Initialize parts with empty lists and their total sizes
remaining_chunks_split = [[] for _ in range(ThreadCount)]
part_sizes = [0] * ThreadCount

# Distribute chunks to minimize size difference between parts
for chunk, size in remaining_chunks_with_sizes:
    # Find the part with the smallest total size
    smallest_part_index = part_sizes.index(min(part_sizes))
    remaining_chunks_split[smallest_part_index].append(chunk)
    part_sizes[smallest_part_index] += size

# print(remaining_chunks_split)

thread_chunks = {}
for i, part in enumerate(remaining_chunks_split):
    workitems = {}
    for j, chunk in enumerate(part, start=1):
        workitems[j] = chunk
    thread_chunks[i] = workitems
    print(f"Thread {i} will process {len(part)} chunks")

with open(os.path.join(WeAreInFolder, 'workitems.pickle'), 'wb') as f:
    pickle.dump(thread_chunks, f)
    
print("threadSpread.json created ready for startThreads.ps1")


