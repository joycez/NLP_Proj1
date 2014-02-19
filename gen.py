from lm import *
import random

class generator:
        def __init__(self, lm, ngram):
                self.gen_words = []
                self.ngram = 0
                self.bag = []                           
                self.whitelist = []
                self.ngram = ngram
                self.lm = lm
                # restore dataset from distribution
                if self.ngram == 1:
                        for word in lm.UnigramCount.keys():
                                number = lm.UnigramCount[word]
                                while(number>0 and word!='<s>' and word!='</s>'):
                                        self.bag.append(word)
                                        number -= 1
                elif self.ngram == 2:
                        for pair in lm.BigramCount.keys():
                                if isinstance(pair,basestring)==False:
#                                       print pair
                                        word1,word2 = pair
                                        if word1!='<s>' and word1!='</s>' and word2!='<s>' and word2!='</s>':
                                                self.whitelist.append(word1)
                                                number = lm.BigramCount[pair]
                                                while(number>0):
                                                        self.bag.append(pair)
                                                        number -= 1
#                print self.bag
#                print self.whitelist
        def go(self,length):
                initial = None
                option1 = None
                option2 = None
                if self.ngram == 1:
                        self.gen_words = []
                        for i in range(length):
                                w1 = random.choice(self.bag)
                                self.gen_words.append(w1)
                        print ' '.join(self.gen_words)
                        
                elif self.ngram == 2:
                        self.gen_words = []
                        (initial,whatever) = random.choice(self.bag)    # Assumption: every word has the same chance of being chosen as the first word in the sentence
                        w1 = initial
                        self.gen_words.append(w1)
#                        print ('w1 is',w1)
                        for i in range(length-1):
                                while(option1!=w1 or (option2 not in self.whitelist)):  # avoid infinite loops where (option2,*) does not exist
                                        (option1,option2) = random.choice(self.bag)          
                                w2 = option2
#                                print ('w2 is',w2)      
                                self.gen_words.append(w2)
                                w1 = w2
                        print ' '.join(self.gen_words)
                                
                        

