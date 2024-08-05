import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
slices=[35,15]#35+15=50 , 70% of 50 is 35,30% of 50 is 15(internally calculated and plotted on pie chart)
plt.pie(slices)
plt.title('first pie chart')
plt.show()#1st window

#need labels for pie,then u have to give list of labels in sequence (ie;in what manner u given a value)
slices=[70,30]
lbl=['Attempted','left']#70 question are attempted and 30 are left
plt.title('no of question attempted/left')
plt.pie(slices,labels=lbl)
plt.show()#2nd winodw

#lets change the color of pie.(you have to give it in sequence)
slices=[70,30,20,40]
lbl=['correct','wrong','Reviwed','left']#u can use label as variable also,,but for simplicity purpose i have given
clr=['green','red','blue','yellow']#you can use hex values
plt.pie(slices,labels=lbl,colors=clr)
plt.title('first pie chart')
plt.show()

slices=[70,30,20,40]
lbl=['correct','wrong','Reviwed','left']
clr=['#fc4f30','#008fd5','#6d904f','#e5ae37']
plt.pie(slices,labels=lbl,colors=clr)
plt.title('first pie chart')
plt.show()
#want to give emphasis on one item(Ie;heighlight any pie/slice)
slices=[70,30,20,40]
lbl=['correct','wrong','Reviwed','left']
clr=['green','red','blue','yellow']
explode=[0,0.1,0,0]#same name as argument also allowed,,u can give any name as variable.0.1 means 'wrong' labeled slice/pie/piece is separated 10% from center,so that piece is highlighted.
plt.pie(slices,labels=lbl,colors=clr,explode=explode)
plt.title('first pie chart')
plt.show()

slices=[70,30,20,40]
lbl=['correct','wrong','Reviwed','left']
clr=['green','red','blue','yellow']
explode=[0,0.1,0,0]
plt.pie(slices,labels=lbl,colors=clr,explode=explode,shadow=True)#shadow is applied to all pieces
plt.title('first pie chart')
plt.show()

#percentage of pie.displaying percentage of each piece
slices=[70,30,20,40]
lbl=['correct','wrong','Reviwed','left']
clr=['green','red','blue','yellow']
explode=[0,0.1,0,0]
plt.pie(slices,labels=lbl,colors=clr,explode=explode,autopct='%1.1f%%')#autopct is formated string(ie;predefined) not need to know the meaning of this
plt.title('first pie chart')
plt.show()

#IN MACHINE LEARNING BAR CHART IS MOST USED ONE