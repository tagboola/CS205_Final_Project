class Subset: 

	def __init__(self, data_handler, indices):

		self.data_handler = data_handler
		self.indices = np.int32(indices)
		self.indices_d = gpu.to_gpu

	def shape():
		return self.data_handler.shape()

	def purity():
		return self.data_handler.purity(self.indices_d)

	def split(feature, threshold):
		return self.data_handler.split(self.indices_d)

	def test_purity_on_split(feature, threshold):
		
