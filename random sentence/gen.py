from lm import *
import random

class generator:
        def __init__(self, lm, ngram):
                self.gen_words = []
                self.ngram = 0
                self.bag = []                           
                self.whitelist = []
                self.whitepairs = []
                self.ngram = ngram
                self.lm = lm
                # restore dataset from distribution
                if self.ngram == 1:
                        for word in lm.UnigramCount.keys():
                                number = lm.UnigramCount[word]
                                while(number>0 and word!='<s>'):
                                        self.bag.append(word)
                                        number -= 1
                # The usage of whitelist ensures no pairs in the bag end with a string which is not the first word in any pair
                elif self.ngram == 2:
                        self.whitelist.append('</s>')
                        for pair in lm.BigramCount.keys():
                                if len(pair) == 2:
                                        word1,word2 = pair
                                        self.whitelist.append(word1)
                                        number = lm.BigramCount[pair]
                                        while(number>0):
                                                self.bag.append(pair)
                                                number -= 1
                elif self.ngram == 3:
                        for three in lm.TrigramCount.keys():
                                if len(three) == 3:
                                        word1,word2,word3 = three
                                        self.whitelist.append((word1,word2))
                                        number = lm.TrigramCount[three]
                                        while(number>0):
                                                self.bag.append(three)
                                                number -= 1
                        
        def go(self,length):
                initial = None
                sign = None
                option1 = None
                option2 = None
                # Generate EXACTLY "length" number of words to make up a sentence directly
                if self.ngram == 1:
                        self.gen_words = []
                        for i in range(length):
                                w1 = random.choice(self.bag)
                                if(w1 == '</s>'):
                                        break
                                self.gen_words.append(w1)
                        print ' '.join(self.gen_words)
                # Generate a sentence which is NO MORE THAN "length" number of words and has the same endings with the        
                elif self.ngram == 2:                                                   # sentences in the corpus
                        self.gen_words = []
                        while(sign!='<s>'):
                                (sign,initial) = random.choice(self.bag)    # Assumption: sentence starts from the words 
                        w1 = initial                                            # who are initials in the sentences in the corpus
                        self.gen_words.append(w1)
                        for i in range(length-1):
                                while(option1!=w1 or (option2 not in self.whitelist)):  # avoid infinite loops where (option2,*) does not exist
                                        (option1,option2) = random.choice(self.bag)          
                                w2 = option2    
                                if(w2 == '</s>'):
                                        break
                                self.gen_words.append(w2)
                                w1 = w2
                        print ' '.join(self.gen_words)
                elif self.ngram == 3:                                                   
                        self.gen_words = []
                        while(sign!='<s>'):
                                (sign,first,second) = random.choice(self.bag)     
                        w1 = first
                        w2 = second
                        self.gen_words.append(w1)
                        self.gen_words.append(w2)
                        for i in range(length-2):
                                while(option1!=w1 or option2!=w2 or ((option2,option3) not in self.whitelist)):  # avoid infinite loops where (option2,*) does not exist
                                        (option1,option2,option3) = random.choice(self.bag)
                                w3 = option3
#                                print w1,w2,w3
                                if(w3 == '</s>'):
                                        break
                                self.gen_words.append(w3)
                                if(w3 == '.' or w3 == '?' or w3 == '!'):
                                        break
                                w1 = w2
                                w2 = w3
                        print ' '.join(self.gen_words)          
                        

