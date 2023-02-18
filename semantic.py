## This program uses the spaCy library to compare the similarities between words.

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


## -- Notes --
# Monkey and Cat have the highest value of similarity, probably due to them categorised as Animals.
# Monkey and Banana have the next highest value of similarity, probably due to the association by Food.
# Cat and Banana have the lowest value of similarity, due to weakest association links.


## --- Notes on running the example.py file using 'en_core_web_md' vs 'en_core_web_sm' ---
#   The similarity values from the simpler language model was smaller, even though the text parsed was unchanged.
#   Using 'en_core_web_sm' gave the warning:
#       UserWarning: [W007] The model you're using has no word vectors loaded, 
#       so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements.
#   This explains the poorer results from the simpler language model.
