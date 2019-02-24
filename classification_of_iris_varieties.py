import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.datasets import load_iris
iris_dataset = load_iris()

print(iris_dataset.keys())
print(iris_dataset['DESCR'][:193] + '\n...')
print('Answers names: {}'.format(iris_dataset['target_names']))
print('feature names: \n{}'.format(iris_dataset['feature_names']))
print(type(iris_dataset['data']))
print(iris_dataset['data'].shape)
print('first five rows \n{}'.format(iris_dataset['data'][:5]))
print('Target type {}'.format(type(iris_dataset['target'])))
print(iris_dataset['target'].shape)
print('Answers \n{}'.format(iris_dataset['target'])) #0 – setosa ,
# 1 – versicolor , а 2 – virginica

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

'''Create DataFrame from X_train'''

iris_dataframe = pd.DataFrame(X_train, columns = iris_dataset.feature_names)

'''
create a scattering matrix from the dataframe, set the color of the points with the help of y_train
'''

grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                        hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

'''k model'''

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

print(knn.fit(X_train, y_train))

'''example by one flower'''
X_new = np.array([[5, 2.9, 1, 0.2]])
print('massive form X_new:{}'.format(X_new.shape))

'''predict'''

prediction = knn.predict(X_new)
print('predict{}'.format(prediction))
print('Predicted label {}'.format(iris_dataset['target_names'][prediction]))

'''Testing'''

y_pred = knn.predict(X_test)
print('Predict of the test suite: \n {}'.format(y_pred))
# Predict of the test suite:
#  [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
#  2]
print('Correctness in the test suite: {:.2f}'.format(np.mean(y_pred == y_test)))
# Correctness in the test suite: 0.97
print("Correctness in the test suite: {:.2f}".format(knn.score(X_test, y_test)))
# Correctness in the test suite: 0.97