__author__ = 'Jeevan'

"""
Reducer program takes the sorted and shuffled output from mapper and  
prepares bag-of-words for the test data.
"""

import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer # to convert reviews into a matrix of token counts

def main():
    label_list = []
    review_list = []
    for line in sys.stdin:
        label,id,review = line.strip().split('\t')
        print '%s\t%s\t%s' % (label,id,review) # to maintain the output in hdfs
        label_list.append(label)
        review_list.append(review) # complete list of test review sentences from both pos and neg labels
    vocab = np.load('vocab.npy') # load vocabulary generated from train data
    vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 10000,vocabulary = vocab) # create vectorizer with train data vocab
    review_features_test = vectorizer.transform(review_list) # transform all reviews into term matrix
    review_features_test = review_features_test.toarray()
    np.save('review_features_test',review_features_test) # saving the numpy array into file, used to predict
    np.save('sentiment_list_test',np.array(label_list))
if __name__ =="__main__":
    main()
