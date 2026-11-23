## Demo of the different features 

# Import all of our modules 
from Least import Emp_mean,Var,CoVar,Slope,Intercept,Plot
import pandas as pd

#Imports a CSV with data for our X and Y
df = pd.read_csv("data/sample.csv")
X = df['X']
Y = df['Y']
#Sub X and Y into each function and print the result 
print('This is our Empirical mean:',Emp_mean(X))
print('This is our Variance:',Var(X))
print('This is our Covariance:',CoVar(X,Y))
print('This is our Slope:',Slope(X,Y))
print('This is our Intercept:',Intercept(X,Y))

#This gives us our plot of the data
Plot(X,Y,Slope(X,Y),Intercept(X,Y))
