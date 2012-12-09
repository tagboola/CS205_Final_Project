import numpy as np

class DataHandler: 

	def __init__(self, data):
		self.data = np.float64(data)

	def get_shape():
		return self.data.shape

	def get_labels(indices):
		labels = {}
		for index in indices:
			label = self.data[index][0]
			if label in labels:
				labels[label] = 1
			else:
				labels += 1
		return labels







