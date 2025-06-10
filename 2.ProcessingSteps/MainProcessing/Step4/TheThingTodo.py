import ast
import re
import pandas as pd

def reassign_pos(row):
    patterns = [
    (3, lambda a, b, c: a[1] == 'PROPN' and b[0] == 'woke' and c[1] == 'PROPN'),
    (3, lambda a, b, c: a[1] == 'DET' and b[0] == 'woke' and c[1] == 'NOUN'),
    (2, lambda a, b: a[1] == 'PROPN' and b[0] == 'woke'),
    (2, lambda a, b: a[1] == 'PROPN' and b[0] == 'woke'),
    (2, lambda a, b: a[1] == 'AUX' and b[0] == 'woke'),
    (2, lambda a, b: a[1] == 'NOUN' and b[0] == 'woke'),
    (3, lambda a, b, c: a[1] == 'PRON' and b[0] == 'woke' and c[1] == 'CCONJ'),
    (3, lambda a, b, c: a[1] == 'PRON' and b[1] == 'PRON' and c[0] == 'woke'),
    (3, lambda a, b, c: a[0] == 'woke' and b[1] == 'PRON' and c[1] == 'PROPN'),
    (3, lambda a, b, c: a[0] == 'woke' and b[1] == 'ADJ' and c[1] == 'CCONJ'),
    (2, lambda a, b: a[0] == 'woke' and b[1] == 'PROPN'),
    (3, lambda a, b, c: a[1] == 'ADJ' and b == ('woke', 'VERB') and c[1] == 'PROPN'),
    (2, lambda a, b: a == ('woke', 'VERB') and b[1] == 'PROPN'),
    (3, lambda a, b, c: a[1] == 'VERB' and b == ('woke', 'VERB') and c[1] == 'PROPN'),
    (2, lambda a, b: a[1] == 'PRON' and b == ('woke', 'VERB')),
    (3, lambda a, b, c: a[1] == 'PRON' and b[1] == 'PART' and c == ('woke', 'VERB')),
    (2, lambda a, b: a[1] == 'CCONJ' and b == ('woke', 'VERB')),
    (3, lambda a, b, c: a == ('woke', 'VERB') and b[1] == 'NOUN' and c[1] == 'VERB'),
    (3, lambda a, b, c: a == ('woke', 'VERB') and b[1] == 'NOUN' and c[1] == 'ADJ'),
    (2, lambda a, b: a == ('woke', 'VERB') and b[1] == 'NOUN'),
    (3, lambda a, b, c: a == ('woke', 'NOUN') and b[1] == 'NOUN' and c[1] == 'NOUN'),  # 'woke' followed by two nouns
    (3, lambda a, b, c: a[1] == 'DET' and b == ('woke', 'NOUN') and c[1] == 'PROPN'),  # 'woke' before a proper noun
    (2, lambda a, b: a[1] == 'ADP' and b == ('woke', 'NOUN')),  # 'woke' before a preposition
    (3, lambda a, b, c: a[1] == 'DET' and b == ('woke', 'NOUN') and c[1] == 'PRON'),  # NEW: 'woke' followed by a pronoun
    (3, lambda a, b, c: a == ('woke', 'NOUN') and b[0] == 'mind' and c[0] == 'virus'),  # NEW: 'woke' followed by a pronoun
    (2, lambda a, b: a == ('being', 'AUX') and b == ('woke', 'NOUN')),  # NEW: 'being' before 'woke'
    (4, lambda a, b, c, d: a == ('woke', 'NOUN') and b[0] == 'liberal' and c[0] == 'mind' and d[0] == 'virus'),  # NEW: 'woke' followed by three nouns
    (4, lambda a, b, c, d: a == ('woke', 'NOUN') and b[0] == 'mind' and c[0] == 'gay' and d[0] == 'virus'),  # NEW: 'woke' followed by three nouns
    (3, lambda a, b, c: a[0] == 'sleepy' and b == ('woke', 'NOUN') and c[0] == 'joe'),  # NEW: 'woke' followed by two nouns
    (4, lambda a, b, c, d: a[1] == 'DET' and b[0] == 'woke' and c[1] == 'ADJ' and d[1] == 'NOUN'),  # NEW: 'woke' followed by adj and noun
    (2, lambda a, b: a[0] == 'going' and b[0] == 'woke'), 
    (2, lambda a, b: a[0] == 'woke' and b[1] == 'PROPN'),  # NEW: 'woke' followed by a proper noun
    (4, lambda a, b, c, d: a[1] == 'DET' and b[0] == 'woke' and c[1] == 'ADJ' and d[1] == 'PROPN'),  # NEW: 'woke' followed by adj and noun
    (2, lambda a, b: a[0] == 'woke' and b[1] == 'PROPN'),  # NEW: 'woke' followed by a proper noun
    (2, lambda a, b: a[0] == 'woke' and b[1] == 'NOUN'),  # NEW: 'woke' followed by an adjective 
    (5, lambda a, b, c, d, e: a[1] == 'DET' and b[0] == 'woke' and c[1] == 'ADJ' and d[1] == 'ADJ' and e[1] == 'NOUN'),  # NEW: 'woke' followed by adj and noun
    (5, lambda a, b, c, d, e: a[1] == 'DET' and b[0] == 'woke' and c[1] == 'ADV' and d[1] == 'ADJ' and e[1] == 'NOUN'),  # NEW: 'woke' followed by adj and noun
    (3, lambda a, b, c: a[0] == 'woke' and b[1] == 'PUNCT' and c[1] == 'ADJ'),  # NEW: 'woke' followed by an adjective
    (2, lambda a, b: a[0] == 'gone' and b[0] == 'woke'),  # NEW: 'woke' followed by an adjective
    (2, lambda a, b: a[0] == 'stay' and b[0] == 'woke'),  # NEW: 'woke' followed by an adjective
]

def reassign_pos(row):
    pos_word_tuples = ast.literal_eval(row['pos_word_tuples']) if isinstance(row['pos_word_tuples'], str) else row['pos_word_tuples']

    if not isinstance(pos_word_tuples, list) or len(pos_word_tuples) < 2:
        return pos_word_tuples

    for i in range(len(pos_word_tuples)):
        for length, condition in patterns:
            if i + length <= len(pos_word_tuples):
                segment = tuple(pos_word_tuples[i + j] for j in range(length))
                if condition(*segment):
                    for j, token in enumerate(segment):
                        if token[0] == 'woke':
                            pos_word_tuples[i + j] = ('woke', 'ADJ')  # Reassign 'woke' to ADJ
    return pos_word_tuples

def DOThis(df)->pd.DataFrame:
    df['self_text_pos'] = df.apply(reassign_pos, axis=1)
    return df
