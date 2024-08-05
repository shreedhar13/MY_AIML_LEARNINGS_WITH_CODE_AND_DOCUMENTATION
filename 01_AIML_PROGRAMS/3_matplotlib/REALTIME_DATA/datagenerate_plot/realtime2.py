#first run DataGeneration.py in command prompt so that data is generated and stored in data.csv file in cwd then run the realtime2.py,,
# so that ur graph/plot become dynamic

import random
import pandas as pd 
from itertools import count 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
index=count()
def animate(i):
    data=pd.read_csv('D:\AIML_PROGRAMS\matplotlib\REALTIME_DATA\datagenerate_plot\data.csv')
    x=data['x_value']
    y1=data['total_1']
    y2=data['total_2']
    plt.cla()
    plt.plot(x,y1,label='channel1')#you can do same with histogram ,bar,pie etc plots
    plt.plot(x,y2,label='channel2')
    plt.legend(loc='upper left')
ani=FuncAnimation(plt.gcf(),animate,interval=1000,cache_frame_data=False)
plt.tight_layout()
plt.show()