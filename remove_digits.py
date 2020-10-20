import csv
import pandas as pd
import string

review = pd.read_csv('/Users/alonzofamily5/Desktop/AI-Fall-2020-Dev/Export1.csv')
#csv_f = csv.reader(review)

review['reviewText'] = review['reviewText'].str.replace(r'\d+', '')
print(review['reviewText'].head(48))

