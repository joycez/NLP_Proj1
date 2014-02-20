import re

"""
A list of (regexp, repl) pairs applied in sequence.
The resulting string is split on whitespace.
(Adapted from the Punkt Word Tokenizer)
"""

_tokenize_regexps = [
    
    # for hotel train
    (re.compile(r'([\d],[\d],)'),r''),
    (re.compile(ur'([^a-zA-Z0-9,.<>;\':\"!\?\-$% ])'),r"'"),
    (re.compile(r"'(?=\W)"),r''),
    
    #for hotel test
    (re.compile('\?,\?,+'),''),
    (re.compile('!+'),'!'),
    
    # for hotel valid
    #same as for hotel train
    
    # uniform quotes
    (re.compile(r'\'\''), r'"'),
    (re.compile(r'\`\`'), r'"'),

    # Separate punctuation (except period) from words:
    (re.compile(r'(^|\s)(\')'), r'\1\2 '),
    (re.compile(r'(?=[\(\"\`{\[:;&\#\*@])(.)'), r'\1 '),
    
    (re.compile(r'(.)(?=[?!)\";}\]\*:@\'])'), r'\1 '),
    (re.compile(r'(?=[\)}\]])(.)'), r'\1 '),
    (re.compile(r'(.)(?=[({\[])'), r'\1 '),
    (re.compile(r'((^|\s)\-)(?=[^\-])'), r'\1 '),

    # Treat double-hyphen as one token:
    (re.compile(r'([^-])(\-\-+)([^-])'), r'\1 \2 \3'),
    (re.compile(r'(\s|^)(,)(?=(\S))'), r'\1\2 '),

    # Only separate comma if space follows:
    (re.compile(r'(.)(,)(\s|$)'), r'\1 \2\3'),

    # Combine dots separated by whitespace to be a single token:
    (re.compile(r'\.\s\.\s\.'), r'...'),

    # Separate "No.6"
    (re.compile(r'([A-Za-z]\.)(\d+)'), r'\1 \2'),
    
    # Separate words from ellipses
    (re.compile(r'([^\.]|^)(\.{2,})(.?)'), r'\1 \2 \3'),
    (re.compile(r'(^|\s)(\.{2,})([^\.\s])'), r'\1\2 \3'),
    (re.compile(r'([^\.\s])(\.{2,})($|\s)'), r'\1 \2\3'),

    ## adding a few things here:

    # fix %, $, &
    (re.compile(r'(\d)%'), r'\1 %'),
    (re.compile(r'\$(\.?\d)'), r'$ \1'),
    (re.compile(r'(\w)& (\w)'), r'\1&\2'),
    (re.compile(r'(\w\w+)&(\w\w+)'), r'\1 & \2'),

    # fix (n 't) --> ( n't)
    (re.compile(r'n \'t( |$)'), r" n't\1"),
    (re.compile(r'N \'T( |$)'), r" N'T\1"),

    # treebank tokenizer special words
    (re.compile(r'([Cc])annot'), r'\1an not'),
    (re.compile(r'\s+'), r' '),

        
    ]

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
        

def tokenize(s):
    """
    Tokenize a string using the rule above
    """

    for (regexp, repl) in _tokenize_regexps:
        s = regexp.sub(repl, s)   
    return s

