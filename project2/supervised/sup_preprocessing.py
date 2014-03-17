#!/usr/bin/env python

from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

import re
import xml.etree.ElementTree as ET

######################################################
# 		global variables
######################################################

glob_Lucene = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"];

def parse_supervised(train_filename, windowsize):
    traindata = {}
    trainfile = open(train_filename,'r')
    for line in trainfile.readlines():
        words = line.split()
        example = words[4:]
        useful = lemma_stem_sentence(" ".join(example))
        index = useful.index('%%')
        prevCon = " ".join(useful[index-windowsize:index])
        nextCon = " ".join(useful[index+3:index+windowsize+3])
        useful = " ".join([prevCon, nextCon])
        if (words[0], words[2]) in traindata:
            traindata[(words[0], words[2])].append(useful)
        else:
            traindata[(words[0], words[2])] = []
            traindata[(words[0], words[2])].append(useful)
    print traindata
    return traindata

def lemma_stem_sentence(sentence):
    lmtzr = WordNetLemmatizer()
    ls = LancasterStemmer()
    word_list = []
    single_words = re.findall("\w+|%%",sentence)
    for single_word in single_words:
        lemmed = lmtzr.lemmatize(single_word)
##        stemmed = ls.stem(lemmed)
##        if not stemmed in glob_Lucene:
##            word_list.append(stemmed)
        if not lemmed in glob_Lucene:
            word_list.append(lemmed)
    return word_list

if __name__ == '__main__':
##	parse_supervised("training_data.data")
	parse_supervised("sample.data", 3)

