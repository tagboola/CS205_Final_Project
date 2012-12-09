import numpy as np

class DataHandler: 

	def __init__(self, features, data):
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


	def split(indices, feature, threshold):
		left, right = [], []

		for index in indices:
			if self.data[index][feature] >= threshold:
				left.append(index)
			else:
				right.append(index)

		return left, right