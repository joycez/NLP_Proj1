from lm import *
from gen import *

def main():
#        lm1 = LangModel("sample.lm", 1)
#        lm2 = LangModel("sample.lm", 2)
#       print lm2.prob_bigram("God", "saw");

        lm1 = LangModel("train.lm", 1)
        lm2 = LangModel("train.lm", 2)
        
        g1 = generator(lm1,1)
        g2 = generator(lm2,2)

        print '------Sentences by Unigram Model------'
        for i in range(3):
                g1.go(15)
        print '------Sentences by Bigram Model------'
        for i in range(3):
                g2.go(15)

        print '------End------'
                
if __name__ == "__main__":
        main()
