import pickle
from nltk import everygrams

with open(".\\models\\randomforest.pkl", "rb") as file1:
    trained_model = pickle.load(file1)

with open(".\\models\\tfid_vectorizer.pkl", "rb") as file2:
    vectorizer = pickle.load(file2)


def is_kbs(input_data, analyzer='word', model='randomForest'):
    if (model == 'randomForest'):
        if (analyzer == 'word'):
            if (len(input_data) == 1):
                return 0
            input_data = [input_data]
            input_ngrams = []

            for i in range(len(input_data)):
                ngram = map(''.join, list(everygrams(input_data[i], 2, 4)))
                input_ngrams.extend(ngram)

            predprob = trained_model.predict_proba(
                vectorizer.transform(input_ngrams))[:, 1]
            prob = sum(predprob)/len(input_ngrams)
            if (prob >= 0.5):
                return 1
            else:
                return 0
        elif (analyzer == 'phrases'):
            if (len(input_data) == 1):
                return 0
            mashs = []
            words = input_data.split()

            for word in words:
                if (len(word) == 1):
                    words.remove(word)

            for word in words:
                input_ngrams = []
                word = [word]
                for char in word:
                    ngram = map(''.join, list(everygrams(char, 2, 4)))
                    input_ngrams.extend(ngram)
                predprob = sum(trained_model.predict_proba(
                    vectorizer.transform(input_ngrams))[:, 1])/len(input_ngrams)
                if (predprob >= 0.5):
                    mashs.append(word)
            if (len(mashs) != 0):
                return mashs
        return 0