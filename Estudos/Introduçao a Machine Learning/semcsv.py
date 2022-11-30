from sklearn.linear_model import LinearRegression
import random

variableSet = []
resultSet = []

nRows = 250
nLimit = 2500

for i in range(0, nRows):
    x = random.randint(0, nLimit)
    y = random.randint(0, nLimit)
    z = random.randint(0, nLimit)
    w = random.randint(0, nLimit)

    function = (5*x) + (7*y) + (10*z) + (3.5*w)
    variableSet.append([x, y, z, w])
    resultSet.append(function)

model = LinearRegression()
model.fit(variableSet, resultSet)

testSet = [[7, 5, 10, 4]] #output = function(7, 5, 10, 4) = 184
prediction = model.predict(testSet)

print('Prediction:'+str(prediction)+' Coefficients:'+str(model.coef_))