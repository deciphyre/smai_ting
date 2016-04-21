from gensim.models import word2vec
import logging
import os
import sys
from nltk.util import ngrams
import numpy as np
n=3
model = word2vec.Word2Vec.load("../forpos.model")
f_line_open=open(sys.argv[1],"r")
start=np.zeros(100)
end=np.ones(100)
for line in f_line_open:
	point=[]
	start=np.zeros(100)
	end=np.ones(100)
	trigram=ngrams(line.split(),n)
	line=line.split()
	if len(line)>1:
		st=np.concatenate((start,model[line[0]],model[line[1]]))
		en=np.concatenate((model[line[-2]],model[line[-1]],end))
	elif len(line)==1:
		st=np.concatenate((start,model[line[0]],end))
	for s in st:
		print str(s),
	print 
	if len(line)>2:
		for gram in trigram:
			temp_g=np.concatenate((model[gram[0]],model[gram[1]],model[gram[2]]))
			for s in temp_g:
				print str(s),
			print
	elif len(line)==2:
		en=np.concatenate((model[line[0]],model[line[1]],end))
	if len(line)>1:
		for s in en:
			print str(s),
		print
f_line_open.close()
