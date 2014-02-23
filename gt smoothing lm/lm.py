#############################################################
# Project 1: Language Modeling
#	2.1 Unsmoothed ngrams
# Haotian Pan (hp343), Jiang Jian (jj544), Jue Zhang (jz578) 
#############################################################

import pickle

class LangModel:
	UNIGRAM_MODEL = "unigram_model.lm"
	BIGRAM_MODEL = "bigram_model.lm"
	UnigramCount = None
	UnigramTokens = 0
	UnigramTypes = 0
	BigramCount = None
	BigramTokens = 0
	BigramTypes = 0

	# initialize the instance object with the trained model
	# takes 2 attributes
	# infile_name: string, training corpora
	# ngram: integer, 1 == Unigram, 2 == Bigram
	def __init__(self, infile_name, ngram):
		if ngram == 1:
			self.train_model(infile_name, self.UNIGRAM_MODEL, 1)
			model = self.load_model(self.UNIGRAM_MODEL)
			self.UnigramCount = model["count"]
			self.UnigramTokens = model["TotalTokens"]
			self.UnigramTypes = model["TotalTypes"]
		elif ngram == 2:
			self.train_model(infile_name, self.BIGRAM_MODEL, 2)
			model = self.load_model(self.BIGRAM_MODEL)
			self.BigramCount = model["count"]
			self.BigramTokens = model["TotalTokens"]
			self.BigramTypes = model["TotalTypes"]

  # train the language model with the given corpora,
  # and dump the model into a file.
  # takes 3 attributes
  # infile_name: string, training corpora
  # outfile_name: string, UNIGRAM_MODEL or BIGRAM_MODEL
  # ngram: integer, 1 == Unigram, 2 == Bigram
	def train_model(self, infile_name, outfile_name, ngram):
		count = {}
		TotalTokens = 0
		TotalTypes = 0
		infile = open(infile_name, 'r')
		for line in infile.readlines():
			words = line.split()
			for word in words:
				if word in count:
					count[word] += 1
				else:
					count[word] = 1
					TotalTypes += 1
				TotalTokens += 1
			if ngram == 2:
				for i in range(len(words)-1):
					if (words[i], words[i+1]) in count:
						count[(words[i],words[i+1])] += 1
					else:
						count[(words[i],words[i+1])] = 1
		fout = open(outfile_name,'w')
		pickle.dump(count, fout)
		pickle.dump(TotalTokens, fout)
		pickle.dump(TotalTypes, fout)

	# load the language model from the file
	# takes 1 attribute
	# infile_name: string, UNIGRAM_MODEL or BIGRAM_MODEL
	def load_model(self, infile_name):
		model = {}
		fin = open(infile_name,'r')
		model["count"] = pickle.load(fin)
		model["TotalTokens"] = pickle.load(fin)
		model["TotalTypes"] = pickle.load(fin)
		return model

	# calculates the probability of the word using the Unigram Model
	# takes 1 attribute
	# word: string
	def prob_unigram(self,word):
		prob = 0
		if self.UnigramTokens != 0:
			prob = self.UnigramCount[word] / (0.0 + self.UnigramTokens)
		return prob

  # calculates the probability of a word following another word
  # takes 2 attributes
  # preWord: string
  # word: string
	def prob_bigram(self, preWord, word):
		prob = 0
		preWordCount = self.BigramCount[preWord]
		if preWordCount != 0:
			prob = self.BigramCount[(preWord, word)] / (0.0 + self.BigramCount[preWord])
		return prob

