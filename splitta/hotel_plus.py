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
    train = 'file:///Users/jianjiang/Desktop/splitta/train.sent.text'
    test  = 'file:///Users/jianjiang/Desktop/splitta/test.sent.text'
    valid = 'file:///Users/jianjiang/Desktop/splitta/valid.sent.text'


    def getCorpus(a):
        """Returns: the string of corpus"""
        u = urllib2.urlopen(a)
        return u.read()
            
    tr = getCorpus(train)
    te = getCorpus(test)
    va = getCorpus(valid)
    
    tr = slice(tr)
    te = slice(te)
    va = slice(va)

    trfile = file("hotel_train.txt","w")
    tefile = file("hotel_test.txt","w")
    vafile = file("hotel_valid.txt","w")

    print >> trfile, tr
    print >> tefile, te
    print >> vafile, va

    trfile.close()
    tefile.close()
    vafile.close()


if __name__ == '__main__':
    do_all()