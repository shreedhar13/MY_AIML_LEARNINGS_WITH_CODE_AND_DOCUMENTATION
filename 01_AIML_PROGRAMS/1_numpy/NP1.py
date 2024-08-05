# it is faster than list,(nympy enables us to use array concepts in python,,,array concept is same as c lan)
# 1-bcz in list elements are of diff types but in numpy elements are of same type
#2-elemets are stored in contiguous manner(bcz of same data type).(in list ele are of diff type so each elements location is diff so accessing is slow)
import numpy as np 
a=np.array([1,2,3]) #creating array with array() FUNCTION
print(a)
#op->[1 2 3]

"""
a=np.array([1,2.0,3]) bcz array is series of same type of elements so each element is converted to float bcz no loss of data.(op->[1.0 2.0 3.0])
a=np.array([1,2,"shree"]) bcz array is series of same type of elements so each element is converted to String bcz no loss of data.(op->['1' '2' 'shree'])
a=np.array([1,2.2,'shree']) bcz array is series of same type of elements so each element is converted to String bcz no loss of data.(op->['1' '2.2' 'shree'])
"""
#accesssing elements
print(a[1])  #op-> 2
print(a[-2])    #op-> 2
print(a[0:3])  #op-> [1 2 3]
b=np.array([[1,2,3],[5,8,9]]) #2d array
print(b)  # ^row0     ^row1
print(b[0,1]) #2  (in c and c++ and java b[0][1])

#get dimension (using ndim ATTRIBUTE)
print(a.ndim)
print(b.ndim)

#shape of array (no of rows,no of columns)(using shape attribute)
print(a.shape) #(3,) bcz 3 elements are ppresent
print(b.shape) #(2,3) 2rows each with 3columns

#reshape function
x=np.array([1,2,3,4,5,6])
y=x.reshape(2,3)
print(x)
print(y)

#get type
print(x.dtype) #int32   float is 64bit 
#get size in  bytes
print(x.itemsize) #4   8 for flioat in bytes

#get total size of array
print(a.nbytes) #12bytes 4*3 (3 elements and 4bytes for each elements)

#get no of elements
print(a.size) #3
#accessing/changing elements{same cocept as c but syntax is changed littlebit}
#   0th row   0,1,2,3,4,5   0,1,2,3,4,5 1th row
ar=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#get specific row
print(ar[1,:])
#get specific column from all row present
print(ar[:,2]) #from all row 2nd index column is selected ie;[3,9]
#[startindex:endindex(exclusive):stepsize]
print(ar[1,1:6:2]) #[8,10,12]

ar[:,2]=5 #2ndcolumn of all rows is updated
print(ar)  #[[1,2,5,4,5,6]
            #   [7,8,5,10,11,12]]
ar[1,:]=5 #1th rows all elements are updated with 5
print(ar)
ar[:,2]=[18,19] #2nd column of 1st row replaced with 18 and 2nd row with 19 

#3D array is a combination of 2d array
d3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d3)
print(d3[0,:,:]) #all rows and columns of 0th 2d array
print(d3[0,1,0]) #inside 0th 2d array select 1th row and inside it select 0th column element op->3

#intializing diff kind of array
#all o's matrix(array)
c=np.zeros((2,3)) #create array with 2 rows and 3 column and intialized with 0's and difault datatype of elements is double
print(c)
#for userdefined datatype
d=np.zeros((2,3),dtype="int32") 
print(d)

e=np.zeros((2,3,3),dtype='int32') #3d array ie;two 2d arrays with each 3x3 .you can give int16 also

e=np.ones((4,2,2),dtype='int32') #3d array with 4 2x2 matrix with intial value as 1
#any other intialization value
e=np.full((2,2),27) #2d array with 2x2 and all cells are intialized with 27
e=np.full_like(a,4) #takes array(1,2,3..etc D) and replace all cells with 4

#generate random number (normal distribition o-1) bn 0 to 1 ,takes parameter as 1d or 2d or 3d or etc array
e=np.random.rand(4,2)
print('ahree')
print(e)

#fro random integer 
e=np.random.randint(1,100,size=(3,3)) #generates random no bn 1 to 100(inclusive) and store it in given array
print(e)

#the identiti elements
e=np.identity(5) #create identity array with 5x5
print(e)

#copy and other operation
a=np.array([1,2,3])
#SHALOW COPY,,,upar upar ka copy rna,,ie;copying reference
b=a #copy reference,,,
b[0]=100
print(a)
print(b)

#for data copy not reference
#DEEP COPY,,,each item is copied by going deep inside it,,recursively each item is copied into another list
b=a.copy()
b[0]=99
#only change in b array bcz not refernced
print(a)
print(b)

