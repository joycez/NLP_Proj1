#############################################################
# Project 1: Language Modeling
#	2.6 Classification of 'Train' and 'Valid' corpus(in Deception Detection)
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

from lm import *
import random
import pickle
import math

# Divide original hotel_review corpus(unpreprocessed) into Two parts:
#       Truthful reviews        and     Nontruthful reviews
class classifier:
        def __init__(self, train_fileName, trainORvalid):
                self.trainORvalid = trainORvalid
                self.splitModels(train_fileName)
              
        def splitModels(self, train_fileName):
                trainfile = open(train_fileName, 'r')
                if self.trainORvalid == 'train':
                        Truthful = open("hotel_subsets/Truthful_train.txt", 'w')
                        Nontruthful = open("hotel_subsets/Nontruthful_train.txt", 'w')
                elif self.trainORvalid == 'valid':
                        Truthful = open("hotel_subsets/Truthful_valid.txt", 'w')
                        Nontruthful = open("hotel_subsets/Nontruthful_valid.txt", 'w')
                for line in trainfile.readlines():
                        words = line.split()
			if words[0][0] == '0':
                                Nontruthful.write(line)
                        if words[0][0] == '1':
                                Truthful.write(line)
                print 'Reconstruction Complete!'        
                
                

                
