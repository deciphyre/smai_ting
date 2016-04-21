from gensim.models import word2vec
import logging
import os
import sys
from nltk.util import ngrams
import numpy as np
n=3
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec.load("../forpos.model")
f_line_open=open(sys.argv[1],"r")
#f_label_open=open(sys.argv[2],"r")
#fwrite_line=open("data_trigram","w")
start=np.zeros(100)
end=np.ones(100)
for line in f_line_open:
	#entry=[]	
	point=[]
	#lbl=[]
	start=np.zeros(100)
	end=np.ones(100)
	#st.append(start)
	#print line
	trigram=ngrams(line.split(),n)
	line=line.split()
	#label_line=label_line.split()
	#print "lllllllll"	
	#print line[0],line[1]
	if len(line)>1:
		st=np.concatenate((start,model[line[0]],model[line[1]]))
		#st.append(model[line[0]])
		#st.append(model[line[1]])
		en=np.concatenate((model[line[-2]],model[line[-1]],end))
		#en.append(model[line[-2]])
		#en.append(model[line[-1]])
		#en.append(end)
		#entry.append([st,label_line[0]])
		#point.append(st)
	elif len(line)==1:
		st=np.concatenate((start,model[line[0]],end))
	for s in st:
		print str(s),
	print 
	#lbl.append(label_line[0])
	#labl_id=1
	if len(line)>2:
		for gram in trigram:
			#temp_g=[]
			#for x in gram:
			#	temp_g.append(model[x])
			temp_g=np.concatenate((model[gram[0]],model[gram[1]],model[gram[2]]))
			#entry.append([temp_g,label_line[labl_id]])
			#point.append(temp_g)
			for s in temp_g:
				print str(s),
			print
			#lbl.append(label_line[labl_id])
			#labl_id+=1	
	elif len(line)==2:
		en=np.concatenate((model[line[0]],model[line[1]],end))
	#entry.append([en,label_line[-1]])
	if len(line)>1:
		for s in en:
			print str(s),
		print
	#point.append(en)
	#lbl.append(label_line[-1])
	#fwrite_line.write(str(entry))
	#print point
	#print lbl
f_line_open.close()
#f_label_open.close()
#fwrite_line.close()
