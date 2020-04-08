#
#  toxic_comment_classifier.py
#
#  Númi og Pétur :D
#

import numpy as np
import pandas as pd
from sklearn.feature_extraction import stop_words
import string


def aFunction():
  print("This is a function")

def textpreprocess(sentence):
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


if __name__ == "__main__":
   aFunction()
