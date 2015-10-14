__author__ = 'Jeevan'
"""
Reducer program takes the sorted and shuffled output from mapper and  
prepares bag-of-words for the train data.
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
        review_list.append(review) # complete list of review sentences from both pos and neg labels
    vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 10000) # to prepare bag of words
    review_features_train = vectorizer.fit_transform(review_list) # learns vocabulary dictionary and return term-document matrix
    review_features_train = review_features_train.toarray() # converting into numpy array
    vocab = vectorizer.get_feature_names() # getting the feature names as vocab
    np.save('vocab',vocab)
    np.save('review_features_train',review_features_train) # saving the numpy array in files, which can be used to predict
    np.save('sentiment_list_train',np.array(label_list))
if __name__ =="__main__":
    main()
