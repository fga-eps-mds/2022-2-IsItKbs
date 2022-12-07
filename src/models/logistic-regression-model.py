from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
## Reading files:

dataset = pd.read_pickle("data/processed/database.pkl")
dataY = pd.read_pickle("data/processed/dataY.pkl")

## Splitting into training and testing data:
reshaped_dataset = dataset

bigram_vectorizer = CountVectorizer(ngram_range=(2, 2),
                            lowercase=True,
                            analyzer='char',
                            strip_accents="unicode")
bigram_vectorizer.fit(reshaped_dataset)
X = bigram_vectorizer.transform(reshaped_dataset)


X_train, X_test, Y_train, Y_test = train_test_split(X, dataY, test_size=0.3, stratify=dataY, random_state=12)

## Training the model:

model = BernoulliNB(binarize = True)
model.fit(X_train, Y_train)
print(model)

##  Accuracy score:

from sklearn.metrics import accuracy_score

Y_pred = model.predict(X_test)

acc = accuracy_score(Y_test, Y_pred) ##0.97
print('Acc:', acc)

## Evaluating the model with new metrics

from sklearn.metrics import balanced_accuracy_score

score1 = balanced_accuracy_score(Y_test, Y_pred)

print('Acc:', score1)

from sklearn.metrics import f1_score

score2 = f1_score(Y_test, Y_pred, labels=None, pos_label='0', average='binary', sample_weight=None, zero_division='warn')

print('Acc:', score2)

from sklearn.metrics import recall_score

score3 = recall_score(Y_test, Y_pred, labels=None, pos_label='0', average='binary', sample_weight=None, zero_division='warn')

print('Acc:', score3)

## Compressing Model

import pickle

pickle.dump(model, open("models/bernoulli.sav", 'wb'))

