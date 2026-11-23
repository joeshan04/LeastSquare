import pandas as pd 
#Creates a list with 2 columns of data
ltmp = [[1,2],
        [2,4],
        [3,6],
        [4,8],
        [5,10]]

#Prepares an index for the dataframe - produces item 00i where where is the number on list 
cindex = [f'item{i:03d}' for i in range(1, 6)]

#Creates the data frame and sets columns to be X and Y and index to be cindex
df = pd.DataFrame(ltmp,columns = ['X','Y'],index = cindex)
print(df)


df.to_csv("data/sample.csv", index=False)