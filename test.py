import os, sys
import argparse
import numpy as np
import pandas as pd
from joblib import dump, load # [pickle doesnt work on my comp] # import pickle
from sklearn.linear_model import LogisticRegression

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

print("Accuracy is ...")
print("Perplexity is...")

#########

#clf = load(modelfile+'.joblib') 

# classifier.decision_function(X)
# predictions = classifier.predict(X)
# results = (predictions == y)
# accuracy = sum(results.replace({True:1,False:0}))/len(results)
