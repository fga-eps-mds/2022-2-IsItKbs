import pandas as pd
from nltk import everygrams

with open (".\\data\\interim\\naturals.csv", "r", encoding="utf-8") as file0:
    X0 = pd.read_csv(file0, keep_default_na=False).squeeze(1)

with open (".\\data\\interim\\mashings.csv", "r", encoding="utf-8") as file1:
    X1 = pd.read_csv(file1, keep_default_na=False).squeeze(1)

#Percorre as palavras naturais e transforma em ngramas
natbigrams = []
for row in range (len(X0)):
    ngram = map(''.join,list(everygrams(X0.iloc[row], 2, 4)))
    natbigrams.extend(ngram)

#Percorre os mashings e transforma em ngramas
mashbigrams = []
for row in range (len(X1)):
    ngram = map(''.join,list(everygrams(X1.iloc[row], 2, 4)))
    mashbigrams.extend(ngram)

# #Diminui os dados de mashing para ficarem no mesmo tamanho que os de linguagem natural 
mashbigrams = mashbigrams[:len(natbigrams)]

#Cria um novo df somente com ngramas e separa as features (X) e os targets (Y)
mashdf = pd.DataFrame({'strings':mashbigrams + natbigrams, 'mashing': [1] * len(mashbigrams) + [0] * len(natbigrams)})
X = mashdf['strings']
Y = mashdf['mashing']
X.to_csv(".\\data\\interim\\ngrams_features.csv", index = False)
Y.to_csv(".\\data\\processed\\ngrams_target.csv", index = False)