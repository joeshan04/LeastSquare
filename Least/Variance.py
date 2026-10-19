import numpy as np 
from .EmpMean import Emp_mean

def Var(X):
#Uses our empirical mean from previous module
    X_bar = Emp_mean(X)
#This just sets U to be equal to variance from the general formula for variance 
    U = np.sum((X - X_bar)**2)/len(X)
    return U

def CoVar(X,Y):
#Prints error message if X and Y are not the same length
    if len(X)!=len(Y):
             raise ValueError('X and Y must be the same length')
#Takes input of 2 arrays X and Y and finds empirical mean 
    X_bar = Emp_mean(X)
    Y_bar = Emp_mean(Y)
#Uses general formula for co variance
    V = np.sum((X-X_bar)*(Y-Y_bar))/len(X)
    return V



    
