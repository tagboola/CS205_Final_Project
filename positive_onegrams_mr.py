import re

from mrjob.job import MRJob

MINIMUM_OCCURENCES = 1000

stop_words = ['a','about','above','after','again','against','all','am','an','and','any','are','as','at','be','because','been','before','being','below','between','both','but','by','could','did','do','does','doing','down','during','each','few','for','from','further','had','has','have','having','he','he'd','he'll','he's','her','here','here's','hers','herself','him','himself','his','how','how's','i','i'd','i'll','i'm','i've','if','in','into','is','it','it's','its','itself','let's','me','more','most','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','she','she'd','she'll','she's','should','so','some','such','than','that','that's','the','their','theirs','them','themselves','then','there','there's','these','they','they'd','they'll','they're','they've','this','those','through','to','too','under','until','up','very','was','we','we'd','we'll','we're','we've','were','what','what's','when','when's','where','where's','which','while','who','who's','whom','why','why's','with','won't','would','you','you'd','you'll','you're','you've','your','yours','yourself','yourselves']

def avg_and_total(iterable):
	"""Compute the average over a numeric iterable."""
	items = 0
	total = 0.0

	for item in iterable:
		total += item
		items += 1

	return total / items, items

class PositiveOneGrams(MRJob):
	"""Find the most positive onegrams in the dataset."""

	# Each line of the input file will be delivered as key-value pair to the mapper; the key being null in this case
	DEFAULT_INPUT_PROTOCOL = 'json_value'

	def mapper(self, _, data):
		"""Process each review, emitting each onegram and its rating."""
		if data['type'] != 'review':
			return

		# normalize words by lowercasing and dropping non-alpha characters
		norm = lambda word: re.sub('[^a-z]', '', word.lower())
		# only include a word once per-review (which de-emphasizes proper nouns)
		words = set(norm(word) for word in data['text'].split())

		for word in words:
			if word not in stop_words and word != "":
				yield word, data['stars']

	def reducer(self, word, ratings):
		"""Emit average star rating, in a json format for easy input to the cumalative onegram emr job"""
		avg, total = avg_and_total(ratings)

		#make sure that only the higher frequency onegrams are emitted
		if total < MINIMUM_OCCURENCES:
			return

		yield '{"one_gram": "'+word+'","score":'+str(int(avg * 100))+',"count":'+str(total)+'}', None

if __name__ == "__main__":
	PositiveOneGrams().run()