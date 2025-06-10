import pandas as pd
import string
import os
import re
import spacy
import contractions
import unicodedata as unicode
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

print("*" * 150)
print("Starting Step 1")
csv_file = fr'C:\Users\Mariana\Documents\Python\csv\Data_0_done.csv'

df = pd.read_csv(csv_file)
print("reading csv...")
pd.set_option('display.max_colwidth', 200)
print(df['self_text'].head(20))
# print(df.columns)
## We do stuff here

print('progress point 1')

df = df [df['author_name'] != 'M_i_c_K'] #keeps posting the same shit over and over again
df = df[df['author_name'] != 'changemyview-ModTeam'] # remove posts by changemyview-ModTeam
print(f"Progress point 2")
df = df[df['author_name'] != 'tacostats'] # remove posts by bot
print(f"Progress point 3")
df = df[df['author_name'] != 'groupbot'] # remove posts by bot
print(f"Progress point 4")
df = df[df['author_name'] != 'DeltaBot'] # remove posts by bot
print(f"Progress point 5")
df = df[df['author_name'] != 'jobautomator'] # remove posts by bot/mod 
print(f"Progress point 6")
df = df[df['author_name'] != 'AutoModerator'] # remove posts by bot/mod
print(f"Progress point 7")
df = df[df['author_name'] != 'BM2018Bot'] # remove posts by bot/mod 
print(f"Progress point 8")
df = df[df['author_name'] != 'PoliticsModeratorBot'] # remove posts by bot/mod
print(f"Progress point 9")
df = df[df['author_name'] != 'critiqueextension'] # remove posts by bot
print(f"Progress point 10")
df = df[df['author_name'] != 'autotldr'] # remove posts by bot
print(f"Progress point 11")
df = df[df['author_name'] != 'newswall-org'] # remove posts by bot
print(f"Progress point 12")
df = df[df['author_name'] != 'toorad4momanddad']
print(f"Progress point 13")
df = df[df['author_name'] != 'rrybwyb']
print(f"Progress point 14")
df = df[df['author_name'] != 'newswall-org']
print(f"Progress point 15")
df = df[df['author_name'] != 'AmputatorBot']
print(f"Progress point 16")
df = df[df['author_name'] != 'Paid-Not-Payed-Bot']
print(f"Progress point 17")
df = df[df['author_name'] != 'TotesMessenger']
print(f"Progress point 18")
df = df [df['author_name'] != 'Ansuz07'] # seems to be a mod, has deleted their account
print(f"Progress point 19")
df = df [df['author_name'] != 'Urmomjuicypussy'] #shitposter
print(f"Progress point 20")
df = df [df['author_name'] != 'Razwog'] #shitposter
print(f"Progress point 21")
df = df [df['author_name'] != 'CWoldren'] #shitposter
print(f"Progress point 22")
df = df [df['author_name'] != 'Alert_Study_4261'] #shitposter
print(f"Progress point 23")
df = df [df['author_name'] != 'thebenshapirobot'] #bot
print(f"Progress point 24")    
df = df [df['author_name'] != 'running_against_bot'] #bot or shitposter, account deactivated
print(f"Progress point 25")
df = df [df['author_name'] != 'ColonelCorn69'] #bot or shitposter, account deactivated
print(f"Progress point 26")
df = df [df['author_name'] != 'botsallthewaydown'] #bot or shitposter, account deactivated
print(f"Progress point 27")



def clean_text(text):
    text = str(text).replace('woke-up', 'wake-up')
    text = str(text).replace(' /s', ' sarcasm')
    text = str(text)  # ensure text is a string
    text = re.sub(r'!\[gif\]\(giphy\|[^)]+\)', '', text)  # remove gif links
    text = re.sub(r'\[.*?\]\((https?://.*?)\)', '', text)  # remove links with link text
    text = re.sub(r'http\S+', '', text) # remove naked links
    text = text.replace('\n', ' ') # remove newlines
    text = text.replace('!delta', ' ') # remove delta function
    text = text.replace('!remindme', ' ') # remove remindme function  
    text = text.replace('!ping', ' ') # remove ping function
    text = text.replace('"', '') 
    text = text.replace('&gt', ' ') # remove weird characters
    text = text.replace('&amp', ' ') # remove weird characters
    text = text.replace(r'\"', ' ') # remove quotes
    text = text.replace(r'\'', '') # remove single quotes
    text = text.replace('/', ' ') # remove forward slashes
    text = text.replace('|', ' ') # remove vertical bars
    text = text.replace('\\', ' ') # remove backslashes
    text = text.replace('_', ' ') # remove underscores
    text = text.replace('[', ' ') # remove square brackets
    text = text.replace(']', ' ') # remove square brackets
    text = text.replace('(', ' ') # remove parentheses
    text = text.replace(')', ' ') # remove parentheses
    text = text.replace('#x200B', ' ') # remove zero-width space
    text = text.replace('“', ' ') # remove quotes
    text = text.replace('”', ' ') # remove quotes
    text = text.replace('‘', ' ') # remove quotes
    text = text.replace('’', ' ') # remove quotes
    text = text.replace('Woke', 'woke') # to prevent spacy from reading "Woke" as a proper noun
    text = text.replace('Wokeness', 'wokeness') # to prevent spacy from reading "Wokeness" as a proper noun
    text = text.replace('Wokest', 'wokest') # to prevent spacy from reading "Wokest" as a proper noun
    text = text.replace('Wokism', 'wokism') # to prevent spacy from reading "Wokism" as a proper noun
    text = text.replace('beingg', 'being') 
    return text

df['self_text'] = df['self_text'].apply(clean_text)

print(f"progress point 28")

print(f"Progress point 29")

df['self_text'] = df['self_text'].str.lstrip()

print(f"Progress point 30")


def replace_strings(text):
    for key, value in replacement.items():
        text = text.replace(key, value)
    return text

# Dictionary for text replacements
replacement = {
    '•': ' ',
    'E.G.': 'for example',
    'let s ': 'let’s ',
    'Let s ': 'Let’s ',
    'o clock ': 'o’clock ',
    'O clock ': 'O’clock ',
    'oclock ': 'o’clock ', 
    '"&gt;': ' ',
    '…': ' ',
    'woke up': 'wake up',
    'woke me up': 'wake me up',
    'woke him up': 'wake him up',
    'woke most people up': 'wake most people up',
    'woke paralyzed ': 'wake paralyzed ',
    'woke lots more people up': 'wake lots more people up',
    'woke some of you up': 'wake some of you up',
    'woke the electorate up': 'wake the electorate up',
    'woke a LOT of people up': 'wake a LOT of people up',
    'woke my ass up': 'wake my ass up',
    'woke the fuck up': 'wake the fuck up',
    'woke us up': 'wake us up',
    'woke her up': 'wake her up',
    'woke a lot of people up': 'wake a lot of people up',
    'woke everybody up': 'wake everybody up',
    'woke to see ': 'wake to see ',
    'I woke this morning ': 'I wake this morning ',
    'woke people’s butts up': 'wake people’s butts up',
    'woke them all up': 'wake them all up',
    'I woke feeling refreshed ': 'I wake feeling refreshed',
    'I woke in the morning ': 'I wake in the morning ',
    'woke them up': 'wake them up',
    'woke my wife up': 'wake my wife up',
    'woke Tommy up': 'wake Tommy up',
    'woke joe up': 'wake joe up',
    'I shouldn’t be woke at 1am': 'I shouldn’t be awake at 1am',
    'woke a lot of women up': 'wake a lot of women up',
    'woke him out of bed': 'wake him out of bed',
    'woke these girls up': 'wake these girls up',
    'woke before dawn': 'wake before dawn',
    'I woke in an anesthesiainduced': 'I wake in an anesthesiainduced',
    'woke the left up': 'wake the left up',
    'woke many people up': 'wake many people up',
    'woke my kids up': 'wake my kids up',
    'woke the country up': 'wake the country up',
    'woke back up': 'wake back up',
    'woke America up': 'wake America up',
    'woke everyone up': 'wake everyone up',
    'we woke a sleeping giant': 'we wake a sleeping giant',
    'He woke nobody': 'He wake nobody',
    'woke a lot of us up': 'wake a lot of us up',
    'they woke us one morning ': 'they wake us one morning ',
    'woke some poeple up': 'wake some people up',
    'it woke the democratic party ': 'it wake the democratic party ',
    'we woke tomorrow': 'we wake tomorrow',
    'woke people up': 'wake people up',
    'woke them all back up': 'wake them all back up',
    'woke that president up': 'wake that president up',
    'woke the FBI up': 'wake the FBI up',
    'being woke in the middle of the night': 'being awakened in the middle of the night',
    'woke some of you people up': 'wake some of you people up',
    'woke my mom up': 'wake my mom up',
    'woke you up': 'wake you up',
    'I woke from': 'I wake from',
    'I was woke by God': 'I was awakened by God',
    'woke most of us up': 'wake most of us up',
    'woke my roommate': 'awakened my roommate',
    'woke the insurrectionists right up': 'wake the insurrectionists right up',
    'woke at least one of my kids up': 'wake at least one of my kids up',
    'woke my dad up': 'wake my dad up',
    'woke the dead': 'wake the dead',
    'she woke thinking it': 'she wake thinking it',
    'woke to find himself': 'wake to find himself',
    'woke from': 'wake from',
    'woke more up': 'wake more up',
    'woke even more up': 'wake even more up',
    'woke the cancer': 'wake the cancer',
    'my partner also woke next to me': 'my partner also wake next to me',
    'woke my cat up': 'wake my cat up',
    'I woke you': 'I wake you',
    'America woke up': 'America wake up',
    'someone just woke one day': 'someone just wake one day',
    'WOKE YOU UP': 'WAKES YOU UP',
    'woke them u': 'wake them up',
    'Trump woke in the Republican base': 'Trump wake in the Republican base',
    'you woke out': 'you wake out',
    'being woke to this fact is bad': 'being awaken to this fact is bad',
    'woke the hell up': 'wake the hell up',
    'woke my dog up': 'wake my dog up',
    'woke my poor dog up': 'wake my poor dog up',
    'woke the baby up': 'wake the baby up',
    'woke his ass up': 'wake his ass up',
    'woke some people tf up': 'wake some people tf up',
    'when I woke': 'when I wake',
    'when we all woke': 'when we all wake',
    'Trump woke the dark heart': 'Trump wake the dark heart',
    'He is now woke to the spell': 'He is now awakened to the spell',
    'he never woke again': 'he never awakened again',
    'woke my baby': 'wake my baby',
    'woke everyone’s ass up': 'wake everyone’s ass up',
    'you woke and ': 'you wake and ',
    'woke the f up': 'wake the f up',
    'woke anyone up': 'wake anyone up',
    'woke his moron cult followers up': 'wake his moron cult followers up',
    'woke all my neighbors': 'wake all my neighbors',
    'woke my kid up': 'wake my kid up',
    'woke a monster': 'wake a monster',
    'they woke us': 'they wake us',
    'we woke tomorrow': 'we wake tomorrow',
    'woke a lot more people up': 'wake a lot more people up',
    'woke people out': 'wake people out',
    'I woke to that': 'I wake to that',
    'woke some of them up': 'wake some of them up',
    'woke Durbin up': 'wake Durbin up',
    'woke us out': 'wake us out',
    'I woke my mind': 'I wake my mind',
    'woke a lot of folks up': 'wake a lot of folks up',
    'woke the sleeping giant': 'wake the sleeping giant',
    'woke nakeed ': 'wake naked ',
    'He woke later': 'He wake later',
    'We already woke you': 'We already wake you',
    'woke only to lift': 'wake only to lift',
    'woke Trump up': 'wake Trump up',
    'woke NATO up': 'wake NATO up',
    'woke out of': 'wake out of',
    'We woke our whole lives': 'We worked our whole lives',
    'when he woke': 'when he wakes',
    'woke Merrick Garland up': 'wake Merrick Garland up',
    'woke my up from sleep': 'wake me up from sleep',
    'woke me from': 'wake me from',
    'woke more up': 'wake more up',
    'Putin just all of sudden woke': 'Putin just all of sudden wake',
    'woke some people up': 'wake some people up',
    'on the trend sleep and woke': 'on the trend sleep and wake',
    'woken up': 'waken up',
    ' WOKE ': ' woke ',
    ' bein ': ' being ',
    ' ppl ': ' people ',
    ' dems ': ' Democrats',
    ' libs': ' liberals',
    ' b c ': ' because ',
    ' bc ': ' because ',
    ' sry ': ' sorry ',
    ' Ds ': ' Democrats',
    ' jan ': ' January ',
    ' Jan ': ' January ',
    'â€“': ' ',
    'â€‹': ' ',
    ' don t ': ' do not ',
    ' Dems ': 'Democrats ',
    ' Libs ': 'Liberals',
    ' bs ': 'bullshit',
    ' autonimity ': 'autonomy',
    ' jsut ': 'just',
    ' obvs ': ' obviously ',
    ' srly ': ' seriously '
}

df['self_text'] = df['self_text'].apply(replace_strings)



print(f"Progress point 31")

# Function to convert word numerals to numbers
def word_to_num(text):
    num_dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10', 'eleven': '11',
        'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16',
        'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '20', 'thirty': '30',
        'forty': '40', 'fifty': '50', 'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90', 'hundred': '100', 
        'thousand': '1000', 'million': '1000000', 'billion': '1000000000', 'trillion': '1000000000000'
    }
    
    # Replace word numerals with numbers
    for word, num in num_dict.items():
        text = re.sub(r'\b' + word + r'\b', num, text)
    
    return text

df['self_text'] = df['self_text'].apply(word_to_num)

print(f"Progress point 32")

def remove_accented_chars(text):
    text = unicode.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

df['self_text'] = df['self_text'].apply(remove_accented_chars)

print(f"Progress point 33")


df['self_text'] = df['self_text'].str.replace(r'[\u4e00-\u9fff]+', '', regex=True) # remove Chinese characters not tested yet
print(f"Progress point 34")

df['self_text'] = df['self_text'].str.replace(r'[\u0400-\u04FF]+', '', regex=True) # remove Cyrillic characters
print(f"Progress point 35")

def expand_acronyms(text):
    acronyms = {
        'FYI': 'for your information',
        'WTF': 'what the fuck',
        'RBG': 'Ruth Bader Ginsburg',
        'CMV': 'change my view',
        'U.S.': 'United States',
        'CA': 'California',
        'SJW': 'social justice warrior',
        'ANC': 'African National Congress',
        'DA': 'Democratic Alliance',
        'EFF': 'Economic Freedom Fighters',
        'IDK': 'I don’t know',
        'IMO': 'in my opinion',
        'IMHO': 'in my humble opinion',
        'BTW': 'by the way',
        'DIY': 'do it yourself',
        'LOL': 'laughing out loud',
        'OMG': 'oh my god',
        'BRB': 'be right back',
        'GTG': 'got to go',
        'TTYL': 'talk to you later',
        'SMH': 'shaking my head',
        'TBH': 'to be honest',
        'TBA': 'to be announced',
        'TBD': 'to be decided',
        'AKA': 'also known as',
        'FAQ': 'frequently asked questions',
        'RSVP': 'please respond',
        'ETA': 'estimated time of arrival',
        'BFF': 'best friends forever',
        'YOLO': 'you only live once',
        'FOMO': 'fear of missing out',
        'NSFW': 'not safe for work',
        'TL;DR': 'too long didn’t read',
        'ffs': 'for fuck’s sake',
        'CPI': 'Consumer Price Index',
        'OP': 'original poster',
        'SS': 'social security',
        'US': 'United States',
        'UK': 'United Kingdom',
        'EU': 'European Union',
        'UN': 'United Nations',
        'SF': 'San Francisco',
        'NYC': 'New York City',
        'DJT': 'Donald J. Trump',
        'MLK': 'Martin Luther King',
        'LBJ': 'Lyndon B. Johnson',
        'M.O.': 'modus operandi',
        'E.G.': 'for example',
        'e.g.': 'for example',
        'LBJs': 'Lyndon B. Johnson',
    }
    
    for acronym, full_form in acronyms.items():
        text = re.sub(r'\b' + acronym + r'\b', full_form, text)
    
    return text

df['self_text'] = df['self_text'].apply(expand_acronyms)

# Remove punctuation except period
df['self_text'] = df['self_text'].apply(lambda x: ''.join([char for char in x if char not in string.punctuation or char in ['.', ',', "'"]]))

print(f"Progress point 36")

nltk.download('punkt')
nltk.download('wordnet')

print(f"Progress point 37")

def expand_contractions(text):
    expanded_words = [] 
    for word in text.split():
        # using contractions.fix to expand the shortened words
        expanded_words.append(contractions.fix(word))

    expanded_text = ' '.join(expanded_words)
    #print('Original text: ' + text)
    #print('Expanded_text: ' + expanded_text)
    return expanded_text

df['self_text'] = df['self_text'].apply(expand_contractions)

print(f"Progress point 38")

df['self_text'] = df['self_text'].str.lower()

print("progress point 39")

def expand_contractions_2(text):
    contractions = {
        'don t': 'do not',
        'won t': 'will not',
        'can t': 'cannot',
        'i m': 'i am',
        'you re': 'you are',
        'he s': 'he is',
        'she s': 'she is',
        'it s': 'it is',
        'we re': 'we are',
        'they re': 'they are',
        'i ve': 'i have',
        'ive':  'i have',
        'you ve': 'you have',
        'youve': 'you have',
        'we ve': 'we have',
        'they ve': 'they have',
        'i ll': 'i will',
        'you ll': 'you will',
        'he ll': 'he will',
        'she ll': 'she will',
        'it ll': 'it will',
        'ill': 'i will',
        'we ve': 'we have',
        'they ve': 'they have',
        'i ve': 'i have',
        'you ve': 'you have',
        'should ve': 'should have',
        'could ve': 'could have',
        'would ve': 'would have',
        'might ve': 'might have',
        'must ve': 'must have',
        'isn t': 'is not',
        'aren t': 'are not',
        'wasn t': 'was not',
        'weren t': 'were not',
        'hasn t': 'has not',
        'haven t': 'have not',
        'hadn t': 'had not',
        'doesn t': 'does not',
        'didn t': 'did not',
        'wont': 'will not',
        'doesnt': 'does not',
        'cant': 'cannot',
        'dont': 'do not',
        'it s': 'it is',
        'its': 'it is',
        'im': 'I am',
        'i m': 'I am',
        'hes':  'he is',
        'shes': 'she is',
        'i d': 'i would',
        'ya': 'you',
        'ha': 'has',
        'doesnt': 'does not',
        'what s': 'what is',
        'whats': 'what is',
        'corpo': 'corporate',
        'govt': 'government',
        'gov': 'government',
        'that s': 'that is',
        'wan na': 'want to',
        'gon na': 'going to',
        'gotta': 'got to',
        'doe': 'does',
        'sry': 'sorry',
        'peoplefor': 'people for',
        'peopleto': 'people to',
        'laughingrolling': 'laughing rolling',
        'laughingface': 'laughing face',
        'joyface': 'joy face',
        'faceenraged': 'face enraged',
        'engineeringoriented': 'engineering oriented',
        'allin': 'all in',
        'genderaffirming': 'gender affirming',
        'there s': 'there is',
        'rightofcenter': 'right of center',
        'lib': 'liberal',
        'ai':  'artificial intelligence',
        "would n't": 'would not',
        'i \'m': 'i am',
        "do n't": 'do not',
        "that 's": 'that is',
        'y all': 'you all',
        'yall': 'you all',
        "ca n't": 'can not',
        "let 's": 'let us',
        "do n't": 'do not',
        "what 's": 'what is',
        "it 's": 'it is',
        "i 've": 'i have',
        "doin '": 'doing',
        'gon na': 'going to', 
        'are n\'t': 'are not',
        'she d': 'she would',
        'he d': 'he would',
        'does n\'t': 'does not',
        'yup': 'yes',
        'nope': 'no',
        'have n\'t': 'have not',
        'did n\'t': 'did not',
        'could n\'t': 'could not',
        'who\'s said': 'who has said',
        'is n\'t': 'is not',
        'ain\'t': 'is not',
        'should n\'t': 'should not',
        'would n\'t': 'would not',
        'might n\'t': 'might not',
        'must n\'t': 'must not',
        'can \'t': 'can not',
        'won \'t': 'will not', 
    }
    
    for contraction, full_form in contractions.items():
        text = re.sub(r'\b' + contraction + r'\b', full_form, text)
    
    return text

df['self_text'] = df['self_text'].apply(expand_contractions_2)

print(f"Progress point 40")


df['self_text'] = df['self_text'].str.replace(r'\s+', ' ', regex=True).str.strip()

print(f"Progress point 41")

df['self_text'] = df['self_text'].str.replace(' .', '.')
df['self_text'] = df['self_text'].str.replace(' , ', ', ')
df['self_text'] = df['self_text'].str.replace(' wa ', ' was ')
df['self_text'] = df['self_text'].str.replace(' wa,', ' was,')
df['self_text'] = df['self_text'].str.replace('dems ', 'democrats ')
df['self_text'] = df['self_text'].str.replace(" 's", "'s")



print("*"*200)
print(df['self_text'].head(20))
## We save the stuff here

    
df_output_file = fr'C:\Users\Mariana\Documents\Python\csv\Data_1_done.csv'

df.to_csv(df_output_file, encoding='utf-8', index=False)
print(f"Processed {len(df)} rows ({len(df) / df.shape[0] * 100:.2f}% remaining)")
print(f"Combined DataFrame saved to {df_output_file}")

print("Step 1 Done")
