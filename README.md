# Lokaverkefni í Gervigreind
## Lýsing á verkefninu
###  2. Toxic comment classification
Topics: Text preprocessing, multi-label classification, word embeddings, RNNs.
This project is based on a Kaggle competition from 2018 which aimed at developing tools for
improving online conversation.
You are provided with a large number of comments from Wikipedia talk page edits. The comments
have been labeled by human raters for toxic behavior. 

The types of toxicity are:

   - toxic
   - severe_toxic
   - obscene
   - threat
   - insult
   - identity_hate
    
The main objective is to create a model to predict the probability of each type of toxicity for each
comment. This is a multi-label classification task where each example can belong to zero, one or
more categories (this is not the same as multi-class classification).
Important Notice: Discussion, reports and code for analyzing this data set are all over the internet,
e.g. on Kaggle, github and medium.com. In order to select this as a final project in REI602M you
cannot consult any existing analysis or discussion of this data set. The work you hand in must be your
own. You can of course freely discuss the data and strategies with the teachers in REI602M.


### Tasks
This is an open ended project but you should start by exploring the data, e.g. by examining the
number of examples in each category and how they relate to each other. Some minor cleanup of the
data may be needed.

Construct a baseline classifier which treats the labels independently by training a binary classifier on
each label separately. We want the final classifier to perform significantly better than the baseline.
You need to consider performance evaluation in the multi-label setting. The baseline classifier should
be trained on bag-of-words or TF-IDF representations of the texts.

Use only the training data (train.csv) while exploring the data and building and evaluating classifiers
(splitting into validation and test sets as needed). After the competition ended. Kaggle provided the
test set labels. Use this to evaluate the performance of your final classifier. You are encouraged to
submit your results as a „Late submission“ to see how your classifier performs with respect to others.
Once a baseline classifier is in place, construct one or more multi-label classifiers, e.g. using scikitlearn and evaluate their performance

If you have come up with multiple classifiers that each performs reasonably well on the data, you
may want to consider stacking them to obtain a single classifier (see lecture notes on ensemble
classifiers on Piazza) that performs better than the individual classifiers.

Recurrent neural networks (RNNs) such as LSTM are able to capture sentence structure whereas bagof-words models ignore word ordering completely). Whether RNNs give better performance than
traditional methods is an open question though. Here you might consider using a LSTM (or GRU) 
network together with word embeddings (either pre-trained or dataset specific) to classify the
Wikipedia comments.

Pre-trained word embedings such as GloVe have been used to train “traditional” classifiers instead of
bag-of-words representations. Keras provides su
Try to identify which words are most often associated with toxic comments. Does your model have
unintended bias? E.g. does it incorrectly associate frequently attacked identities (e.g. gay, black,
muslim) with toxic comments? 
