import csv
import pandas as pd
import string

review = pd.read_csv("C:/Users/mpink/OneDrive/Desktop/ai_fall2020/AI-Fall-2020/export1.csv")
#print(review.head(48))

exclude = set(string.punctuation)

def testRemove(sentence):
   for ele in sentence:
      if (ele in exclude):
         sentence = sentence.replace(ele, "")
   return sentence

# s = "hello. world!"
# xe = testRemove(s)
# print("Original String: ",s)
# print("Renewed String: ")
# print(xe)

#  def remove_punctuation(x):
#      testRemove(x)#
#      x = ''.join(ch for ch in x if ch not in exclude)
#      return x
# # Apply the function to the DataFrame

#review["reviewText"] = review["reviewText"].astype("|S")
actualReview = review["reviewText"]
#print(actualReview.head(48))

#review.reviewText = review.reviewText.apply(remove_punctuation)

#

for index, value in actualReview.items():
   #print(f"Index : {index}, Review : {value}")
   value = str(value)
   value = testRemove(value)
   print(value)


#print(actualReview.head(48))

#actualReview["reviewText"] = review['reviewText'].str.replace('[^\w\s]','')
#print(actualReview.head())

#checks
#print(review.dtypes)
#print(review.head(10))