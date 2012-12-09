import abc

from subset_base import SubsetBase

class Subset(SubsetBase):

	PURITY_THRESHOLD = 0.95
	K_FEATURES = 10

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

		return None


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
		"""
		Returns a tuple of arrays of (feature, values, subsets) 
		given the feature to split on.
		"""
		n, f = self.data_handler.get_shape()
		# Selects k features without replacement
		#TODO match up the features 1 is star rating? if so ignore that feature
		features = random.sample(range(f), K_FEATURES) 

		#try different splits
		splits = {}
		for feature in features:
			threshold = #TODO - come up with the threshold?
			purity = test_purity_on_split(feature, threshold)			
			splits[feature] = {'threshold':threshold, 'purity':purity}

		#finds optimal split, from all tests
		best_feature, threshold, max_purity = None, None, -1
		for feature, results in splits.iteritems():
			if results['purity'] > max_purity:
				best_feature, threshold, max_purity = feature, results['threshold'], results['purity']

		#Split remaining data
		subset_left, subset_right = get_subsets(best_feature, threshold)
		return best_feature, threshold, subset_left, subset_right

	def purity(feature, threshold):
		
		return 

	def test_purity_on_split(feature, threshold):
		purity = 0
		return purity







