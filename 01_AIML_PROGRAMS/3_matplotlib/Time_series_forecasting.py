#Forecasting involves taking models, fit on historical data and using them to predict future observation
#it is best domain for predictive analysis or predictive machine learning
#ie;you create one model which takes past data as input and predict the future
#note-->on time series graph x axis must be Date or time and we have sort it
#NOTE2-->DATE FORMAT IS NOT A STRING.DATE TIME FORMAT IS A SPECIFIC FORMAT IT IS NOT A STRING
#ie;date time is special datatye is therer in HLL
import matplotlib.pyplot as plt 
import pandas as pd 
from datetime import datetime,timedelta
import matplotlib.dates as mpl_dates
'''shift + alt + up arrow or down arrow'''
dates=[
    datetime(2021,6,10),
    datetime(2021,6,11),
    datetime(2021,6,12),
    datetime(2021,6,13) ,    
    datetime(2021,6,14),
    datetime(2021,6,15),
    datetime(2021,6,16)
]
y=[0,1,3,4,6,5,7]
plt.plot_date(dates,y)
plt.show()#by default dot plot 

#lets connect dots with line
plt.plot_date(dates,y,linestyle='solid')
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price in crore')
plt.show()

#changing date format
plt.plot_date(dates,y,linestyle='solid')
date_format=mpl_dates.DateFormatter('%b,%d %Y')#read documentation to know more
plt.gca().xaxis.set_major_formatter(date_format)
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price in crore')
plt.show()

#ABOVE IS JUST A PLOT ..WE DOESNT DID ANY FORECASTING OR PREDICTING