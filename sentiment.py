from sys import argv
import numpy as np
from mpi4py import MPI
from subset import Subset

import dtree

p_root = 0
data_file = 'small_data.txt'
data_features_file = 'small_data_features.txt'

def create_random_forest(comm, rank, data, features):

	size = comm.Get_size()
	data = comm.bcast(data, root=p_root)	
	
	h, w = data.shape
	indices = range(h)
	subset = Subset(indices, data=data)
	decision_tree = dtree.create(subset, features)

	print "-------------"
	print decision_tree
	print "-------------"

	print 



	#TODO - return the decision trees

def read():

	data = np.loadtxt(fname=data_file, delimiter=',')
	f = open(data_features_file, 'r+')
	features = f.read().split(',')
	f.close()

	return data, features

if __name__ == '__main__':

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	if rank == p_root:
		data, features = read()
	else:
		data, features = None, None



	rf = create_random_forest(comm, rank, data, features)




