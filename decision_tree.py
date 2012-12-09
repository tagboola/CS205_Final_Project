import random

from Node import Node


class DecisionTree: 

	PURITY_THRESHOLD = 0.95 #TODO - determine an appropriate threshold
	K_FEATURES = 10
	LEFT_SIDE = 'left'
	RIGHT_SIDE = 'right'
	NO_SIDE = 'none'

	def __init__(data_handler): 
		#height = number of samples, width = number of features
		height, width = data_handler.shape()
		n, f = height, width

		#bootstrap sampling w/ replacement
		samples = [random.randint(0,n-1) for i in range(n)]
		subset = Subset(data_handler,samples)

		self.head = Node()
		add_leaf(self.head, NO_SIDE, subset)


	def add_leaf(parent, side, subset):

		n, f = subset.shape()

		#assign head
		purity = subset.purity()
		if purity > PURITY_THRESHOLD:
			return 

		#selects k features without replacement
		#TODO match up the features 1 is star rating? if so ignore that feature
		features = random.sample(range(f), K_FEATURES) 

		#try different splits
		splits = {}
		for feature in features:
			threshold = #TODO - come up with the threshold?
			purity = subset.test_purity_on_split(feature, threshold)			
			splits[feature] = {'threshold':threshold, 'purity':purity}

		#finds optimal split, from all tests
		best_feature, max_purity = None, -1
		for feature, results in splits.iteritems():
			if results['purity'] > max_purity:
				best_feature, max_purity = feature, results['purity']

		#Create a new node in the DT
		node = Node(best_feature, splits[best_feature])

		#Link parent to child
		if side == LEFT_SIDE:
			parent.left = node
		elif side == RIGHT_SIDE:
			parent.right = node
		else: #head node, hasn't been assigned yet
			parent = node

		#Split remaining data
		subset_left, subset_right = subset.split(node.feature, node.threshold)
		add_leaf(node, LEFT_SIDE, subset_left) 
		add_leaf(node, RIGHT_SIDE, subset_right)


	
	#classify an item
	def decide(item):
		#TODO
		pass


