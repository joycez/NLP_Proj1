#############################################################
# Project 2: Supervised Modeling
#############################################################

from collections import Counter
from sup_preprocessing import *

class featureModel:
	def __init__(self, trainFileName, windowsize):
                self.count = {}
                self.countFea = {}
                self.traindataSize = 0
                self.windowsize = windowsize
                self.traindata = parse_supervised(trainFileName, windowsize)
		self.trainModel(self.traindata, windowsize)
		             
 	def trainModel(self, traindata, windowsize):
                for word_n_ID, examples in traindata.items():
                        word = word_n_ID[0]
                        ID = word_n_ID[1]
                        for example in examples:
                                if (word, ID) in self.count:
                                        self.count[(word, ID)] += 1
                                else:
                                        self.count[(word, ID)] = 1
                                for featureword in example.split():
                                        if (word, ID, featureword) in self.countFea:
                                                self.countFea[(word, ID, featureword)] += 1
                                        else:
                                                self.countFea[(word, ID, featureword)] = 1
                
        def probSense(self, targetword, targetID):
		number1 = 0
		number2 = 0
		for (word, ID) in self.count:
                        if word == targetword:
                                number1 += self.count[(word, ID)]
                                if ID == targetID:
                                        number2 = self.count[(word, ID)]
                if number1 == 0:
                        print 'Error: No such word in the training data'
                        return
                prob = 1.0 * number2/number1
                return prob

	def probFeature(self, targetword, targetID, targetfea):
                if self.countFea[(targetword, targetID, targetfea)] == 0:
                        print 'Error: No such context in the training data'
                        return
		prob = 1.0 * self.countFea[(targetword, targetID, targetfea)]/self.count[targetword, targetID]
                return prob

        
