__author__ = 'Jeevan'
"""
Mapper program takes  input files from the hadoop job, i.e data from pos and neg 
folders from both training and testing.
"""
import sys
import glob
from nltk.corpus import stopwords # Import the stop word list
import re
from bs4 import BeautifulSoup # Imported to remove html tags from the review data
def main():
    from nltk.stem import SnowballStemmer # Imported to perform stemming on the data
    stemmer = SnowballStemmer('english')
    stop_words = stopwords.words("english")
    for line in sys.stdin:
        line = line.strip()
        id,label,review = line.split('||') # Separates each line into id,label,review
        html_strip = BeautifulSoup(review,'html.parser')
        words = re.sub("[^a-zA-Z]"," ",html_strip.get_text() )
        words = words.split()
        words = [w.lower() for w in words if w.lower() not in stop_words] #collecting words which are not stop words
        words = [stemmer.stem(word) for word in words]
        print '%s\t%s\t%s' % (label,id,' '.join(words)) # Mapper output with Label as key and the rest are values
if __name__ =="__main__":
    main()
