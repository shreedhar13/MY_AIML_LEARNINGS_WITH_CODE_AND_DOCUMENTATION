#heatmap is graphical reprsentation of 2D data ,each data value reprsent in a matrix and it has special color
#and this is mainly used for "FEATURE SELECTION" 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
print(np.arange(0,10))#[0 1 2 3 4 5 6 7 8 9]

arr=np.linspace(1,5,12).reshape(4,3)
print(arr)
sns.heatmap(arr)
plt.show()

df=pd.read_csv(r"D:\AIML_PROGRAMS\4_seaborn\Who_is_responsible_for_global_warming.csv")
print(df)
country_code=df['Country Code']
#bcz heatmap uses numeric value s0 drop the column [country code,indicator code,indicator name]bcz this column contains string value and now index is 0 1 etc but we make indexing as country name therefore it is used as y  axis ticks and remaining column as x axis
df=df.drop(columns=['Country Code','Indicator Name','Indicator Code'],axis=1).set_index('Country Name')#axis=1 for droping columns
# print(df)
# df.set_index('Country Name',inplace=True)
print(df)
sns.heatmap(df)
plt.show()#automatically takes Country Name on y axis and all numeric years on x axis
#at hte side of heatmap u get the color bar where bottom colors represent minimum and top colors reprsent maximum co2 emission and mid color is for mid 
#you can chage the color bar
plt.figure(figsize=(16,9))
sns.heatmap(df,vmin=0,vmax=21)
plt.show()
#as u see United states emission rate decreasing year by year(ie;color moving from top to bottom)

#change color
plt.figure(figsize=(16,9))
sns.heatmap(df,vmin=0,vmax=21,cmap='coolwarm')
plt.show()#this one becom more meaningfull

#to show the value on each year for each country use annotation (tippani in kannada)
plt.figure(figsize=(16,9))
sns.heatmap(df,vmin=0,vmax=21,cmap='coolwarm',annot=True)
plt.show()#this is more beautifull

#suppose you want to show annotation of ur own(ie;not from current dataset then) 
annot_arr=np.array([['a00','a01','a02'],['a10','a11','a12'],['a20','a21','a22'],['a30','a31','a32']])#note should be of same dimesnison as actual array you are plotted
sns.heatmap(arr,annot=annot_arr,fmt='s')#f(format)-->'s' for string,'d' for decimal
plt.show()

#if we want a separate box for each value then
plt.figure(figsize=(16,9))
sns.heatmap(df,vmin=0,vmax=21,cmap='coolwarm',annot=True,linewidth=4)
plt.show()
#give line color in hexadecimal
plt.figure(figsize=(16,9))
sns.heatmap(df,vmin=0,vmax=21,cmap='coolwarm',annot=True,linewidth=4,linecolor='k')#k for black,u can give hex value also
plt.show()

#to hide color bar, cbar=False
#kws-->keyword arguments
#modifying color bar
plt.figure(figsize=(16,9))
cbar_kws={
    'orientation':'horizontal',
    'shrink':1,                 
    'extend':'min',             
    'extendfrac':0.1,           
    'ticks':np.arange(0,22),  
    'drawedges':True            
}
'''to show sharpness at min side
 how much you want to extend sharpness
privious cbar is plane but if u want to give segment of eavh color then '''
sns.heatmap(df,cbar_kws=cbar_kws)
plt.show()

#to change x and y labels
sns.heatmap(df,cbar_kws=cbar_kws,xticklabels=np.arange(0,15),yticklabels=country_code)
plt.show()

#to represent prof
ax=sns.heatmap(df,cmap='coolwarm')
ax.set(title='heatmap is for"who is responsible for global warming"',xlabel="co2 emission (metric tons pr capita)per year",ylabel='Country name')
sns.set(font_scale=5)
plt.show()

demo=df.corr()
sns.heatmap(demo,annot=True,linewidth=3)
plt.title("heatmap of'who is responsible for global warming'",fontsize=10)
plt.show()