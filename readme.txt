Performed Sentiment Analysis as part of Bigdata class challenge over a large movie review dataset found here: http://ai.stanford.edu/~amaas/data/sentiment/ 

The dataset contains binary sentiment classification for 50,000 highly polar movie reviews.

Tasks Done :

Implemented in Hadoop file system as the dataset is large. Done the following in MapReduce with Hadoop Streaming API.

1. Preprocessing : removed html tags, junk characters, stop words and performed stemming.
2. Data Representation : Bag-of-words representation.SciKit Learn toolbox’s feature_extraction module is used to generate a matrix of token counts.
3. Classification : Used Random Forest to classify the reviews. Trained the model with train dataset and predicted the unknown labels for test dataset
4. Evaluation : Predicted the unknown labels with an accuray of 84.984

Confusion Matrix :

[10735  1765]
[ 1989 10511]

Command to run for Train Dataset:

 hadoop jar /opt/local/data_science/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper 'python /users/jeevan4/mapper.py' -reducer 'python /users/jeevan4/reducer.py' -input  /users/jeevan4/try1/train_neg_new.txt  -input  /users/jeevan4/try1/train_pos_new.txt  -output /users/jeevan4/try2/classify-train/

Command to run for Test Dataset:

 hadoop jar /opt/local/data_science/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper 'python /users/jeevan4/mapper.py' -reducer 'python /users/jeevan4/test_data_recuder.py' -input  /users/jeevan4/try1/test_neg_new.txt  -input  /users/jeevan4/try1/test_pos_new.txt  -output /users/jeevan4/try2/classify-test/
