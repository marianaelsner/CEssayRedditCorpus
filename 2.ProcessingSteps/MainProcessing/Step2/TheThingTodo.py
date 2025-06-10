import re
import pandas as pd

def check_and_reassign(row):
    if isinstance(row['self_text_corrected'], str) and (
        "the word woke" in row['self_text_corrected'] or
        "the term woke" in row['self_text_corrected'] or
        "define woke" in row['self_text_corrected']
    ):
        row['self_text_pos'] = re.sub(r"\('woke', 'VERB'\)", "('woke', 'NOUN')", row['self_text_pos'])
    return row


def check_and_reassign_wild_woke(row):
    if isinstance(row['self_text_corrected'], str) and (
        "the wild wild woke" in row['self_text_corrected']
    ):
        row['self_text_pos'] = re.sub(r"\('woke', 'AJD'\)", "('woke', 'NOUN')", row['self_text_pos'])
    return row


def reassign_pos(row):
    try:
        # Ensure pos_word_tuples is a list of tuples
        pos_word_tuples = ast.literal_eval(row['pos_word_tuples']) if isinstance(row['pos_word_tuples'], str) else row['pos_word_tuples']
        
        # Skip if pos_word_tuples is not a list or is empty
        if not isinstance(pos_word_tuples, list) or len(pos_word_tuples) < 3:
            return pos_word_tuples
        
        # Iterate through the list of tuples to find specific structures
        for i in range(len(pos_word_tuples)):
            if i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'NOUN')

        # Second structure: ('x', 'DET'), ('woke', 'ADJ')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'ADJ')
            ):
                pos_word_tuples[i + 1] = ('woke', 'NOUN')

        # Third structure: ('x', 'ADP'), ('woke', 'ADJ')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADP' and
                pos_word_tuples[i + 1] == ('woke', 'ADJ')
            ):
                pos_word_tuples[i + 1] = ('woke', 'NOUN')

        # Fourth structure: ('woke', 'VERB'), ('y', 'PROPN')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'PROPN'
            ):
                pos_word_tuples[i] = ('woke', 'NOUN')

        # Fifth structure: ('woke', 'VERB'), ('y', 'AUX')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'AUX'
            ):
                pos_word_tuples[i] = ('woke', 'NOUN')

        # Sixth structure: ('woke', 'VERB'), ('y', 'PART')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'PART'
            ):
                pos_word_tuples[i] = ('woke', 'NOUN')

        # Seventh structure: ('woke', 'VERB'), ('y', 'VERB')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'VERB'
            ):
                pos_word_tuples[i] = ('woke', 'NOUN')

        # Eighth structure: ('woke', 'PROPN')
            elif  i < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'PROPN')
            ):
                pos_word_tuples[i] = ('woke', 'NOUN')

        # Ninth structure: ('wokeness', 'ADJ')
            elif  i < len(pos_word_tuples) and ( 
                pos_word_tuples[i] == ('wokeness', 'ADJ')
            ):
                pos_word_tuples[i] = ('wokeness', 'NOUN')

        # Tenth structure: ('wokeness', 'VERB')
            elif i < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('wokeness', 'VERB')
            ):                
                pos_word_tuples[i] = ('wokeness', 'NOUN')
            
        return pos_word_tuples
    except Exception as e:
        print(f"Error processing row: {row}")
        print(e)
        return row['pos_word_tuples']


def DOThis(df)->pd.DataFrame:
    df = df.apply(check_and_reassign, axis=1)
    df = df.apply(check_and_reassign_wild_woke, axis=1)
    df['self_text_pos'] = df.apply(reassign_pos, axis=1)
    return df
