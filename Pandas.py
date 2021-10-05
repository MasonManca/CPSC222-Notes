import pandas as pd


"""
Pandas is short for panel data
It is a library, like numpy, for data science

one of the major shortcomings of using lists
for data science, is the lack of label-based indexing
    The header!
Pandas uses Label based indexing
    good built in functionality for indexing, cleaning, stats etc

There are two main objects we work with in pandas

1d: pandas Series
2d: pandas DataFrame (every column is a series)

Lets start with Series
There are a few ways to make a series

"""
population  = [219190, 74495, 147599, 2010]
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]

pop_ser = pd.Series(population, index = cities)
print(pop_ser)
print(pop_ser["Seattle"])


