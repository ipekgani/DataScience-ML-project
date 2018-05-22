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

train_df = pd.read_csv('one_hot_data/crimes_TRAINING.csv', header=0, index_col=0)
train_df = train_df.drop('Sample num', axis=1)
train_df = train_df.dropna(axis=0, how='any')

mlp_classifier = MLPClassifier(warm_start=True, hidden_layer_sizes=[100, 50], solver="sgd",
                               learning_rate_init=0.001,
                               shuffle=True, random_state=0, tol=1e-6,
                               verbose=True, early_stopping=False, batch_size=BATCH_SIZE)

X = train_df.iloc[:, 1:]
y = train_df['Descript']
print("Starting training, batch size: %i, training samples: %i" % (BATCH_SIZE, len(X)))
mlp_classifier.fit(X, y)

print('Writing classifier to file. Time: {:.2f}'.format(time.time() - start_time))

# filename = 'neural1.sav'
# pickle.dump(mlp_classifier, open(filename, 'wb'))
print('Accuracy of classifier on test set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(mlp_classifier.score(X, y),
                                                    time.time() - start_time, len(X)))


# TESTING
test_df = pd.read_csv('neuraldata/crimes_TESTING.csv', header=0, index_col=0)
test_df = test_df.drop('Sample num', axis=1)
test_df = test_df.dropna(axis=0, how='any')

X = test_df.iloc[:, 1:]
y = test_df['Descript']

print('Accuracy of classifier on test set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(mlp_classifier.score(X, y),
                                                    time.time() - start_time, len(test_df)))


