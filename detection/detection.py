#############################################################
# Project 1: Language Modeling
#	2.6 Deception Detection
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

from test import *
from lm import *
import random
import pickle
import math

class detector:
        def __init__(self, trainT_filename, trainNT_filename, validT_filename, validNT_filename, ngram):
                self.ngram = ngram
                if ngram == 1:
                        self.lmT = GTLangModel(trainT_filename, validT_filename, 1)
                        self.lmNT = GTLangModel(trainNT_filename, validNT_filename, 1)
                elif ngram == 2:
                        self.lmT = GTLangModel(trainT_filename, validT_filename, 2)
                        self.lmNT = GTLangModel(trainNT_filename, validNT_filename, 2)
                print 'Models are ready'
                
        def detect(self, testFileName):
                bigtable = {}
                testfile = open(testFileName, 'r')
                number = 1
                resultfile = open("TestResult%s.txt" % self.ngram,'w')
                resultfile.write("Id, Label\n")
                for line in testfile.readlines():
                        tempfile = open("hotel_test_clip.lm", 'w')
                        tempfile.write(line)
                        tempfile.close()
                        Ttest = test(self.lmT, self.ngram, "hotel_test_clip.lm")
                        NTtest = test(self.lmNT, self.ngram, "hotel_test_clip.lm")
                        if Ttest.pp() >= NTtest.pp():
                                bigtable[number] = '0'
                        else:
                                bigtable[number] = '1'                     
                        result = str(number) + ', '
                        result += bigtable[number]
                        result += '\n'
                        resultfile.write(result)
                        number += 1                    
                print 'done!'
                
                
                
                

                
