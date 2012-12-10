import numpy as np

from classifier.forest import RandomForest

number_of_trees = 24
size = 'medium'
data_features_file = 'data/features.txt'
#data_testing_file = 'data/testing/%s.txt' % size
data_testing_file = 'data/testing/twitter.txt'
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

	total_diff = 0
	errors = 0
	reviews = get_reviews()
	off_by = [0]*5

	for review in reviews:
		answer = forest.classify(review)
		if answer != review['star']:
			diff = abs(answer-float(review['star']))
			off_by[int(diff)] += 1
			#print "Answer: %f, Star: %f, Diff: %f" %(answer, float(review['star']), diff) 
			errors += 1
			total_diff += diff

	print "%i error(s) / %i reviews. %f %% accuracy" % (errors, len(reviews), 100*float(len(reviews)-errors)/len(reviews))
	print "Average error %f" % (total_diff/errors)
	print "Average difference %f" % (total_diff/len(reviews))
	print "Differences"
	for i in range(1,5):
		print "%i difference - Count: %i, %f %% of errors" % (i, off_by[i], 100*off_by[i]/errors)