import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn import metrics as m
import pandas as pd
from sklearn.metrics import confusion_matrix

# dataset 1
#train = pd.read_csv('AE_train_v1.csv', encoding = 'cp949')
#test = pd.read_csv('AE_test_v1.csv', encoding ='cp949')

#train = train.drop(['Unnamed: 0'], axis = 1)
#test = test.drop(['Unnamed: 0'], axis = 1)

# kl4 / l0j0 llml / l4 j14j0j2 l' ml -> l j7m
#train['AGE'] = np.float64(((train['AGE'] - np.mean(train['AGE']))/ np.std(train['AGE'])+3))
#train['CRFAY'] = np.float64(((train['CRFAY'] - np.mean(train['CRFAY']))/ np.std(train['CRFAY'])+3))
#test['AGE'] = np.float64(((test['AGE'] - np.mean(test['AGE']))/ np.std(test['AGE'])+3))
#test['CRFAY'] = np.float64(((test['CRFAY'] - np.mean(test['CRFAY']))/ np.std(test['CRFAY'])+3))



# dataset 2
#train = pd.read_csv('AE_train_v2.csv', encoding = 'cp949')
#test = pd.read_csv('AE_test_v2.csv', encoding ='cp949')

#train = train.drop(['Unnamed: 0'], axis = 1)
#test = test.drop(['Unnamed: 0'], axis = 1)

# kl4 / l0j0 llml / l4 j14j0j2 l' ml -> l j7m
#train['AGE'] = np.float64(((train['AGE'] - np.mean(train['AGE']))/ np.std(train['AGE'])+3))
#train['CRFAY'] = np.float64(((train['CRFAY'] - np.mean(train['CRFAY']))/ np.std(train['CRFAY'])+3))
#train['CGJ'] = np.float64(((train['CGJ'] - np.mean(train['CGJ']))/ np.std(train['CGJ'])+3))
#train['DIFF_DAY'] = np.float64(((train['DIFF_DAY'] - np.mean(train['DIFF_DAY']))/ np.std(train['DIFF_DAY'])+3))
#train['DIFF_YYYY'] = np.float64(((train['DIFF_YYYY'] - np.mean(train['DIFF_YYYY']))/ np.std(train['DIFF_YYYY'])+3))
#test['AGE'] = np.float64(((test['AGE'] - np.mean(test['AGE']))/ np.std(test['AGE'])+3))
#test['CRFAY'] = np.float64(((test['CRFAY'] - np.mean(test['CRFAY']))/ np.std(test['CRFAY'])+3))
#test['CGJ'] = np.float64(((test['CGJ'] - np.mean(test['CGJ']))/ np.std(test['CGJ'])+3))
#test['DIFF_DAY'] = np.float64(((test['DIFF_DAY'] - np.mean(test['DIFF_DAY']))/ np.std(test['DIFF_DAY'])+3))
#test['DIFF_YYYY'] = np.float64(((test['DIFF_YYYY'] - np.mean(test['DIFF_YYYY']))/ np.std(test['DIFF_YYYY'])+3))


# dataset 3
train = pd.read_csv('AE_train_v3.csv', encoding = 'cp949')
test = pd.read_csv('AE_test_v3.csv', encoding ='cp949')

train = train.drop(['Unnamed: 0'], axis = 1)
test = test.drop(['Unnamed: 0'], axis = 1)

# kl4 / l0j0 llml / l4 j14j0j2 l' ml -> l j7m
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
# k	4k4k7 Label Input mml2k< k0j>8j80
Y_index = Y_Train.shape[0]
Y_Train = Y_Train.reshape(Y_index, 1)
Y_Train = np.tile(Y_Train, 2)
Y_Train[:,1] = np.where(Y_Train[:,0] == 1, 0, 1)

Y = test.values
Y_Test = Y[:,11]
X_Test = np.delete(Y, 11, 1)
# k	4k4k7 Label Input mml2k< k0j>8j80
Y_index = Y_Test.shape[0]
Y_Test = Y_Test.reshape(Y_index, 1)
Y_Test = np.tile(Y_Test, 2)
Y_Test[:,1] = np.where(Y_Test[:,0] == 1, 0, 1)

del train, test, X, Y


os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Training Parameters
AE_learning_rate = 0.001
AE_epochs = 20
AE_batch_size = 64

AE_train_flag = False

# Network Parameters
AE_n_hidden_1 = 1024 # 1st layer num features
AE_n_hidden_2 = 512 # 2nd layer num features (the latent dim)
AE_n_input = X_Train.shape[0]
AE_input_shape = X_Train.shape[1]

iterations = int(AE_n_input / AE_batch_size)

# tf Graph input (only pictures)
X = tf.placeholder("float", [None, AE_input_shape])

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([AE_input_shape, AE_n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([AE_n_hidden_1, AE_n_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal([AE_n_hidden_2, AE_n_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([AE_n_hidden_1, AE_input_shape])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([AE_n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([AE_n_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal([AE_n_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([AE_input_shape])),
}

# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.relu(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    # Encoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2


# Building the decoder
def decoder(x):
    # Decoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.relu(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2

# Construct model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

# Prediction
y_pred = decoder_op
# Targets (Labels) are the input data.
y_true = X

# Define loss and optimizer, minimize the squared error
AE_loss = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
AE_optimizer = tf.train.RMSPropOptimizer(AE_learning_rate).minimize(AE_loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
AE_Model_saver = tf.train.Saver(max_to_keep=None)

AE_test_loss_best = 100
# Start Training
# Start a new TF session
with tf.Session() as sess:
    # Run the initializer
    sess.run(init)
    if AE_train_flag: 
        # Training
        for i in range(AE_epochs):
            for j in range(iterations):
                randidx = np.random.randint(AE_n_input, size=AE_batch_size)
                batch_x = X_Train[randidx, :]
                # Run optimization op (backprop) and cost op (to get loss value)
                _, l = sess.run([AE_optimizer, AE_loss], feed_dict={X: batch_x})
                # Display logs per step
                #print('Step %i: Minibatch Loss: %f' % (j, l))
            # Testing
            AE_train_loss = sess.run(AE_loss, feed_dict={X: X_Train})
            print(" Autoencoder Training Loss: %.4f" % (AE_train_loss))
            # Testing
            AE_test_loss = sess.run(AE_loss, feed_dict={X: X_Test})
            print(" Autoencoder Test Loss: %.4f" % (AE_test_loss))
            if AE_test_loss < AE_test_loss_best:
                AE_test_loss_best = AE_test_loss
                AE_model_path = "/out/AE_model.ckpt"
                AE_save_path = AE_Model_saver.save(sess, AE_model_path)
                print ("Model saved in file: ", AE_save_path)
                X_Train_Encode = sess.run(encoder_op, feed_dict={X: X_Train})
                X_Test_Encode = sess.run(encoder_op, feed_dict={X: X_Test})
    else:
        AE_model_path = "/out/AE_model.ckpt"
        AE_Model_saver.restore(sess, AE_model_path)
        X_Train_Encode = sess.run(encoder_op, feed_dict={X: X_Train})
        X_Test_Encode = sess.run(encoder_op, feed_dict={X: X_Test})


def softmax(x):
    if x.ndim  == 1:
        x = x.reshape([1, x.size])
    softmaxInvx = x - np.max(x,1).reshape(x.shape[0],1)
    matExp = np.exp(softmaxInvx)
    return matExp/np.sum(matExp, axis=1).reshape([matExp.shape[0],1])


# Network Parameters
n_hidden_1 = 256 # 1st layer #
n_hidden_2 = 128 # 2nd layer #
#n_input    = X_Train.shape[1] # data input (# of feature)
n_input    = AE_n_hidden_2 # data input (# of feature)
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
training_epochs = 40
batch_size      = 64
display_step    = 1
log_step = int(training_epochs/display_step)

#Minor Class weights
class_weights = 1000


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
        batch_xs = X_Train_Encode[randidx, :]
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
        print(" Training accuracy: %.4f" % (train_acc))
        test_acc = sess_run.run(accr, feed_dict={x: X_Test_Encode, y: Y_Test})
        print(" Test accuracy: %.4f" % (test_acc))
        #y_pred_test = sess_run.run(softmax_pred, feed_dict={x: X_Test_AE, y: Y_Test_AE})
        y_pred_test = sess_run.run(pred, feed_dict={x: X_Test_Encode})
        y_pred_test_softmax = softmax(y_pred_test)
        fpr, tpr, thresholds = m.roc_curve(Y_Test[:,0], y_pred_test_softmax[:,0])
        test_auc[epoch] = m.auc(fpr, tpr)
        print(" Test AUC: %.4f" % (test_auc[epoch]))
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

np.savetxt("Y_Test.txt", Y_Test, delimiter=',')