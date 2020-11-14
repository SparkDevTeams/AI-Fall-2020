import spacy, csv, io
import pandas as pd


# Initialize spacy 'en' model, keeping only tagger component
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])


all_stopwords = nlp.Defaults.stop_words


# Input and output CSV files
IN_FILE_NAME = "Export1.csv"
OUT_FILE_NAME = "Stop.csv"

col_list = ["reviewText", "overall"]
df = pd.read_csv(IN_FILE_NAME, usecols=col_list)


def stopwordRemover(column):
    """Takes a string as an input and outputs the string without stopwords"""

    # Join words that aren't stopwords
    new_words = []
    for row in column:
        new_words.append(" ".join([word for word in (str(row).split()) if word.lower() not in all_stopwords]))
    return new_words
   

df["reviewText"] = stopwordRemover(df["reviewText"].values)
print(df.head(10))
