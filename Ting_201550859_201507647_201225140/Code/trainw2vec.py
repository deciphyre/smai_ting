import gensim,logging,sys
import os
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class MySentences(object):
	def __init__(self, dirname):
	    self.dirname = dirname

	def __iter__(self):
	    for fname in os.listdir(self.dirname):
	        for line in open(os.path.join(self.dirname, fname)):
	             yield line.split()

sentences=MySentences(sys.argv[1])
model = gensim.models.Word2Vec(sentences, min_count=1, size=100, workers=2)
model.save(sys.argv[2]+'.model')
