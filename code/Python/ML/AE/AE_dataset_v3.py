import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn import metrics as m
import pandas as pd
from sklearn.metrics import confusion_matrix
from rbm import RBM
from au import AutoEncoder

# dataset 3
train = pd.read_csv('train_v3.csv', encoding = 'cp949')
test = pd.read_csv('test_v3.csv', encoding ='cp949')

train = train.drop(['Unnamed: 0'], axis = 1)
test = test.drop(['Unnamed: 0'], axis = 1)

# 나이 / 연간 입원횟수 / 총 건강검진 횟수 -> 정규화
train['AGE'] = np.float64(((train['AGE'] - np.mean(train['AGE']))/ np.std(train['AGE'])+3))
train['CRFAY'] = np.float64(((train['CRFAY'] - np.mean(train['CRFAY']))/ np.std(train['CRFAY'])+3))
train['CGJ'] = np.float64(((train['CGJ'] - np.mean(train['CGJ']))/ np.std(train['CGJ'])+3))
train['DIFF_DAY'] = np.float64(((train['DIFF_DAY'] - np.mean(train['DIFF_DAY']))/ np.std(train['DIFF_DAY'])+3))
train['DIFF_YYYY'] = np.float64(((train['DIFF_YYYY'] - np.mean(train['DIFF_YYYY']))/ np.std(train['DIFF_YYYY'])+3))
test['AGE'] = np.float64(((test['AGE'] - np.mean(test['AGE']))/ np.std(test['AGE'])+3))
test['CRFAY'] = np.float64(((test['CRFAY'] - np.mean(test['CRFAY']))/ np.std(test['CRFAY'])+3))
test['CGJ'] = np.float64(((test['CGJ'] - np.mean(test['CGJ']))/ np.std(test['CGJ'])+3))
test['DIFF_DAY'] = np.float64(((test['DIFF_DAY'] - np.mean(test['DIFF_DAY']))/ np.std(test['DIFF_DAY'])+3))
test['DIFF_YYYY'] = np.float64(((test['DIFF_YYYY'] - np.mean(test['DIFF_YYYY']))/ np.std(test['DIFF_YYYY'])+3))




X = train.values
Y_Train = X[:,11]
X_Train = np.delete(X, 11, 1)
# 뉴럴넷 Label Input 형태처럼 바꾸기
Y_index = Y_Train.shape[0]
Y_Train = Y_Train.reshape(Y_index, 1)
Y_Train = np.tile(Y_Train, 2)
Y_Train[:,1] = np.where(Y_Train[:,0] == 1, 0, 1)

Y = test.values
Y_Test = Y[:,11]
X_Test = np.delete(Y, 11, 1)
# 뉴럴넷 Label Input 형태처럼 바꾸기
Y_index = Y_Test.shape[0]
Y_Test = Y_Test.reshape(Y_index, 1)
Y_Test = np.tile(Y_Test, 2)
Y_Test[:,1] = np.where(Y_Test[:,0] == 1, 0, 1)

del train, test, X, Y


os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
RBM_batchsize = 64
RBM_epochs = 10
RBM_input_shape = X_Train.shape[1]
RBM_n_input = X_Train.shape[0]
n_RBM_1 = 2048
n_RBM_2 = 1024
n_RBM_3 = 512
AE_n_output = 256

AE_epochs = 10

# RBMs
rbmobject1 = RBM(RBM_input_shape, n_RBM_1, ['rbmw1', 'rbvb1', 'rbmhb1'], 0.1)
rbmobject2 = RBM(n_RBM_1, n_RBM_2, ['rbmw2', 'rbvb2', 'rbmhb2'], 0.1)
rbmobject3 = RBM(n_RBM_2, n_RBM_3, ['rbmw3', 'rbvb3', 'rbmhb3'], 0.1)
rbmobject4 = RBM(n_RBM_3, AE_n_output,   ['rbmw4', 'rbvb4', 'rbmhb4'], 0.1)

restore_rbm = False
if restore_rbm:
  rbmobject1.restore_weights("/out/rbmw1.chp")
  rbmobject2.restore_weights("/out/rbmw2.chp")
  rbmobject3.restore_weights("/out/rbmw3.chp")
  rbmobject4.restore_weights("/out/rbmw4.chp")

# Autoencoder
autoencoder = AutoEncoder(RBM_input_shape, [n_RBM_1, n_RBM_2, n_RBM_3, AE_n_output], [['rbmw1', 'rbmhb1'],
                                                    ['rbmw2', 'rbmhb2'],
                                                    ['rbmw3', 'rbmhb3'],
                                                    ['rbmw4', 'rbmhb4']], tied_weights=False)

iterations = int(RBM_n_input / RBM_batchsize)

# Train First RBM
print('===First RBM===')
for i in range(RBM_epochs):
    for j in range(iterations):
        randidx = np.random.randint(RBM_n_input, size=RBM_batchsize)
        batch_xs = X_Train[randidx, :]
        rbmobject1.partial_fit(batch_xs)
    print(rbmobject1.compute_cost(X_Train))

rbmobject1.save_weights("/out/rbmw1.chp")


# Train Second RBM
print('===Second RBM===')
for i in range(RBM_epochs):
    for j in range(iterations):
        randidx = np.random.randint(RBM_n_input, size=RBM_batchsize)
        batch_xs = X_Train[randidx, :]
        # Transform features with first rbm for second rbm
        batch_xs = rbmobject1.transform(batch_xs)
        rbmobject2.partial_fit(batch_xs)
    print(rbmobject2.compute_cost(rbmobject1.transform(X_Train)))
rbmobject2.save_weights("/out/rbmw2.chp")

# Train Third RBM
print('===Third RBM===')
for i in range(RBM_epochs):
    for j in range(iterations):
        randidx = np.random.randint(RBM_n_input, size=RBM_batchsize)
        batch_xs = X_Train[randidx, :]
        # Transform features
        batch_xs = rbmobject1.transform(batch_xs)
        batch_xs = rbmobject2.transform(batch_xs)
        rbmobject3.partial_fit(batch_xs)
    print(rbmobject3.compute_cost(rbmobject2.transform(rbmobject1.transform(X_Train))))
rbmobject3.save_weights("/out/rbmw3.chp")

# Train Fourth RBM
print('===Fourth RBM===')
for i in range(RBM_epochs):
    for j in range(iterations):
        randidx = np.random.randint(RBM_n_input, size=RBM_batchsize)
        batch_xs = X_Train[randidx, :]
        # Transform features
        batch_xs = rbmobject1.transform(batch_xs)
        batch_xs = rbmobject2.transform(batch_xs)
        batch_xs = rbmobject3.transform(batch_xs)
        rbmobject4.partial_fit(batch_xs)
    print(rbmobject4.compute_cost(rbmobject3.transform(rbmobject2.transform(rbmobject1.transform(X_Train)))))
rbmobject4.save_weights("/out/rbmw4.chp")




# Load RBM weights to Autoencoder
autoencoder.load_rbm_weights("/out/rbmw1.chp", ['rbmw1', 'rbmhb1'], 0)
autoencoder.load_rbm_weights("/out/rbmw2.chp", ['rbmw2', 'rbmhb2'], 1)
autoencoder.load_rbm_weights("/out/rbmw3.chp", ['rbmw3', 'rbmhb3'], 2)
autoencoder.load_rbm_weights("/out/rbmw4.chp", ['rbmw4', 'rbmhb4'], 3)

# Train Autoencoder
print('===Autoencoder===')
for i in range(AE_epochs):
    cost = 0.0
    for j in range(iterations):
        randidx = np.random.randint(RBM_n_input, size=RBM_batchsize)
        batch_xs = X_Train[randidx, :]
        cost += autoencoder.partial_fit(batch_xs)
    print(cost)

autoencoder.save_weights("/out/au.chp")
autoencoder.load_weights("/out/au.chp")



def softmax(x):
    if x.ndim  == 1:
        x = x.reshape([1, x.size])
    softmaxInvx = x - np.max(x,1).reshape(x.shape[0],1)
    matExp = np.exp(softmaxInvx)
    return matExp/np.sum(matExp, axis=1).reshape([matExp.shape[0],1])


# Network Parameters
n_hidden_1 = 128 # 1st layer #
n_hidden_2 = 128 # 2nd layer #
#n_input    = X_Train.shape[1] # data input (# of feature)
n_input    = AE_n_output # data input (# of feature)
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

print("Network Ready to Go!")

tf.set_random_seed(0)
# Parameters
learning_rate_value   = 0.001
training_epochs = 30
batch_size      = 128
display_step    = 1
log_step = int(training_epochs/display_step)

#Minor Class weights
class_weights = 100


# Add ops to save and restore all the variables.
Model_saver = tf.train.Saver(max_to_keep=None)

# Construct model
with tf.device('/gpu:0'):
    pred = multilayer_perceptron(x, weights, biases)
    softmax_pred = tf.nn.softmax(pred)
    # Define loss and optimizer
    #cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = pred, labels = y)) 
    #cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = weighted_pred, labels = y))
    cost = tf.reduce_mean(tf.nn.weighted_cross_entropy_with_logits(logits = pred, targets = y, pos_weight=class_weights))
    optm = tf.train.AdamOptimizer(learning_rate=lr).minimize(cost)
    corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accr = tf.reduce_mean(tf.cast(corr, "float"))

# Initializing the variables
init = tf.global_variables_initializer()

test_auc = np.zeros(log_step)
test_auc_best=np.zeros(1)
n_train = X_Train.shape[0]

import scipy.io as sio

# Train Model
# Launch the graph
sess_run = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
sess_run.run(init)

# Training cycle
for epoch in range(training_epochs):
    avg_cost = 0.
    total_batch = int(n_train/batch_size)
    # Loop over all batches
    for i in range(total_batch):
        randidx = np.random.randint(n_train, size=batch_size)
        batch_xs = X_Train[randidx, :]
        batch_xs = autoencoder.transform(batch_xs)
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
        print("Epoch: %03d/%03d cost: %.9f" % (epoch, training_epochs, avg_cost))
        train_acc = sess_run.run(accr, feed_dict={x: batch_xs, y: batch_ys})
        print(" Training accuracy: %.3f" % (train_acc))
        X_Test_AE = autoencoder.transform(X_Test)
        Y_Test_AE = Y_Test
        test_acc = sess_run.run(accr, feed_dict={x: X_Test_AE, y: Y_Test_AE})
        print(" Test accuracy: %.3f" % (test_acc))
        #y_pred_test = sess_run.run(softmax_pred, feed_dict={x: X_Test_AE, y: Y_Test_AE})
        y_pred_test = sess_run.run(pred, feed_dict={x: X_Test_AE})
        y_pred_test_softmax = softmax(y_pred_test)
        fpr, tpr, thresholds = m.roc_curve(Y_Test_AE[:,0], y_pred_test_softmax[:,0])
        test_auc[epoch] = m.auc(fpr, tpr)
        if test_auc_best < test_auc[epoch]:
            test_auc_best = test_auc[epoch]
            y_pred_test_best = y_pred_test_softmax
            model_path = "/out/AE_NN_model.ckpt"
            save_path = Model_saver.save(sess_run, model_path)
            print ("Model saved in file: ", save_path)
            sio.savemat("AE_NN_result_%.4f_%d_v3.mat" % (test_auc[epoch], epoch), {"Best_AUC":test_auc_best, "Best_y_pred":y_pred_test_best})
            print("Best Model Checked at epoch: %d" % epoch)
            np.savetxt("AE_NN_result_%.4f_%d_v3.txt" % (test_auc[epoch], epoch), y_pred_test_best, delimiter=',')
            plt.figure()
            plt.plot(fpr, tpr, linestyle='--')
            plt.xlim([-0.5,1.0])
            plt.ylim([0.0,1.05])
            plt.savefig("NN_ROC_%.4f_%d_v3.png" % (test_auc[epoch], epoch))
            plt.close()
            y_pred_value = (y_pred_test_best[:,0]>thresholds[1]).astype(int)
            np.savetxt("NN_CF_%.4f_v3.txt" % (test_auc[epoch]), confusion_matrix(Y_Test[:,0], y_pred_value, labels = [0, 1]))


print("Optimization Finished!")
sess_run.close()
print("Session closed.")