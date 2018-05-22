import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from sklearn import preprocessing
import time, pickle
start_time = time.time()
from sklearn.naive_bayes import GaussianNB

DROP = ['Sample num', 'X', 'Y', 'Resolution', 'Distance']  # 'Time', 'DayOfWeek', 'Date', , 'PdDistrict'

EPOCH = 1
le = preprocessing.LabelEncoder()

train_df = pd.read_csv('categoriacal/some_train.csv', header=0, index_col=0)
# train_df = pd.read_csv('neuraldata/crimes_TRAINING.csv', header=0, index_col=0)
#
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

gnb = GaussianNB()
X = train_df.iloc[:, :-1]
y = train_df['Descript']
print("Starting training, training samples: %i" % (len(X)))

gnb.fit(X, y)

print('Writing classifier to file. Time: {:.2f}'.format(time.time() - start_time))
print('Accuracy of classifier on train set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(gnb.score(X, y),
                                                    time.time() - start_time, len(X)))
# filename = 'decisiontree2.sav'
# pickle.dump(decisiontree, open(filename, 'wb'))

# TESTING
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
      ' time: {:.2f}, test set size: {:.2f}'.format(gnb.score(X, y),
                                                    time.time() - start_time, len(test_df)))
