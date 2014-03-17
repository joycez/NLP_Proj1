#############################################################
# Project 1: Language Modeling
#	2.6 Classification of 'Train' and 'Valid' corpus(in Deception Detection)
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

from lm import *
import random
import pickle
import math

Ttrain = "hotel_truthful_train.txt"
NTtrain = "hotel_Nontruthful_train.txt"
Tvalid = "hotel_truthful_valid.txt"
NTvalid = "hotel_Nontruthful_valid.txt"

# Divide original hotel_review corpus(unpreprocessed) into Two parts:
#       Truthful reviews        and     Nontruthful reviews
class classifier:
        def __init__(self, train_fileName, trainORvalid):
                self.trainORvalid = trainORvalid
                self.splitModels(train_fileName)
              
        def splitModels(self, train_fileName):
                trainfile = open(train_fileName, 'r')
                if self.trainORvalid == 'train':
                        Truthful = open(Ttrain, 'w')
                        Nontruthful = open(NTtrain, 'w')
                elif self.trainORvalid == 'valid':
                        Truthful = open(Tvalid, 'w')
                        Nontruthful = open(NTvalid, 'w')
                for line in trainfile.readlines():
                        words = line.split()
                        if len(words) == 0:
                                continue
			if words[0][0] == '0':
                                line = line[5:]
                                Nontruthful.write(line)
                        if words[0][0] == '1':
                                line = line[5:]
                                Truthful.write(line)
                Truthful.close()
                Nontruthful.close()
                print 'Reconstruction Complete!'        
                
                

                
