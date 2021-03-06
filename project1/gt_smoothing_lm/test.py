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
                if N == 0:
                        print 'Do not keep empty lines in your file!'
                        return None
                if self.ngram == 1 or N == 1:
                        logresult = self.lm.probUnigram(self.testdata[0])
                        for i in range(1,N):
                                logresult += math.log10(self.lm.probUnigram(self.testdata[i]))
                elif self.ngram == 2:
                        logresult = 0.0
                        for i in range(0,N-1):
                                if(self.testdata[i]!='</s>'):
                                        logresult += math.log10(self.lm.probBigram(self.testdata[i],self.testdata[i+1]))
                elif self.ngram == 3:
                        logresult = 0.0
                        for i in range(0,N-2):
##                                print self.testdata[i], self.testdata[i+1], self.testdata[i+2]
                                if(self.testdata[i]!='</s>' and self.testdata[i+1]!='</s>'):
                                        logresult += math.log10(self.lm.probTrigram(self.testdata[i],self.testdata[i+1],self.testdata[i+2]))                        
                result = math.pow(10,logresult*(-1.0/N))
                return result
                


                

                
