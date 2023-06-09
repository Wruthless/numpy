from pandas import *
import numpy as np

# Pandas series come with indices.
sr = Series([12, 33, 45, 67], index=[1, 2, 3, 4], dtype=complex)
print(sr, "\n")

print('--------------------------------')

# Using letters as indices.
sr1 = Series([12, 33, 45, 67], index=['a', 'b', 'c', 'd'])
print(sr1, "\n")

print('--------------------------------')

# Convert numpy arrays to pandas series.
ar = np.array([1, 2, 3, 4, 5, 6])
sr2 = Series(data=ar, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(sr2, "\n")

print('--------------------------------')

# Printing a single index from a series.
sr3 = Series([1, 23, 4, 5, 66, 7], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(sr3['e'])
print(sr3[5], "\n")

# Printing using local index and iloc.
sr4 = Series([1, 23, 4, 5, 66, 7], index=[1, 2, 3, 4, 5, 6])
print(sr4.loc[1])
print(sr4.iloc[1], "\n")

print('--------------------------------')

# Dataframe with dictionary.
df = DataFrame({'Age': [17, 21, 33],
                'Colors': ["Blue", "Red", "Yellow"]})
print(df, "\n")

# Dataframe with two-dimensional numpy array.
ar2 = np.array([[17, 21, 33],
                [22, 45, 71],
                [34, 67, 99]])
df2 = DataFrame(data=ar2, columns=['C1', 'C2', 'C3'], index=['a', 'b', 'c'])
print(df2, "\n")
print("Access to column 'C1' and 'C3' from dataframe")
print(df2['C1'], "\n")
print(df2['C3'], "\n")
print("All rows in 'c' and all rows in 'a' (using iloc[0])")
print(df2.loc['c'])
print(df2.iloc[0], "\n")

print('--------------------------------')

print("Single values.")

# Single values
print(df2.loc['b', 'C2'])
print(df2.iloc[1, 1], "\n")

print('--------------------------------')

