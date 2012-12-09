import random
from sys import argv
from mpi4py import MPI
from subset import Subset
from collections import Counter
import numpy as np

import dtree

p_root = 0
data_file = 'small_data.txt'
data_features_file = 'small_data_features.txt'
number_of_decision_trees = 12

def create_random_forest(comm, rank, data, features):

	size = comm.Get_size()
	data = comm.bcast(data, root=p_root)	

	forest = []
	for i in range(number_of_decision_trees):
		#boostrap sampling
		n, f = data.shape
		indices = [random.randint(0,n-1) for i in range(n)]
		subset = Subset(indices, data=data)
		decision_tree = dtree.create(subset, features)
		forest.append(decision_tree)

		# print "-------------"
		# print decision_tree
		# print "-------------"

	return forest

def get_reviews():

	f = open(data_features_file, 'r+')
	features = f.read().split(',')
	f.close()

	reviews = []

	f = open(data_file, 'r+')
	for line in f:
		reviews.append(dict(zip(line.split(','), features)))
	f.close()

	return reviews

def read():

	data = np.loadtxt(fname=data_file, delimiter=',')
	f = open(data_features_file, 'r+')
	features = f.read().split(',')
	f.close()

	return data, features

if __name__ == '__main__':

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	reviews = get_reviews()
	for review in reviews:
		print review

	if rank == p_root:
		data, features = read()
	else:
		data, features = None, None

	forest = create_random_forest(comm, rank, data, features)

	errors = 0
	for review in reviews:
		answers = []
		for tree in forest:
			answers.append(dtree.classify(tree, review))
		answer = Counter(answers)[0][0]
		if answer != review['star']:
			errors += 1

	print errors




	





