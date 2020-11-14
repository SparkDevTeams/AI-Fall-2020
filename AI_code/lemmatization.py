import spacy, csv, io


# Initialize spacy 'en' model, keeping only tagger component needed for lemmatization
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# Input and output CSV files
IN_FILE_NAME = "Export1.csv"
OUT_FILE_NAME = "Lemma.csv"


def lemmatize(sentence: str):
    """Takes a string as an input and outputs the lemmatized version of that string"""
    # Parse the sentence using the loaded 'en' model object `nlp`
    doc = nlp(sentence)

    # Extract the lemma for each token and join
    end = " ".join([token.lemma_ if token.lemma_ != '-PRON-' else token.lower_ for token in doc])
    return end


def lemma(IN_FILE_NAME:str, OUT_FILE_NAME:str):
    """Takes input and output files to modify the reviewText column"""
    with open(IN_FILE_NAME, newline='') as csvfile, open(OUT_FILE_NAME, 'w', newline='') as out_csv:
        reader = csv.DictReader(csvfile)
        csv_writer = csv.DictWriter(out_csv, fieldnames=reader.fieldnames)
        csv_writer.writeheader()
        for row in reader:
            row['reviewText'] = lemmatize(row['reviewText'])
            csv_writer.writerow(row)

# lemma(IN_FILE_NAME, OUT_FILE_NAME)
