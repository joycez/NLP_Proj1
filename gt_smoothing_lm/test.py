#############################################################
# Project 1: Language Modeling
#	2.4 Perplexity
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

from lm import *
import random
import pickle
import math

class test:
        def __init__(self,lm,ngram,testfile_name):
                self.ngram = ngram
                self.lm = lm
                self.testdata = []
                self.testfile_name = testfile_name
                testfile = open(testfile_name, 'r')
                for line in testfile.readlines():
                        words = line.split()
			for word in words:
				self.testdata.append(word)

        def pp(self):
                N = len(self.testdata)
                if self.ngram == 1:
                        logresult = self.lm.probUnigram(self.testdata[0])
                        for i in range(1,N):
                                logresult += math.log10(self.lm.probUnigram(self.testdata[i]))
                elif self.ngram == 2:
                        logresult = 0.0
                        for i in range(0,N):
                                if(self.testdata[i]!='</s>'):
                                        logresult += math.log10(self.lm.probBigram(self.testdata[i],self.testdata[i+1]))
                result = math.pow(10,logresult*(-1.0/N))
                print result


                

                
