import abc

class SubsetBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def pure():
		"""Determine if subset is pure. Returns label of pure item if pure and None otherwise"""
		return

	@abc.abstractmethod
	def majority_label():
		"""Return label of majority item."""
		return

	@abc.abstractmethod
	def split():
		"""Returns a tuple of arrays of (values, subsets) given the feature to split on."""
		return

	@abc.abstractmethod
	def best_feature():
		"""Determines the feature that best splits the subset."""
		return

	@abc.abstractmethod
	def empty():
		"""Checks if the subset is empty."""
		return
	
	@abc.abstractmethod
	def feature_count():
		"""Returns the number of features remaining."""
		return