__author__ = 'Jeevan'

"""
Predictor program takes the test and train vectors as input from saved numpy files and  
implements RandomForestClassifier to learn and predit the labels
Output : Confusion Matrix and Accuracy
"""

import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier # To implement Random Forest Classifier
from sklearn.metrics import confusion_matrix # imported to implement confusion matrix

def main():
   review_features_train = np.load('review_features_train.npy')
   sentiment_list_train = np.load('sentiment_list_train.npy') 
   review_features_test = np.load('review_features_test.npy')
   sentiment_list_test = np.load('sentiment_list_test.npy') 
   forest = RandomForestClassifier(n_estimators = 100) # initialize random forest classifier with 100 n-estimators
   forest = forest.fit( review_features_train, sentiment_list_train ) # Build a forest of trees from training set
   result = forest.predict(review_features_test) # Predict classes for Test set
   confusion_mat = confusion_matrix(sentiment_list_test,result) # Calculation of Confusion Matrix
   print confusion_mat
   accuracy = float(np.sum(confusion_mat.diagonal()))*100.0/len(sentiment_list_test) # Calculation of Accuracy
   print "Accuracy Obtained : ",accuracy
if __name__ =="__main__":
    main()
