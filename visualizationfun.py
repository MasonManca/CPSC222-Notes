import matplotlib.pyplot as plt



'''
EDA- explatory data analysis
getting familiar with your data
    exploring it

goals:
    1) clearly and accurately represent data
    2) be creative, with the goal of increasing readability and understanding
    3) Label the units and points of interest

some jargon
chart: a 2d visualization
plot: a chart with data points (e.g. scatter plot)
graph: a chart for a mnathfunction (e.g. sine)

we will use the matplotlib library for charting w/python

3 ways to use matplotlib
1) using the pyplot module (what data scientists typically use)
*there is always a "current" figure*
2) using the oop interface
3) a mix of the first two

'''

def line_chart_example(x,y, filename):
    plt.plot(x,y)
    # 3 main ways
    # plt.show(): opens a window
    plt.show()
    #plt.savefig(filename): saves to a file
    plt.savefig(filename)
    # inline with jupyter notebook


def main():
    x = list(range(6))
    y = []
    z = []

    for value in x:
        y.append(val**2)
    for value in x:
        z.append(val**3)
    print(x)
    print(y)
    #add another y line for x values cubed
    line_chart_example(x, z, "line_example.png")

main()