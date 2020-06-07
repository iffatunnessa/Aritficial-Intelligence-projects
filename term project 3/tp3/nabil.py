# Import the necessary libraries
import numpy
import matplotlib.pyplot as plot
import pandas
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import cross_val_score

# Import the dataset
dataset = pandas.read_csv('WhiteWineQuality.csv')

# Differentiate attribute and target columns
X = dataset.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]]
Y = dataset.iloc[:, [11]]

# Split the dataset into the training set and test set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 2/3)

# Creating a DecisionTreeRegressor on our trainging set.
decision_tree_regressor = DecisionTreeRegressor()
decision_tree_regressor.fit(x_train, y_train)

# Creating a AdaptiveBoostingRegressor on our training set
adaptive_boost_regressor = AdaBoostRegressor()
adaptive_boost_regressor.fit(x_train, y_train.values.ravel())

# Predicting the test set results
y_prediction = decision_tree_regressor.predict(x_test)
y_prediction2 = adaptive_boost_regressor.predict(x_test)

# Calculating the evaluation metrices
mean_absolute_error_decision_tree = metrics.mean_absolute_error(y_test, y_prediction)
max_error_decision_tree = metrics.max_error(y_test, y_prediction)
explained_variance_decision_tree = metrics.explained_variance_score(y_test, y_prediction)
r2_score_decision_tree = metrics.r2_score(y_test, y_prediction)

mean_absolute_error_adaptive_boosting = metrics.mean_absolute_error(y_test, y_prediction2)
max_error_adaptive_boosting = metrics.max_error(y_test, y_prediction2)
explained_variance_adaptive_boosting = metrics.explained_variance_score(y_test, y_prediction2)
r2_score_adaptive_boosting = metrics.r2_score(y_test, y_prediction2)

# Displaying errors
print("Mean Absolute Error for Decision Tree Regression:", mean_absolute_error_decision_tree)
print("Max Error for Decision Tree Regression:", max_error_decision_tree)
print("Explained Variance for Decision Tree Regression:", explained_variance_decision_tree)
print("R2 Score for Decision Tree Regression:", r2_score_decision_tree)
print()
print("Mean Absolute Error for Adaptive Boosting Regression:", mean_absolute_error_adaptive_boosting)
print("Max Error for Adaptive Boosting Regression:", max_error_adaptive_boosting)
print("Explained Variance for Adaptive Boosting Regression:", explained_variance_adaptive_boosting)
print("R2 Score for Adaptive Boosting Regression:", r2_score_adaptive_boosting)

# Cross Validation check
cross_validation_decision_tree = cross_val_score(decision_tree_regressor, X, Y.values.ravel(), cv = 5, scoring = 'neg_median_absolute_error')
cross_validation_adaptive_boosting = cross_val_score(adaptive_boost_regressor, X, Y.values.ravel(), cv = 5, scoring = 'neg_median_absolute_error')

print("Cross Validation score for Decision Tree:",cross_validation_decision_tree)
print("Cross Validation score for Adaptive Boosting:",cross_validation_adaptive_boosting)

# Figure and comparison show
names = ['Decision Tree', 'Adaptive Boosting']
values = [mean_absolute_error_decision_tree, mean_absolute_error_adaptive_boosting]
plot.figure(figsize= (15, 5))
plot.subplot(121).set_ylabel('Mean Absolute Error')

plot.bar(names, values)

values2 = [explained_variance_decision_tree, explained_variance_adaptive_boosting]
plot.subplot(122).set_ylabel('Explained Variance')
plot.bar(names, values2)

plot.show()

plot.figure(figsize= (15, 5))
values3 = [max_error_decision_tree, max_error_adaptive_boosting]
plot.subplot(121).set_ylabel('Max Error')
plot.bar(names, values3)

values4 = [r2_score_decision_tree, r2_score_adaptive_boosting]
plot.subplot(122).set_ylabel('R2 Score')
plot.bar(names, values4)

plot.show()

names = ['Split-1', 'Split-2', 'Split-3', 'Split-4', 'Split-5']
plot.figure(figsize = (15, 5))
plot.subplot(111)
plot.bar(names, cross_validation_decision_tree)

plot.title('Decision Tree Cross Validation', loc = 'center')
plot.show()

plot.figure(figsize = (15, 5))
plot.subplot(111)
plot.bar(names, cross_validation_adaptive_boosting)

plot.title('Adaptive Boosting Cross Validation', loc = 'center')
plot.show()