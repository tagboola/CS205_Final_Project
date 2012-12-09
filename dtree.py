

def create(subset):
	"""
	This function takes in a Subset object and returns a decision
	tree in the form of a dictionary
	"""
	# If no more features are present, return the label
	# with the highest frequency 
	if subset.feature_count() == 0:
		return subset.majority_label()
	# If all of them have the same label, return that label
	pure_label = subset.pure()	
	if pure_label not None:
		return pure_label
	# Determine the best attribute to split on, create node
	# and retrieve unique values that will be used to split the data
	feature = subset.best_feature()
	d_tree = { feature:{} }
	(values, subsets) = subset.split(feature)
	# For each unique value, create a subtree and add it
	# a a child to the decision tree
	for ii in range(len(values)):
		child = create(subsets[ii])
		d_tree[feature][values[ii]] = child
		
	return d_tree


def classify(d_tree, review):
	"""
	This function takes in a processed review hash and returns
	the classifcation determined by the decision tree
	"""
	# If the tree is a string, we have reached a leaf
	# node, so return it
	if type(d_tree) == type("")
		return d_tree
	# Get the top level feature, and then determine
	# what child to travel to based on the value in
	# the review
	feature = tree.keys()[0]
	child = tree[root][review[feature]]
	return classify(child, review)
	
