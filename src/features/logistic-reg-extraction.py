from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np
import pandas as pd

txt = ""
with open("data/raw/mashing.txt", "r", encoding="utf-8") as g:
    txt = g.read()

sentences = txt.split("\n")
for i in range(len(sentences)):
    sentences[i] = sentences[i].strip()

sentences = [x for x in sentences if x != ""]

with open('data/raw/data2.pkl', "wb") as h:
    pickle.dump(sentences, h)

data2 = pd.read_pickle("data/raw/data2.pkl")

bigram_vectorizer = TfidfVectorizer(ngram_range=(2, 2),
                            lowercase=True,
                            analyzer='char_wb',
                            strip_accents="unicode")

categories = ['sci.med', 'sci.space', 'talk.politics.misc', 'sci.electronics']

news_train = datasets.fetch_20newsgroups(data_home = "data/raw", subset = 'train', categories=categories)

with open('data/raw/newsgroup.pkl', 'wb') as f:
    pickle.dump(news_train.data, f)

news = pd.read_pickle("data/raw/newsgroup.pkl")
dataY = np.array(['1']*len(data2) + ['0']*len(news))

dataset = np.array(data2 + news)

bigram_vectorizer.fit(dataset)
X = bigram_vectorizer.transform(dataset)


with open('data/processed/database.pkl', 'wb') as f:  
    pickle.dump(X, f)


with open('data/processed/dataY.pkl', "wb") as d:
    pickle.dump(dataY, d)