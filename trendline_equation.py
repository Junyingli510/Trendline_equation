# import lib
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
 
# define the true objective function
def objective(x, a, b):
	return a * x + b

# set data
data = [
        [10, 15.4], 
	[19, 19.4], 
	[28, 10.8], 
	[37, 30.2], 
	[46, 11.7], 
	[55, 49.3],
	[64, 8.86], 
	[73, 61.1], 
	[82, 69.3], 
	[91, 75]
]

x = []
y = []

for i in range(0, len(data)):
    value = data[i]
    x.append(value[0])
    y.append(value[1])

print(x)
print(y)

# # load the dataset from online
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
# dataframe = read_csv(url, header=None)
# data = dataframe.values
# # choose the input and output variables
# x, y = data[:, 4], data[:, -1]
# print(x)
# print(y)
# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b = popt
print('y = %.5f * x + %.5f' % (a, b))
# plot input vs output
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b)
# create a line plot for the mapping function
title = 'Trend Line Equation: y = %.5f * x + %.5f' % (a, b)
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.title(title)
pyplot.show()
