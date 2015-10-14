__author__ = 'Jeevan'

import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

def main():
   review_features_train = np.load('review_features_train.npy')
   sentiment_list_train = np.load('sentiment_list_train.npy') 
   review_features_test = np.load('review_features_test.npy')
   sentiment_list_test = np.load('sentiment_list_test.npy') 
   forest = RandomForestClassifier(n_estimators = 100) 
   forest = forest.fit( review_features_train, sentiment_list_train )
   result = forest.predict(review_features_test)
   confusion_mat = confusion_matrix(sentiment_list_test,result) 
   print confusion_mat
   accuracy = float(np.sum(confusion_mat.diagonal()))*100.0/len(sentiment_list_test)
   print "Accuracy Obtianed : ",accuracy
if __name__ =="__main__":
    main()
