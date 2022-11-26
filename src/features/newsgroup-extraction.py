from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

news_train = datasets.fetch_20newsgroups(data_home = "data/raw", subset = "all", shuffle = True, remove = ("headers", "footers", "quotes"))

bigram_vectorizer = TfidfVectorizer(ngram_range=(2, 2),
                            lowercase=True,
                            analyzer='char_wb')

bigrams_vectors = bigram_vectorizer.fit_transform(news_train.data)
bigrams_vectors.shape

with open('data/processed/newsgroup.pkl', 'wb') as f:  
    pickle.dump(bigrams_vectors, f)

    