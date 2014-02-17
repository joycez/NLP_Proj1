def do_all():

    import urllib2

    train = 'file:///Users/jianjiang/Desktop/bible_corpus/kjbible.train.html'
    test  = 'file:///Users/jianjiang/Desktop/bible_corpus/kjbible.test.html'
    valid = 'file:///Users/jianjiang/Desktop/bible_corpus/kjbible.valid.html'

    def getCorpus(a):
        """Returns: the string of corpus"""
        u = urllib2.urlopen(a)
        return u.read()

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
        s = s.replace("'"," ' ")
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
                x += s[x:].find('.')+2
            if min(s[x:].find('.'),s[x:].find('?'),s[x:].find('!')) == s[x:].find('?'):
                text += after_space_before_question_mark(s[x:]) + "\n"
                x += s[x:].find('?')+2
            if min(s[x:].find('.'),s[x:].find('?'),s[x:].find('!')) == s[x:].find('!'):
                text += after_space_before_exclamation_mark(s[x:]) + "\n"
                x += s[x:].find('!')+2
            if s[x:].find('.') == -1 or s[x:].find('?') == -1 or s[x:].find('!') == -1:
                return text 
    
    tr = getCorpus(train)
    te = getCorpus(test)
    va = getCorpus(valid)
    
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

