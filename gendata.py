import os, sys, re
import glob
import argparse
import numpy as np
import pandas as pd

# gendata.py -- 
parser = argparse.ArgumentParser(description="Convert text to features")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int,
                    default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                    default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
parser.add_argument("-E", "--end", metavar="E", dest="endline",
                    type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
parser.add_argument("inputfile", type=str,
                    help="The file name containing the text data.")
parser.add_argument("outputfile", type=str,
                    help="The name of the output file for the feature table.")
parser.add_argument("-P", "--pos", action="store_true",
                    help="to use POS tags")
parser.add_argument("-A", "--along", action="store_true",
                    help="to use POS tags ALONGSIDE")

args = parser.parse_args()

print("Loading data from file {}".format(args.inputfile))
print("Starting from line {}.".format(args.startline))
if args.endline:
    print("Ending at line {}.".format(args.endline))
else:
    print("Ending at last line of file.")

print("Constructing {}-gram model.".format(args.ngram))
print("Writing table to {}".format(args.outputfile))
if args.pos:
    if not args.along:
        print("Using only POS tags.")
    else:
        print("Using POS tags alongside words.")
# we cant have the -A argument without the -P        
if args.along and not args.pos:
    sys.exit("the argument -A needs the -P argument")

# open the inputfile, create the list of vocabulary
def get_vocab(filename, start, end):
    vocab = []
    with open(filename, encoding = "utf-8") as f:
        for line in f.readlines()[start:end]:
            for word in line.split():
                word_pair = tuple(word.split("/"))
                if (re.search( r"[a-z]*", word_pair[0]).group(0) != ""):
                    if word_pair not in vocab:                            
                        vocab.append(word_pair)
    vocab = [("<s>", "START")] + sorted(vocab) + [("<ss>", "END")]
    return vocab

# open file again, get ngrams
def get_ngrams(filename, N, start, end):
    ngrams = list()
    myregex = r"[^a-z]\/[^\w]*"
    with open(filename, encoding = "utf-8") as f:
        for line in f.readlines()[start:end]:
            line = ("<s>/START "*N + re.sub(myregex, "", line) + " <ss>/END "*N).split()
            for i in range(len(line)-N+1):
                gram = list()
                j = 0
                while len(gram) < N:
                    pair = tuple(line[i+j].split("/"))
                    if len(pair)==2:
                        if (pair[0] != "" and pair[1] != ""):
                            gram += [tuple(line[i+j].split("/"))]
                    j += 1
                ngrams.append(tuple(gram))
    return ngrams

# convert an ngram to the concatenated n-1 hot vectors + the w_n word   
def hot_encode(gram, vocab):
    encoded = list()
    for word in gram[:-1]:
        vect = [1 if x == word else 0 for x in vocab]
        encoded += vect
    encoded += [gram[-1]]
    return encoded

######### RUN
if __name__ == "__main__":
    vocab = get_vocab(args.inputfile, args.startline, args.endline)
    ngrams = get_ngrams(args.inputfile, args.ngram, args.startline, args.endline)

    ## get rid of words or pos depending on the params
    if not args.pos:
        vocab = sorted(list(set([word for (word, tag) in vocab])))
        new_ngrams = list()
        for gram in ngrams:
            new_gram = tuple([word for (word, tag) in gram])
            new_ngrams.append(new_gram)
        ngrams = new_ngrams
    elif not args.along:
        vocab = list(set([tag for (word, tag) in vocab]))
        new_ngrams = list()
        for gram in ngrams:
            new_gram = tuple([tag for (word, tag) in gram])
            new_ngrams.append(new_gram)
        ngrams = new_ngrams
    else: # args.pos and args.along
        vocab = list(set([word for (word, tag) in vocab])) + list(set([tag for (word, tag) in vocab]))
        new_ngrams = list()
        for gram in ngrams:
            new_gram = tuple([item for tup in gram[:-1] for item in tup] + [gram[-1][0]+"/"+gram[-1][1]])
            new_ngrams.append(new_gram)
        ngrams = new_ngrams

    ###   
    encoded_df = pd.DataFrame()               
    for gram in ngrams:
        new_row = pd.Series(hot_encode(gram, vocab))
        encoded_df = encoded_df.append(new_row, ignore_index=True)
        print( round(len(encoded_df)*100/ len(ngrams), 3), "%" )

# split train and test and save
    k = encoded_df.shape[0]*(0.8)
    train = encoded_df.loc[:k,:]
    test = encoded_df.loc[(k+1):,:]
    train.to_csv(path_or_buf = args.outputfile + "_train.txt", header = False, index= False)
    test.to_csv(path_or_buf = args.outputfile + "_test.txt", header = False, index= False)
