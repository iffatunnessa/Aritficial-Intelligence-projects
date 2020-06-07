# Import the necessary libraries
import matplotlib.pyplot as plot
import pandas
import numpy as np 

def getAlpha():
    global xTrain,yTrain,xMean,yMean
    
    n = 0
    for i in range(len(xTrain)):
        n = n + (xTrain[i] - xMean) * (yTrain[i] - yMean)
        
    dn = 0
    for i in range(len(xTrain)):
        dn = dn + pow((xTrain[i] - xMean),2)
        
    return n/dn

def meanAbsoluteError():
    global yTest, pred
    
    n = 0
    for i in range(len(yTest)):
        nom = n + abs(yTest[i] - pred[i])
        
    return n/len(yTest)

def meanSquaredError():
    global yTest, pred
    
    n = 0
    for i in range(len(yTest)):
        n = n + pow((yTest[i] - pred[i]),2)
        
    return n/len(yTest)


# Import the dataset
dataset = pandas.read_csv('salaryData.csv')


# Differentiate attribute and target columns
x = dataset['YearsExperience'].values
y = dataset['Salary'].values

# Reshaping 
X = x.reshape(len(x),1)
Y = y.reshape(len(y),1)

# Spliting dataset into test and training data
xTrain, yTrain, xTest, yTest, pred = ([] for i in range(5))
for i in range(int(len(X)*1/3)):
    xTrain.append(X[i])
    yTrain.append(Y[i])

for i in range(int(len(X)*1/3), len(X)):
    xTest.append(X[i])
    yTest.append(Y[i])

# Calculating the mean values and alpha, beta
xMean = np.mean(xTrain)
yMean = np.mean(yTrain)

alpha = getAlpha()
beta = yMean - alpha*xMean

# Prediction on Training data
for i in range(len(xTest)):
    pred.append( alpha* xTest[i] + beta)

print(np.asarray(pred).shape)
df = pandas.DataFrame({'Actual': np.asarray(yTest).flatten(), 'Predicted': np.asarray(pred).flatten()})
print(df)
df1 = df
df1.plot(kind='bar')
plot.show()

print('Mean Absolute Error:', meanAbsoluteError())
print('Mean Squared Error:', meanSquaredError())
print('Root Mean Squared Error:', np.sqrt(meanSquaredError()))

