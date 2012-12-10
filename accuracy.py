import random
import numpy as np

from mpi4py import MPI
from classifier.forest import RandomForest

number_of_trees = 12#24
size = 'medium'#'large'
data_features_file = 'data/features.txt'
data_testing_file = 'data/testing/%s.txt' % size
forest_file = 'data/classifiers/%i_trees_%s_training.txt' %(number_of_trees, size)

def get_reviews():
	features = get_features()
	reviews = []

	f = open(data_testing_file, 'r+')
	for line in f:
		reviews.append(dict(zip(features, np.float64(line.split(',')))))
	f.close()

	return reviews


def get_features():
	features = []
	
	f = open(data_features_file, 'r+')
	for line in f:
		features.append(line.strip())
	f.close()

	return features


if __name__ == '__main__':

	forest = RandomForest.load(forest_file)

	errors = 0
	reviews = get_reviews()
	for review in reviews:
		answer = forest.classify(review)
		if answer != review['star']:
			print "Answer: %f, Star: %f" %(answer, float(review['star'])) 
			errors += 1

	print "%i error(s) / %i reviews. %f %% accuracy" % (errors, len(reviews), 100*float(len(reviews)-errors)/len(reviews))