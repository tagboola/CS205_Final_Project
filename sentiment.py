from sys import argv
import numpy as np
from mpi4py import MPI
from subset import Subset

p_root = 0

def create_random_forest(comm, rank, data):

	size = comm.Get_size()

	data = comm.bcast(data, root=p_root)	
	
	subset = Subset(data)
	decision_tree = DecisionTree(subset)

	#TODO - return the decision trees


if __name__ == '__main__':

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	if rank == p_root:
		data = read(data) #TODO
	else:
		data = None


	rf = create_random_forest(comm, rank, data)




