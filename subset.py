import abc
import random
from subset_base import SubsetBase
from data_handler import DataHandler

class Subset(SubsetBase):

	K_FEATURES = 10

	def __init__(self, indices, data_handler=None, data=None):
		self.indices = indices
		self.labels = None
		if data_handler:
			self.data_handler = data_handler
		else:
			self.data_handler = DataHandler(data)

	def get_size(self):
		"""
		Returns the size of the subset i.e the number
		of rows in the subset
		"""
		return len(self.indices)

	def purity(self):
		"""
		Determines the "purity" of the subset by calculating
		the gini index of the data
		"""
		return self.data_handler.gini_index(self.indices)



	def majority_label(self):
		"""
		Returns the mode of the all the labels in the subset
		"""
		labels = self.data_handler.get_freq(self.indices)
		#Loop frequency hash and find the mode
		majority, count = None, -1
		for label, value in labels.iteritems():
			if value > count:
				majority = label

		return majority

	def split(self):
		"""
		Returns a tuple of arrays of (feature, values, subsets) 
		given the feature to split on.
		"""
		n, f = self.data_handler.get_shape()
		# Selects k features without replacement
		features = random.sample(range(1, f), self.K_FEATURES) 
		# Calculate the gini index of k different splits
		splits = {}
		for feature in features:
			(gini, threshold) = self.data_handler.test_split(self.indices, feature)			
			splits[feature] = {'threshold':threshold, 'gini':gini}
		# Finds the optimal split from all the splits above
		best_feature, threshold, min_gini = None, None, 100
		for feature, results in splits.iteritems():
			if results['gini'] < min_gini:
				best_feature, threshold, min_gini = feature, results['threshold'], results['gini']
		#Split the subset
		subset_left, subset_right = self.get_subsets(best_feature, threshold)
		return best_feature, threshold, subset_left, subset_right


	def get_subsets(self,feature, threshold):
		"""
		Splits the current subset into two based on the 
		input feature and threshold
		"""
		left_indices, right_indices = self.data_handler.split(self.indices, feature, threshold)
		left_subset = Subset(left_indices, data_handler=self.data_handler)
		right_subset = Subset(right_indices, data_handler=self.data_handler)

		return left_subset, right_subset









