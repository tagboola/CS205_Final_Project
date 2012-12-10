import random
import numpy as np

from sys import argv
from mpi4py import MPI

from classifier.tree import DecisionTree
from classifier.forest import RandomForest
from handler.serial.subset import Subset
from handler.cuda.subset import SubsetCUDA

size = 'medium'
data_features_file = 'data/features.txt'
data_training_file = 'data/training/%s.txt' % size
data_testing_file = 'data/testing/%s.txt' % size
number_of_trees = 12
p_root = 0


def parallel_create_random_forest(comm, rank, data, features):
	size = comm.Get_size()

	features = comm.bcast(features, root=p_root)
	data = comm.bcast(data, root=p_root)	

	num_trees = int(number_of_trees/size)
	if rank < number_of_trees%size:
		num_trees += 1	

	trees = []
	for t in range(num_trees):
		#boostrap sampling
		n, f = data.shape
		indices = [random.randint(0,n-1) for i in range(n)]
		subset = Subset(indices, data=data)
		decision_tree = DecisionTree(subset, features)
		trees.append(decision_tree)

	trees = comm.gather(trees, root=p_root)

	if rank == p_root:
		#flatten array
		trees = [t for tree in trees for t in tree]

	return trees

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

def get_data():
	data = np.loadtxt(fname=data_training_file, delimiter=',')
	return data


if __name__ == '__main__':

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	if rank == p_root:
		data = get_data()
		features = get_features()
	else:
		data, features = None, None

	trees = parallel_create_random_forest(comm, rank, data, features)

	if rank == p_root:
		print "Random Forest was built. Beginning classification."
		forest = RandomForest(trees)
		errors = 0
		reviews = get_reviews()
		for review in reviews:
			answer = forest.classify(review)
			if answer != review['star']:
				print "Answer: %f, Star: %f" %(answer, float(review['star'])) 
				errors += 1

		print "%i error(s) / %i reviews. %f %% accuracy" % (errors, len(reviews), 100*float(len(reviews)-errors)/len(reviews))
