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
    #delete  "IsTruthful,review"
    s = s.replace("IsTruthful,review",'')
    
    #add sentence mark before every paragraph
    s = s.replace("?,","?, <s> ")
    
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
    s = s.replace("Mr . </s> <s> ", "Mr. ")
    s = s.replace("Mrs . </s> <s> ", "Mrs. ")
    
    #fix the "..." "!!!" "???" problem
    s = s.replace(". </s> <s> . </s> <s> . </s> <s>","... </s> <s>")
    s = s.replace("! </s> <s> ! </s> <s> ! </s> <s>","!!! </s> <s>")
    s = s.replace("? </s> <s> ? </s> <s> ? </s> <s>","??? </s> <s>")
    
    #delete the " ? , " at the beginning of every paragraph
    s = s.replace(" ? , ", "")
    
    return s
    

if __name__ == '__main__':
    kt = open_file("kaggle_test.txt")
    ktfile = file("KTest.txt","w")
    print >> ktfile, replace(kt)
    ktfile.close()