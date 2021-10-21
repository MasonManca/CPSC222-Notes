import pandas as pd
import numpy as np

def warm_up_task():
    msrp_df = pd.read_csv("msrp.csv")
    
    new_row = pd.Series(["chevy corvette", 77, 2212], index = ["CarName", "ModelYear", "MSRP"])
    msrp_df = msrp_df.append(new_row, ignore_index=True)
    print(msrp_df)
    counts_ser = msrp_df["ModelYear"].value_counts()
    print(counts_ser)

    grouped_df = msrp_df.groupby("ModelYear")
    mean_ser = grouped_df["MSRP"].mean()
    print(mean_ser)


# EDA: exploratory data analysis
# getting familiar with your data
# visualizing data, mining data (looking for groups, patterns, etc.), etc.

# goals of data vis
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing readability and understanding
# 3. label the units, and points of interest

# some jargon
# chart: a 2D visualization
# plot: a chart with data points (e.g. scatter plot)
# graph: a chart for a math function (e.g. sine)

# we will use the matplotlib library for charting w/python
# 3 ways to use matplotlib
# 1. using the pyplot module (what data scientists typically use)
# *there is always a "current" figure*
import matplotlib.pyplot as plt
# 2. using the OOP interface
# 3. a mix of the first two

# let's start with a simple line chart
def line_chart_example(x, y, y2, filename):
    # x and y could be:
    # 1D lists, 1D numpy arrays, pandas series, etc.
    plt.plot(x,y,label="X Squared")
    # now we need to "show" the plot
    plt.plot(x,y2,color="red",lw=5,label="X Cubed")
    plt.legend()
    plt.grid()
    plt.title("First Graph")
    # 3 main ways
    # 1. plt.show(): opens a window
    # plt.show()
    # 2. plt.savefig(filename): saves to a file (e.g. png, jpg, pdf,..)
    plt.savefig(filename)
    # 3. inline with jupyter notebook

def main():
    # we need some data
    x = list(range(6)) # [0, 1, 2, 3, 4, 5]
    y = [] # will be squares of x
    y2 = []
    for val in x:
        y.append(val ** 2)
        y2.append(val ** 3)
    print(x) 
    print(y)
    # task: add another "y" line 
    # for x values cubed
    line_chart_example(x, y, y2, "line_example.png")
    scatter_chart(x, y, "scatter_chart.png")
    bar_chart(x, y, "bar_chart.png")
    pie_chart(x, y, "pie_chart.png")

#game plan
#line chart
#scatter chart
def scatter_chart(x,y, filename):
    plt.figure() #creates a new blank current figure
    plt.scatter(x,y, color = "green", s = 500, marker = 'X')
    plt.savefig(filename)


#bar chart
def bar_chart(x,y,filename):
    plt.figure()
    plt.bar(x, y, facecolor = "blue", edgecolor = "black")
    plt.savefig(filename)

#pie chart
def pie_chart(x,y,filename):
    plt.figure()
    plt.pie(y, labels = x, autopct = "%1.1f%%")
    plt.savefig(filename)

#histogram
def histogram(data,filename):
    plt.figure()
    plt.hist(data, bins = 30, edgecolor = "black") #by default there are 10 bins
    plt.savefig(filename)

#box plots


#lets randomly sample 1000 points frmo a normal distrubution
#wiht mean 100 and stdv 20
np.random.seed(0)
mean = 100
stdev = 20
num_samples = 1000
random_data = np.random.normal(mean, stdev, num_samples)
histogram(random_data, "histogram_graph.png")

main()

