import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files 

test_files = load_files("data/raw/corpora/reuters", categories=["test", "training"], encoding="utf-8", decode_error="ignore")

bigrams = TfidfVectorizer(ngram_range=(2, 2),
                            lowercase=True,
                            analyzer='char_wb',
                            strip_accents="unicode")

bigram_v = bigrams.fit_transform(test_files.data)
bigram_v

with open('data/processed/reuters.pkl', 'wb') as f:
    pickle.dump(bigram_v, f)