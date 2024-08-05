#lets work on real data from csv file
import matplotlib.pyplot as plt 
import pandas as pd 
from datetime import datetime,timedelta
import matplotlib.dates as mpl_dates

data=pd.read_csv(r'D:\AIML_PROGRAMS\3_matplotlib\TimeSeries Data.csv')
price_date=data['Date']
price_close=data['Close']
print(data)
''' Date         Open         High  ...        Close    Adj Close     Volume
0   2019-05-18  7266.080078  8281.660156  ...  8193.139648  8193.139648  723011166
1   2019-05-19  8193.139648  8193.139648  ...  7998.290039  7998.290039  637617163
2   2019-05-20  7998.290039  8102.319824  ...  7947.930176  7947.930176  357803946
3   2019-05-21  7947.930176  8033.759766  ...  7626.890137  7626.890137  424501866
4   2019-05-22  7626.890137  7971.259766  ...  7876.500000  7876.500000  386766321
5   2019-05-23  7876.500000  8165.450195  ...  7996.399902  7996.399902  413162746
6   2019-05-24  7996.399902  8140.819824  ...  8059.129883  8059.129883  179206342
7   2019-05-25  8059.129883  8779.000000  ...  8726.230469  8726.230469  483663699
8   2019-05-26  8726.230469  8931.530273  ...  8785.169922  8785.169922  507164714
9   2019-05-27  8785.169922  8818.709961  ...  8718.849609  8718.849609  360752199
10  2019-05-28  8718.849609  8760.480469  ...  8664.559570  8664.559570  380343928
11  2019-05-29  8664.559570  9065.889648  ...  8276.250000  8276.250000  815525590
12  2019-05-30  8276.250000  8570.780273  ...  8560.080078  8560.080078  500141087
13  2019-05-31  8550.629883  8576.339844  ...  8504.980469  8504.980469   69915456 
'''
plt.plot_date(price_date,price_close,linestyle='solid')
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price')
plt.show()#JUST PLOTING IS DONE<NO ANY PREDICTION
#formatting dates
plt.plot_date(price_date,price_close,linestyle='solid')
plt.gcf().autofmt_xdate()
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price')
plt.show()

#supposse i add new row in csv file by updating excel file with(17-05-2019,7266.080078,8281.660156,7257.259766,8193.139648,8193.139648,723011166)
plt.plot_date(price_date,price_close,linestyle='solid')
plt.gcf().autofmt_xdate()
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price')
plt.show()#as u see date is in string thats why 17-05-2019 come at last in plot(ie;not sorted),,and thus it breaks time series forecast,bcz we have to move from past to future but here we breaj the rule
#so the column price_date is not the actual date , so legs convert it to datebusing pandas method

#VVVVVIMP

data['Date']=pd.to_datetime(data['Date'])#1st coverting to datetime type
data.sort_values('Date',inplace=True)#sorting is done respectively.not in csv file,it is done in data ,named datafame variable
price_date=data['Date']#now accesing updated csv file
price_close=data['Close']
plt.plot_date(price_date,price_close,linestyle='solid')
plt.gcf().autofmt_xdate()
plt.title('share price of xyz')
plt.xlabel('dates')
plt.ylabel('closing price')
plt.show()#some dates are hided bcz less space ,,but all are sorted and obeys rule of timeseries forecasting

#Time_series_forecasting and Time_series_forecasting2 are just plotting,,w further see forecasting
#forecasting involves taking models fit on historical data and using  then to predict future observation


