import sys
import os
import codecs

f1=False
f2=False
count = 0
ct=0
for i in codecs.open(sys.argv[1]):
	i=i.strip()
	if '</s>' == i:
		count = 0
		ct+=1
		f1=False
		print
	if ct==10000000:
		break
	if '<s>'==i:
		f1=True
		continue
	if f1 and count >1:
		j = i.split('\t')
		try:
			print j[0],
		except:
			print ct
		
	count =count +1
	
