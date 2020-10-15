import stanza, re, csv, io
import pandas as pd
from stanza.pipeline.processor import Processor, register_processor
import spacy
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


IN_FILE_NAME = "Export1.csv"
OUT_FILE_NAME = "Lemma.csv"

@register_processor("extrastem")
class ExtraStemming(Processor):
    ''' An extra lemmatizer for useful algorithms we find. Removes apostrophes for now. '''
    
    _requires = set(['tokenize', 'mwt', 'pos', 'lemma'])
    _provides = set(['extrastem'])

    def __init__(self, config, pipeline, use_gpu):
        pass

    def _set_up_model(self, *args):
        pass

    def process(self, document):
        ps = WordNetLemmatizer()
        APOSTROPHE = ["'s","’s"] 
        for sentence in document.sentences:
            for word in sentence.words:
                if word.text in APOSTROPHE:
                    word.lemma = None
                elif word.upos == "ADV": word.lemma = ps.lemmatize(word.lemma, pos = 'r')
                elif word.upos == "VERB": word.lemma = ps.lemmatize(word.lemma, pos = 'v')
                elif word.upos == "ADJ": word.lemma = ps.lemmatize(word.lemma, pos = 'a')

        return document


sentence = "The diminutive county treats into the undesirable flight. It was then the shivering spend met the wobbly pen."


# SpaCy model
# # Initialize spacy 'en' model, keeping only tagger component needed for lemmatization
# nlp = spacy.load('en', disable=['parser', 'ner'])

# # Parse the sentence using the loaded 'en' model object `nlp`
# doc = nlp(sentence)

# # Extract the lemma for each token and join
# end = " ".join([token.lemma_ if token.lemma_ != '-PRON-' else token.lower_ for token in doc])
# print(end)


nlp = stanza.Pipeline('en', processors = 'tokenize, mwt, pos, lemma, extrastem')
# doc = nlp(sentence)
# lemmatized = ''
# for sent in doc.sentences:
#     for word in sent.words:
#         if word.lemma != None:
#             lemmatized = lemmatized + word.lemma + ' '
# print(lemmatized)

with open(IN_FILE_NAME, newline='') as csvfile, open(OUT_FILE_NAME, 'w', newline='') as out_csv:
    reader = csv.DictReader(csvfile)
    csv_writer = csv.DictWriter(out_csv, fieldnames=reader.fieldnames)
    csv_writer.writeheader()
    # x = 0
    for row in reader:
        doc = nlp(row['reviewText'])
        lemmatized = ''
        for sent in doc.sentences:
            for word in sent.words:
                if word.lemma != None:
                    lemmatized = lemmatized + word.lemma + ' '
        row['reviewText'] = lemmatized
        csv_writer.writerow(row)
        # x = x+1
        # print(x)
