#!/bin/bash
# call all the programs at once with the right parameters and names
inputfile=brown_rga.txt
E=100
for N in 4 5
do
out=data_N"$N"E"$E"
    ## python3 gendata.py [-N N] [-S S] [-E E] inputfile outputfile
    python3 gendata.py -N $N -E $E $inputfile  $out
    python3 gendata.py -N $N -S $E -E $((E*2)) $inputfile  "$out"S
    python3 gendata.py -N $N -E $E - P $inputfile  "$out"P
    python3 gendata.py -N $N -S $E -E $((E*2)) -P $inputfile  "$out"SP
    python3 gendata.py -N $N -E $E -P - A $inputfile  "$out"PA
    python3 gendata.py -N $N -S $E -E $((E*2)) -P -A $inputfile  "$out"SPA
    # train
    ## python3 train.py [-N N] datafile modelfile
    #python3 train.py -N $N "$out"S_train.txt "$out"model
    #python3 train.py -N $N "$out"_train.txt "$out"model
    # test
    ## python3 test.py [-N N] datafile modelfile
    #python3 test.py -N $N "$out"_test.txt "$out"model
    #python3 test.py -N $N "$out"S_test.txt "$out"model

done
