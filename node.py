class Node: 

	def __init__(self, feature=None, threshold=None):
		self.feature = feature
		self.threshold = threshold 
		self.left = None
		self.right = None 

	def __str__(self): 
		return "Feature: %d, Threshold %d" %(self.feature, self.threshold)

	def decide(item):
		if item.getFeature(self.feature) < self.threshold:
			return left
			
		return right

