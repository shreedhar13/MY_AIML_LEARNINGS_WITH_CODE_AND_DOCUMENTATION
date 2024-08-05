import matplotlib.pyplot as plt
#comparing scores of 2 teams
over_x=[15,16,17,18,19,20,21,22,23,24,25]
india_y=[101,106,114,134,140,141,149,152,166,170,171]
nzl_y=[91,96,104,111,112,120,124,129,131,141,151]

plt.plot(over_x,india_y)
plt.plot(over_x,nzl_y)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()

#but can u recognize which line represents which teams score
#hence use legend( ) method of matplot library.(ie;represents which line belongs to which group/team)
#1st way to use legend()
plt.show()#doesnt open a new window,,bcz there is no content to display,,so plt.show() immediately use after data is set
#so copy above statement for setup data
plt.plot(over_x,india_y)
plt.plot(over_x,nzl_y)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
#use legend() 
plt.legend(['india','newziland'])
plt.show()
#2nd way is preffered one to use legend()
plt.plot(over_x,india_y,label='India',color='#ff0000',linestyle='--',linewidth='3')#bydefault linewidth is 1
plt.plot(over_x,nzl_y,label='newziland',marker='o')#marker--->which marks the (x,y) coordinate
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.legend()#dont pass anything bcz u already passed label in plot method
plt.show()

#if u dont comment any plt.show()  statement then 3 windows are created(not at a time) ,one after another, after closing one after another in serially
#changing color and style of graph ,,type this matplotlib format strings (documentation) on google
#plt.plot(over_x,india_y ,color='b',linestyle='--',label='india') you can do manythings just search the documentation
#u can give colors in hexa value--->color='#5a7d9a'  2for R ,G,B respectively

#if u want to draw a graph in grid then plt.grid(True)
#copy paste above code
plt.plot(over_x,india_y,label='India',color='#ff0000',linestyle='--')
plt.plot(over_x,nzl_y,label='newziland')
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.legend()#dont pass anything bcz u already passed label in plot method
plt.grid(True)
plt.show()

#matplotlib offers many styling options on visibility of grapgh..
print(plt.style.available)
#['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
#above list is returned,,and u can select any one of them to style graph

#u have to use plt.style.use('any_item_from_above_list').
plt.style.use('ggplot')#u have to declare this statement at the begining,,so that it works on complete data what u write below this statement
over_x=[15,16,17,18,19,20,21,22,23,24,25]
india_y=[101,106,114,134,140,141,149,152,166,170,171]
nzl_y=[91,96,104,111,112,120,124,129,131,141,151]

plt.plot(over_x,india_y)
plt.plot(over_x,nzl_y)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()

#a surprise looking plot
plt.xkcd()#comic type graph is plotted.ie;borders are not in shape
over_x=[15,16,17,18,19,20,21,22,23,24,25]
india_y=[101,106,114,134,140,141,149,152,166,170,171]
nzl_y=[91,96,104,111,112,120,124,129,131,141,151]

plt.plot(over_x,india_y)
plt.plot(over_x,nzl_y)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()

#if u want to save the output graph then plt.savefig('location') is used
over_x=[15,16,17,18,19,20,21,22,23,24,25]
india_y=[101,106,114,134,140,141,149,152,166,170,171]
nzl_y=[91,96,104,111,112,120,124,129,131,141,151]

plt.plot(over_x,india_y)
plt.plot(over_x,nzl_y)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('runs per over')
plt.show()
plt.savefig('demo.png')#inside cwd it is saved