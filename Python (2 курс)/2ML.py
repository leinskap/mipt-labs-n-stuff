import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
from scipy.stats import trim_mean
from scipy.stats import iqr
import seaborn as sns

from sklearn.datasets import load_iris
iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0, test_size=0.8)

from sklearn.neighbors import KNeighborsClassifier

scores = []

for N in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=N)
    knn.fit(X_train, y_train)
    scores.append(round(knn.score(X_test, y_test), 2))
print(scores)

def mad(arr):
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))



mean_score = st.mean(scores)
median_score = st.median(scores)
trim_mean_score = trim_mean(scores, 0.2)
score_variance = st.variance(scores)
std_dev = st.stdev(scores)
MAD = mad(scores)
score_range = max(scores) - min(scores)
IQR = iqr(scores)
print(mean_score, median_score, trim_mean_score, score_variance, std_dev, MAD, score_range, IQR)

df = pd.DataFrame({'A': [7, 8, 9, 12, 14],
 'B': [5, 6, 6, 8, 11],
 'C': [8, 9, 11, 13, 17]})






IQR = []
scores = np.zeros((9, 100))
for N in range(1, 10):
    for a in range(100):
        X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=a,
                                                        test_size=0.8)

        knn = KNeighborsClassifier(n_neighbors=N)
        knn.fit(X_train, y_train)
        scores[N-1][a] = round(knn.score(X_test, y_test), 2)
    IQR.append(iqr(scores[N-1]))
print(scores[0])


df = pd.DataFrame({'1': scores[0],
'2': scores[1],
'3': scores[2],
'4': scores[3],
'5': scores[4],
'6': scores[5],
'7': scores[6],
'8': scores[7],
'9': scores[8]})

print(IQR)

sns.boxplot(x='variable', y='value', data=pd.melt(df)).set (
 xlabel='N',
 ylabel='score')
plt.show()




IQR_mean = []
distance_metrics = ['minkowski', 'chebyshev', 'euclidean', 'manhattan', 'cosine']
for metrica in distance_metrics:
    IQR = []
    scores = np.zeros((9, 100))
    for N in range(1, 10):
        for a in range(100):
            X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'],
                                                                random_state=a,
                                                                test_size=0.8)

            knn = KNeighborsClassifier(n_neighbors=N, metric = metrica)
            knn.fit(X_train, y_train)
            scores[N - 1][a] = round(knn.score(X_test, y_test), 2)
        IQR.append(iqr(scores[N - 1]))
    IQR_mean.append(trim_mean(IQR, 0.2))


df = pd.DataFrame({'metric': distance_metrics, 'mean_trim IQR': IQR_mean})

ax = df.plot.bar(x='metric', y='mean_trim IQR')
plt.show()

import math
x = np.linspace(0.1, 3, 50)
df = pd.DataFrame({'k/x': 0.03/x, 'gaussian': 1/(2*math.pi)**0.5 * math.exp(-x**2/2)})
df.plot()
plt.show()