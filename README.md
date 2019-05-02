# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Elena Rodríguez

## Additional instructions

Outputfile and modelfile names should be given without the extension

By adding the argument -P -A in gendata, the script uses POS tags and words, only using the -P would only use the tags.

## Reporting for Part 4

(Still running the models)

## Reporting for Part Bonus 
I decided to treat the POS tags as new words and added to the vocabulary, and flatten the vector with the tags to get a 2xN vector in order to fit it in the same program. The label is the word with its tag.
(Still running the models)

## Problems encountered
My first intuition was to use the N parameter somehow while building the model, but I couldn't see how. My guess is that we could improve the model if we could "tell" it that the hot vectors come from N vectors.
