import pandas as pd 
from matplotlib import pyplot as plt 
plt.style.use('seaborn')

data=pd.read_csv(r'D:\AIML_PROGRAMS\3_matplotlib\subplot\plotdata.csv')
ages=data['Age']
dev_salaries=data['All_Devs']
py_salaries=data['Python']
js_salaries=data['JavaScript']

plt.plot(ages,dev_salaries,color='#444444',linestyle='--',label='all devs')
plt.plot(ages,py_salaries,label='python')
plt.plot(ages,js_salaries,label='javascript')

plt.legend()
plt.title('median salry by age')
plt.xlabel('age')
plt.ylabel('median salary')
plt.show()

#above show() will displays 1 figure and inside that 1x1 plot (1row and 1column)
#but if we want multiple plots(xy planes) inside 1 figure then use subplot concept
fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True)#hence 2 plots are drwan inside 1 figure ie;2 rows means 2 xyplane,1 column means 1 plot below another plot
#if u give(nrows=1,ncols=2) 2 plots are drawn one after another ie;side by side plot(xyplane) is plotted
#if u use fig,ax=plt.subplots() -->then it is same as previous one ie;1 plot is drawn inside 1 figure ,and hence subplotting is done
ax1.plot(ages,dev_salaries,color='#444444',linestyle='--',label='all devs')
ax2.plot(ages,py_salaries,label='python')
ax2.plot(ages,js_salaries,label='javascript')

ax1.legend()
ax1.set_title('median salry by age')
ax1.set_xlabel('age')
ax1.set_ylabel('median salary')

ax2.legend()
ax2.set_title('median salry by age')
ax2.set_xlabel('age')
ax2.set_ylabel('median salary')
plt.tight_layout()#now it is used to to fit the subplot inside 1 figure
plt.show()

#for 1 row 2 column
fig,(ax1,ax2)=plt.subplots(nrows=1,ncols=2,sharey=True)
ax1.plot(ages,dev_salaries,color='#444444',linestyle='--',label='all devs')
ax2.plot(ages,py_salaries,label='python')
ax2.plot(ages,js_salaries,label='javascript')

ax1.legend()
ax1.set_title('median salry by age')
ax1.set_xlabel('age')
ax1.set_ylabel('median salary')

ax2.legend()
ax2.set_title('median salry by age')
ax2.set_xlabel('age')
ax2.set_ylabel('median salary')
plt.tight_layout()
plt.show()

#sharex and sharey used to share same occurence bn subplot

#fow 2 figure
fig1,ax1=plt.subplots()
fig2,ax2=plt.subplots()
ax1.plot(ages,dev_salaries,color='#444444',linestyle='--',label='all devs')
ax2.plot(ages,py_salaries,label='python')
ax2.plot(ages,js_salaries,label='javascript')

ax1.legend()
ax1.set_title('median salry by age')
ax1.set_xlabel('age')
ax1.set_ylabel('median salary')

ax2.legend()
ax2.set_title('median salry by age')
ax2.set_xlabel('age')
ax2.set_ylabel('median salary')
plt.tight_layout()
plt.show()#both figures are displayed at once which are independent