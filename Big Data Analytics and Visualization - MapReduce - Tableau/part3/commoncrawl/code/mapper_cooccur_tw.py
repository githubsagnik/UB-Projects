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
    top10 = sys.argv[1]
    stop_words = set(stopwords.words('english'))
    
    firearm = ['gun','firearms','firearm','concealedcarry','ccw','marchforourlives','amp','carry','concealed','nra']

    nra = ['nra','gun','amp','trump','maga','gop','violence','people','member','america']

    gunman = ['rifle','weapon','assault','gun','amp','war','ericswalwell','people','weapons','think']

    gunsense = ['gun','nra','gunsense','marchforourlives','gunviolence','violence','amp','people','shooting','law']

    guncontrol = ['gun','law','guncontrol','people','amp','control','ban','nra','shooting','violence']
    
    if(top10=='firearm'):
    	wordList = firearm
    if(top10=='nra'):
    	wordList = nra
    if(top10=='gunman'):
    	wordList = gunman
    if(top10=='gunsense'):
    	wordList = gunsense
    if(top10=='guncontrol'):
    	wordList = guncontrol
    

    for words in data:

        length = len(words)
        for i in range(0,length-1):
        	word1 = words[i]
        	word2 = words[i+1]

        	word1 = removeChars(word1)
        	word2 = removeChars(word2)

        	word1 = stemData(word1)
        	word2 = stemData(word2)

        	if word1 in stop_words or word2 in stop_words or word1 in ('bgunsense','bericswalwell','know','get','need','want','bNRA','bThe','You','’', '“', 'said', '”', 'wa', 'Mr', 'new', '—', 'hi', 'ha', 'thi',
             'I','new','would','one','mr','two','also','use','last','say','like','right','unit','time','year','New','could','He','used','byBy',
             'by','By','The','the','and','And','dont','Ms','One') or word2 in ('bgunsense','bericswalwell','know','get','need','want','bNRA','bThe','You','’', '“', 'said', '”', 'wa', 'Mr', 'new', '—', 'hi', 'ha', 'thi', 
             'I','new','would','one','mr','two','also','use','last','say','like','right','unit','time','year','New','could','He','used','byBy','by',
             'By','The','the','and','And','dont','Ms','One') or '/' in word1 or '\\' in word1 or word1 == '' or len(word1) < 3 or '/' in word2 or '\\' in word2 or word2 == '' or len(word2) < 3:
        		pass
        	else:
        		if(word1.lower() in wordList and word2.lower() in wordList):
        			word_cooccur = word1.lower() +","+ word2.lower()
        			print ('%s%s%d' % (word_cooccur, separator, 1))
        	
        	

if __name__ == "__main__":
    main()
