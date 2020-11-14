import pandas as pd
#import re
from os import system
# from os.path import isfile, join
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from joblib import dump, load # used for saving and loading sklearn objects
from scipy.sparse import save_npz, load_npz # used for saving and loading sparse matrices
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from scipy.sparse import csr_matrix
import numpy as np


system("mkdir 'data_preprocessors'")
system("mkdir 'vectorized_data'")

col_list = ["overall", "reviewText"]
df_og = pd.read_csv("Cleaned_million1.csv", usecols=col_list)

def vectorization():
    """Bigram vectorizer that has a pdDataFram["columnName"].values as input"""

    # Bigram Counts
    bigram_vectorizer = CountVectorizer(ngram_range=(1, 2))
    bigram_vectorizer.fit(df_og["reviewText"].values.astype('U'))

    dump(bigram_vectorizer, 'data_preprocessors/bigram_vectorizer.joblib')
    # bigram_vectorizer = load('data_preprocessors/bigram_vectorizer.joblib')

    X_train_bigram = bigram_vectorizer.transform(df_og["reviewText"].values.astype('U'))

    save_npz('vectorized_data/X_train_bigram.npz', X_train_bigram)
    # X_train_bigram = load_npz('vectorized_data/X_train_bigram.npz')


    # Bigram Tf-Idf
    bigram_tf_idf_transformer = TfidfTransformer()
    bigram_tf_idf_transformer.fit(X_train_bigram)

    dump(bigram_tf_idf_transformer, 'data_preprocessors/bigram_tf_idf_transformer.joblib')
    # bigram_tf_idf_transformer = load('data_preprocessors/bigram_tf_idf_transformer.joblib')

    X_train_bigram_tf_idf = bigram_tf_idf_transformer.transform(X_train_bigram)
    save_npz('vectorized_data/X_train_bigram_tf_idf.npz', X_train_bigram_tf_idf)
    # X_train_bigram_tf_idf = load_npz('vectorized_data/X_train_bigram_tf_idf.npz')

#vectorization()

def train_and_show_scores(X: csr_matrix, y: np.array, title: str) -> None:
        X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, train_size=0.75, stratify=y
    )

        clf = SGDClassifier()
        clf.fit(X_train, y_train)
        train_score = clf.score(X_train, y_train)
        valid_score = clf.score(X_valid, y_valid)
        print(f'{title}\nTrain score: {round(train_score, 2)} ; Validation score: {round(valid_score, 2)}\n')


X_train_bigram_tf_idf = load_npz('vectorized_data/X_train_bigram_tf_idf.npz')
y_train = df_og["overall"].values
y_train[y_train <= 2] = 0
y_train[y_train >= 3] = 1

train_and_show_scores(X_train_bigram_tf_idf, y_train, "Bigram TFIDF")