#MATPLOTLIB is a comprehensive library for creating static,animated,and interactive visulization in python

import matplotlib.pyplot as plt
x=[15,16,17,18,19,20,21,22,23,24,25]

y=[101,106,114,134,140,141,149,152,166,170,171]
plt.plot(x,y)
plt.show()#to open a new window where graph is drawn.window(1) is created and data is plotted
#lets label the graph
plt.figure(figsize=(16,9))#to increase window size of graph
plt.plot(x,y)
plt.xlabel('Overs')#labeling x axis 
plt.ylabel('Runs')#labeling y axis
plt.title('Runs per over')
plt.show()#window(2) is created after  window(1) closed,,,,and it can be seen by closing window(1)...ie; window(2) is created and graphs are drawn

#thats why,,,, use plt.show() after performing all required operation on data,,,so that unneccessary window creating is avoided
#so that, at this point i am creating new file so that i can use only 1 plt.show().
