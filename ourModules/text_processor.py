import numpy as np
from sklearn.feature_extraction import stop_words
import string

def textPreprocess(sentence):
    sentence = sentence.lower()
    
    #Taka út ensk stopporð
    stopwords = stop_words.ENGLISH_STOP_WORDS
    for sw in stopwords:
        if len(sw) > 1 and sw in sentence:
            sentence.replace(sw,'')
    
    #Taka út tölur
    sentence = ''.join([i for i in sentence if not i.isdigit()])
    
    #Taka út punkta, kommur og þannig lagað
    sentence=sentence.translate(str.maketrans('', '', string.punctuation))
    
    return sentence

def getProcessedText(dataset):
    x_train = dataset['comment_text'].to_numpy()
    for i in range(len(x_train)):
        x_train[i] = textPreprocess(x_train[i])
    return x_train

if __name__ == "__main__":
   print("textProcessor.py was run")