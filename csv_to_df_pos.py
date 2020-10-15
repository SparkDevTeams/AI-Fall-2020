import pandas as pd 
import json
from io import StringIO
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth', 5000)
#import stanza 

#THE CHUNK BELOW IS ONLY IF YOU NEED TO MAKE A NEW CSV FILE IF YOU WANT TO CHANGE SIZE

    # with open('directory of OG json') as f:  #change to file directory for the json file
    #     chunks = pd.read_json(f, lines=True, chunksize=100000)
    #     x=0
    #     # while x<10:    
    #     for c in chunks:
    #         data = c.to_csv('Export1.csv',index = False)
    #         break
    #             #x+=1 

col_list = ["reviewText"]   #specify which columns you want to load into the dataframe from csv
df = pd.read_csv("Export1.csv", usecols=col_list) 

# nlp = stanza.Pipeline(lang='en', processors='tokenize', 'mwt', 'pos')   #USE WHEN STANZA FINALLY IMPORTS

stanza.download('en')
stanza_nlp = stanza.Pipeline('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize, mwt, pos')   
##

def pos_tag(review): 
    doc = nlp(review)  #function directly from stanza POS tag 
    print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
       


pos_tag(df.to_string(columns=col_list, index=False,header=False,max_rows=5))   #still need to figure out how to store the output from this function 

