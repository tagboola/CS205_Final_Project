CS 205 Final Project - Sentiment Analysis
=========================================

###Authors

* Tunde Agboola
* Omar Shammas
* Shashank Sunkavalli


###Description

A sentiment analysis tool that will output a rating between 1 (negative) and 5 (positive) for a given text. A random forest classifier is built using MPI and trained on the Yelp! academic dataset, which was pre-processed using MapReduce.

DATASET : A dataset of ~300,000 annotated Yelp! reviews was split into training corpus and testing corpus (in a 4:1 ratio). All the data is in the folder 'data'.

CODE : The code is basically divided into 3 phases :
	* Pre-processing data : [code is present in the mapreduce folder]. Using MapReduce, a feature set was created from the training and testing data. The feature set consists of :
		* One-Gram scores 
		* One-Gram count
		* Bi-Gram score
		* Bi-Gram count
		* Positive Word count
		* Negative Word count
		* Character count
		* Count of Uppercase letters
		* Count of Lowercase letters
		* Count of punctuation characters
		* Count of alphabets
		* Count of numbers
		* Ratio of Uppercase to Lowercase characters
		* Ratio of Alphabets to Total Character count
		The One-gram and Bi-gram scores for the text are calculated based on an index of one-gram and bi-gram scores created using the entire training corpus.
	* Creating and Training the Random Forests : [code is present in train.py] Using the training data, a Random Forest (group of Decision Trees) are created. First the training data given as input is sampled with replacement to create a random sample to train each Decision Tree. The number of Decision Trees, the threshold for purity of the feature , and the number of features used for splitting at each node of each Decision Tree is configurable. Once the Random Forest is trained, it is saved in a serialized format for making predictions.
	* Prediction : [code is present in accuracy.py] The data given as input for prediction is pre-processed to extract a feature set. This feature set is taken in as input to predict the sentiment [a rating] on a scale of 1-5, where 1 represents 'unhappiness' and 5 represents 'happiness'. When tested against testing data derived from the Yelp! dataset, the code shows the predicted rating, the overall accuracy of predictions, the number of instances for each time the difference between the predicted rating and the actual rating is 1, 2, 3 and 4.
