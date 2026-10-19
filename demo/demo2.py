## Second demo of the different features 

# Import all of our modules 
from Least import Emp_mean,Var,CoVar,Slope,Intercept,Plot

# Set arrays X and Y which will be used for this demo
X = [12, 5, 18, 7, 23, 15, 9, 30, 14, 21, 3, 27, 11, 19, 25, 8, 16, 29, 6, 22]
Y = [10, 4, 15, 8, 18, 11, 7, 22, 10, 16, 2, 20, 9, 14, 19, 6, 13, 21, 5, 17]

#Sub X and Y into each function and print the result 
print('This is our Empirical mean:',Emp_mean(X))
print('This is our Variance:',Var(X))
print('This is our Covariance:',CoVar(X,Y))
print('This is our Slope:',Slope(X,Y))
print('This is our Intercept:',Intercept(X,Y))

#This gives us our plot of the data
Plot(X,Y,Slope(X,Y),Intercept(X,Y))