import sys
import numpy as np
#import json
#import pickle

def append_record(record):
    with open('tags_vector', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

f_line_open=open(sys.argv[1],"r")
f_pos=open(sys.argv[2],"r")
#f_wr=open(sys.argv[3],"w")
#print len(f_line_open)
t=[]
#tags=[]
for line in f_line_open:
	#print line
	line=line.split()
	for x in line:
		t.append(x)
#print t
#print len(t)
for line in f_pos:
	#print line
	line=line.split()
	for tag in line:
		n=np.zeros(len(t))
		n[t.index(tag)]=1.0
		#print n
		#print ' '.join(str(n))
		#np.savetxt('test.out', n)
		#append_record(n)
		#f_wr.writelines([n])
		for item in n:
			print item,
		print
		#print "ddddddddd"
		#	f_wr.write("%s")
		#f_wr.write(n)
		#tags.append(n)
f_line_open.close()
f_pos.close()
#f_wr.close()
#with open(sys.argv[3],'wb') as han:
#	pickle.dump(tags,han)
#with open(str(args.tar)+"_result_"+str(args.id),'wb') as handle_d:
#		pickle.dump(result,handle_d)
