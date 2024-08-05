import matplotlib.pyplot as plt 
#used when relationship bn 2 sets of values to be compared and to see if they are correlated 
plt.style.use('fivethirtyeight')
x=[5,7,8,5,6,7,9,2,3,4,4,4,3,6,3,6,8,6,2,3]
y=[2,4,4,3,1,2,6,5,3,1,2,5,6,7,8,9,1,3,1,1]
plt.scatter(x,y)
plt.show()
#changing the size of dots ,clor
plt.scatter(x,y,s=100,c='red')#c='green',c=-any_color_name'
plt.show()
#instead of dot we can give other markers kike x
plt.scatter(x,y,marker='x',c='black',s=100)
plt.show()
#for boundary/edge of marker
plt.scatter(x,y,edgecolor='black',linewidth=1)#width of edge color
plt.show()

#suppose we want to represent the best rating of for each (x,y)
rating=[7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]#these values represent ratings out of 10.and it is passed to color argument so that each shading of data points is done respectively
plt.scatter(x,y,s=100,c=rating,edgecolor='black',linewidth=1,alpha=0.75)#c means color and we are passed list of values.and we are nor specified any cmap so any random color is choosen for each points,so use cmap
#and according to value each dots are colored according to integer values of color
#darker color represents high ratings
plt.show()

plt.scatter(x,y,s=100,c=rating,cmap='gist_gray',edgecolor='black',linewidth=1,alpha=0.75)
plt.show()
#now darker color represents higher ratings and lighter colore represents lower ratings
'''' valid cmap values
Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 
'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1',
 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 
 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r',
  'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 
  'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 
  'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray',
   'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 
   'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 
   'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 
   'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 
   'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 
   'viridis', 'viridis_r', 'winter', 'winter_r' 

'''
#to give scaling
plt.scatter(x,y,s=100,c=rating,cmap='Greens',edgecolor='black',linewidth=1,alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('Rating scale')
plt.xlabel('x')
plt.ylabel('y')
plt.show()#(8,4),(3,8) has higher rating value ie;9 so these are darker and others are shaded according to valueie;lighter reprsent less and darker represent higher ratings
#every cmap has its different shading rules ex->gist_gray is reverse of Greens.abs#most used Greens and summer