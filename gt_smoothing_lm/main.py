from lm import *
from gen import *
from test import *

def main():
#  ----     part1       ----

##        lm1 = LangModel("sample.lm", 1)
##        lm2 = LangModel("sample.lm", 2)
##        print lm2.prob_bigram("God", "saw");
##
##        lm1 = LangModel("bible_train.lm", 1)
##        lm2 = LangModel("bible_train.lm", 2)
##
##        lm1 = LangModel("hotel_train.lm", 1)
##        lm2 = LangModel("hotel_train.lm", 2)
##        
##        g1 = generator(lm1,1)
##        g2 = generator(lm2,2)

##        print '------Sentences by Unigram Model------'
##        for i in range(3):
##                g1.go(25)
##        print '------Sentences by Bigram Model------'
##        for i in range(3):
##                g2.go(25)
##        print '------End------'

#  ----     part2       ----
##
        lm1 = GTLangModel("bible_train.lm", "bible_valid.lm", 1)
        lm2 = GTLangModel("bible_train.lm", "bible_valid.lm", 2)
        lm3 = GTLangModel("bible_train.lm", "bible_valid.lm", 3)        
        bible_test1 = test(lm1, 1, "bible_test.lm")
        bible_test2 = test(lm2, 2, "bible_test.lm")
        bible_test3 = test(lm3, 3, "bible_test.lm")
        print "bible Unigram perplexity:"        
        print bible_test1.pp();
        print "bible Bigram perplexity:"
        print bible_test2.pp();
        print "bible Trigram perplexity"
        print bible_test3.pp();

        lm1 = GTLangModel("hotel_train.lm", "hotel_valid.lm", 1)
        lm2 = GTLangModel("hotel_train.lm", "hotel_valid.lm", 2)
        lm3 = GTLangModel("hotel_train.lm", "hotel_valid.lm", 3)        
        hotel_test1 = test(lm1, 1, "hotel_test.lm")
        hotel_test2 = test(lm2, 2, "hotel_test.lm")
        hotel_test3 = test(lm3, 3, "hotel_test.lm")
        print "hotel Unigram perplexity:"
        print hotel_test1.pp();
        print "hotel Bigram perplexity:"
        print hotel_test2.pp();
        print "hotel Trigram perplexity"
        print hotel_test3.pp();

        #lm = GTLangModel("sample.train", "sample.valid", 3)
        # print "Unigram Prob:"
        # print lm1.probUnigram("I")
        # print "Bigram Prob:"
        # print lm2.probBigram("I", "miss")
        # print "Trigram Prob:"      
        # print lm3.probTrigram("I", "miss", "something")
        # s = None
        # while s != 'quit':
        #         s = raw_input()
                
if __name__ == "__main__":
  main()
