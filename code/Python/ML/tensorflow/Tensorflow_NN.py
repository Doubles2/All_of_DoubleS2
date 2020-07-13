
# coding: utf-8

# In[1]:

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score

from scipy.io import loadmat
data1 = loadmat('Readmission_Cross_Validation_Trainingset_.mat')
data2= loadmat('Readmission_Cross_Validation_Trainingset_Label.mat')
data3= loadmat('Readmission_Holdout_Data_.mat')
data4 = loadmat('Readmission_Holdout_Label.mat')
X_train = data1['Cross_Validation_Trainingset']
Y_Train = data2['Cross_Validation_Trainingset_Label']
X_Test = data3['Holdout_Testset']
Y_Test = data4['Holdout_Testset_Label']


# In[4]:

# Network Parameters
n_hidden_1 = 128 # 1st layer #
n_hidden_2 = 128 # 2nd layer #
n_input    = 5 # data input (# of feature)
n_classes  = 2 # total classes (1: death, 0: survive)

# tf Graph input
with tf.device('/gpu:0'):
    x = tf.placeholder("float", [None, n_input])
    y = tf.placeholder("float", [None, n_classes])
    lr = tf.placeholder("float", shape=[])
    
# Create model
def multilayer_perceptron(_X, _weights, _biases):
    with tf.device('/gpu:0'):
        layer_1 = tf.nn.relu(tf.add(tf.matmul(_X, _weights['h1']), _biases['b1'])) 
        layer_2 = tf.nn.dropout(tf.nn.relu(tf.add(tf.matmul(layer_1, _weights['h2']), _biases['b2'])), 0.5)
    return tf.matmul(layer_2, _weights['out']) + _biases['out']
    #return tf.matmul(layer_2, _weights['out']) + _biases['out']
    
# Store layers weight & bias
stddev = 0.1 # <== This greatly affects accuracy!! 

with tf.device('/gpu:0'):
    weights = {
        'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1], stddev=stddev)),
        'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2], stddev=stddev)),
        'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes], stddev=stddev))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([n_hidden_1])),
        'b2': tf.Variable(tf.random_normal([n_hidden_2])),
        'out': tf.Variable(tf.random_normal([n_classes]))
    }
print ("Network Ready to Go!")


# In[5]:

tf.set_random_seed(0)
# Parameters
learning_rate_value   = 0.0001
training_epochs = 60
batch_size      = 64
display_step    = 1
log_step = int(training_epochs/display_step)

#Minor Class weights
class_weights = 200


# In[6]:

# Add ops to save and restore all the variables.
Model_saver = tf.train.Saver(max_to_keep=None)


# In[7]:

learning_rate_value = 0.0001
training_epochs = 60

# Construct model
with tf.device('/gpu:0'):
    pred = multilayer_perceptron(x, weights, biases)
    softmax_pred = tf.nn.softmax(pred)
    # Define loss and optimizer
    #cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = pred, labels = y)) 
    #cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = weighted_pred, labels = y))
    cost = tf.reduce_mean(tf.nn.weighted_cross_entropy_with_logits(logits = pred, targets = y, pos_weight=class_weights_EMS_Blunt))
    optm = tf.train.AdamOptimizer(learning_rate=lr).minimize(cost)
    corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accr = tf.reduce_mean(tf.cast(corr, "float"))

# Initializing the variables
init = tf.global_variables_initializer()

test_auc = np.zeros(log_step)
test_auc_best=np.zeros(1)
n_train = X_Train.shape[0]

# Train Model
# Launch the graph
sess_run = tf.Session(config=tf.ConfigProto(log_device_placement=True))
sess_run.run(init)

# Training cycle
for epoch in range(training_epochs):
    avg_cost = 0.
    total_batch = int(n_train/batch_size)
    # Loop over all batches
    for i in range(total_batch):
        randidx = np.random.randint(n_train, size=batch_size)
        batch_xs = X_Train[randidx, :]
        batch_ys = Y_Train[randidx, :]
        # Fit training using batch data
        if epoch < 10:
            sess_run.run(optm, feed_dict={x: batch_xs, y: batch_ys, lr: learning_rate_value})
        elif epoch < 20:
            sess_run.run(optm, feed_dict={x: batch_xs, y: batch_ys, lr: 0.9*learning_rate_value})
        else:
            sess_run.run(optm, feed_dict={x: batch_xs, y: batch_ys, lr: 0.81*learning_rate_value})
        # Compute average loss
        avg_cost += sess_run.run(cost, feed_dict={x: batch_xs, y: batch_ys})/total_batch
        # Display logs per epoch step
    if (epoch+1) % display_step == 0:
        print ("Epoch: %03d/%03d cost: %.9f" % (epoch, training_epochs, avg_cost))
        train_acc = sess_run.run(accr, feed_dict={x: batch_xs, y: batch_ys})
        print (" Training accuracy: %.3f" % (train_acc))
        test_acc = sess_run.run(accr, feed_dict={x: X_Test, y: Y_Test})
        print (" Test accuracy: %.3f" % (test_acc))
        y_pred_test = sess_run.run(softmax_pred, feed_dict={x: X_Test, y: Y_Test})
        test_auc[epoch] = roc_auc_score(Y_Test, y_pred_test)
        if test_auc_best < test_auc[epoch]:
            test_auc_best = test_auc[epoch]
            y_pred_test_best = y_pred_test
            model_path = "/tmp/model.ckpt"
            save_path = model_saver.save(sess_run, model_path)
            #print ("Model saved in file: ", save_path)
            sio.savemat("NN_result.mat" , {"Best_AUC":test_auc_best, "Best_y_pred":y_pred_test_best})
            print("Best Model Checked at epoch: %d" % epoch)
        print (" Test AUC: %.4f" % (test_auc[epoch]))
           
print ("Optimization Finished!")
sess_run.close()
print ("Session closed.")    

