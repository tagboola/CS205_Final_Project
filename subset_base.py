import abc

class SubsetBase(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def get_size(self):
		"""
		Returns the size of the subset i.e the number
		of rows in the subset
		"""
		return

	@abc.abstractmethod
	def purity(self):
		"""
		Determines the "purity" of the subset by calculating
		the gini index of the data
		"""
		return

	@abc.abstractmethod
	def majority_label(self):
		"""
		Returns the mode of the all the labels in the subset
		"""
		return

	@abc.abstractmethod
	def split(self):
		"""
		Returns a tuple of arrays of (feature, values, subsets) 
		given the feature to split on.
		"""
		return

	@abc.abstractmethod
	def get_subsets(self, feature, threshold):
		"""
		Splits the current subset into two based on the 
		input feature and threshold
		"""
		return
