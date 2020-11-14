import pandas as pd
#import re
from os import system
# from os.path import isfile, join
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from joblib import dump, load # used for saving and loading sklearn objects
from scipy.sparse import save_npz, load_npz # used for saving and loading sparse matrices
import numpy as np

system("mkdir 'data_preprocessors'")
system("mkdir 'vectorized_data'")

col_list = ["reviewText"]
df_og = pd.read_csv("Cleaned_million.csv", usecols=col_list)

def vectorization(pdCol: np.array):
    """Bigram vectorizer that has a pdDataFram["columnName"].values as input"""

    # Bigram Counts
    bigram_vectorizer = CountVectorizer(ngram_range=(1, 2))
    bigram_vectorizer.fit(pdCol)

    dump(bigram_vectorizer, 'data_preprocessors/bigram_vectorizer.joblib')
    # bigram_vectorizer = load('data_preprocessors/bigram_vectorizer.joblib')

    X_train_bigram = bigram_vectorizer.transform(pdCol)

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

    return(X_train_bigram_tf_idf)

print(vectorization(df_og["reviewText"].values.astype('U')))