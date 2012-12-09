import abc

from subset_base import SubsetBase

class Subset(SubsetBase):

	def __init__(self, indices, features, data_handler=None, data=None):
		self.indices = indices
		self.features = features
		self.labels = None
		if data_handler:
			self.data_handler = data_handler
		else:
			self.data_handler = DataHandler(data)

	def pure():
		"""Determine if subset is pure. Returns label of pure item if pure and None otherwise"""
		if not self.labels:
			self.labels = self.data_handler.get_labels()

		if len(self.labels) == 1:
			return self.labels.keys()[0]

		return False


	def majority_label():
		"""Return label of majority item."""
		if not self.labels:
			self.labels = self.data_handler.get_labels()

		majority, count = None, -1
		for label, value in self.labels.iteritems():
			if value > count:
				majority = label

		return label

	def split():
		"""Returns a tuple of arrays of (values, subsets) given the feature to split on."""
		return

	def best_feature():
		"""Determines the feature that best splits the subset."""
		return

	def empty():
		"""Checks if the subset is empty."""
		return len(self.indices) == 0
	
	def feature_count():
		"""Returns the number of features remaining."""
		return