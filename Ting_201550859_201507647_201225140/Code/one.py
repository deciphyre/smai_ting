import sys
import os
import codecs

f1=False
f2=False
count = 0
ct=0
for i in codecs.open(sys.argv[1]):
	i=i.strip()
	#if ct<19400000:
	#	ct+=1
	#	continue
	#print ct
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
		#if ct >19399999 :
		j = i.split('\t')
		#print j
		try:
			print j[0],
		except:
			print ct
		
	count =count +1
	
