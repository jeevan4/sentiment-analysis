__author__ = 'Jeevan'

import sys
import glob
from nltk.corpus import stopwords # Import the stop word list
import re
from bs4 import BeautifulSoup
def main():
    from nltk.stem import SnowballStemmer
    stemmer = SnowballStemmer('english')
    stop_words = stopwords.words("english")
    for line in sys.stdin:
        line = line.strip()
        id,label,review = line.split('||')
        html_strip = BeautifulSoup(review,'html.parser')
        words = re.sub("[^a-zA-Z]"," ",html_strip.get_text() )
        # print words.split()
        words = words.split()
        words = [w.lower() for w in words if w.lower() not in stop_words]
        # print "pos\t",','.join(words)
        words = [stemmer.stem(word) for word in words]
        print '%s\t%s\t%s' % (label,id,' '.join(words))
if __name__ =="__main__":
    main()
