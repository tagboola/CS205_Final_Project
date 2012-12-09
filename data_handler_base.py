import abc

class DataHandlerBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_labels(indices):
		"""Returns a dictonary of labels and their respective counts."""
		return 


