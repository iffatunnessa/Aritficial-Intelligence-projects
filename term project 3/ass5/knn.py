from sklearn.datasets import load_iris
import warnings
import random
import math
from operator import itemgetter

warnings.simplefilter("ignore")


def getDistance(x, y):
    return math.sqrt(pow((x[0] - y[0]), 2) + pow((x[1] - y[1]), 2) + pow((x[2] - y[2]), 2) + pow((x[3] - y[3]), 2))


def k_nearest_neighbour(k):
    global xtrain, xtest
    accuracy = 0
    for i in range(len(xtest)):
        distances = []
        for j in range(len(xtrain)):
            check = getDistance(xtest[i][0], xtrain[j][0])
            distances.append([check, xtrain[j][1]])

        distances.sort(key=itemgetter(0))
        variant = 0

        for j in range(k):
            variant = variant + distances[j][1]
        variant = round(variant / k)

        if xtest[i][1] == variant:
            accuracy = accuracy + 1

    print("Accuracy for ", k, " nearest neighbour is ", accuracy / len(xtest))


iris_data = load_iris()
dataset = []
for i in range(len(iris_data.data)):
    temp = [iris_data.data[i], iris_data.target[i]]
    dataset.append(temp)

random.shuffle(dataset)

xtrain, xtest = ([] for i in range(2))
for i in range(int(len(dataset) * 2 / 3)):
    xtrain.append(dataset[i])

for i in range(int(len(dataset) * 2 / 3), len(dataset)):
    xtest.append(dataset[i])

for i in range(1, 6):
    k_nearest_neighbour(i)
