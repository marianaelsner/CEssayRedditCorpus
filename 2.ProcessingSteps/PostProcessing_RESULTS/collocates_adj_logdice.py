import pickle
import pandas as pd
import math
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt

# Load preprocessed data
with open("preprocessed_data_adj.pkl", "rb") as f:
    data = pickle.load(f)

# Extract woke_pos_tuples (not woke_words!)
woke_pos_tuples = data.get("woke_pos_tuples", [])
if not woke_pos_tuples:
    raise ValueError("The 'woke_pos_tuples' list is empty or not found in the preprocessed data.")

# Use the original tuples without lemmatization
processed_tuples = woke_pos_tuples

# Debugging: Compare original tuples
print("Original woke_pos_tuples (first 10):", woke_pos_tuples[:10])

# Total words for normalized frequency
total_words = len(processed_tuples)
print(f"📊 Total words (tokens) in 'woke' sentences: {total_words}")

# Word frequencies
word_pos_freq = Counter(processed_tuples)

# Function to capture collocates in a window of 5 words before and after 'woke'
def find_collocates_in_window(tuples, target_word, window_size=5):
    collocate_counter = Counter()
    for i in range(len(tuples)):
        word, pos = tuples[i]
        # Check if the word is 'woke' and if it's an adjective (ADJ)
        if word == target_word and pos == 'ADJ':
            # Look for words before and after 'woke' in the specified window size
            start = max(0, i - window_size)
            end = min(len(tuples), i + window_size + 1)
            for j in range(start, end):
                # Skip if it's the target word itself or if the collocate is 'woke'
                if j != i and tuples[j][0] != target_word:
                    collocate_counter[tuples[j][0]] += 1
    return collocate_counter

# Find collocates of 'woke' within a window of 5 words before and after it
collocate_counter = find_collocates_in_window(processed_tuples, 'woke', window_size=5)

# Print the most common collocates (first 10 for inspection)
print("Most common collocates within a window of 5 words:")
for collocate, freq in collocate_counter.most_common(10):
    print(f"{collocate}: {freq}")

# Calculate log-dice scores for collocates
def log_dice(collocate, f_collocate, f_woke, f_collocate_woke):
    denominator = f_collocate + f_woke
    numerator = 2 * f_collocate_woke
    if denominator > 0 and numerator > 0:  # Ensure valid values for log2
        return 14 + math.log2(numerator / denominator)
    else:
        return 0  # Assign a default score of 0 if the calculation is invalid

# Word frequencies of 'woke' as an adjective
f_woke = word_pos_freq[('woke', 'ADJ')]

# Calculate log-dice for each collocate
collocates_logdice = {}
collocates_frequency = {}
for collocate, f_collocate in collocate_counter.items():
    # Calculate the frequency of the bigram ('woke', 'ADJ') followed by the collocate
    f_collocate_woke = sum(1 for i in range(1, len(processed_tuples)) 
                           if processed_tuples[i-1] == ('woke', 'ADJ') and processed_tuples[i][0] == collocate)
    
    # Calculate log-dice score
    score = log_dice(collocate, f_collocate, f_woke, f_collocate_woke)
    collocates_logdice[collocate] = score
    collocates_frequency[collocate] = f_collocate

# Sort top 20 by log-dice
top20 = sorted(collocates_logdice.items(), key=lambda x: x[1], reverse=True)[:20]

# Build DataFrame rows
rows = []
for rank, (word, score) in enumerate(top20, 1):
    raw_freq = collocates_frequency[word]
    norm_freq = (raw_freq / total_words) * 1_000
    rows.append({
        'Rank': rank,
        'Collocate': word,
        'Log Dice': score,
        'Raw Frequency': raw_freq,
        'Normalized Freq (per 1k)': norm_freq
    })

logdice_df = pd.DataFrame(rows)

# Save to Excel
output_path = r"C:\Users\Mariana\Documents\Python\results\Woke_Adj_Collocates_Window_LogDice.xlsx"
logdice_df.to_excel(output_path, index=False)
print(f"✅ Saved collocates within a window of 5 words to: {output_path}")

# Print summary
print("\nTop 20 Collocates (window of 5 words before and after 'woke'):")
print(logdice_df.to_string(index=False))

# ================================
# 🎨 OPTIONAL: Generate WordCloud
# ================================
# Limit WordCloud to top 20 collocates
top20_collocates = dict(top20)

if not top20_collocates:
    print("⚠️ No collocates found for 'woke' as an adjective. Skipping WordCloud generation.")
else:
    # Generate WordCloud
    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        max_words=20
    ).generate_from_frequencies(top20_collocates)

    # Plot WordCloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
