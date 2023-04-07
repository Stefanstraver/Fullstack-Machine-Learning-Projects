# importeren afhankelijkheden
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from textblob import Word
from textblob import TextBlob

# definieer de get reviews functie
def get_reviews():
    links = [f'https://www.yelp.com/biz/mcdonalds-los-angeles-106?start={10+x*10}' for x in range(12)]
    links.insert(0, 'https://www.yelp.com/biz/mcdonalds-los-angeles-106')
    regex = re.compile('raw__')

    reviews = []
    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all('span', {'lang':'en'}, class_=regex)
        reviews = [*reviews, *[result.text for result in results]]
    reviews    

def preprocess(reviews):
    df = pd.DataFrame(np.array(reviews), columns=['review'])
    stop_words = stopwords.words('english')

    # lowercase
    df['review_lower'] = df['review'].apply(lambda x: " ".join(x. lower() for x in x.split()))
    # verwijder punction
    df['review_nopunc'] = df['review_lower'].str.replace('[^\w\s]','')
    # verwijder stopwords
    df['review_nostop'] = df['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
    # custom stopwords
    other_stopwords = ['one', 'get', 'go', 'im', '2', 'ive', 'thru', 'tell', 'says', 'two']
    # Andere stopwoorden eruit
    df['review_no_other'] = df['review_nostop'].apply(lambda x: " ".join(x for x in x.split() if x not in other_stopwords))
    # lemmatize de dataset
    df['cleaned_review'] = df['review_no_other'].apply(lambda x: " ".join(Word(word).lemmatize() for word in x.split()))
    # return df
    return df

# Bereken sentiment
def calculate_sentiment(df):
    # sentiment analysere van textblob gebruiken voor polarity en subjectivity
    df['polarity'] = df['cleaned_review'].apply(lambda x: TextBlob(x).sentiment[0])
    df['subjectivity'] = df['cleaned_review'].apply(lambda x: TextBlob(x).sentiment[1])
    # return df
    return df

if __name__ == "__main__":
    reviews = get_reviews()
    df = preprocess(reviews)
    sentiment_df = calculate_sentiment(df)
    sentiment_df.to_csv('results.csv')