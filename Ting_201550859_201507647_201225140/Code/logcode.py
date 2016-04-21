import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
import scipy as sp
import tensorflow as tf
import codecs



Xtrain = 'train_w2v'
Ytrain = 'train_pos_vector'

Xtest = 'test_w2v'
Ytest = 'test_pos_vector'


Xtr=np.zeros(300)
count =0
for i in codecs.open(Xtrain):
	add=[]
	for j in i.split():
		add.append(float(j))
	if count == 0:
		Xtr=add
	else:
		Xtr = np.vstack((Xtr,add))
	count = count + 1
	if count ==10000:
		break

Ytr=np.zeros(300)
count =0
for i in codecs.open(Ytrain):
	add=[]
	for j in i.split():
		add.append(float(j))
	if count == 0:
		Ytr=add
	else:
		Ytr = np.vstack((Ytr,add))
	count = count + 1
	if count ==10000:
		break

Xte=np.zeros(300)
count =0
for i in codecs.open(Xtest):
	add=[]
	for j in i.split():
		add.append(float(j))
	if count == 0:
		Xte=add
	else:
		Xte = np.vstack((Xte,add))
	count = count + 1

	if count ==1000:
		break
Yte=np.zeros(300)
count =0
for i in codecs.open(Ytest):
	add=[]
	for j in i.split():
		add.append(float(j))
	if count == 0:
		Yte=add
	else:
		Yte = np.vstack((Yte,add))
	count = count + 1


	if count ==1000:
		break


print Xtr.shape
print Xte.shape
print Ytr.shape
print Yte.shape


learning_rate = 0.000006
training_epochs = 30
batch_size = Xtr.shape[0]
display_step = 1





x = tf.placeholder("float", [None, Xtr.shape[1]]) # mnist data image of shape 28*28=784
y = tf.placeholder("float", [None, Ytr.shape[1]]) # 0-9 digits recognition => 10 classes
# Set model weights
W = tf.Variable(tf.zeros([Xtr.shape[1], Ytr.shape[1]]))
b = tf.Variable(tf.zeros([Ytr.shape[1]]))


# Construct model
activation = tf.nn.softmax(tf.matmul(x, W) +1*b) # Softmax
cost = -tf.reduce_sum(y*tf.log(activation)) 

# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) 
# Initializing the variables
init = tf.initialize_all_variables()
# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Test model
    correct_prediction = tf.equal(tf.argmax(activation, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))


    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(len(Xtr)/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            #print '---------------------------------',i,0+(i*batch_size),(batch_size*(i+1))
            batch_xs=Xtr[0+(i*batch_size):(batch_size*(i+1)),:]
            batch_ys=Ytr[(0+(batch_size)*i):batch_size*(i+1)]
            #print OY_1[(0+(batch_size)*i):batch_size*(i+1)].shape
            sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
            avg_cost += sess.run(cost, feed_dict={x: batch_xs, y: batch_ys})/total_batch
        # Display logs per epoch step
        if epoch % display_step == 0:
            print "Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost), "Accuracy:", accuracy.eval({x: Xtr, y: Ytr})#,logloss(Ytr,logloss_pre())

    print "Optimization Finished!"
    f = open('output.csv','w')
    for i in zip(activation.eval({x: Xte})):
        f.write(str(np.argmax(i))+'\n')
    f.close()
