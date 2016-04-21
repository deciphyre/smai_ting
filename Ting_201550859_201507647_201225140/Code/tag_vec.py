import sys
import numpy as np

f_line_open=open(sys.argv[1],"r")
f_pos=open(sys.argv[2],"r")
t=[]

for line in f_line_open:
	line=line.split()
	for x in line:
		t.append(x)
for line in f_pos:
	line=line.split()
	for tag in line:
		n=np.zeros(len(t))
		n[t.index(tag)]=1.0
		for item in n:
			print item,
		print
f_line_open.close()
f_pos.close()
