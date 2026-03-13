import numpy as np
array1=np.array([32,56,78,90,45,89,12,13])
print("first array")
print(array1)
print("----------------------------------")
#reshaping in order 4,2
array2 = array1.reshape(4,2)
print("second array : ")
print(array2)
print("---------------------------------")
#reshaping the array into 3d array
array3 = array1.reshape(2,2,2)
print("third array : ")
print(array3)
print("---------------------------------")
array4 = array1.reshape(1,1,8)
print("forth array")
print(array4)
print("---------------------------------")
array5 = array1.reshape(1,2,4)
print("fifth array")
print(array5)
print("---------------------------------")
array6 = array1.reshape(1,4,2)
print("sixth array")
print(array6)
average = np.mean(array1)
print(average)
print("standard deviation : " , np.std(array1))

'''output
first array
[32 56 78 90 45 89 12 13]
----------------------------------
second array : 
[[32 56]
 [78 90]
 [45 89]
 [12 13]]
---------------------------------
third array : 
[[[32 56]
  [78 90]]

 [[45 89]
  [12 13]]]
---------------------------------
forth array
[[[32 56 78 90 45 89 12 13]]]
---------------------------------
fifth array
[[[32 56 78 90]
  [45 89 12 13]]]
---------------------------------
sixth array
[[[32 56]
  [78 90]
  [45 89]
  [12 13]]]
'''
