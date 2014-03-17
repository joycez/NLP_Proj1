#!/usr/bin/env python

from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

import re
import xml.etree.ElementTree as ET

######################################################
# 		global variables
######################################################
glob_path = "/profession/[14Spring]-Natural Language Processing/assignment2/"
glob_dict_path = "/profession/[14Spring]-Natural Language Processing/assignment2/dictionary-modified.xml"
# glob_dict_path = "/profession/[14Spring]-Natural Language Processing/assignment2/small_dictionary.xml"
glob_Lucene = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"];


######################################################
# 		parse methods
######################################################
"""
dictionary [
    "begin":{
        type:"v"
        num:1
        senses:[
            {
                id:1
                wn_ids:[1,2,3,4]
                gloss:["hello","world"]
                examples:["hello","world"]
            },
            ...
        ]
    },
    ...
]
"""
def parse_dictionary(dict_path):
    dictionary = {}
    tree = ET.parse(dict_path)
    root = tree.getroot()
    for lexeme in root:
        senses = []
        word_dict = {}
        word_dict["senses"] = senses
        word_dict["num"] = int(lexeme.attrib['num'])

        """ ATTENTION:
        	In the dictionary.xml, it uses word.type as key, however, I split it here
        """
        word_strs = lexeme.attrib["item"].split('.')
        word_dict["type"] = word_strs[1]
        dictionary[word_strs[0]] = word_dict
        for sense in lexeme:
            sense_id = sense.attrib["id"]
            sense_dict = {}
            sense_dict["id"] = sense_id
            wordnet_ids = sense.attrib["wordnet"]
            wordnet_list = []
            for id_str in wordnet_ids.split(","):
                if id_str != '':
            	    wordnet_list.append(int(id_str))
            sense_dict["wn_ids"] = wordnet_list
            sense_dict["gloss"] = lemma_stem_sentence(sense.attrib["gloss"])
            sense_dict["examples"] = lemma_stem_sentence(sense.attrib["examples"])
            if "#" in sense_id:
                ids = sense_id.split("#")
                for s_itm in senses:
                    if s_itm["id"] in ids:
                        s_itm["examples"] += sense_dict["examples"]
            else:
                senses.append(sense_dict)

    return dictionary

def lemma_stem_sentence(sentence):
    lmtzr = WordNetLemmatizer()
    ls = LancasterStemmer()
    word_list = []
    single_words = re.findall("\w+",sentence)
    for single_word in single_words:
        lemmed = lmtzr.lemmertize(single_word)
        stemmed = ls.stem(lemmed)
        if not stemmed in glob_Lucene:
            word_list.append(stemmed)
    return word_list

if __name__ == '__main__':
	parse_dictionary(glob_dict_path)