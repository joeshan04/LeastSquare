#Imports the functions we need from the previous packages 
from .Variance import CoVar
from .Variance import Var
from .EmpMean import Emp_mean

#This is our function for slope of X and Y, just plugging in the values of the previous functions 
def Slope(X,Y):
#Prints error message if X and Y are not the same length

    if len(X)!=len(Y):
                 raise ValueError('X and Y must be the same length')
    slope = CoVar(X,Y)/Var(X)
    return slope

#This is our function to find the intercept
def Intercept(X,Y):
#Prints error message if X and Y are not the same length

    if len(X)!=len(Y):
                 raise ValueError('X and Y must be the same length')
    intercept = Emp_mean(Y)-Emp_mean(X)*Slope(X,Y)
    return intercept

    