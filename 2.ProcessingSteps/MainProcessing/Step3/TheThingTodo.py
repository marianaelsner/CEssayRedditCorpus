import re
import pandas as pd

def check_and_reassign(row):
    if isinstance(row['self_text_corrected'], str) and ' broke ' in row['self_text_corrected'] and ' woke ' in row['self_text_corrected']:
        row['self_text_pos'] = re.sub(r"\('woke', 'VERB'\)", "('woke', 'ADJ')", row['self_text_pos'])
    return row

def check_go_woke(row):
    if isinstance(row['self_text_corrected'], str) and (
        "go woke" in row['self_text_corrected'] or
        "get woke" in row['self_text_corrected'] or
        "went woke" in row['self_text_corrected'] or
        "its woke" in row['self_text_corrected']
      
    ):
        row['self_text_pos'] = re.sub(r"\('woke', 'VERB'\)", "('woke', 'NOUN')", row['self_text_pos'])
    return row


def reassign_pos(row):
    try:
        # Ensure pos_word_tuples is a list of tuples
        pos_word_tuples = ast.literal_eval(row['pos_word_tuples']) if isinstance(row['pos_word_tuples'], str) else row['pos_word_tuples']
        
        # Skip if pos_word_tuples is not a list or is empty
        if not isinstance(pos_word_tuples, list) or len(pos_word_tuples) < 3:
            return pos_word_tuples
        
        # Iterate through the list of tuples to find the specific structure
        for i in range(len(pos_word_tuples)):
            if i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PROPN' and
                pos_word_tuples[i + 1] == ('woke', 'SCONJ') and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
            # Replace ('woke', 'ADJ') with ('woke', 'NOUN') in the specific structure
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
                
 
        # second structure: ('x', 'PROPN'), ('woke', 'VERB')
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PROPN' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') 
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # third structure
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PROPN' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # fourth structure    
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'AUX' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') 
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # fifth structure    
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'NOUN' and
                pos_word_tuples[i + 1] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')   

        # sixth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'CCONJ'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # seventh structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'PRON' and
                pos_word_tuples[i + 2] == ('woke', 'VERB')
            
            ):  
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
         
        # eighth structure   
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] ==  ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'PRON' and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
         
        # ninth structure   
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'ADJ' and
                pos_word_tuples[i + 2][1] == 'CCONJ'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # tenth structure    
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'PROPN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # eleventh structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADJ' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # twelfth structure    
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'PROPN' 
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # thirteenth structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'VERB' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # fourteenth structure  
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # fifteenth structure  
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'PART' and
                pos_word_tuples[i + 2] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
        
        # sixteenth structure   
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'CCONJ' and
                pos_word_tuples[i + 1] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # seventeenth structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'NOUN' and
                pos_word_tuples[i + 2][1] == 'VERB'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
            
        # eighteenth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'NOUN' and
                pos_word_tuples[i + 2][1] == 'ADJ'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
            
        # nineteenth structure
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'NOUN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # twentieth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'NOUN' and
                pos_word_tuples[i + 2] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
            
        # twenty-first structure
            elif i + 3 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'NOUN' and	
                pos_word_tuples[i + 2][1] == 'VERB' and
                pos_word_tuples[i + 3] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 3] = ('woke', 'ADJ')
        
        # twenty-second structure   
            elif i + 3 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'CCONJ' and
                pos_word_tuples[i + 2] == ('woke', 'VERB') and
                pos_word_tuples[i + 3][1] == 'PRON'
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
        
        # twenty-third structure   
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'ADJ' and
                pos_word_tuples[i + 2][1] == 'ADJ'         
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
            
        # twenty-fourth structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'VERB' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'ADV'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # twenty-fifth structure   
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1] == ('consider', 'VERB') and
                pos_word_tuples[i + 2] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
        
        # twenty-sixth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADJ' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'ADJ'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # twenty-seventh structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1][1] == 'NOUN' and
                pos_word_tuples[i + 2] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
            
        # twenty-eighth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADJ' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
        # twenty-ninth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'CCONJ' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'ADJ'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # thirtieth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'VERB' and
                pos_word_tuples[i + 1] == ('woke', 'VERB') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
        # thirty-first structure
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'NOUN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # thirty-second structure
            elif i + 3 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1][1] == 'ADJ' and
                pos_word_tuples[i + 2] == ('woke', 'VERB') and
                pos_word_tuples[i + 3][1] == 'NOUN'
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
            
        # thirty-third structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'ADJ' and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
            
        # thirty-fourth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'VERB') and
                pos_word_tuples[i + 1][1] == 'ADJ' and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # thirty-fifth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'NUM' and
                pos_word_tuples[i + 1] == ('woke', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
        # thirty-sixth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADV' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
        # thirty-seventh structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADJ' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
         ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
            
        # thirty-eighth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # thirty-ninth structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'PROPN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # fortieth structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PRON' and
                pos_word_tuples[i + 1][1] == 'AUX' and
                pos_word_tuples[i + 2] == ('woke', 'NOUN')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
        
        # forty-first structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'SCONJ' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # forty-second structure    
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'PART' and
                pos_word_tuples[i + 1][1] == 'AUX' and
                pos_word_tuples[i + 2] == ('woke', 'NOUN')
            ):
                pos_word_tuples[i + 2] = ('woke', 'ADJ')
        
        # forty-third structure
            elif i + 3 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'AUX' and
                pos_word_tuples[i + 1][1] == 'PRON' and
                pos_word_tuples[i + 2][1] == 'ADV' and
                pos_word_tuples[i + 3] == ('woke', 'NOUN')
            ):
                pos_word_tuples[i + 3] = ('woke', 'ADJ')
        
        # forty-fourth structure    
            elif i + 1 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'NOUN') and
                pos_word_tuples[i + 1][1] == 'NOUN'
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
        
        # forty-fifth structure
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'ADP' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'NOUN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # forty-sixth structure
            elif i + 3 < len(pos_word_tuples) and (
                pos_word_tuples[i][1] == 'DET' and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2][1] == 'ADJ' and
                pos_word_tuples[i + 3][1] == 'PROPN'
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        # forty-seventh structure  
            elif i < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('woke', 'X')
            ):
                pos_word_tuples[i] = ('woke', 'ADJ')
                
            elif i + 2 < len(pos_word_tuples) and (
                pos_word_tuples[i] == ('the','DET') and
                pos_word_tuples[i + 1] == ('woke', 'NOUN') and
                pos_word_tuples[i + 2] == ('left', 'VERB')
            ):
                pos_word_tuples[i + 1] = ('woke', 'ADJ')
        
        return pos_word_tuples
    except Exception as e:
        print(f"Error processing row: {row}")
        print(e)
    return row['pos_word_tuples']


def DOThis(df)->pd.DataFrame:
    df = df.apply(check_and_reassign, axis=1)
    df = df.apply(check_go_woke, axis=1)
    df['self_text_pos'] = df.apply(reassign_pos, axis=1)
    return df
