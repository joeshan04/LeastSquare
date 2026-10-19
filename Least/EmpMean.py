import numpy as np 

#Defines the empirical mean of X as the sum of all its elements divided by the number of elements

def Emp_mean(X):
    X_bar = np.sum(X)/len(X)
    return X_bar

