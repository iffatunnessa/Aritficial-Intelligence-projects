# Import the necessary libraries
import numpy
import matplotlib.pyplot as plot
import pandas
from sklearn import metrics
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.tree import DecisionTreeRegressor

# Import the dataset
dataset = pandas.read_csv('WhiteWineQuality.csv')

x = dataset.iloc[:,0:10]
y = dataset.iloc[:,11]

print(x)
print(y)

# Split the dataset into the training set and test set
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 2/3)

# Creating a DecisionTreeRegressor on our trainging set.
regressor = DecisionTreeRegressor()
regressor.fit(xTrain, yTrain)

# Predicting the test set results
yPrediction = regressor.predict(xTest)

# Creating a AdaptiveBoostingRegressor on our training set
abr = AdaBoostRegressor()
abr.fit(xTrain, yTrain.values.ravel())
#Prediction
yPrediction2 = abr.predict(xTest)

#calculation errors
mabs1=metrics.mean_absolute_error(yTest, yPrediction)
r21=metrics.r2_score(yTest, yPrediction)
s1=metrics.mean_squared_error(yTest, yPrediction)
max1=metrics.max_error(yTest, yPrediction)

mabs2=metrics.mean_absolute_error(yTest, yPrediction2)
r22=metrics.r2_score(yTest, yPrediction2)
s2=metrics.mean_squared_error(yTest, yPrediction2)
max2=metrics.max_error(yTest, yPrediction2)

# Displaying errors for DecisionTree
print('Mean Absolute Error for DecisionTree:', mabs1)
print('r2:', r21)
print('mean squared error for DecisionTree:', s1)
print('mean squared error for DecisionTree:', max1)
# Displaying errors Adabooster
print('Mean Absolute Error for Adabooster:', mabs2)
print('r2 for Adabooster:', r22)
print('mean squared error for Adabooster:', s2)
print('mean Max error for Adabooster:', max2)

#Cross Validation
print("Cross Validation score for Decision Tree:",cross_val_score(regressor, x,y.values.ravel(),
                                                                  cv = 5, scoring = 'neg_median_absolute_error'))
print("Cross Validation score for Adaptive Boosting:",cross_val_score(abr, x, y.values.ravel(),
                                                                      cv = 5, scoring = 'neg_median_absolute_error'))
# Figure and comparison show
plot.figure(figsize= (10, 2))
#mean absolute
names = ['Decision Tree', 'Adaptive Boosting']
values = [mabs1,mabs2]
plot.subplot(121).set_ylabel('Mean Absolute Error')

plot.bar(names, values)
plot.show()

#r2
values = [r21,r22]
plot.subplot(121).set_ylabel('R2 score')
plot.bar(names, values)
plot.show()

#Mean Squared
values = [s1,s2]
plot.subplot(121).set_ylabel('Mean squared error')

plot.bar(names, values)
plot.show()

#max error
values = [max1,max2]
plot.subplot(121).set_ylabel('Max error')
plot.bar(names, values)
plot.show()
