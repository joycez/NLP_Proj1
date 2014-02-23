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

        lm1 = GTLangModel("bible_train.lm", "bible_valid.lm", 1)
        lm2 = GTLangModel("bible_train.lm", "bible_valid.lm", 2)
        bible_test1 = test(lm1, 1, "bible_test.lm")
        bible_test2 = test(lm2, 2, "bible_test.lm")
        bible_test1.pp();
        bible_test2.pp();
        
        #lm1 = LangModel("hotel_corpus/hotel_train.txt", 1)
        #lm2 = LangModel("hotel_train.lm", 2)
        lm1 = GTLangModel("sample.train", "sample.valid", 1)
        lm2 = GTLangModel("sample.train", "sample.valid", 2)
        #lm1 = GTLangModel("../hotel_corpus/hotel_train.txt","../hotel_corpus/hotel_valid.txt", 1)
        #lm2 = GTLangModel("../hotel_corpus/hotel_train.txt","../hotel_corpus/hotel_valid.txt", 2)

        s = None
        while s != 'quit':
                s = raw_input()
                #print lm1.probUnigram("the")
                print lm2.probBigram("the", s)
                
if __name__ == "__main__":
  main()
