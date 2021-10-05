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
population  = [219190, 744955, 147599, 2010]
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]

pop_ser = pd.Series(population, index = cities)
print(pop_ser)

#Index slicing/indexing
print(pop_ser["Seattle"])
print(pop_ser[["Seattle", "Leavenworth"]])
print(pop_ser["Seattle": "Leavenworth"]) # THE STOP IS INCLUSIVE

# we can still do position based indexing

#We can name a Series
#This si really nice if we add this series as a column to a DataFrame

pop_ser.name = "Population"
print(pop_ser)

#Summary Stats
print(pop_ser.mean())
print(pop_ser.std())

#we can add new data to a series, just like we add a new key-value pair to a dictionary
pop_ser["Pullman"] = 34019
print(pop_ser)

#We can make an empty series
pop_ser2 = pd.Series(dtype = int)


#dataframes
#dataframes are used to store 2D data in pandas
# can make a dataframe from a 2D list
twod_list = [[3,"a",4.5],[7,"b",10.99],[-10,"c",-1.5]]
header = ["col1", "col2", "col3"]
df = pd.DataFrame(twod_list, columns = header)
print(df)
#the column labels are called columns
#The row labels are called the index
row_index = ["row1", "row2", "row3"]
df = pd.DataFrame(twod_list, index = row_index, columns = header)
print(df)

#task: create pop_df
#dataframe for the popluation data
#3 Cols
header = ["City","Population","Class"]
pop_data = [["Seattle",744966,"Large"], ["Spokane",219190,"Medium"],["Bellevue",147599,"Medium"], ["Levenworth",2010,"Small"]]
pop_df = pd.DataFrame(pop_data,columns = header)
print(pop_df)
pop_df = pop_df.set_index("City")
print(pop_df)

#indexing/slicing
#grab column by its label returns a series
pop_ser = pop_df["Population"]
print(pop_ser)
#pop_ser = pop.df.iloc[0]
#print(pop_ser)
#pop_spokane = pop.df.iloc[0,0]


#loc [] is for label based indexing
pop_spokane = pop_df.loc["Spokane", "Population"]
print(pop_spokane)

#slice across columns with more than one column returns a data frame
regions_df = pd.read_csv("regions.csv", index_col = 0)
print(regions_df)
