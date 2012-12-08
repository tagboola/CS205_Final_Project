class Subset: 

	def __init__(self, data_handler, indices):

		self.data_handler = data_handler
		self.indices = np.int32(indices)
		self.indices_d = gpu.to_gpu(self.indices)
		self.results_d = gpu.empty_like(self.indices_d)

	def shape():
		return self.data_handler.shape()

	def purity():
		self.data_handler.purity(self.indices_d, self.results_d)

		results_gpu = self.results_d.get()

		#TODO compute purity
		purity = 0

		return purity 

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

