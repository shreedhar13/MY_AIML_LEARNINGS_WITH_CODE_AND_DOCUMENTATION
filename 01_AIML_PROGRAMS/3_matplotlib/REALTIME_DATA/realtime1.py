#when data coming from website or api or sensors or some source which is real time data(up to date data),,so that you have to plot it
#  (updating in current plot so that latest value is added to plot) ,and we have to do it again and again ie;according to real time data is coming
#so that latest value are also considered for calculation
#previous all plots pie,bar,simplegraph,scatterplot etc(all plots inside matplotlib)are static plotting
#like this
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

x=[0,1,2,3,4,5]
y=[0,1,3,2,3,5]
plt.plot(x,y)
plt.tight_layout()
plt.show()#static one.->not change wrt time

#now plot real time data/dynamic data
#itertools.count() creates iterator that counts up or down infinitely.bydefault it starts with 0 and increased by 1 each time
# index=count()  ->bcz index become iterator which generates infinite values we have to pull values from is so use next() inbuolt method
import random
from itertools import count
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation #for real world/data plot in ur matplotlib u have to import this library

x=[]
y=[]
index=count()#now index become iterator

def animate(i):#i means runs infinitely
    x.append(next(index))#pull the next values from index named iterator 
    y.append(random.randint(0,8))
    plt.cla()#clear axis -->will clear the previous axis so that same color plot will continued else if u dont use it then, after each second new color graph is displayed which not look good
    plt.plot(x,y)
ani=FuncAnimation(plt.gcf(),animate,interval=1000,cache_frame_data=False)#after each 1 second this function automatically called 1000ms=1sec
#gcf -->get current figure   and after each second get real time data (by calling animate()) and it is plotted in it and displayed
plt.tight_layout()#automatically adjusts subplot params so that subplots fits into the figure
plt.show()#this one is dynamic plotting