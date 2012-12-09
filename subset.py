import abc
import random
from subset_base import SubsetBase
from data_handler import DataHandler

class Subset(SubsetBase):

	K_FEATURES = 5

	def __init__(self, indices, data_handler=None, data=None):
		self.indices = indices
		self.labels = None
		if data_handler:
			self.data_handler = data_handler
		else:
			self.data_handler = DataHandler(data)

	def pure(self):
		"""Determine if subset is pure. Returns label of pure item if pure and None otherwise"""
		return self.data_handler.purity(self.indices)



	def majority_label(self):
		"""Return label of majority item."""
		labels = self.data_handler.get_labels(self.indices)

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

		# Try k different splits
		splits = {}
		for feature in features:
			(gini, threshold) = self.data_handler.test_split(self.indices, feature)			
			splits[feature] = {'threshold':threshold, 'gini':gini}

		# Finds the optimal split from all test
		best_feature, threshold, min_gini = None, None, 100
		for feature, results in splits.iteritems():
			if results['gini'] < min_gini:
				best_feature, threshold, min_gini = feature, results['threshold'], results['gini']

		#Split remaining data
		subset_left, subset_right = self.get_subsets(best_feature, threshold)
		return best_feature, threshold, subset_left, subset_right


	def get_subsets(self,feature, threshold):
		left, right = self.data_handler.split(self.indices, feature, threshold)
		left_subset = Subset(left, data_handler=self.data_handler)
		right_subset = Subset(right, data_handler=self.data_handler)
		return left_subset, right_subset









