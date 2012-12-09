import numpy as np

THRESHOLD = 0.2

def create(subset, features):
	"""
	This function takes in a Subset object and returns a decision
	tree in the form of a dictionary
	"""
	# If the subset is pure, return the label majority label
	if subset.pure() < THRESHOLD:
		return subset.majority_label()
	# Determine the best attribute to split point and return
	# the values and subsets associated with that split point
	(feature, split_value, left_subset, right_subset) = subset.split()

	if left_subset.get_size() ==  subset.get_size() or right_subset.get_size == subset.get_size():
		return subset.majority_label()


	# Create node based on optimal feature
	d_tree = {features[feature]:{}}

	# For each unique value, create a subtree and add it
	# a child to the decision tree
	left_child = create(left_subset, features)
	d_tree[features[feature]]["< %f" % (split_value)] = left_child
	right_child = create(right_subset, features)
	d_tree[features[feature]]["> %f" % (split_value)] = right_child
		
	return d_tree


def classify(d_tree, review):
	"""
	This function takes in a processed review hash and returns
	the classifcation determined by the decision tree
	"""
	# If the tree is a string, we have reached a leaf
	# node, so return it
	if type(d_tree) == type(np.float64(0.0)):
		return d_tree
	# Get the top level feature, and then determine
	# what child to travel to based on the value in
	# the review
	feature = d_tree.keys()[0]
	# Parse the node e.g convert "> 55" into 55
	split = float(d_tree[feature].keys()[0][1:])
	# If <= to split, index into the left node i.e "< 55" else
	# go to the right node i.e "> 55"

	if float(review[feature]) <= split:
		#Go to the left
		return classify(d_tree[feature]["< %f" % (split)],review)
	else:
		#Go to the right
		return classify(d_tree[feature]["> %f" % (split)],review)

	
