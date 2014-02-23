from gt_smoothing_lm import lm
from gen import *

def main():
       lm3 = lm.LangModel("sample.train", "sample.valid", 1)
       print lm3.prob_unigram("God")
#        lm2 = LangModel("sample.lm", 2)
#       print lm2.prob_bigram("God", "saw");

#        lm1 = LangModel("train.lm", 1)
 #       lm2 = LangModel("train.lm", 2)

        #lm1 = LangModel("hotel_corpus/hotel_train.txt", 1)
        # lm2 = LangModel("hotel_train.lm", 2)
        
        # g1 = generator(lm1,1)
        # g2 = generator(lm2,2)

        # print '------Sentences by Unigram Model------'
        # for i in range(3):
        #         g1.go(25)
        # print '------Sentences by Bigram Model------'
        # for i in range(3):
        #         g2.go(25)

        # print '------End------'
                
if __name__ == "__main__":
        main()
