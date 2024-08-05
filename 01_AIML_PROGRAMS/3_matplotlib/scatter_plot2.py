#read scatter plot data.csv.work on real data
import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv(r'D:\AIML_PROGRAMS\3_matplotlib\Scatter Plot Data.csv')
print(data)
'''     view_count    likes  ratio
0       8036001   324742  96.91
1       9378067   562589  98.19
2       2182066   273650  99.38
3       6525864    94698  96.25
4       9481284   582481  97.22
..          ...      ...    ...
195     1069693     3970  90.66
196      590760    70454  99.18
197      319347     1208  92.50
198    27594927  1351963  96.40
199    26993425   437561  97.42       ''' #dataframe ie;table like structure to store data
view_count=data['view_count']
likes=data['likes']#pandas series(multiple rows with single column)
ratio=data['ratio']
print(view_count)
plt.scatter(view_count,likes,s=100,edgecolor='black',linewidth=1)
plt.xlabel('views')
plt.ylabel('likes')
plt.show()
#200 rows means 200 data points are therre but they are ovelapped so not visible all points so
#in graph we see that one point is very far from all points ,,it is called outlier 
#to plot the points evenly use logarithmic scale ie;log2(8)=3,log10(100)=2 in this case we use base10
#hence lets scale the plot to log scale
plt.scatter(view_count,likes,edgecolor='black',linewidth=1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('views in log scale')
plt.ylabel('likes in log scale')
plt.show()#now plot is more evenly distibuted

#let use ratio of likes/dislikes to represent more information in plot using colors.ie; ratio as c parameter and u can use cmap
#w.r.t Greens->darker dots/points represents higher likes and lighter dots represents lower liker or say high dislikes
plt.scatter(view_count,likes,c=ratio,edgecolor='black',linewidth=1,cmap='Greens',alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('views')
plt.ylabel('likes')
plt.show() 