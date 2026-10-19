### LeastSquare

## General information
This package can be used to find various values relating to the slopes and intercepts of 2 arrays X and Y as well as plotting a graph of the 2 

X and Y are required to be the same length

The available functions are
-Emp_mean(X)
-Var(X)
-CoVar(X,Y)
-Slope(X,Y)
-Intercept(X,Y)
-Plot(X,Y,slope,intercept)

Numpy is used for its summation function and matplotlib is used for plotting a graph to visulise the relationship between X and Y

## Installation 
From inside the 'LeastSquare' directory install the package in editable mode:

python -m pip install -e .

The required dependencies are specified in `pyproject.toml` and will be installed automatically.

## Example of use 
#Set the values for X and Y (which must be the same length)
X = [1,2,3,4]
Y = [2,4,6,8]

#Use any of the the first 5 functions as listed above 
print(Var(X))
print(Slope(X,Y))

#For a full demonstration on use you can run the files demo1.py or demo2.py:
python demo/demo1.py
python demo/demo2.py










