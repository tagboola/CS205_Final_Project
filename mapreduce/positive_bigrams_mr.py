import re

from mrjob.job import MRJob

MINIMUM_OCCURENCES = 100

def avg_and_total(iterable):
	"""Compute the average over a numeric iterable."""
	items = 0
	total = 0.0

	for item in iterable:
		total += item
		items += 1

	return total / items, items

class PositiveBigrams(MRJob):
	"""Find the most positive bigrams in the dataset."""

	# Each line of the input file will be delivered as key-value pair to the mapper; the key being null in this case
	DEFAULT_INPUT_PROTOCOL = 'json_value'

	def mapper(self, _, data):
		"""Walk over reviews, emitting each word and its rating."""
		if data['type'] != 'review':
			return
		
		# normalize words by lowercasing and dropping non-alpha characters
		norm = lambda word: re.sub('[^a-z]', '', word.lower())
		
		words = list(norm(word) for word in data['text'].split())
		words = filter (lambda a: a != "", words)

		#form bigrams by combining adjacent pairs of onegrams
		bigrams = zip(words[0::2],words[1::2])+zip(words[1::2],words[2::2])

		for bigram in bigrams:
			yield list(bigram), data['stars']

	def reducer(self, bigram, ratings):
		"""Emit average star rating, in a json format for easy input to the cumalative bigram emr job"""
		avg, total = avg_and_total(ratings)

		if total < MINIMUM_OCCURENCES:
			return

		yield '{"bi_gram": "'+str(bigram)+'","score":'+str(int(avg * 100))+',"count":'+str(total)+'}', None

if __name__ == "__main__":
	PositiveBigrams().run()