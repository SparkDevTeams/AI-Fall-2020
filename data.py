import pandas as pd 
import json
from io import StringIO
pd.set_option('display.max_rows',None)
#import stanza 

# df = pd.read_json(StringIO("Video_Games.json"), lines=True)
# print(pd)

#THE CHUNK BELOW IS ONLY IF YOU NEED TO MAKE A NEW CSV FILE 

    # with open('/Users/franM/projects/sparkdev_AI/AI-Fall-2020/Video_Games.json') as f:  #change to file directory for the json file
    #     chunks = pd.read_json(f, lines=True, chunksize=100000)
    #     x=0
    #     # while x<10:    
    #     for c in chunks:
    #         data = c.to_csv('Export1.csv',index = False)
    #         break
    #             #x+=1 

# df = pd.read_json(StringIO("Video_Games.json"), lines=True)
# print(pd)      

# df = pd.DataFrame(columns="reviewText")
df = pd.read_csv("Export1.csv")
df_pretty = pd.DataFrame(df, columns = ["reviewText","overall"])
# print(df_pretty)

 


# nlp = stanza.Pipeline(lang='en', processors='tokenize', 'mwt', 'pos')   #USE WHEN STANZA FINALLY IMPORTS

def pos_tag(review): 
    #  doc = nlp(review)
    #  print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
    print(review)

# df_pretty['reviewText'].map(pos_tag)
pos_tag(df_pretty['reviewText'])                #two ways of running the function on the review, have to figure out which is faster

#vectorize and manipulate text

