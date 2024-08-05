"""              first     last   email  marks
             0   shree  jagatap   sj@    21
             1  hrushi   dongare   hd@    15      ->here,first,last,email,marks is know as features.first,last,email(independent features),,marks(dependent feature)ie;wrt first last feature marks are derived so dependent
             2    yogi   dongare   yd@    40     specifically-->first ,last, email is categorical feature/column(column contains non numeric value),,marks is a numeric value feature """

#dtype : object means String
#pandas is a very very important library in datascience for analysing data if we dont use  pandas then  machine learning,,(but DL can run w/o pandas) is not possible soo...we need pandas
#pandas is a software library written for the pyhton programming language for data manipulation and analysis
#pandas is fast,powerful,flexible and easy to use open source
import pandas as pd
df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_public.csv")  #dataframe(df) it is a table like database
print(df)
#note->in csv file missing values is represented as NA(not available) and when u  brought it as dataframe in python missing value are represented as NaN
#note the op where column are 61 and rows are 64461 but all rows and column not displayed ie;shrinked and only some data is shown, but we can display all using following function
#shape of dataframe
print(df.shape) #(64461,61) 64461 rows and 61 columns
#to get info about dataframe
print(df.info()) #no of rows which has non null value
#object means string type
#to display all columns visible to user
print("all columns")
pd.set_option('display.max_columns',61)
#  OR   pd.set_option('display.max_columns',None)
print(df)
#for displaying all rows
pd.set_option('display.max_rows',61) #we are displaying first 61 rows only,,not displaying all 64461 rows
#pd.set_option('display.max_rows',None) or pd.set_option('display.max_rows',64461)  to display all rows 
print(df)

# metadata or info about each column is written in survey_result_schema .csv
schema_df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_schema.csv")
print("metadta")
print(schema_df)

#displaying selected no of rows
#top 5 rows are displayed
print("top 5  rows")
print(df.head())

print("top n rows")
print(df.head(10)) # therefore top 10 rows are displayed

print("last 5 rows")
print(df.tail()) #botto, 5 rows are displayed

print("bottom or last n rows")
print(df.tail(10)) #bottom 10 rows are displyed

#we can store our data in python ductionary also as key:value pairs
person={"first":"shree","last":"jagatap","email":"sj2002@gmail.com"}
print(person) #{'first': 'shree', 'last': 'jagatap', 'email': 'sj2002@gmail.com'}
#vut here the dictionary can store only one value for each key
#lets go with list of values for each key
people={"first":["shree",'hrushi','yogi','abhi'],'last':["jagatap",'dongre','dongre','sathe'],"email":['sj@','hd@','yd@',"as@"]}
print(people)

#access value of specific key
print(people['email']) #['sj@', 'hd@', 'yd@', 'as@']  or people.email also works but if in place of people you used any other variable which is same as attrubute of pandas then it will produce error so first one is recomended
#problem with dictionary is :it has very limited functionalities,hence lets go to pandas and its data frames
#DATAFRAMES:is a 2D datastructure (rows and column) ie;like database table
#therefore we can transform dictionary to dataframes
df=pd.DataFrame(people)
print(df) 
"""              first     last   email
             0   shree  jagatap   sj@
             1  hrushi   dongre   hd@     -->dataferame 0 1 2 3 bydefault indexing is there
             2    yogi   dongre   yd@
             3    abhi    sathe   as@ """
#for accesing a single column like people['email'] in dictionary for dataframe use df['email']
print(df['email']) 
'''0    sj@
   1    hd@
   2    yd@
   3    as@'''
   #the above printed objects is a series 
   #series --> 1d array(1 column with multiple rows).note indexing is not counted as column
   #dataframe:container for multiple series
print(type(df['email'])) #op->pandas.core.series.series .pandas series means 1 column with asscoicted index,by default 0 1 .... is there but we can change
#access multiple columns
print(df[['first','last']]) 
'''        first     last
       0   shree  jagatap
       1  hrushi   dongre
       2    yogi   dongre
       3    abhi    sathe '''
#where 0 1 2 3 are row indexes or row labels (by default this is there but we can change) ie;0 1 2 3 is default indexing and label
#to get all columns of dataframe
print(df.columns)
#to access rows loc and iloc is used
#loc :it is label based (label is string so use inside single or double quotes).note, for bydefault indexing (o 1 2...) no need to mention insdie single quotes
#iloc :it is integer position based
#loc and iloc is indexer not a method
print(df.iloc[0]) #only first row is displayed
print(df.iloc[[0,1]]) #access multiple rows ie:rows of index 0 1 is dislayed
print(df.iloc[[0,1],2]) #access email of only 1st and 2nd row
print(df.iloc[[0,1],[0,1]]) #first index is 0 , last index is 1,email index is 2

print(df.loc[0]) #here label works but budefault label is 0 1 2 ie;integer so no need to write inside quotes(single or double)
print(df.loc[[0,1]] ) #access 2 rows whose label is 0 and 1 
#print(df.loc[[0,1],[0,1]]) #access first and last of  rows with label 0 and 1 but it gives error bcz it accepts label(string),but we are giving index of column
print(df.loc[[0,1],'email']) #now it is corect
print(df.loc[[0,1],['last','first']]) #note sequence of printing .ie;1st last and then first column is printed bcz u mentioned like this

#get the rows of hobbyist column only
df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_public.csv")
print()
print(df['Hobbyist'])

#how many values in this hobbyist column are yes ,No
print(df['Hobbyist'].value_counts()) #prints the no of occurence of each value in hobbyist column
print(df['Age'].value_counts()) #ie; pandas.core.series.series
s=df['Age'].value_counts()
s2=df['Hobbyist'].value_counts()
print('no of objects with age 25:',s[25.0])#accessing pandas series ie;bcz age column has INTEGER so it is used as index
print('no of yes:',s2[0])#bcz hobbyist column has str values so ,,,bydefault indexing  is 0 1 ....etc but u can change index to yes and no
print(df['Gender'].value_counts())#gender counts ,,bcz gender column has str so ,bydefault indexing is 0 1 ..etc but you can change
#access top 3 rows and only Hobbyist column
#using loc
print(df.loc[[0,1,2],'Hobbyist'])
#using iloc
print(df.iloc[[0,1,2],2])#bcz index of hobbyist column is 2
#note row indexs are 0 1 2 ...bcz we have not changed anything ,,,using bydefault one

#INDEXING AND FILTERING
#index:integer identifir for row or column
df=pd.DataFrame(people)
print(df)
df.set_index('email')
print(df)#lol,,,max methods in pandas doesnt do changes in inplace ie;temporarily changed ie;for up to this statement only
#therefore to make inplace change ie;change in current dataframe
#our dataframe did not changed
#bbcz pandas doesnot allow all such ooperation inplace
#2 ways are there
#1st  newdf=df.set_index('email)
#2nd
df.set_index('email',inplace=True)
print(df)#now changes are done in current dataframe,,therefore u can access rows using emaail as index
print(df.index)
#NOTE bydefault index for dataframe is 0 1 2...etc ie;integer index
print(df.loc['sj@']) 
"""    first      shree
       last     jagatap  --->email is not printed bcz we made it as index therefore not considerd as normal column
"""
print(df.iloc[0]) #op is same as above bcz we have changed label indexing from 0 1 2 3 to sj@ hd@ yd@ as@ but general indexing(ie;internal) is 0 1 2 3(integer index)
#print(df.loc[0])  -->gives error bcz,loc is label based(ie;takes label as input) and we have changed default labels 0 1 2 3 to sj@ hd@ yd@ as@ .note changed LABELS but we cant change integer index to row....understand deeply
#bydefault dataframe has 0 1 2..etc as both LABEL AND INDEX(integer)
#RESET index
df.reset_index(inplace=True)
print(df)#again 0 1 2...act as label as well as integer index of dataframe
#note -->after reset, sequence of column will change ie;previous index is displayed as first column but doesnt effect on data

#while reading(loading) public.csv make Respondent column as index in public.csv
df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_public.csv",index_col='Respondent')
print(schema_df.head())
#while reading csv make Column as index in schema_df
schema_df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_schema.csv",index_col='Column')
print(schema_df)#makes column field as index
#suppose we want to sort the index of dadtaframe(when we set the index to such a column where that column has unsorted values)
#in above case 'Column' column has to be sort
schema_df.sort_index(inplace=True) #or schema_df=schema_df.sort_index() ,both are same,,,but first one is professional
print(schema_df)
#sorting in ascending order
schema_df.sort_index(ascending=False,inplace=True)
print(schema_df)

#FILTERING
pep={
       'first':['shree','hari','krishn'],
       'last':['jagatap','yadav','yadav'],
       'email':['sj@','hy@','ks@']
}
df=pd.DataFrame(pep)
print(df)
#suppose we have to find rows with yadav as value in 'last' named column
#note filtered rows retain there respective index from dataframe before filtering 
#1st way
print('--------------------------------------------------------------')
print(df['last'] == 'yadav')
'''    0      False
       1     True
       2     True  it will not give that rows ,,ie;only gives which rows are contain it so next method'''
#2nd way
print('------------------')
print(df.loc[df['last'] == 'yadav']) #but difficulty in understanding so next waay if preffered
#3rd way
filt=df['last'] == 'yadav'  #filt contains the array of index of rows whoes wvalues are matched according to condition.you can use bracket also for isolating conditions
print(df[filt])#or print(df.loc[filt])

#if we want email column from filtred rows then
print(df.loc[filt,'email'])#print(df.loc[filt,['email','first']])--->for list of column to be displayed

#multiple condition while filtering
#AND and OR in pandas filteringAND ,OR keyword used in python,,,but in pandas use (& for AND,| for OR)
filt= (df['last'] == 'yadav') & (df['first'] == 'hari')
print(df.loc[filt])

filt=(df['last'] == 'yadav') | (df['first'] == 'hari')
print(df.loc[filt])

#if we want those rows which are not matched with written filter(condition) then use NOT ---> ~
print(df.loc[~filt])

#lets work on stackoverflow survey data
df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_public.csv")
schema_df=pd.read_csv(r"D:\AIML_PROGRAMS\2_pandas\my_data\survey_results_schema.csv")
print(df,'\n')
print(schema_df)
#total 64461 rows(employee data is there) ,lets find  who has high salary ie;greater than 50k
filt=(df['ConvertedComp'] > 50000) #add brackets for good practice and to apply multiple filters
print(df[filt])#all that rows (employee data ie;61 column data of each employee is displayed)

#specific columns from filtered rows(in above case just print country and age)  
print(df.loc[filt,['Country','Age']])  
'''  Country
United States       12469
India                8403
United Kingdom       3896
Germany              3890
Canada               2191
                    ...  
Liechtenstein           1
Mali                    1
Marshall Islands        1
Nauru                   1
Lesotho                 1'''
#to count the occurence of each value in country column from above (filtered rows)
print(df.value_counts('Country'))
##we want to filter the rows based on the top 5 countries ie;select those rows(employee data) whose country belongs to top 5 country  where salary > 50k
#united states,india ,united kingdom,germeny,canda is top 5 counties where employee salary is greater than 50k
countries=['United States ','India','United Kingdom','Germeny','Canada']
filt=(df['Country'].isin(countries))
print(df.loc[filt])

#ROW and COLUMN UPDATION
#if we wanto change all column names
df=pd.DataFrame(pep)
print(df)
df.columns=['first_name','last_name','email']
print(df)
#changing specific column name
df.rename(columns={'first_name':'FIRST'})
print(df)#LOL ,,,inplace changes not enabled(ie;changes not done in actual dataframe)
#there are 2 ways to inpplace change
#1st
df=df.rename(columns={'first_name':'FIRST'})
print(df)
#2nd
columns={'first_name':'FIRST'}
df.rename(columns,inplace=True)
print(df)
#every function in pandas returns temporary dataframe
print(df.rename(columns))
''' FIRST last_name email
0   shree   jagatap   sj@
1    hari     yadav   hy@
2  krishn     yadav   ks@ 
'''#if we want to change 3rd row then
df.loc[2]=['Abhijit','Singh','as@']
print(df)#updated successfully
#but,,if we want to change just email of 3rd row then
df.loc[2,'email']='sa@'
print(df)
#how you access data ,,,in that way only u can rewrite data by assigning value after accessing ,,
'''df.loc[2,['last','email']]=['sathe','abhiSathe@']
print(df)
 FIRST last_name       email   last
0    shree   jagatap         sj@    NaN
1     hari     yadav         hy@    NaN
2  Abhijit     Singh  abhiSathe@  sathe#bcz 'last' is changed to 'last_name' so new column is created  after not finding that column(last) and set values to Nan and specified value is written to specific field
#so carefully specify name of column while updating values'''
df.loc[2,['last_name','email']]=['sathe','abhiSathe@']
print(df)
#insert or delete the rows and columns\
#add new column with column name--->full_name
df['full_name']=df['FIRST'] + ' ' +df['last_name']
print(df)
'''
     FIRST last_name       email      full_name
0    shree   jagatap         sj@  shree jagatap
1     hari     yadav         hy@     hari yadav
2  Abhijit     sathe  abhiSathe@  Abhijit sathe'''
#if 'full_name' column is available initially,then values are rewritten else 'full_name' column is created and each cess value is concatination of FIRST and last_name
#lets remove columns
'''df.drop(columns=['FIRST','last_name'],inplace=True)
print(df)'''

#adding rows 
print(df)
df=df._append({'FIRST':'RAM'},ignore_index=True)#bcz,,we given a FIRST name only so  remaining are set to Nan(not a value or number)
print(df)
#note-->append method is updated to _append and doesnt have inplace argument,,soo above technique is used to insert rows
 #delete rows
df.drop(index=3,inplace=True)
print(df)

#PANDAS SERIES
d={'a':1,'b':2,'c':3}
ser=pd.Series(data=d,index=['a','b','c'])#if u use index=['x','y','z'] then value is not extracted
print(ser)#op
'''a   1
   b   2
   c   3 
'''
#if u use index=['x','y','z'] 
''' 
   x   NaN
   y   NaN
   z   NaN 
'''