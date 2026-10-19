## Demo of the different features 

# Import all of our modules 
from Least import Emp_mean,Var,CoVar,Slope,Intercept,Plot

# Set arrays X and Y which will be used for this demo
X = [2,4,6,8,10,12,14,16,18,20]
Y = [1,3,5,5,7,8,9,11,13,14]

#Sub X and Y into each function and print the result 
print('This is our Empirical mean:',Emp_mean(X))
print('This is our Variance:',Var(X))
print('This is our Covariance:',CoVar(X,Y))
print('This is our Slope:',Slope(X,Y))
print('This is our Intercept:',Intercept(X,Y))

#This gives us our plot of the data
Plot(X,Y,Slope(X,Y),Intercept(X,Y))
