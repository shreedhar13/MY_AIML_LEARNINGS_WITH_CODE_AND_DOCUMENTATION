import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

#-------------DATA CLEANING---------------
#---1)method_delete rows and columns
df=pd.read_csv(r'D:\AIML_PROGRAMS\first_model\house-prices-advanced-regression-techniques\train.csv')
print(df)#[1460 rows x 81 columns] and dataframe is printed
#to print all columns and rows
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
# print(df)
pd.set_option('display.max_columns',None)#all columns are include to display ie;doesnt hide anything
pd.set_option('display.max_rows',10)#only 10 rows 5 from head and 5 from tail is selected to display.(even).only 10 rows are displayed and remanining are hided
#if 9 is given then 4 from head and 4 from tail and middle .... is displayed.(odd)
print(df)
print(df.info())#no of rows with non null cell/field in each columns.[1460 rows x 81 columns] 0 to 1459 row indices and 0 to 80 column indices(used as both label and integer indices)
#Id column(feature/independent feature) dont have any null value/missing value ie;all 1460 rows are having valid value
#Alley column(feature/independent feature) having  only 91 rows(cell) as non null and remaining 1369 rows(cell) are having null value(missing value)
print(df.isnull())#to check how many cells in each column are null value/missing value
#further code we continue in jupyter notebook,,bcz easy to visualize
