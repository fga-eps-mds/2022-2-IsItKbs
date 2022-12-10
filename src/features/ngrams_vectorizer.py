from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle

with open (".\\data\\interim\\ngrams_features.csv", "r", encoding="utf-8") as file0:
    X = pd.read_csv(file0).squeeze(1)

#Remoção dos valores vazios no dataframe
X.dropna(inplace = True)

vectorizer = TfidfVectorizer(
                            lowercase=True,
                            analyzer='char',
                            binary=True,
                            strip_accents="unicode")

#Os ngramas são propriamente vetorizados para poderem ser alimentados ao algoritmo
X_train = vectorizer.fit_transform(X)

#Exportação dos dados vetorizados como um pickle
with open('.\\data\\processed\\ngrams_vectfeatures.pkl', 'wb') as file:  
    pickle.dump(X_train, file)