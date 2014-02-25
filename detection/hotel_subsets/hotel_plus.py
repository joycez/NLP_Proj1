def after_space_before_dot(s):
    """Returns: Substring of s; from but not including, the first space,
    and up to andincluding, the first dot
    Precondition: s has at least one space and one dot in it"""
    space = s.find(' ')
    dot   = s.find('.')
    sub  = "<s> "+s[(space+1):(dot+1)]+" </s>"
    return sub

def slice(s):
    x = 0
    text = ""
    if x== 0:
        dot = s.find('.')
        text += "<s> " + s[:(dot+1)] + " </s>" + '\n'
        x += dot + 1
    while x >0:
        text += after_space_before_dot(s[x:]) + "\n"
        if s[x:].find('.') == -1:
            return text 
        x += s[x:].find('.')+1
        
import urllib2
import re

def do_all():    
##    Truthful = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Truthful_train.sent.text'
##    Nontruthful  = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Nontruthful_train.sent.text'

##    Truthful = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Truthful_valid.sent.text'
##    Nontruthful  = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/Nontruthful_valid.sent.text'

    test = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/detection/hotel_subsets/test.sent.text'

    def getCorpus(a):
        """Returns: the string of corpus"""
        u = urllib2.urlopen(a)
        return u.read()

##    t = getCorpus(Truthful)
##    Nt = getCorpus(Nontruthful) 
    tt = getCorpus(test)

##    t = slice(t)
##    Nt = slice(Nt)
    tt = slice(tt)

##    tfile = file("hotel_truthful_train.txt","w")
##    Ntfile = file("hotel_Nontruthful_train.txt","w")

##    tfile = file("hotel_truthful_valid.txt","w")
##    Ntfile = file("hotel_Nontruthful_valid.txt","w")
    ttfile = file("hotel_test.txt","w")

##    print >> tfile, t
##    print >> Ntfile, Nt
    print >> ttfile, tt
    
##    tfile.close()
##    Ntfile.close()
    ttfile.close()

if __name__ == '__main__':
    do_all()
