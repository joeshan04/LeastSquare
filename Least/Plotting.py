import matplotlib.pyplot as plt

#This function is to plot a scatter graph of X and Y,it has inputs of X, Y and the slope and intercept 

def Plot(X, Y, slope, intercept):

    plt.scatter(X, Y, label="Data")

#This sets x_line to be equal to an array of each value in X
    x_line = [min(X), max(X)]

#This sets y_line to be equal to the corresponding Y value for each X
    y_line = [slope * x + intercept for x in x_line]

#We then plot the regression line on the scatter graph 
    plt.plot(x_line, y_line, color="red", label="Regression line")

#Customisation - adds labels and a legend then displays the plot
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

