__author__ = 'Jeevan'

import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def main():
    # for line in sys.stdin:
        # line = line.strip()
        # label,id,tokens = line.split('\t')
        # print '%s\t%s\t%s' % (label,id,tokens)
    label_list = []
    review_list = []
    for line in sys.stdin:
        label,id,review = line.strip().split('\t')
        print '%s\t%s\t%s' % (label,id,review)
        label_list.append(label)
        review_list.append(review)
    vocab = np.load('vocab.npy')
    vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 10000,vocabulary = vocab)
    review_features_train = vectorizer.transform(review_list)
    review_features_train = review_features_train.toarray()
    np.save('review_features_test',review_features_train)
    np.save('sentiment_list_test',np.array(label_list))
if __name__ =="__main__":
    main()
