#!/bin/bash
# call all the programs at once with the right parameters and names
inputfile=brown_rga.txt
# for file in ./data_N5*_train*
# out=data_N"$N"E"$E"
# do
#     # gendata
#     ## python3 gendata.py [-N N] [-S S] [-E E] inputfile outputfile
#     # train
#     ## python3 train.py [-N N] datafile modelfile
#     python3 train.py -N 4 $file "$file"_model
#     # test
#     ## python3 test.py [-N N] datafile modelfile
# done
#########
E=500
for N in 3 4 5
do
    # gendata
    #outputfile=./data/data
    python3 gendata.py -N $N -E $E $inputfile data_N"$N"E"$E"
    python3 gendata.py -N $N -S $E -E -E $((E*2)) $inputfile data_N"$N"E"$E"S
    python3 gendata.py -N $N -E $E -P -A $inputfile data_N"$N"E"$E"PA
    python3 gendata.py -N $N -S $E -E -E $((E*2)) -P -A $inputfile data_N"$N"E"$E"SPA
done

for file in ./data/*_train.txt
    # train
    ## python3 train.py [-N N] datafile modelfile
    python3 train.py -N 3 $file "$file"_model
done

for file in ./data/*_test.txt
# test
    ## python3 test.py [-N N] datafile modelfile
    python3 test.py -N 3 $file "$file"_model
done