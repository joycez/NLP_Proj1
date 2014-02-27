import re

tr = ''
te = ''
va = ''

def open_file(s):
    t = ''
    fp = open(s)
    for line in fp:
        t += line
    return t 

    
def replace(s):
    #delete "IsTruthFul,IsPositive,review'"
    s = s.replace("IsTruthFul,IsPositive,review'",'')
    
    #add sentence mark after every sentence
    s = s.replace(". ",'. </s> <s> ')
    s = s.replace("! ",'! </s> <s> ')
    s = s.replace("? ",'? </s> <s> ')
    
    s = s.replace(".'",".' </s> <s> ")
    s = s.replace("!'","!' </s> <s> ")
    s = s.replace("?'","?' </s> <s> ")
    
    s = s.replace('."','." </s> <s> ')
    s = s.replace('!"','!" </s> <s> ')
    s = s.replace('?"','?" </s> <s> ')
    
    #delete the addtional <s> at every paragraph
    s = s.replace(" </s> <s> \n",' </s> \n')
    
    #tokenize the punctuations
    s = s.replace(":"," : ")
    s = s.replace(";"," ; ")
    s = s.replace('"',' " ')
    s = s.replace("."," . ")
    s = s.replace("!"," ! ")
    s = s.replace("?"," ? ")
    s = s.replace("'"," '")
    
    #delete addtional blank
    s = s.replace("   "," ")
    s = s.replace("  "," ")
    
    #fix the "Mr." "Mrs." problem
    s = s.replace(". </s> <s> . </s> <s> . </s> <s>","... </s> <s>")
    s = s.replace("! </s> <s> ! </s> <s> ! </s> <s>","!!! </s> <s>")
    s = s.replace("? </s> <s> ? </s> <s> ? </s> <s>","??? </s> <s>")
    
    #fix the "..." "!!!" "???" problem
    s = s.replace("Mr . </s> <s> ", "Mr. ")
    s = s.replace("Mrs . </s> <s> ", "Mrs. ")
    
    #delete the " ? , " at the beginning of every paragraph
    s = s.replace(" ? , ? , ", "")
    
    #delete the addtional </s> at the end of text
    s = s[:(len(s)-4)]
    
    return s
    
    
def r(s):
    #replace unknown words with "'"
    unknown = re.compile(ur'[^a-zA-Z0-9,.<>;\':\"!\?\-$% ]')
    s = unknown.sub("'",s)
    
    #replace the start of every paragraph
        #for train and valid
    start1 = re.compile(r'0,0,')
    s = start1.sub("\n0,0, <s> ",s)
    start2 = re.compile(r'0,1,')
    s = start2.sub("\n0,1, <s> ",s)
    start3 = re.compile(r'1,0,')
    s = start3.sub("\n1,0, <s> ",s)
    start4 = re.compile(r'1,1,')
    s = start4.sub("\n1,1, <s> ",s)
        #for test
    start5 = re.compile(r'\?,\?,')
    s = start5.sub("\n?,?, <s> ",s)
    return s
    
if __name__ == '__main__':
    
    tr = open_file("reviews.train.txt")
    te = open_file("reviews.test.txt")
    va = open_file("reviews.valid.txt")
    
    trfile = file("hotel_train.txt","w")
    tefile = file("hotel_test.txt","w")
    vafile = file("hotel_valid.txt","w")
    
    print >> trfile, replace(r(tr))
    print >> tefile, replace(r(te))
    print >> vafile, replace(r(va))
    
    trfile.close()
    tefile.close()
    vafile.close()

    
    
    
    