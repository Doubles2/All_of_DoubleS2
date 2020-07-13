import pandas as pd
import numpy as np
from scipy.io import loadmat


data1 = loadmat('Readmission_Cross_Validation_Trainingset_.mat')
data2= loadmat('Readmission_Cross_Validation_Trainingset_Label.mat')
data3= loadmat('Readmission_Holdout_Data_.mat')
data4 = loadmat('Readmission_Holdout_Label.mat')

X_train = data1['Cross_Validation_Trainingset']
Y_Train = data2['Cross_Validation_Trainingset_Label']
X_Test = data3['Holdout_Testset']
Y_Test = data4['Holdout_Testset_Label']

print(X_train.shape)
print(Y_Train.shape)
print(X_Test.shape)
print(Y_Test.shape)

import sklearn
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn import metrics as m

n_tree_list = [100, 200, 300, 400, 500]
min_samples_split_list = [0.05, 0.1, 0.15, 0.2, 0.25]


for n_tree in n_tree_list
    for n_min_sample_split in min_samples_split_list
        RF = rf(criterion = 'gini', n_estimators = n_tree, min_samples_split = n_min_sample_split, min_samples_leaf = 20, oob_score = False)
        y_r = np.ravel(Y_Train)
        RF.fit(X_train, y_r)
        Y_Predict = RF.predict_proba(X_Test)
        y_t_r = np.ravel(Y_Test)
        fpr, tpr, thresholds = m.roc_curve(y_t_r, Y_Predict[:,1:2], pos_label = 1)
        auc_value = m.auc(fpr,tpr)
		print(auc_value)
        np.savetxt("RF_%4f_%d_%2f" % (auc_value, n_tree, n_min_sample_split), (fpr,tpr,thresholds))
