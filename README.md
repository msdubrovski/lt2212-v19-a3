# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Elena Rodríguez

## Additional instructions

Outputfile and modelfile names should be given without the extension

By adding the argument -P -A in gendata, the script uses POS tags and words, only using the -P will only use the tags.

## Reporting for Part 4
Expected trends in results:
- bigger improvement from N = 3 to 4 than from 4 to 5 (in the size of N-grams)
- same-sized pieces of the text will have similar results, from a certain size.


| -N | -E -S | Accuracy (%) | PerPlexity |  
| --- | :---: | :---: | :---: | 
| 3  |  E100  |  13.067  |  41.745  | 
| 3  |  E200 S100  |  15.269  |  49.953  | 
| 4  |  E100  |  22.624  |  44.356  | 
| 4  |  E200 S100  |  24.858  |  50.479  | 
| 5  |  E100  |  25.108  |  45.263  |
| 5  |  E200 S100  |  27.605  |  51.561  | 

Here we are taking 100 lines at a time while varying the size of the N grams. We see the accuracy is not great, but it does increase with N as expected. (I can't explain those perplexity results, I might be computing it wrong)
The variation from using different pieces of the text suggest we need to train over larger sets.

## Reporting for Part Bonus 
I decided to treat the POS tags as new words and added them to the vocabulary, and flatten the vector with the tags to get a 2xN vector in order to fit it in the same script. The label is the word with its tag.

| -N | -E -S | PA | Accuracy | PerPlexity |  
| :---: | :---: | :---: | ---: | ---: | 
| N3 | E100 | |  13.067  |  41.745  | 
| N3 | E100 | PA |  21.09  |  45.891 | 
| N4 | E200 S100 | |  24.858  |  50.479  | 
| N4 | E200 S100 | PA |  25.617  |  53.752  | 
| N5 | E200 S100 |   |  27.605  |  51.561  | 
| N5 | E200 S100 |  PA  |  27.788  |  55.331  | 

This enriched approach only slightly improves accuracy, while also icnreasing perplexity, that is, not great news. In the case of trigrams, however, the increase is important. (This should be further tested over different lines of the text.)

I left the option of only building the models for POS tags, thus reducing dramatically the size of the vocabulary (possible POS tags), which gives the best accuracy scores. The increase in perplexity might be due to the small n-grams, as in the case of only using tags it might make more sense to allow longer combinations (perhaps up to a mean length of sentences).

| File | Options | Accu | PP |  
| --- | :---: | :---: | :---: | 
| data  |  N4 E200 S100 P  |  40.038  |  69.064  | 
| data  |  N5 E200 S100 P  |  41.499  |  70.163  | 

## Problems encountered
My first intuition was to use the N parameter somehow while building the model, but I couldn't see how. My guess is that we could improve the model if we could "tell" it that the hot vectors come from N-grams.
