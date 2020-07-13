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
from sklearn import linear_model as lm
from sklearn import model_selection as ms
from sklearn import metrics as m

lr = lm.LogisticRegression()
y_r = np.ravel(Y_Train)
lr.fit(X_train, y_r)
Y_Predict = lr.predict_proba(X_Test)
y_t_r = np.ravel(Y_Test)
fpr, tpr, thresholds = m.roc_curve(y_t_r, Y_Predict[:,1:2], pos_label = 1)
print(m.auc(fpr,tpr))
