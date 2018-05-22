import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from sklearn import tree, preprocessing
import time, pickle
start_time = time.time()

EPOCH = 1
BATCH_SIZE = 1024
le = preprocessing.LabelEncoder()

# train_df = pd.read_csv('categoriacal/categorical_TRAINING.csv', header=0, index_col=0)
train_df = pd.read_csv('neuraldata/crimes_TRAINING.csv', header=0, index_col=0)

train_df = train_df.sample(frac=1)
train_df = train_df.dropna(axis=0, how='any')
train_df = train_df.drop(['Sample num'], axis=1)

decisiontree = tree.DecisionTreeClassifier(max_depth=30)

X = train_df.iloc[:, 1:]
y = train_df['Descript']
print("Starting training, training samples: %i" % (len(X)))

decisiontree.fit(X, y)

print('Writing classifier to file. Time: {:.2f}'.format(time.time() - start_time))
print('Accuracy of classifier on test set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(decisiontree.score(X, y),
                                                    time.time() - start_time, len(X)))
# filename = 'decisiontree2.sav'
# pickle.dump(decisiontree, open(filename, 'wb'))

# TESTING
test_df = pd.read_csv('neuraldata/crimes_TESTING.csv', header=0, index_col=0)
test_df = test_df.sample(frac=1)
test_df = test_df.drop('Sample num', axis=1)
test_df = test_df.dropna(axis=0, how='any')

X = test_df.iloc[:, 1:]
y = test_df['Descript']

print('Accuracy of classifier on test set: {:.2f},'
      ' time: {:.2f}, test set size: {:.2f}'.format(decisiontree.score(X, y),
                                                    time.time() - start_time, len(test_df)))
# import graphviz
# dot_data = tree.export_graphviz(decisiontree, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("treegraph3")
# print(list(X.columns), list(y.unique()))
# dot_data = tree.export_graphviz(decisiontree, out_file=None,
#                                 feature_names=list(X.columns),
#                                 class_names=str(list(y.unique())),
#                                 filled=True, rounded=True,
#                                 special_characters=True)
# graph = graphviz.Source(dot_data)
