import os, sys
import argparse
import numpy as np
import pandas as pd
from joblib import dump, load # [pickle doesnt work on my comp] # import pickle
from sklearn.linear_model import LogisticRegression
from scipy.stats import entropy

# test.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here.

parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features in the test data.")
parser.add_argument("modelfile", type=str,
                    help="The name of the saved model file.")

args = parser.parse_args()

print("Loading data from file {}.".format(args.datafile))
print("Loading model from file {}.".format(args.modelfile))

print("Testing {}-gram model.".format(args.ngram))

print("Computing accuracy and perplexity ...")

#########

# load the trained model
clf = load(args.modelfile+'.joblib')
# load the data and separate labels
data = pd.read_csv(args.datafile, sep=',', delimiter=None, header=None, names=None)
k = data.shape[1] - 1
y = data[k] 
X = data.drop(k, axis=1)

# clf.decision_function(X)
predictions = clf.predict(X)
results = (predictions == y)
accuracy = clf.score(X,y)
probs = clf.predict_proba(X)
probs_max = [max(probs[i]) for i in range(len(y))]
perplexity = 2**(entropy(probs_max)) 
#print("Accuracy = ", round(accuracy, 3))
#print("Perplexity = ", round(perplexity, 3))

print("| File | Options | Accu | PP | ", "\n|",
            "--- | :---: | ---: | ---: |", "\n|",
            args.datafile.split("_")[0], " | ",
            args.datafile.split("_")[1][:-4], " | ",
            round(accuracy*100, 3), " | ",
            round(perplexity, 3), " | ")

