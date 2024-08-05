#BAR CHARTS(vartical bar)
import matplotlib.pyplot as plt
import numpy as np
x_overs=[15,16,17,18,19,20,21,22,23,24,25]
y_score=[101,106,114,134,140,141,149,152,166,170,171]

plt.bar(x_overs,y_score,color='#444444',label='indias score')
plt.xlabel('overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()#1st window

#showing data in 2d graph and bar
over_x=[15,16,17,18,19,20,21,22,23,24,25]
india_y=[101,106,114,134,140,141,149,152,166,170,171]
nzl_y=[91,96,104,111,112,120,124,129,131,141,151]
plt.plot(over_x,india_y,label='India')
plt.bar(over_x,nzl_y,label='newziland')
plt.xlabel('overs')
plt.ylabel('runs')
plt.legend()
plt.title('runs per over')
plt.show()#2nd window

#reverse above
plt.bar(over_x,india_y,label='India',color='#000000')
plt.plot(over_x,nzl_y,label='newziland',color='#00ffff')
plt.xlabel('overs')
plt.ylabel('runs')
plt.legend()
plt.title('runs per over')
plt.show()#3rd window

#showing all data in single bar(ie;using plt.bar())
plt.bar(over_x,india_y,label='India',color='#002a5f')
plt.bar(over_x,nzl_y,label='newziland',color='#00ffff')
plt.xlabel('overs')
plt.ylabel('runs')
plt.legend()
plt.title('runs per over')
plt.show()#4th window


#best way to reperent bar graph
#above bar's are overlapped 
#if we want each bar is displayed side by side then,,reduce the size of eaqch bar(ie;default 0.8 is there ,,u can make it as 0.4 so that we can show 2 bar at size of 1bar).bcz to adjust the graph in window we are reducung
w=0.4
x_indices=np.arange(len(over_x))#[0,1,2,3,4,5,6,7,8,9,10],,bcz 11 bars are there so..and
#if u use over_x then it will produce error so use indices for plotting bar graph after perfect plotting u can convert it to over_x see below
plt.bar(x_indices,india_y,width=w,color='#e5ae39',label='India')
plt.bar(x_indices + w,nzl_y,width=w,color='#444444',label='Newziland')#x_indices+w,,bcz each bar of newziland is printed after india(not ovelapped)ie;if 1st bar of india is at 1 then 1st bar of newziland is at 1.4 and so on for further points\
#u can use x_indices - w ,,,,hence each india bar will follow newziland bar.
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('runs per over')
plt.legend()
plt.show()#5th window
#but the overs on x axis are not overs but the indexes,we need to change it using x-ticks
plt.bar(x_indices,india_y,width=w,color='#e5ae39',label='India')
plt.bar(x_indices + w,nzl_y,width=w,color='#444444',label='Newziland')
plt.xticks(ticks=x_indices,labels=over_x)#each index replace with over_x values
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('runs per over')
plt.legend()
plt.show()#6th window

#bar chart in horizontal-->plt.barh()   
x_overs=[15,16,17,18,19,20,21,22,23,24,25]
y_score=[101,106,114,134,140,141,149,152,166,170,171]

plt.barh(x_overs,y_score,color='#4a4d4f',label='indias score')
plt.xlabel('overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()#horizontal bar
