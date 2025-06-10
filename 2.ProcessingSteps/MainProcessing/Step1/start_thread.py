import os
import pickle
import pandas as pd
from TheThingTodo import DOThis
import time
import re
import sys
import json



# Directory containing the CSV files
directory = r'C:\Users\Mariana\Documents\Python\steps\TODOcsvs'


# Change theese for each step
Filein  = "DONE_step0"
Fileout = "DONE_step1"
WeAreInFolder = r"C:\Users\Mariana\Documents\Python\steps\step1"

# Update the process_csv_file function to handle a list of files
def process_csv_files(thread_id:int, csv_files)->None:
    runtimes = []
    i=0 # i is the counter for the number of files processed
    TODOCount = len(csv_files) # Total number of files to process
    print(f"Thread {thread_id} processing {TODOCount} files {csv_files}")
    for csv_file in csv_files:
        chunk_nr = int(csv_file.split('_')[-1].split('.')[0])
        outputfilename = f"{Fileout}_{chunk_nr}.csv"
        start_time = time.time() # Start time of processing the file    
        i = i + 1 # Increment the counter for the number of files processed   
        # *read the file ********************************************************
        print(f"Thread {thread_id} processing {csv_file}")
        TODOfile_path = os.path.join(directory, csv_file)
        df = pd.read_csv(TODOfile_path)
        df = DOThis(df)  ## the useful bit is in the TheThingTodo.py file
        # save the file
        DONEfile_path = os.path.join(directory, outputfilename)        
        df.to_csv(DONEfile_path, index=False, mode='w')
        # **analyse runtime *******************************************************
        runtime = time.time() - start_time
        print(f"Thread {thread_id} processed {csv_file} in {runtime:.2f} seconds.")
        runtimes.append(runtime)
        # Save runtime statistics to a file
        stats_file_path = os.path.join(WeAreInFolder, r"runstatistics\files", f"{chunk_nr}.txt")
        os.makedirs(os.path.dirname(stats_file_path), exist_ok=True)
        with open(stats_file_path, 'w') as stats_file:
            stats_file.write(f"{int(runtime)}")
            
        avg_runtime = sum(runtimes) / len(runtimes) if runtimes else 0
        remaining_chunks = TODOCount - i
        estimated_time_remaining = avg_runtime * remaining_chunks
        estimated_completion_time = time.time() + estimated_time_remaining
        completion_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(estimated_completion_time))
        print(f"Thread {thread_id} i={i} of {TODOCount} processed successfully. Estimated time remaining: {estimated_time_remaining:.2f} seconds ({estimated_time_remaining/60:.2f} Min, {estimated_time_remaining/3600:.2f} Hrs). Estimated completion time: {completion_time_str}")


def run(threadid:int)->None:
    includedcsvs = []
    with open(f'{WeAreInFolder}/workitems.pickle', 'rb') as file:
        workitems = pickle.load(file)
    threadworkitems=workitems[threadid]
    threadworkitems = set(threadworkitems.values())
    print(threadworkitems)
    csv_files = [f for f in os.listdir(directory) if f.startswith(Filein) and f.endswith('.csv')]
    for file in csv_files:
        chunk_nr = int(file.split('_')[-1].split('.')[0])
        if chunk_nr in threadworkitems:
            includedcsvs.append(file)
    csv_files = includedcsvs # this makes sure we only process files that are in the range of first to last
    

    # Remove files that are already in the completed list
    process_csv_files(thread_id=threadid, csv_files = csv_files)
    
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python start_thread.py <threadid>")
        sys.exit(1)
    run(threadid = int(sys.argv[1]))
    # run(threadid = 0) # for testing
