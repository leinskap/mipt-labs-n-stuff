import numpy as np
import random
import csv
import math
with open('iris.csv', 'r') as file:
    reader = csv.reader(file)
    iris = [row for row in reader]
print(iris)

def MinMaxScaler(x):
    for j in range(len(x[0])-1):
        mx = max([float(x[k][j]) for k in range(len(x))])
        mn = min([float(x[k][j]) for k in range(len(x))])
        for i in range(len(x)):
            x[i][j] = (float(x[i][j])-mn)/(mx-mn)

label = iris[0]
iris = iris[1:]
y_train = []
for i in range(100):
    y_train.append(iris[i][-1])


iris = np.array(iris)
MinMaxScaler(iris)
print(iris)

random.shuffle(iris)
print(iris)


X_train = np.array(iris[:70, :-1])

X_test = np.array(iris[70:100, :-1])
y_test = iris[70:100, -1:]

y_predicted = []

n=5
for x_tst in X_test:
    distances = []
    for k, x_trn in enumerate(X_train):
        distance = math.sqrt(sum((float(x_tst[i])-float(X_train[k][i]))**2 for i in range(len(X_train[0]))))
        distances.append(distance)
    nearest_dist = sorted(distances)[:n]
    nearest = []
    for a in nearest_dist:
        for i in range(len(distances)):
            if len(nearest)<n and a==distances[i] and not(i in nearest):
                    nearest.append(i)
    variety = [y_train[h] for h in nearest]
    counts = [variety.count(v) for v in variety]
    y_predicted.append(str(variety[counts.index(max(counts))]))
    print(variety[counts.index(max(counts))])
print(len(y_predicted))

c=0
for i in range(30):
    print(str(y_predicted[i]))
    if y_predicted[i] == y_test[i] : c+=1
print(c/30)






train = np.array([[1, 1], [2, 2], [3, 3]])
test  = np.array([[1, 1]])
print(train-test)



