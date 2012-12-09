import numpy as np
import math 

class DataHandler: 

	LABEL_INDEX = 0

	def __init__(self, data):
		self.data = np.float64(data)

	def get_shape():
		return self.data.shape

	def get_labels(indices):
		labels = {}
		for index in indices:
			label = self.data[index][0]
			if label in labels:
				labels[label] = 1
			else:
				labels += 1
		return labels

	def purity(feature, threshold, indices):
		# Initialize variables
		freq1, freq2 = {}, {}
		n1, n2 = 0, 0
		# Compute the frequency of the labels for the two
		# two subsets i.e <= threshold or > threshold
		for index in indices:
			key = data[index][0]
			if data[index][feature] <= threshold:
				n1 += 1
				if freq1.has_key():
					freq1[key] += 1
				else:
					freq1[key] = 1  
			else:
				n2 += 1
				if freq2.has_key():
					freq2[key] += 1
				else:
					freq2[key] = 1
		#Print out subsets		
		print subset1
		print subset2
		gini1, gini2 = 0, 0
		#Calculate the Gini impurity of both sets
		for freq in freq1.val():
			gini1 += math.pow(freq/float(n1),2)
		for freq in freq2.val():
			gini2 += math.pow(freq/float(n2),2)
		gini1 = 1 - gini1
		gini2 = 1 - gini2
		# Combine the Gini values, multiplying them by the probability
		# of each subset
		total_gini = (n1/float(n1+n2))*gini1 + (n2/float(n1+n2))*gini2
		print total_gini
		return total_gini
		  
		return 
		 
				
			
				





