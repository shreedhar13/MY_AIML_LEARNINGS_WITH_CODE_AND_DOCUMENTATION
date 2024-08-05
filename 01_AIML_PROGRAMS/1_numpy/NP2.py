#Arithmetic and algebra, statistics operations on numpy arrays
import numpy as np
a=np.array([1,2,3])
print(a+2) #all elements are incremented with 2 and return a array.other operation (a-2,a*2,a/2,a**2,a%2....etc arithmatic operation)
print(a) #[1 2 3] bcz not update innactual array ie;creates new array and perform operation

#arithmetic operation on 2 or more arrays(possible only if involving arrays are of same dimension,ie;compatible with each other)
b=np.array([4,5,6])
c=a+b
print(c)

#trignometric operation
c=np.sin(a) #sin(1 radian)==0.84147098
print(c) #value of sin fro each elements
#applying for specif elements
print(np.sin(a[0])) #op->0.84147098

#linear algebra
#matrix multipliacation
m1=np.array([[1,2,3,4],[8,9,10,11]]) #2d 2x4
m2=np.array([[4,1],[5,3],[6,8],[3,2]]) #2d 4x2
re=np.matmul(m1,m2)
re2=np.dot(m1,m2)
print(re)
print(re2)
#determinent of matrix
m3=np.array([[1,2,6],[7,8,9],[4,5,6]]) #2d 3x3
re=np.linalg.det(m3) #linalg is sublibrary present inside numpy
print(re)

#eigen value of square matrix
m=np.array([[1,6],[8,9]])
re=np.linalg.eig(m)
print(re)
#for more linearalgebra functions
#https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
#ie;trace,singular vector decompositionin.inverse....etc(read diocumentation)

#statistics
print('stats')
a=np.array([[3,6,2],[4,5,1]])
#find minimum
print(np.min(a)) #op->1 
#row wise minimum
print(np.min(a,axis=1)) #[2 1]
#column wise minimum
print(np.min(a,axis=0)) #op->[3 5 1]
#similarly for max
#sum of elements
print('sum')
print(np.sum(a)) #all elements of array(1d,2d,3d....etc) is added 
#axis for sum
#sum of each row
print(np.sum(a,axis=1)) #returns list where each cell represents sum of each row
#colimn wise sum
print(np.sum(a,axis=0)) #returns list where each cell represents sum of each column

#mean median mode(measure of central dependency)
a=np.array([[1,6,9],[4,5,1]])
print(np.mean(a)) #(1+6+9+4+5+1)/6  op->4.333333

print(np.median(a)) #even no so mean of middle 2 element is median (NOTE->elements should be sorted)
#ie; 1,1,4,5,6,9   therefore (4+5)/2   op->4.5

#standard deviation and variance (measure of dispersion) variation=(standarddeviation)^2
print(np.std(a))
print(np.var(a))

#more statistical function https://numpy.org/doc/stable/reference/routines.statistics.html  (read documentation for more informtion)

#Linear equation
#4x + 5y = 13
#5x - 3y = 7
cf1=np.array([[4,5],[5,-3]])
cf2=np.array([13,7])
res=np.linalg.solve(cf1,cf2)
print(res) #value of x and y is finded op->[2. 1.] ie;float or double bydefault where x=2. y=1.

###FOR MORE Arithmetic , algebra AND statistics operations on numpy arrays read documentation from org(ie;above mentioned links or official sites)

print('shree')
import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5,6], [7, 8, 9]]),
                   columns=['A', 'B', 'C'])
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]] -->must me 2d,,,bcz as u see dataframe is 2d matrix,,,rows X cols
#NOTE->passed array/matrix should be SQUARE MATRIX(ie;N X N)same no of rows and same no of cols otherwise error 
col_sum = df.sum(axis=0)
print(col_sum) 
print(df)
row_sum = df.sum(axis=1)
print(row_sum)