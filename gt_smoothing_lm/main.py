from lm import *
from gen import *

def main():
  lm1 = GTLangModel("sample.train", "sample.valid", 1)
  lm2 = GTLangModel("sample.train", "sample.valid", 2)
  #lm1 = GTLangModel("../hotel_corpus/hotel_train.txt","../hotel_corpus/hotel_valid.txt", 1)
  #lm2 = GTLangModel("../hotel_corpus/hotel_train.txt","../hotel_corpus/hotel_valid.txt", 2)

  # g1 = generator(lm1,1)
  # g2 = generator(lm2,2)

  # print '------Sentences by Unigram Model------'
  # for i in range(3):
  #   g1.go(25)
  # print '------Sentences by Bigram Model------'
  # for i in range(3):
  #   g2.go(25)

  s = None
  while s != 'quit':
    s = raw_input()
    #print lm1.probUnigram("the")
    print lm2.probBigram("the", s)
                
if __name__ == "__main__":
  main()
