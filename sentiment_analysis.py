import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import re
import string

nlp = spacy.load('en_core_web_lg')
nlp.add_pipe('spacytextblob')

df = pd.read_csv('amazon_product_reviews.csv', delimiter=',', low_memory=False)

""" 
    Assigns the data set for processing and removes the rows that contains NULL values 
"""
reviews_dataset = df['reviews.text'].dropna()

review1_index = 100
review2_index = 300 

print("\n\t\t\t Sentiment Analysis Report")
print("\t\t\t -------------------------- \n")

def review_sentiment(cleaned_reviews): 
    doc = nlp(cleaned_reviews)
    """
    prints the strength of sentiment based on polarity score
    """
    if doc._.blob.polarity > 0.0:
        print ("\nPositive Sentiment\n")
    elif doc._.blob.polarity == 0.0:
        print ("\nNeutral\n")
    else:
        print ("\nNegative Sentiment\n")
    print(doc._.blob.sentiment)
    

clean_txt = ""
doc_remove_punctuation = ""

for i in reviews_dataset:
    """ 
    Pre-processing the dataset icluding removing punctuation, removing numbers and removing stop words
    """
    doc_lower = i.lower()
    doc_remove_line_break = re.sub(r'\n', '', doc_lower)
    translator = str.maketrans('', '', string.punctuation)
    doc_remove_punctuation = doc_lower.translate(translator)
    doc_remove_number = [re.sub(r'\d+', '', doc_remove_punctuation)]
    doc_remove_number = " ".join([token for token in doc_remove_number])
    filtered_tokens = [token for token in nlp(doc_remove_number) if not token.is_stop]
    clean_txt += " ".join([token.text for token in filtered_tokens])

print(review_sentiment(f"\n {clean_txt}"))

doc1 = nlp(reviews_dataset[review1_index])
doc2 = nlp(reviews_dataset[review2_index])

"""
Calculates the similarity score and prints relevant message 
"""
similarity_score = doc1.similarity(doc2)

if similarity_score > 0.5:
    print(f"\nReviews from {review1_index}th and {review2_index}th record looks similar \n")
else:
    print(f"\nReviews from {review1_index}th and {review2_index}th record looks dissimilar \n")


