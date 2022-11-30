import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

bacterias = pd.read_csv('function.csv')

train = bacterias[bacterias["time"] < 25].copy()
test = bacterias[bacterias["time"] >= 25].copy()

reg = LinearRegression()

predictors = ["time", "temperature"]
target = "bacteria"

reg.fit(train[predictors], train["bacteria"])

predictions = reg.predict(test[predictors])

test["predictions"] = predictions

test["predictions"] = test["predictions"].round()

error = mean_absolute_error(test["bacteria"], test["predictions"])

coisa = bacterias.describe()["bacteria"]

print(error)