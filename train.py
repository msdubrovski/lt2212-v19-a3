import os, sys
import argparse
import numpy as np
import pandas as pd
from joblib import dump, load # [pickle doesnt work on my comp] # import pickle
from sklearn.linear_model import LogisticRegression

# train.py --

parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features.")
parser.add_argument("modelfile", type=str,
                    help="The name of the file to which you write the trained model.")

args = parser.parse_args()

print("Loading data from file {}.".format(args.datafile))
print("Training {}-gram model.".format(args.ngram))
print("Writing table to {}.".format(args.modelfile))

############################
# read fileinput:
# datafile = '../EDU/S2.1-statistics/ass3_git/try1.txt'
data = pd.read_csv(args.datafile, sep=',', delimiter=None, header=None, names=None)

# figure out how to interpret the features, !!!!!!!!!!!
# #TODO

# the last column of our data is the class label
k = data.shape[1] - 1
y = data[k] 
X = data.drop(k, axis=1)
# ‘newton-cg’, ‘sag’, ‘saga’ and ‘lbfgs’
classifier = LogisticRegression(multi_class= 'multinomial', solver='lbfgs')
classifier.fit(X,y)

classifier.decision_function(X)
# predictions = classifier.predict(X)
# results = (predictions == y)
# accuracy = sum(results.replace({True:1,False:0}))/len(results)

# safe the model to the outputfile
# modelfile = '../EDU/S2.1-statistics/ass3_git/try_model'
dump(classifier, args.modelfile+'.joblib') 
#clf = load(modelfile+'.joblib') 