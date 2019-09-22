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
    data_type = sys.argv[1]
    stop_words = set(stopwords.words('english'))
    
    nyt = ['gun','law','people','shooting','police','zealand','firearm','gunman','weapon','state']

    twitter = ['nra','gun','rifle','guncontrol','weapon','amp','firearm','gunsense','people','shooting']

    cc = ['nra','gun','law','shooting','legislation','firearm','program','legal','woman','bill']

    cc1day = ['gun','control','school','death','state','law','social','marijuana','age','suicide']
    
    if(data_type=='nyt'):
    	wordList = nyt
    if(data_type=='twitter'):
    	wordList = twitter
    if(data_type=='cc'):
    	wordList = cc
    if(data_type=='cc1day'):
    	wordList = cc1day

    for words in data:

        length = len(words)
        for i in range(0,length-1):
            word1 = words[i]
            word2 = words[i+1]
            word1 = removeChars(word1)
            word2 = removeChars(word2)
            word1 = stemData(word1)
            word2 = stemData(word2)
            word1 = word1.lower()
            word2 = word2.lower()
            if word1 in stop_words or word2 in stop_words or word1 in ('bericswalwell','know','get','need','want','bNRA','bThe','You','’', '“', 'said', '”', 'wa', 'Mr', 'new', '—', 'hi', 'ha', 'thi',
            'I','new','would','one','mr','two','also','use','last','say','like','right','unit','time','year','New','could','He','used','byBy',
            'by','By','The','the','and','And','dont','Ms','One') or word2 in ('bericswalwell','know','get','need','want','bNRA','bThe','You','’', '“', 'said', '”', 'wa', 'Mr', 'new', '—', 'hi', 'ha', 'thi', 
            'I','new','would','one','mr','two','also','use','last','say','like','right','unit','time','year','New','could','He','used','byBy','by',
            'By','The','the','and','And','dont','Ms','One') or '/' in word1 or '\\' in word1 or word1 == '' or len(word1) < 3 or '/' in word2 or '\\' in word2 or word2 == '' or len(word2) < 3:
                pass
            else:
                if(word1 in wordList and word2 in wordList):
                    word_cooccur = word1 +","+ word2
                    print ('%s%s%d' % (word_cooccur, separator, 1))
        	
        	

if __name__ == "__main__":
    main()
