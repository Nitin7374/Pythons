import numpy as np
temp =np.array([33.2,50.1,44.3,35.7,31.8])
avg = np.mean(temp)
print(type(avg))

# creating an array (matrix)
array1 = np.full((2,3),8)
print(array1)

# creating a sequence number using numpy

arr =np.arange(0,10,2)
print(arr)

# creating identity matrix

identity_mat =np.eye(5)
print(identity_mat)

# shape used to define no of row and column
def_shape =np.array([[1,2,3],
                    [4,5,6]])
print(def_shape.shape)
# size define size of array
print(def_shape.size)
print(def_shape.ndim)

# converstion of datatype

arr1 =np.array([1.2,2.5,3.4])
arr2 = arr1.astype(int)
print(arr2)
print(arr2.dtype)

# mathematic operator

operator = np.array([12,22,8])
print(operator + 2)
print(operator - 1)
print(operator * 2)
print(operator / 2)
print(operator ** 2)
print(operator ** 3)

# aggrigation function

agg =np.array([10,20,30,40,50])
print(np.sum(agg))
print(np.min(agg))
print(np.max(agg))
print(np.average(agg))
print(np.mean(agg))
print(np.std(agg))
print(np.var(agg))

# indexing abd slicing
# [start: stop :step]
sl =np.array([10,20,30,40,50])
print(sl[1:5])
print(sl[:4])
print(sl[::2])
print(sl[::-1])
print(sl[::-2])

# fancing means to extract multiple data from list
print(sl[[0,2,4]])

# filtering data from list  
print(sl[sl<45])

# inserting into array
inserting = np.array([10,50,40,70])
new_inserting = np.insert(inserting,1,100)
print(new_inserting)

# insering into 2D array
two_D = np.array([[1,2],[3,4]])
new_2D = np.insert(two_D,1,[5,6],axis=0)
print(new_2D)
# append
# concatenate
# delete 

# split the array
spliting =np.array([100,200,300,400,500,600])
print(np.split(spliting,2))
# print(new_spliting)   

# brodcasting
prices = np.array([100,200,300])
discount = 15
print("before discount")
print(prices)
final_prices = prices -(prices *discount/100)
print("after discount")
print(final_prices)

# vectorization
vect = np.array([10,20,30])
multi = vect * 3
print(multi)

# handling missing values

miss = np.array([10,np.nan,50,74])
clear = np.nan_to_num(miss,nan =100)
print(clear)
