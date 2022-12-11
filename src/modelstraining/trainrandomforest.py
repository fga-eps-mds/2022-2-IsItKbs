from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

#Leitura das features
with open (".\\data\\processed\\ngrams_vectfeatures.pkl", "rb") as file0:
    X = pickle.load(file0)

#Leitura dos targets
with open (".\\data\\processed\\ngrams_target.csv", "rb") as file1:
    Y = pd.read_csv(file1, keep_default_na=False).squeeze(1)

#Leitura do vetorizador que foi usado nas features
with open (".\\models\\tfid_vectorizer.pkl", "rb") as file2:
    vectorizer = pickle.load(file2)

#Instanciação do modelo
model = RandomForestClassifier()
model.fit(X,Y)

#Compressão do modelo para um pickle
with open (".\\models\\randomforest.pkl", "wb") as file3:
    pickle.dump(model, file3)