from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np
import pandas as pd

## Reading and filtering data:

txt = ""
with open("data/raw/mashing.txt", "r", encoding="utf-8") as g:
    txt = g.read()

sentences = txt.split("\n")
for i in range(len(sentences)):
    sentences[i] = sentences[i].strip()

sentences = [x for x in sentences if x != ""]

texto = ""
with open("data/raw/large-2014.txt", "r", encoding="utf-8") as k:
    texto = k.read()
    
texto = texto.replace("?",".")
texto = texto.replace("!",".")
texto = texto.replace("»","")
texto = texto.replace("«","")
texto = texto.replace(":","")
texto = texto.replace(";","")
texto = texto.replace("...",".")
texto = texto.replace("…",".")
texto = texto.replace("\n",".")
texto = texto.replace("  "," ")
texto = texto.replace("—", "")
texto = texto.replace("\"","")
texto = texto.replace("„","")
texto = texto.replace("eKGWB", "")
texto = texto.replace("Studia Nietzscheana (2014), www.nietzschesource.org/SN/large-2014.","")
sentencas = texto.split(" ")
for i in range(len(sentencas)):
    sentencas[i] = sentencas[i].strip()
      
sentencas = [x for x in sentencas if x != ""]

## Splitting into training and testing data:

X = np.array(sentences + sentencas)
Y = np.array(['Y']*len(sentences) + ['N']*len(sentencas))
df = pd.DataFrame({'sentence':X,'mashing':Y})
df.to_csv("data/processed/dataframe.csv")  ##saving the filtered data as csv

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=2)

## Training the model:

from sklearn.linear_model import LogisticRegression

vectorizer = TfidfVectorizer(ngram_range=(1, 4),
                            lowercase=True,
                            analyzer='char', binary=True,
                            strip_accents="unicode")
vectorizer.fit(X_train)
model = LogisticRegression()

model.fit(vectorizer.transform(X_train),Y_train)

from sklearn.metrics import confusion_matrix, accuracy_score

Y_pred = model.predict(vectorizer.transform(X_test))

confusion_matrix(Y_test, Y_pred)

##  Accuracy score:

from sklearn.metrics import accuracy_score

Y_pred = model.predict(X_test)

acc = accuracy_score(Y_test, Y_pred) ##0.985
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

pickle.dump(model, open("models/logistic-reg.sav", 'wb'))

## Input in case you want to test it:
#input_data = [(input(""))]
#pred = model.predict(vectorizer.transform([x[0] for x in input_data]))
#print(pred)

print('Acc:', training_data_accuracy)

## Compressing Model

import pickle

pickle.dump(model, open("models/logistic-reg.pkl", 'wb'))


