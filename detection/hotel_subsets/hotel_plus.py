"""Need to change the path"""
##Truthful = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Truthful_train.sent.text'
##Nontruthful  = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Nontruthful_train.sent.text'
##Truthful = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Truthful_valid.sent.text'
##Nontruthful  = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Nontruthful_valid.sent.text'
##test = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/test.sent.text'
kaggle = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Kaggle.sent.text'

import urllib2

def after_space_before_return(s):
    """Returns: Substring of s; from but not including, the first space,
    and up to andincluding, the first dot
    Precondition: s has at least one space and one dot in it"""
    space = s.find(' ')
    ret   = s.find('/n')
    sub  = "<s> "+s[(space+2):(dot+1)]+" </s>"
    return sub

def getCorpus(a):
        """Returns: the string of corpus"""
        u = urllib2.urlopen(a)
        return u.read()

def add_space_return(s):
    """add space after '.' and ',', and add a return after '?' & '!'
    Also delete the 'IsTruthFul , IsPositive , review '"""
    s = s.replace("."," . ")
    s = s.replace(","," , ")
    s = s.replace("? ","? \n")
    s = s.replace("!","! ")
    s = s.replace("!  ","! \n")
    s = s.replace('IsTruthFul , IsPositive , review ', '')
    return s

def add_s_marks(s):
    """add '<s>' at the start of every sentece and '</s>' at the end.
    At the same time, remove the extra '<s></s>'"""
    text = ""
    fp = open(s)
    for line in fp:
        text += "<s> " + line[:(len(line)-1)] + "</s>" + '\n'
    text = text.replace('<s> </s>','')
    return text

if __name__ == '__main__':

##    t = getCorpus(Truthful)
##    Nt = getCorpus(Nontruthful) 
##    tt = getCorpus(test)
    k = getCorpus(kaggle)
    
##    t = add_space_return(t)
##    Nt = add_space_return(Nt)
##    tt = add_space_return(tt)
    k = add_space_return(k)
    
##    tfile = file("h_truthful_train.txt","w")
##    Ntfile = file("h_Nontruthful_train.txt","w")

##    tfile = file("h_truthful_valid.txt","w")
##    Ntfile = file("h_Nontruthful_valid.txt","w")
##    ttfile = file("h_test.txt","w")
    kfile = file("k_test.txt", "w")
    
##    print >> tfile, t
##    print >> Ntfile, Nt
##    print >> ttfile, tt
    print >> kfile, k
    
##    tfile.close()
##    Ntfile.close()
##    ttfile.close()
    kfile.close()
    
##    Ttrainfile = file("hotel_truthful_train.txt","w")
##    NTtrainfile = file("hotel_Nontruthful_train.txt","w")
##    Tvalidfile = file("hotel_truthful_valid.txt","w")
##    NTvalidfile = file("hotel_Nontruthful_valid.txt","w")
##    testfile = file("hotel_test.txt","w")
    kagglefile = file("kaggle_test.txt", "w")
    
##    print >> Ttrainfile, (add_s_marks('h_truthful_train.txt'))
##    print >> NTtrainfile, (add_s_marks('h_Nontruthful_train.txt'))
##    print >> Tvalidfile, (add_s_marks('h_truthful_valid.txt'))    
##    print >> NTvalidfile, (add_s_marks('h_Nontruthful_valid.txt'))    
##    print >> testfile, (add_s_marks('h_test.txt'))
    print >> kagglefile, (add_s_marks('k_test.txt'))
    
##    Ttrainfile.close()
##    NTtrainfile.close()
##    Tvalidfile.close()
##    NTvalidfile.close()
##    testfile.close()
    kagglefile.close()    
    
    

