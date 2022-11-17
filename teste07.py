import pandas as pd
# Aqui você deve especificar o caminho em que o .csv está na sua máquina
vinhos = pd.read_csv("wine_dataset.csv")
vinhos.head()
vinhos['style'] = vinhos['style'].replace('red', 0)
vinhos['style'] = vinhos['style'].replace('white', 1)
vinhos.head()
y = vinhos['style']
# A função drop do pandas remove linhas ou colunas de um dataframe com a especificação do nome e do eixo a ser removido (0 para linhas e 1 para colunas). Nesse caso
# removemos  a coluna "Styles" do dataframe
x = vinhos.drop('style', axis = 1)
x.head()
y.head()
from sklearn.model_selection import train_test_split
# A train_test_split separa, de forma aleatória, nossos dataframes em teste e treino, nesse caso especificamos que 30% do dataframe original ficará para teste
# e o resto para treino do algoritmo
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
print(f"Dimensões do dataframe original: {vinhos.shape}\n" + 
     f"Dimensões das features de treino: {x_treino.shape}\n" +
     f"Dimensões das features de teste: {x_teste.shape}\n" +
     f"Dimensões do target de treino: {y_treino.shape}\n" +
     f"Dimensões do target de teste: {y_teste.shape}\n")
# Uso do algoritmo Classifier pois o problema é de classificação, isto é, o objetivo é classificar o vinho entre tinto ou branco
from sklearn import tree
# Chamada da função do algoritmo
arvore = tree.DecisionTreeClassifier()
# O método fit é usado para passar ao algoritmo nossas features e target
arvore.fit(x_treino, y_treino)
# O método score mostra a acurácia de acerto do modelo
resultado = arvore.score(x_teste, y_teste)
print(f"Acurácia = {resultado}\n")
# Selecão aleatoria de uma amostra de 10 linhas do target de teste
y_teste.iloc[74:84]
# Dadas apenas as 12 features iniciais colocamos o algoritmo para prever qual será o respectivo valor target para cada linha
previsao = arvore.predict(x_teste[74:84])
print(previsao)     