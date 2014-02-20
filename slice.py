def do_all():

    import urllib2
    import re
    
#    train = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/bible_corpus/kjbible.train.html'
#    test  = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/bible_corpus/kjbible.test.html'
#    valid = 'file:///Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/bible_corpus/kjbible.valid.html'

    train = 'file://C:/Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/splitta/hotel_train.html'
    test  = 'file://C:/Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/splitta/hotel_test.html'
    valid = 'file://C:/Users/Asus/Documents/Cornell/Courses/2014Spring/Natural Language Processing/NLP_Proj1/splitta/hotel_valid.html'

    def getCorpus(a):
        """Returns: the string of corpus"""
        u = urllib2.urlopen(a)
        return u.read()
    
    def replace_starter(s):
        info1 = re.compile("/d:/d")
        info2 = re.compile("/d/d:/d")
        info3 = re.compile("\d:\d\d")
        info4 = re.compile("\d\d:\d\d")
        info5 = re.compile("  ")
        news = info4.sub("",s)
        news = info3.sub("",news)
        news = info2.sub("",news)
        news = info1.sub("",news)
        news = info5.sub(" ",news)
        return news
        
    def after_space_before_dot(s):
        """Returns: Substring of s; from but not including, the first space,
        and up to andincluding, the first dot
        Precondition: s has at least one space and one dot in it"""
        space = s.find(' ')
        dot   = s.find('.')
        sub  = "<s> "+s[(space+1):(dot+1)]+" </s>"
        return sub
    
    def after_space_before_question_mark(s):
        """Returns: Substring of s; from but not including, the first space,
        and up to andincluding, the first question mark
        Precondition: s has at least one space and one question mark in it"""
        space = s.find(' ')
        question   = s.find('?')
        sub  = "<s> "+s[(space+1):(question+1)]+" </s>"
        return sub
    
    def after_space_before_exclamation_mark(s):
        """Returns: Substring of s; from but not including, the first space,
        and up to andincluding, the first exclamation mark
        Precondition: s has at least one space and one exclamation mark in it"""
        space = s.find(' ')
        exclamation   = s.find('!')
        sub  = "<s> "+s[(space+1):(exclamation+1)]+" </s>"
        return sub
    
    def add_space_before_punctuation(s):
        s = s.replace(","," ,")
        s = s.replace(":"," :")
        s = s.replace(";"," ;")
        s = s.replace('"',' "')
        s = s.replace("'"," '")
        s = s.replace("."," .")
        s = s.replace("!"," !")
        s = s.replace("?"," ?")
        return s
    
    def slice(s):
        x = 0
        text = ""
        while x >=0:
            if min(s[x:].find('.'),s[x:].find('?'),s[x:].find('!')) == s[x:].find('.'):
                text += after_space_before_dot(s[x:]) + "\n"
                x += s[x:].find('.')+1
            if min(s[x:].find('.'),s[x:].find('?'),s[x:].find('!')) == s[x:].find('?'):
                text += after_space_before_question_mark(s[x:]) + "\n"
                x += s[x:].find('?')+1
            if min(s[x:].find('.'),s[x:].find('?'),s[x:].find('!')) == s[x:].find('!'):
                text += after_space_before_exclamation_mark(s[x:]) + "\n"
                x += s[x:].find('!')+1
            if s[x:].find('.') == -1 or s[x:].find('?') == -1 or s[x:].find('!') == -1:
                return text 
    
    tr = getCorpus(train)
    te = getCorpus(test)
    va = getCorpus(valid)
    
    tr = replace_starter(tr)
    te = replace_starter(te)
    va = replace_starter(va)
    
    tr = add_space_before_punctuation(slice(tr))
    te = add_space_before_punctuation(slice(te))
    va = add_space_before_punctuation(slice(va))
    
    trfile = file("train.txt","w")
    tefile = file("test.txt","w")
    vafile = file("valid.txt","w")

    print >> trfile, tr
    print >> tefile, te
    print >> vafile, va

    trfile.close()
    tefile.close()
    vafile.close()

if __name__ == '__main__':
    do_all()

