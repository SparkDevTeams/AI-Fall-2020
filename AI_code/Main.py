import spacy, csv, io
import pandas as pd 
import json
import string
from io import StringIO
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth', 5000)
import stanza 


# Initialize spacy 'en' model, keeping only tagger component
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
all_stopwords = nlp.Defaults.stop_words

col_list = ["reviewText"]
df_og = pd.read_csv("Export1.csv", usecols=col_list)
# Input and output CSV files
IN_FILE_NAME = "Export1.csv"
OUT_FILE_NAME = "Stop.csv"

# print("Before Edits")
# print(df_og.to_string(columns=col_list, index=False,header=False,max_rows=5))


def stopwordRemover(column): 
    """Takes a string as an input and outputs the string without stopwords"""
    # Parse the sentence using the loaded 'en' model object `nlp`  
   # """Takes a string as an input and outputs the string without stopwords"""

    # Join words that aren't stopwords
    new_words = []
    for row in column:
        new_words.append(" ".join([word for word in (str(row).split()) if word.lower() not in all_stopwords]))
    return new_words
   
    
    

###################
# Removing Punctuation
exclude = set(string.punctuation)

def removePunctuation(sentence):
   for ele in sentence:
      if (ele in exclude):
         sentence = sentence.replace(ele, " ")
   return sentence

# reviews_cleaned = df_og.copy()

test = "The game itself worked!! great but the story line videos would never play, the sound was fine but the picture!! would freeze and go black every time."
test = removePunctuation(test)
print(test)




#print("Before: ", df_og['reviewText'].head(10))

df_og['reviewText'] = df_og['reviewText'].str.replace(r'\d+', '')  #removing digits 

df_og['reviewText'] = stopwordRemover(df_og["reviewText"].values)
df_og['reviewText'] = df_og['reviewText'].str.replace('[^\w\s]','')
#df_og['reviewText'] = removePunctuation(df_og["reviewText"].values)

print(df_og.head(10))

df_og.to_csv("Cleanedre.csv")

#df_og['reviewText'] = stopwordRemover(df_og["reviewText"].head(10))
#print(df_og['reviewText'].to_numpy(dtype=str))

#print("Stopwords")

#print(stopwordRemover(df_og.to_string(columns=col_list, index=False,header=False,max_rows=10)))

#print("After:", df_og['reviewText'].head(10))

# print(testRemove(test))
# print(stopwordRemover(test))
# #Punctuation remove
# print("Remove Punctuation")
# testRemove(df_og.to_string(columns=col_list, index=False,header=False,max_rows=5))




# #Remove Digits

# stopwordRemover(df_og.to_string(columns=col_list, index=False,header=False,max_rows=5))

# print(df_og.to_string(columns=col_list, index=False,header=False,max_rows=5))

