import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#with pie,,we cant represent set of value foe each item ie;see below..we are using stack_plots
min=[1,2,3,4,5,6,7,8,9]

player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]
labels=['player-1','player-2','player-3']
plt.stackplot(min,player1,player2,player3,labels=labels)
plt.title('my stack plot')
plt.legend()
plt.show()     
#to change the location of legend .also u can change the color of plots
labels=['player-1','player-2','player-3']
clr=['#6d904f','#fc4f30','#008fd5']
plt.stackplot(min,player1,player2,player3,labels=labels,colors=clr)
plt.title('my stack plot')
plt.legend(loc='upper left')#lower left,lower right
plt.show()

#you can customize position of legend
labels=['player-1','player-2','player-3']
plt.stackplot(min,player1,player2,player3,labels=labels)
plt.title('my stack plot')
plt.legend(loc=(0.07,0.05))#(x,y) coordinate representing postion,x-distance form left boundary,y-distance from bottom boundary
plt.show()


