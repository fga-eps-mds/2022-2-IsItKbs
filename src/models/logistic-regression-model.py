from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

## Reading files:

dataset = pd.read_pickle("data/processed/database.pkl")
dataY = pd.read_pickle("data/processed/dataY.pkl")

## Splitting into training and testing data:

X_train, X_test, Y_train, Y_test = train_test_split(dataset, dataY, test_size=0.3, stratify=dataY, random_state=777)

## Training the model:

model = LogisticRegression()
model.fit(X_train, Y_train)

##  Accuracy score:

from sklearn.metrics import accuracy_score

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Acc:', training_data_accuracy)