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
		text = sys.stdin.readline().strip()

		if text == 'quit':
			break
		elif text == '':
			continue

		f = get_features()
		f.remove('star')
		processed_text = dict(zip(f, features.extract(text)))

		answer = forest.classify(processed_text)

		if answer < 3:
			print "Negative\n"
		elif answer > 3:
			print "Positive\n"
		else:
			print "Neutral\n"