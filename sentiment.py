from sys import argv
import numpy as np
from mpi4py import MPI
from subset import Subset

import dtree

p_root = 0
data_file = 'small_data.txt'
data_features_file = 'small_data_features.txt'

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object. 
    """
    if type(tree) == dict:
        print "%s%s" % (str, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (str, item)
            print_tree(tree.values()[0][item], str + "\t")
    else:
        print "%s\t->\t%s" % (str, tree)


def create_random_forest(comm, rank, data, features):

	size = comm.Get_size()
	data = comm.bcast(data, root=p_root)	
	
	h, w = data.shape
	indices = range(h)
	subset = Subset(indices, data=data)
	decision_tree = dtree.create(subset, features)

	print "-------------"
	print print_tree(decision_tree,"")
	print "-------------"

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




