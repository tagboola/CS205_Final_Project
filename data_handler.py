import math 
import random
import numpy as np
from data_handler_base import DataHandlerBase

class DataHandler(DataHandlerBase):

	LABEL_INDEX = 0

	def __init__(self, data):
		self.data = np.float64(data)

	def get_shape(self):
		"""
		Returns the shape of all the data
		"""
		return self.data.shape

	def get_freq(self, indices):
		"""
		Creates a frequency hash of the unique labels
		in the subset determined by the input indices
		"""
		freq = {}
		for index in indices:
			key = self.data[index][self.LABEL_INDEX]
			if freq.has_key(key):
				freq[key] += 1
			else:
				freq[key] = 1
		return freq


	def gini_index(self, indices):
		"""
		Calcutes the gini index of the data
		"""
		freq = self.get_freq(indices)
		gini = 0
		# For all unique label values, sum up the squares
		# and then subtract 1 from this sum to get the gini index
		for value in freq.values():
			gini += math.pow(float(value)/len(indices),2)
		return 1 - gini
	
	def get_threshold(self, feature, indices):
		"""
		Calculates a random threshold for the given feature by
		determining the min and max values
		"""
		min_val = 10000000
		max_val = -1
		for index in indices:
			val = self.data[index][feature]
			if val > max_val:
				max_val = val
			if val < min_val:
				min_val = val
		# Create a random threshold in between the min and max values
		return random.random()*(max_val-min_val) + min_val		

	def test_split(self, indices, feature):
		"""
		Calculates gini index by applying the a split using
		a random threshold on the given feature
		"""
		threshold = self.get_threshold(feature, indices)
		# Initialize variables
		freq1, freq2 = {}, {}
		n1, n2 = 0, 0
		# Compute the frequency of the labels for the two
		# two subsets i.e <= threshold or > threshold
		for index in indices:
			key = self.data[index][LABEL_INDEX]
			if self.data[index][feature] <= threshold:
				n1 += 1
				if freq1.has_key(key):
					freq1[key] += 1
				else:
					freq1[key] = 1  
			else:
				n2 += 1
				if freq2.has_key(key):
					freq2[key] += 1
				else:
					freq2[key] = 1
		gini1, gini2 = 0, 0
		#Calculate the Gini index of both sets
		for freq in freq1.values():
			gini1 += math.pow(freq/float(n1),2)
		for freq in freq2.values():
			gini2 += math.pow(freq/float(n2),2)
		gini1 = 1 - gini1
		gini2 = 1 - gini2
		# Combine the Gini values, multiplying them by the probability
		# of each subset
		total_gini = (n1/float(n1+n2))*gini1 + (n2/float(n1+n2))*gini2
		return (total_gini, threshold)			


	def split(self, indices, feature, threshold):
		"""
		Creates two seperates index vectors by applying the 
		threshold on the input feature
		"""
		left, right = [], []
		for index in indices:
			if self.data[index][feature] <= threshold:
				left.append(index)
			else:
				right.append(index)

		return left, right
