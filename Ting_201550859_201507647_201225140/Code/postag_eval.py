import sys
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
op=[]
ref=[]
fop=open(sys.argv[1],"r")
frf=open(sys.argv[2],"r")
arr=[',','JJ','NN',':','CC','DT','NNS','SENT','VBP','IN','WRB','VVD','TO','VB','VBZ','VVP','NP','CD','PP$','WP','PP','RB','VBD','VVN','RP','VVZ','MD','VH','POS','JJR','WDT','EX',"''",'VHD','PDT','VVG','RBR','VHZ','VV','(',')','VHP','``','VHN','VBG','$','RBS','JJS','WP$','VBN','SYM','NPS','VHG','LS','FW','UH','#']

def create_conf_matrix(expected, predicted, n_classes):
    m = [[0] * n_classes for i in range(n_classes)]
    for pred, exp in zip(predicted, expected):
        m[exp][pred] += 1
    return m
def error_matrix(matrix,k_number,arr):
	#0-TP,1-FP,2-FN,3-TN
	error=np.zeros((k_number,4))
	for i in range(k_number):
		error[i][0]+=matrix[i][i]
		for k in range(k_number):
			if i!=k:
				error[i][1]+=matrix[k][i]
		for k in range(k_number):
			if i!=k:
				error[i][2]+=matrix[i][k]
		for k in range(k_number):
			for l in range(k_number):
				if i!=k and i!=l:
					error[i][3]+=matrix[k][l]
	#return error
	
	table=[]
	posi=['pos_tags','0-TP','1-FP','2-FN','3-TN']
	#print ("    0-TP   1-FP   2-FN   3-TN")
	i=0
	table.append(posi)
	for temp in error:
		line=[]
		line.append(arr[i])
		for x in temp:
			line.append(x)
		#print (str(arr[i])+" "+str(temp))
		i+=1
		table.append(line)
	#print tabulate(table)
	print tabulate(table, headers="firstrow", tablefmt="latex")
	p = PrettyTable()
	for row in table:
		p.add_row(row)
	#print (p.get_string(header=False, border=False))
	table=[]
	preci=['pos_tags','precision','recall','specifity','accuracy']
	#0-precsion,1-recall,2-specifity,3-accuracy
	metrics=np.zeros((k_number,4))
	#print (metrics)
	for i in range(k_number):
		metrics[i][0]=error[i][0]/(error[i][0]+error[i][1])
		metrics[i][1]=error[i][0]/(error[i][1]+error[i][3])
		metrics[i][2]=error[i][3]/(error[i][1]+error[i][3])
		metrics[i][3]=(error[i][0]+error[i][3])/(error[i][0]+error[i][1]+error[i][2]+error[i][3])
		#metrics[i][4]=(1-metrics[i][3])
	#print ("   precision   recall\t   specifity\taccuracy")
	table.append(preci)
	i=0
	for temp in metrics:
		line=[]
		line.append(arr[i])
		for x in temp:
			line.append(x)
		#print (str(arr[i])+" "+str(temp))
		i+=1
		table.append(line)
	print tabulate(table, headers="firstrow", tablefmt="latex")
	p = PrettyTable()
	for row in table:
		p.add_row(row)
	#print (p.get_string(header=False, border=False))
		
def display_table(matrix,k,arr):
	table=[]
	line=[]
	line.append("expected/predicted")
	for i in range(k):
		line.append(str(arr[i]))
	table.append(line)
	ch=0
	for x in matrix:
		line=[]
		line.append(str(arr[ch]))
		for var in x:
			line.append(var)
		ch+=1
		table.append(line)
	print tabulate(table, headers="firstrow", tablefmt="latex")
	p = PrettyTable()
	for row in table:
		p.add_row(row)
	#print (p.get_string(header=False, border=False))

def vectorise(add):
	temp=np.zeros(len(add))
	#v=max(add)
	temp[add.index(max(add))]=1
	return temp
def digi(vec):
	return vec.index(max(vec))
count=0
for y_op,y_rf in zip(fop,frf):
	y_op=y_op.split()
	y_rf=y_rf.split()
	#print y_rf
	add=[]
	for j in y_op:
		add.append(float(j))
	op.append(vectorise(add))
	add=[]
	for j in y_rf:
		add.append(float(j))
	ref.append(add)
predicted=[]
expected=[]
for x,y in zip(op,ref):
	x=[int(i) for i in x]
	y=[int(i) for i in y]
	predicted.append(digi(x))
	expected.append(digi(y))
	#print x,y

	if np.array_equal(x,y):
		#print "11111111"
		count+=1
display_table(create_conf_matrix(predicted,expected,57),57,arr)
error_matrix(create_conf_matrix(predicted,expected,57),57,arr)
