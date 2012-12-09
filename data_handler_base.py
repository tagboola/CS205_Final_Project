import abc

class DataHandlerBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_freq(self, indices):
		"""
		Creates a frequency hash of the unique labels
		in the subset determined by the input indices
		"""
		return

	@abc.abstractmethod
	def gini_index(self, indices):
		"""
		Calcutes the gini index of the data
		"""
		return

	@abc.abstractmethod
	def get_threshold(self, feature, indices):
		"""
		Calculates a random threshold for the given feature by
		determining the min and max values
		"""
		return

	@abc.abstractmethod
	def test_split(self, indices, feature):
		"""
		Calculates gini index by applying the a split using
		a random threshold on the given feature
		"""
		return

	@abc.abstractmethod
	def split(self, indices, feature, threshold):
		"""
		Creates two seperates index vectors by applying the 
		threshold on the input feature
		"""
		return
