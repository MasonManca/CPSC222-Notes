import pandas as pd
from pandas.core.reshape.merge import merge


populations = [219190, 744955, 147599, 2010] # these are parallel lists
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]


pop_ser = pd.Series(populations)

print(pop_ser)

pop_ser = pd.Series(populations, index = cities)

print(pop_ser)

pop_ser.name = "Populations"

print(pop_ser)