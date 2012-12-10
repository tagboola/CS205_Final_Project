from collections import Counter

class RandomForest: 

	def __init__(self, forest=[]):
		self.forest = forest

	def add_tree(self, tree):
		self.forest.append(tree)

	def classify(self, item):
		answers = []
		for tree in self.forest:
			answer = tree.classify(item)  #dtree.classify(tree, review)
			answers.append(answer)
		answer = Counter(answers).most_common(1)[0][0]
		return answer