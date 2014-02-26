from lm import *
from detection import *
from classifier import *

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
##        lm1 = GTLangModel("bible_train.lm", "bible_valid.lm", 1)
##        lm2 = GTLangModel("bible_train.lm", "bible_valid.lm", 2)
##        bible_test1 = test(lm1, 1, "bible_test.lm")
##        bible_test2 = test(lm2, 2, "bible_test.lm")
##        bible_test1.pp();
##        bible_test2.pp();
##
##        lm1 = GTLangModel("hotel_train.lm", "hotel_valid.lm", 1)
##        lm2 = GTLangModel("hotel_train.lm", "hotel_valid.lm", 2)
##        hotel_test1 = test(lm1, 1, "hotel_test.lm")
##        hotel_test2 = test(lm2, 2, "hotel_test.lm")
##        hotel_test1.pp();
##        hotel_test2.pp();
        
#  ----     part3       ----

##        c1 = classifier("hotel_train.lm", 'train')
##        c2 = classifier("hotel_valid.lm", 'valid')
        
        d1 = detector("hotel_truthful_train.lm", "hotel_Nontruthful_train.lm", "hotel_truthful_valid.lm", "hotel_Nontruthful_valid.lm", 1)
        d1.detect("hotel_test.lm")
        d1.detect("KTest.txt")
        d2 = detector("hotel_truthful_train.lm", "hotel_Nontruthful_train.lm", "hotel_truthful_valid.lm", "hotel_Nontruthful_valid.lm", 2)
        d2.detect("hotel_test.lm")
        d2.detect("KTest.txt")
     
##
##        s = None
##        while s != 'quit':
##                s = raw_input()
##                
if __name__ == "__main__":
  main()
