import sys

from classifier.forest import RandomForest
from preprocess import features

number_of_trees = 12
size = 'medium'
forest_file = 'data/classifiers/%i_trees_%s_training.txt' %(number_of_trees, size)
data_features_file = 'data/features.txt'

def get_features():
	fs = []
	
	f = open(data_features_file, 'r+')
	for line in f:
		fs.append(line.strip())
	f.close()

	return fs

if __name__ == '__main__':

	forest = RandomForest.load(forest_file)

	while True:

		print "Please enter a phrase to analyze it's sentiment:"
		text = sys.stdin.readline()

		if text == 'quit':
			break

		f = get_features()
		f.remove('star')
		print f
		print "====="
		print text
		processed_text = dict(zip(f, features.extract(text)))
		print "-----"
		print processed_text

		answer = forest.classify(processed_text)

		print str(answer),
		if answer < 3:
			print "Negative"
		elif answer > 3:
			print "Positive"
		else:
			print "Neutral"
		print "-----"