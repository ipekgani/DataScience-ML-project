import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from sklearn.neural_network import MLPClassifier
import time, pickle
start_time = time.time()

EPOCH = 1
BATCH_SIZE = 1024
# DROP = ['Sample num', 'X', 'Y', 'Resolution', 'School Type', 'General Type', 'Distance']
DROP = ['Sample num', 'X', 'Y', 'Resolution', 'Distance']

le = preprocessing.LabelEncoder()

train_df = pd.read_csv('categorical_data/some_train.csv', header=0, index_col=0)
train_df = train_df.sample(frac=1)
train_df = train_df.drop(DROP, axis=1)
train_df = train_df.dropna(axis=0, how='any')
#
train_df['PdDistrict'] = le.fit_transform(train_df['PdDistrict'])
train_df['DayOfWeek'] = le.fit_transform(train_df['DayOfWeek'])
train_df['Date'] = le.fit_transform(train_df['Date'])
# train_df['Distance'] = le.fit_transform(train_df['Distance'])
train_df['General Type'] = le.fit_transform(train_df['General Type'])
train_df['School Type'] = le.fit_transform(train_df['School Type'])

mlp_classifier = MLPClassifier(hidden_layer_sizes=[100, 50], solver="sgd",
                               learning_rate_init=0.001, max_iter=len(train_df)*2,
                               shuffle=True, random_state=0, tol=1e-6,
                               verbose=True, early_stopping=False, batch_size=BATCH_SIZE)

X = train_df.iloc[:, :-1]
y = train_df['Descript']
print("Starting training, batch size: %i, training samples: %i" % (BATCH_SIZE, len(X)))

mlp_classifier.fit(X, y)

print('Writing classifier to file. Time: {:.2f}'.format(time.time() - start_time))
print('Accuracy of classifier on train set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(mlp_classifier.score(X, y),
                                                    time.time() - start_time, len(X)))

test_df = pd.read_csv('categoriacal/some_test.csv', header=0, index_col=0)
test_df = test_df.drop(DROP, axis=1)
test_df = test_df.sample(frac=1)

test_df['PdDistrict'] = le.fit_transform(test_df['PdDistrict'])
test_df['DayOfWeek'] = le.fit_transform(test_df['DayOfWeek'])
test_df['Date'] = le.fit_transform(test_df['Date'])
# test_df['Distance'] = le.fit_transform(test_df['Distance'])
test_df['General Type'] = le.fit_transform(test_df['General Type'])
test_df['School Type'] = le.fit_transform(test_df['School Type'])

test_df = test_df.dropna(axis=0, how='any')

X = test_df.iloc[:, :-1]
y = test_df['Descript']

print('Accuracy of classifier on test set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(mlp_classifier.score(X, y),
                                                    time.time() - start_time, len(test_df)))

mlp_classifier.loss_curve_