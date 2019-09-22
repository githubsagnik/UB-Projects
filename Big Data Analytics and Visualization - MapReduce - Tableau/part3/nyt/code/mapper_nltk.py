import zipimport
importer = zipimport.zipimporter('nltkandyaml.mod')

nltk = importer.load_module('nltk')

import nltk
import string
import sys
#import spacy  
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 

nltk.download("wordnet")
#nltk.download('punkt')


def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def removeChars(words):
	words = words.replace('“','')
	words = words.replace('’','')
	words = words.replace('”','')
	words = words.replace('.','')
	words = words.replace(',','')
	words = words.replace(':','') 
	words = words.replace(';','')
	words = words.replace('(','')
	words = words.replace(')','')
	words = words.replace('!','')
	words = words.replace('?','')
	words = words.replace('$','') 
	words = words.replace('@','')
	words = words.replace('#','')
	words = words.replace('&','')
	words = words.replace('^','')
	words = words.replace('[','')
	words = words.replace(']','')
	words = words.replace('{','')
	words = words.replace('}','')
	words = words.replace('%','')
	words = words.replace('*','')
	words = words.replace('\'','')
	words = words.replace('\"','')
	words = words.replace('+','')
	words = words.replace('-','')
	words = words.replace('http','')
	words = words.replace('https','')
	if words in punctuation:
		return ''
	else:
		return words

        
def stemData(word):
    #ps = SnowballStemmer("english")
    #word = ps.stem(word)
    lemmatizer = WordNetLemmatizer()
    word = lemmatizer.lemmatize(word)
    return word

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    stop_words = set(stopwords.words('english'))
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        
        # tab-delimited; the trivial word count is 1

        
        for word in words:
            word = word.lower()
	    # to remove symbols and special characters
            word = removeChars(word)
            # to stem the data
            word = stemData(word)
        
            if word in stop_words or word in ('2019','january','2018','lady','melania','first','died','white','getty','photo','2017','take','bgunsense','bericswalwell','know','get','need','want','bNRA','bThe','You','’', '“', 'said', '”', 'wa', 'Mr', 'new', '—', 'hi', 'ha', 'thi', 'I','new','would','one','mr',
            	'two','also','use','last','say','like','right','unit','time','year','New','could','He','used','byBy','by','By','The','the','and','And','dont','Ms','One') or '/' in word or '\\' in word or word == '' or len(word) < 3:
                pass 
            else :
                print ('%s%s%d' % (word.lower(), separator, 1))

if __name__ == "__main__":
    main()
