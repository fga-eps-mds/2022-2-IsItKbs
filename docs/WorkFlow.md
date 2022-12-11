# WorkFlow

**Workflows — também chamados de fluxos de trabalho — são a maneira como as pessoas realizam o trabalho e podem ser ilustradas como uma série de etapas que precisam ser concluídas sequencialmente em um diagrama ou lista de verificação.**



<img src="images/WorkFlow.png" width=100%>
<center>Visão geral do WorkFlow de ML</center>



<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [WorkFlow](#workflow)
  - [Coleta de base de dados:](#coleta-de-base-de-dados)
  - [Pré-processamento de dados:](#pré-processamento-de-dados)
  - [Feature Extraction:](#feature-extraction)
  - [Modelo Selecionado:](#modelo-selecionado)
  - [Treinamento do Modelo:](#treinamento-do-modelo)
  - [Avaliação dos Resultados do Modelo:](#avaliação-dos-resultados-do-modelo)
  - [Definição das Funções de KeyBoard Smashing:](#definição-das-funções-de-keyboard-smashing)
  - [Empacotamento:](#empacotamento)

## Coleta de base de dados:
O processo de coleta de dados depende do tipo de projeto que desejamos fazer, se quisermos fazer um projeto de ML que use dados em tempo real, podemos construir um sistema IoT que use dados de sensores diferentes. O conjunto de dados pode ser coletado de várias fontes, como arquivo, banco de dados, sensor e muitas outras fontes.

Em nosso caso utilizamos um conjunto de dados gratuitos que estão presentes na internet no [Kaggle](https://www.kaggle.com/) um dos sites mais visitados que é usado para praticar algoritmos de aprendizado de máquina. Posteriormente, criamos duas bases de dados distintas por conta própria, uma com keyboard smashings e outra como uma coletânea de diversos textos que pegamos na internet.Posteriormente, criamos duas bases de dados distintas por conta própria, uma com keyboard smashings e outra como uma coletânea de diversos textos que pegamos na internet.

## Pré-processamento de dados:
O pré-processamento de dados é um processo de limpeza dos dados brutos, ou seja, os dados são coletados no mundo real e convertidos em um conjunto de dados limpo. Em outras palavras, sempre que os dados são coletados de diferentes fontes, eles são coletados em formato bruto e esses dados não são viáveis ​​para análise.
Portanto, certas etapas são executadas para converter os dados em um pequeno conjunto de dados limpo; essa parte do processo é chamada de pré-processamento de dados.
Para o nosso projeto, foram criados scripts que passam por várias etapas do pré-processamento dos dados, como a remoção de espaços em branco, normalização do texto e remoção de caracteres especiais.

## Feature Extraction:
Essa é, talvez, uma das etapas mais importantes de qualquer projeto de machine learning. A feature engineering envolve, a priori, um processo de pensar quais são os traços mais significativos dos nossos dados para determinar a(s) característica(s) que queremos prever com o nosso algoritmo, durante essa etapa perguntas como “Quais características de uma palavra se interrelacionam para que ela seja considerada um keyboard smashing?” foram muito importantes para o grupo. Após a determinação de quais são essas features, esses dados são passados a um algoritmo vetorizador antes do processo de treinamento começar, de forma que os dados, que podem ser numéricos, textuais ou de imagens, fiquem em um formato que a máquina possa entender durante seu treinamento. No caso do nosso projeto, extraímos como features os bigramas, trigramas e quadrigamas que formam cada palavra, no exemplo da palavra “that” temos os seguintes ngramas: th, ha, at, tha, hat, that. E logo após usamos um vetorizador para transformar essas features textuais em um vetor de valores numéricos, isso foi feito com base na frequência em que um determinado ngrama aparece dentro da nossa base de dados. Dessa maneira, o nosso algoritmo associaria ngramas mais frequentes em keyboard smashing com essa classe de palavras, e ngramas mais comuns na língua inglesa com a classe de palavras comuns.

## Modelo Selecionado:
Na Seleção de um Modelo temos que analisar 3 aspectos antes de aplicarmos os modelos de ML. O primeiro é em relação a estrutura dos dados, que podem ser numéricos, imagens ou texto, e para cada uma dessas estruturas de dados será um tipo abordagem. O segundo é em relação ao paradigma de aprendizado, e aí inclui aprendizado supervisionado e não supervisionado, análise textual ou processamento de imagens. O terceiro aspecto é sobre o tipo de problema, por exemplo, classificação, clusterização, regressão, redução de dimensionalidade, entre outras. Após analisar esses aspectos você pode experimentar os algoritmos, e computar seus resultados. E essa é a forma indicada para se trabalhar com os algoritmos, pois não há uma forma de identificar qual modelo terá melhor desempenho nos seus dados sem essa experimentação.
A equipe optou pelo modelo de Árvore de Decisão, mais especificamente o Random Forest Classifier, um modelo de aprendizado de máquina supervisionado que tem bom desempenho em problemas de classificação textual. 


## Treinamento do Modelo:
Para treinar um modelo, inicialmente dividimos o modelo em 3 três seções que são ' Dados de treinamento ', ' Dados de validação ' e ' Dados de teste '.
Você treina o classificador usando ' conjunto de dados de treinamento ', ajusta os parâmetros usando ' conjunto de validação ' e então testa o desempenho de seu classificador em ' conjunto de dados de teste ' não visto . **Um ponto importante a ser observado é que durante o treinamento do classificador apenas o conjunto de treinamento e/ou validação está disponível. O conjunto de dados de teste não deve ser usado durante o treinamento do classificador. O conjunto de testes só estará disponível durante o teste do classificador.**

Após realizarmos o treinamento adequado ao modelo, precisamos avaliar seus resultados para decidirmos se continuamos com o mesmo modelo ou testamos outros.

## Avaliação dos Resultados do Modelo:
A avaliação do modelo é parte integrante do processo de desenvolvimento do modelo. Ajuda a encontrar o melhor modelo que representa nossos dados e quão bem o modelo escolhido funcionará no futuro.
Para melhorar o modelo, podemos ajustar os hiperparâmetros do modelo e tentar melhorar a precisão.

Ao analisarmos os resultados discutiremos sobre o modelo escolhido, seus resultados e outros modelos que se enquadrem também em nosso problema para testes futuramente.

## Definição das Funções de KeyBoard Smashing:
Criação das funções necessárias para detectar KeyBoard Smashing com algoritmos treinados.
Para a Release 1, fizemos a definição de uma única função:
```python
def is_kbs(input_data, analyzer, model)
```
É possível ver mais sobre a função no [README](https://github.com/fga-eps-mds/2022-2-Squad03/blob/main/README.md) do projeto.

## Empacotamento:
Após a definição das funções precisamos empacotar para que outros usuários possam utilizar nosso pacote em outras bases de dados e cumpra seu dever de detectar KeyBoard Smashing de acordo com as funções que o usuário utilizar. Fizemos esse processo por meio da plataforma Pypi e usando o twine, de maneira que qualquer pessoa usando o python 3 consiga instalar nosso pacote usando o pip.
