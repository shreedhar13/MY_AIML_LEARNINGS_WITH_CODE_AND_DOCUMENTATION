import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#histogram == bar chart when,bins == n of item.in below case if  bins=11 then histogram is bar chart only
#histograms are used to represents the continous distribution of values over multiple bins
# #ie; in bar charts we have bar for each over,,at 15 th over this much runs are made and at 16th this much and so on,...abs
# #but histograms allows to represent how many run scored bn 15 to 20 over and so on.ie;range  
#bin-->means 'DABBA(marathi)' like dustbin
ages=[18,19,21,25,26,26,30,32,38,45,55]
plt.hist(ages)
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.show()

#use 5 bins only.to represent range

plt.hist(ages,bins=5,edgecolor='black')
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.show()

#userdefind range or  list of bins

bins=[10,20,30,40,50,60]#not neccessory to give bins name only.5 bins(range )is defined-->10 to20,20 to30,30to40,40to50,50 to 60
plt.hist(ages,bins=bins,edgecolor='black')#w/o color border of each bin is not recognizable by user so give.edge color of each range
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.show()

#if we provide the bins which are not covering all values,,then those values are not include in plot ie;negotisted

bins=[20,30,40,50,60]
plt.hist(ages,bins=bins,edgecolor='black')
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.show()#ages 18,19 are negotiated

#to represent median (ie;in this case 26 is middle value)in graph 
bins=[20,30,40,50,60]
median_age=26
plt.hist(ages,bins=bins,edgecolor='black')
plt.axvline(median_age,color='red',label='Median age',linewidth=2)#axis varticalline.
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.legend()#to display labels,,whenever we specified label as argument in method
plt.show()
#what if 60 to 70 bin is defined..ages bn 60 ro 70 not there so distibution is 0
bins=[20,30,40,50,60,70]
plt.hist(ages,bins=bins,edgecolor='black')
plt.title('ages of student')
plt.xlabel('ages')
plt.ylabel('total student')
plt.show()

