import spacy, csv, io


# Initialize spacy 'en' model, keeping only tagger component
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])


all_stopwords = nlp.Defaults.stop_words


# Input and output CSV files
IN_FILE_NAME = "Export.csv"
OUT_FILE_NAME = "Stop.csv"


def stopwordRemover(sentence: str):
    """Takes a string as an input and outputs the string without stopwords"""
    # Parse the sentence using the loaded 'en' model object `nlp`
    doc = nlp(sentence)

    # Join words that aren't stopwords
    end = " ".join([token.text for token in doc if not token.lower_ in all_stopwords])
    return end
  

def stopwords(IN_FILE_NAME:str, OUT_FILE_NAME:str):
    """Takes input and output files to modify the reviewText column"""
    with open(IN_FILE_NAME, newline='') as csvfile, open(OUT_FILE_NAME, 'w', newline='') as out_csv:
        reader = csv.DictReader(csvfile)
        csv_writer = csv.DictWriter(out_csv, fieldnames=reader.fieldnames)
        csv_writer.writeheader()
        for row in reader:
            row['reviewText'] = stopwordRemover(row['reviewText'])
            csv_writer.writerow(row)

# stopwords(IN_FILE_NAME, OUT_FILE_NAME)