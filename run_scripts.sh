#!/bin/bash
# call all the programs at once with the right parameters and names
inputfile=brown_rga.txt
N=3
for E in 100 1000 10000
do
    out=data_N3E"$E"
    ## python3 gendata.py [-N N] [-S S] [-E E] inputfile outputfile
    python3 gendata.py -N $N -E $E $inputfile  $out
    python3 gendata.py -N $N -S $E -E $((E*2)) $inputfile  "$out"S
    # train
    ## python3 train.py [-N N] datafile modelfile
    python3 train.py -N $N "$out"S_train.txt "$out"model
    python3 train.py -N $N "$out"_train.txt "$out"model
    # test
    ## python3 test.py [-N N] datafile modelfile
    python3 test.py -N $N "$out"_test.txt "$out"model
    python3 test.py -N $N "$out"S_test.txt "$out"model

done

# run a for loop in bash:
#for i in {1..8}
#do
#  python3 simdoc.py -M output_0"$i"*.txt
#done