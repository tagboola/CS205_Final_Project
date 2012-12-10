import re

from mrjob.job import MRJob

MINIMUM_OCCURENCES = 1000

def avg_and_total(iterable):
	"""Compute the average over a tuple iterable."""
	total_count = 0
	total_score = 0.0

	for item in iterable:
		(score,count) = item
		total_score += score * count
		total_count += count

	return total_score / total_count, total_count

class CumalativeScore(MRJob):
	"""Find the cumalative positive scores for the onegrams in the partially processed dataset."""

	# Each line of the input file will be delivered as key-value pair to the mapper; the key being the onegram
	DEFAULT_INPUT_PROTOCOL = 'json_value'

	def mapper(self, _, data):
		yield data["one_gram"],(data["score"]/100.0,data["count"])

	def reducer(self, word, ratings):
		
		avg, total = avg_and_total(ratings)

		if total < MINIMUM_OCCURENCES:
			return

		yield word+':', int(avg * 100)

if __name__ == "__main__":
	CumalativeScore().run()