#############################################################
# Project 1: Language Modeling
#	2.3 Smoothing; unknown words.
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

import pickle
from collections import Counter

class GTLangModel:
	MODEL = ["","unigram_model.lm","bigram_model.lm","trigram_model.lm"]
	UnigramCount = None
	UnigramTokens = 0
	UnigramTypes = 0
	BigramCount = None
	BigramTokens = 0
	BigramTypes = 0
	TrigramCount = None
	TrigramTokens = 0
	TrigramTypes = 0
	UNK = "<UNK>"
	THRES = 5
	gtZeroFreq = 0

	# initialize the instance object with the trained model
	# takes 3 attributes
	# trainFileName: string, training corpus
	# validFileName: string, validatin corpus
	# ngram: integer, 1 == Unigram, 2 == Bigram, 3 == Trigram
	def __init__(self, trainFileName, validFileName, ngram):
		self.trainModel(trainFileName, validFileName, ngram)
		self.loadModel(ngram)

  # train the language model with the given corpus,
  # handle the unknown words, Good-Turing smoothing,
  # and dump the model into a file.
  # takes 4 attributes
  # trainFileName: string, training corpus
  # validFileName: string, validating corpus
  # ngram: integer, 1 == Unigram, 2 == Bigram, 3 == Trigram
	def trainModel(self, trainFileName, validFileName, ngram):
		count = {}
		totalTokens = 0
		totalTypes = 0
		infile = open(trainFileName, 'r')
		for line in infile.readlines():
			words = line.split()
			for word in words:
				if word in count:
					count[word] += 1
				else:
					count[word] = 1
					totalTypes += 1
				totalTokens += 1
			if ngram == 2 or ngram == 3:
				length = len(words)
				for i in range(length-1):
					if (words[i], words[i+1]) in count:
						count[(words[i],words[i+1])] += 1
					else:
						count[(words[i],words[i+1])] = 1
						totalTypes += 1
					totalTokens += 1
				if ngram == 3:
					for i in range(length-2):
						if (words[i], words[i+1], words[i+2]) in count:
							count[(words[i], words[i+1], words[i+2])] += 1
						else:
							count[(words[i], words[i+1], words[i+2])] = 1
							totalTypes += 1
						totalTokens += 1

		# handling unknown words
		with open(validFileName, 'r') as fvalid:
			for line in fvalid.readlines():
				words = line.split()
				newWords = []
				for word in words:
					if word in count: newWords.append(word)
					else: newWords.append(self.UNK)
				for newWord in newWords:
					if newWord in count:
						count[newWord] += 1
					else:
						count[newWord] = 1
						totalTypes += 1
					totalTokens += 1
				if ngram == 2 or ngram == 3:
					length = len(newWords)
					for i in range(length-1):
						if (newWords[i], newWords[i+1]) in count:
							count[(newWords[i],newWords[i+1])] += 1
						else:
							count[(newWords[i],newWords[i+1])] = 1
							totalTypes += 1
						totalTokens += 1
					if ngram == 3:
						for i in range(length-2):
							if (newWords[i], newWords[i+1], newWords[i+2]) in count:
								count[(newWords[i], newWords[i+1], newWords[i+2])] += 1
							else:
								count[(newWords[i], newWords[i+1], newWords[i+2])] = 1
								totalTypes += 1
							totalTokens += 1

		# turn count(key, freq) to
		# sameFreqCount(freq, number of words with the same freq)
		sameFreqCount = Counter()
		for (key, freq) in count.items():
			sameFreqCount[freq] += 1

		# smooth the frequency of the word
		# whose current frequency is under the defined threshold
		gtFreq = {}
		for i in sorted(sameFreqCount.keys()):
			if i in range(self.THRES) and sameFreqCount[i+1] != 0 and sameFreqCount[i] != 0:
				gtFreq[i] = (i+1) * (float(sameFreqCount[i+1])/sameFreqCount[i])
			else: gtFreq[i] = i
		gtZeroFreq = float(sameFreqCount[1]) / totalTokens

		for (key, freq) in count.items():
			count[key] = gtFreq[freq]

		#totalTokens = gtZeroFreq

		fout = open(self.MODEL[ngram],'w')
		pickle.dump(count, fout)
		pickle.dump(gtZeroFreq, fout)
		pickle.dump(totalTokens, fout)
		pickle.dump(totalTypes, fout)

	# load the language model from the file
	# takes 1 attribute
	# ngram: integer, 1 == Unigram, 2 == Bigram, 3 == Trigram
	def loadModel(self, ngram):
		fin = open(self.MODEL[ngram],'r')
		print str(ngram)+"gram: "
		if ngram == 1:
			self.UnigramCount = pickle.load(fin)
			self.gtZeroFreq = pickle.load(fin)
			self.UnigramTokens = pickle.load(fin)
			self.UnigramTypes = pickle.load(fin)
			print "tokens: " + str(self.UnigramTokens)
			print "gtZeroFreq: " + str(self.gtZeroFreq)
			print "types: " + str(self.UnigramTypes)
		elif ngram == 2:
			self.BigramCount = pickle.load(fin)
			self.gtZeroFreq = pickle.load(fin)
			self.BigramTokens = pickle.load(fin)
			self.BigramTypes = pickle.load(fin)
			print "tokens: " + str(self.BigramTokens)
			print "gtZeroFreq: " + str(self.gtZeroFreq)			
		elif ngram == 3:
			self.TrigramCount = pickle.load(fin)
			self.gtZeroFreq = pickle.load(fin)
			self.TrigramTokens = pickle.load(fin)
			self.TrigramTypes = pickle.load(fin)	
			print "tokens: " + str(self.TrigramTokens)
			print "gtZeroFreq: " + str(self.gtZeroFreq)		

	# calculates the Unigram probability
	# using the Good-Turing Smoothed Unigram Model
	# takes 1 attribute
	# word: string
	def probUnigram(self, word):
		prob = 0
		if word not in self.UnigramCount:
			word = self.UNK
		if self.UnigramTokens != 0:
			if word not in self.UnigramCount:
				prob = self.gtZeroFreq / (0.0 + self.UnigramTokens)
			else:
				prob = self.UnigramCount[word] / (0.0 + self.UnigramTokens)
		return prob

  # calculates the Bigram probability
  # using the Good-Turing Smoothed Bigram Model
  # takes 2 attributes
  # preWord: string
  # word: string
	def probBigram(self, preWord, word):
		prob = 0
		if preWord not in self.BigramCount:
			preWord = self.UNK
		if word not in self.BigramCount:
			word = self.UNK 

		preWordCount = self.BigramCount[preWord]
		if preWordCount != 0:
			if (preWord, word) not in self.BigramCount:
				prob = self.gtZeroFreq / (0.0 + preWordCount)
			else:
				prob = self.BigramCount[(preWord, word)] / (0.0 + preWordCount)
		return prob

  # calculates the Trigram probability
  # using the Good-Turing Smoothed Trigram Model
  # takes 3 attributes
  # triWord: string
  # preWord: string
  # word: string
	def probTrigram(self, triWord, preWord, word):
		prob = 0
		if triWord not in self.TrigramCount:
			triWord = self.UNK
		if preWord not in self.TrigramCount:
			preWord = self.UNK
		if word not in self.TrigramCount:
			word = self.UNK

		if (triWord, preWord) in self.TrigramCount:
			preTwoWordsCount = self.TrigramCount[(triWord, preWord)]
			print preTwoWordsCount
			if preTwoWordsCount != 0:
				if (triWord, preWord, word) not in self.TrigramCount:
					prob = self.gtZeroFreq / (0.0 + preTwoWordsCount)
				else:
					prob = self.TrigramCount[(triWord, preWord, word)] / (0.0 + preTwoWordsCount)
		return prob

