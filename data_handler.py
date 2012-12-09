import numpy as np
import math 

class DataHandler: 

	LABEL_INDEX = 0

	def __init__(self, features, data):

		self.data = np.float64(data)

	def get_shape():
		return self.data.shape

	def get_freq(indices):
		freq = {}
		for index in indices:
			key = data[index][LABEL_INDEX]
			if freq.has_key(key):
				freq[key] += 1
			else:
				freq[key] = 1

	def get_labels(indices):
		return get_freq(indices)


	def purity(indices):
		freq = get_freq(indices)
		gini = 0
		for value in freq.values():
			gini += math.pow(float(value)/len(indices),2)
		return 1 - gini
	
	def get_threshold(feature, indices):
		min_val = 10000000
		max_val = -1
		for index in indices:
			val = data[index][feature]
			if val > max_val:
				max_val = val
			if val < min_val:
				min_val = val
		return random.random()*(max_val-min_val) + min_val		

	def test_split(feature, threshold, indices):
		threshold = get_threshold(feature, indices)		
		# Initialize variables
		freq1, freq2 = {}, {}
		n1, n2 = 0, 0
		# Compute the frequency of the labels for the two
		# two subsets i.e <= threshold or > threshold
		for index in indices:
			key = data[index][0]
			if data[index][feature] <= threshold:
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
		#Print out subsets		
		print subset1
		print subset2
		gini1, gini2 = 0, 0
		#Calculate the Gini impurity of both sets
		for freq in freq1.values():
			gini1 += math.pow(freq/float(n1),2)
		for freq in freq2.values():
			gini2 += math.pow(freq/float(n2),2)
		gini1 = 1 - gini1
		gini2 = 1 - gini2
		# Combine the Gini values, multiplying them by the probability
		# of each subset
		total_gini = (n1/float(n1+n2))*gini1 + (n2/float(n1+n2))*gini2
		print total_gini
		return (total_gini, threshold)
		 
				
			


	def split(indices, feature, threshold):
		left, right = [], []
		for index in indices:
			if self.data[index][feature] <= threshold:
				left.append(index)
			else:
				right.append(index)

		return left, right
