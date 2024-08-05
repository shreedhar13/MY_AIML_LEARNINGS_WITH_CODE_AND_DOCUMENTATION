#python library for data visualization build on the top of matplotlib
#use for statistical graphics
#heatmap,pair plot,facet grid,bar plot,scatterplot,line plot,displot(distplot is no longer valid,u get warning if u use),boxplot,violin plot...Etc
# #displot and histplot are almost same 
#pip install seaborn in command prompt..but in anaconda bydefault all library related to data science is present so no need to install,
#but suppose any error occurs while coding then in anaconda prompt type this-->conda install seaborn
#bcz seaborn build over matplotlib so u have to use matplot.pyplot module for some functions of seaborn
#seaborn has some extra features so sometime u can use seaborn and sometime matplotlib
# now try the jupyter notebook to get  easyness while coding
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[36.6,37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.2]
df=pd.DataFrame({'days':days,'temperature':temp})
sns.lineplot(x='days',y='temperature',data=df,markers='o') #shshould to use style='some_column_name' to use markers argument
plt.show()

df=pd.read_csv(r"D:\AIML_PROGRAMS\4_seaborn\tips.csv")  #if u dont give as raw string then \4 treated as s[ecial char and give error so use it evrywhere,wherever u used foldername started with no
sns.lineplot(x='total_bill',y='tip',data=df)
plt.show()

 
sns.lineplot(x='size',y='total_bill',data=df,hue='sex')#hue-sex ,and sex has 2 category(male and female) so 2 lines are plotted on same graph
plt.show()


sns.lineplot(x='size',y='total_bill',data=df,hue='sex',style='sex',dashes=False, markers = ['o','>'])#like how we used here style
plt.show()
