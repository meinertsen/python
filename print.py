# Print text-based documents in the console
# print(chr(27) + "[2J")

import os, re, nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

# Open document and create tokens for each sentence
# This function will ONLY treat Double Newline ('\n\n' or '\n \n') as a seperator NOT Single Newline ('\n')
def tread(s):
    tread = open(s, 'r').read()
    tread = unicode(tread, errors='ignore')
    while '  ' in tread:
        tread = tread.replace('  ', ' ')
    tread = re.split('\\\n\\\n|\\\n\\ \\\n',tread)
    lst=[]
    for each in tread:
        lst.extend(tokenizer.tokenize(each))
    z = map( lambda x: " ".join(x.replace('\n', " ").split()),lst)
    return z
# This functions prints your document to the console one character at the time using time.sleep delay
def dprint(s): 
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)

# Defines sprint function that calls tread and dprint
def sprint(s): # Prints sentences
x = tread(s)
print(chr(27) + "[2J")
for each in x:
    print '\n'
    dprint(each)
    
# Call sprint function using file name as argument
sprint(s)
