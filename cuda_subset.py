import abc

from subset_base import SubsetBase

class CUDA_Subset(SubsetBase):

	def __init__(self, indices, features, data_handler=None, data=None):

		self.data_handler = data_handler
		self.indices = np.int32(indices)
		self.indices_d = gpu.to_gpu(self.indices)
		self.results_d = gpu.empty_like(self.indices_d)

	def pure():
		"""Determine if subset is pure. Returns label of pure item if pure and None otherwise"""
		return

	def majority_label():
		"""Return label of majority item."""
		return

	def split(feature):
		"""Returns a tuple of arrays of (values, subsets) given the feature to split on."""
		return

	def best_feature():
		"""Determines the feature that best splits the subset."""
		return

	def empty():
		"""Checks if the subset is empty."""
		return
	
	def feature_count():
		"""Returns the number of features remaining."""
		return


	def shape():
		return self.data_handler.shape()

	def split(feature, threshold):
		self.data_handler.split(self.indices_d, self.results_d, feature, threshold)

		#items that are above the threshold are positive, items that are below are negative
		#the number represents the class. if it is -4 then the review has rating 4 and it
		#did was below the threshold
		results_gpu = self.results_d.get()

		#create a new subset object. all those that are
		left_indices = [i for i in self.indices if results_gpu[i] > 0] #items that are above the threshold
		right_indices = [i for i in self.indices if results_gpu[i] < 0]

		#sanity check
		assert len(left_indices) + len(right_indices) == len(results_gpu)

		left_subset = Subset(self.data_handler, left_indices)
		right_subset = Subset(self.data_handler, right_indices)
		return left_subset, right_subset

	def test_purity_on_split(feature, threshold):
		pass

