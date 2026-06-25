# import numpy as np
# a = np.array([1, 2, 3])
# print(a)


# import numpy
# print("hello")


# import numpy
# n = numpy.arange(10)
# print(type(n))
# print(n)
# print(n[0])



# Example 

# import numpy
# n = numpy.arange(12)
# d = n.reshape(3,4)
# print(type(d))
# print(d)


# Example 2d

# import numpy
# n = numpy.arange(12).reshape(4,3)
# print(n)


# Example 3d

# import numpy
# n = numpy.arange(24).reshape(2,3,4) # 3 --> row or 4 --> column
# n = numpy.arange(24).reshape(1,6,4) # 6 --> row or 4 --> column
# print(n)


# example split

# import numpy
# n = numpy.arange(12).reshape(4,3)
# print(n)
# print(n[0][2])
# print(n[1][2])
# print(n[2][2])
# print(n[3][2])

# print(n[0:4:,2])
# print(n[1:3,1:2])



# list
# l = [1,2,3]
# print(l)

#array 1d
# import numpy as np
# arr = np.array(l)
# print(arr)

# 2d arrary
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0][0])



# list
# l = [[1,2,3],[4,5,6]]
# l[1][0] = 100
# print(l)

# array
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# arr[1][0] = 100
# print(arr)



# list
# l = [1,2,3]
# lm = l*2
# print(lm)

# array
# import numpy as np
# arr = np.array(l)
# arrm = arr*2
# print(arrm)



# comparsion 

# list
# import time
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output: ",time.time() - start)

# array
# import numpy as np
# start = time.time()
# arr = np.array(100000)*2
# print("array output: ",time.time() - start)



# Zeros

# 1d
# import numpy as np
# arr = np.zeros(5)
# print(arr)

# 2d
# import numpy as np
# arr1 = np.zeros((3,4))
# print(arr1)



# Ones

# 1d
# import numpy as np
# arr = np.ones(5)
# print(arr)

# 2d
# import numpy as np
# arr1 = np.ones((3,4))
# print(arr1)



# Question 

# zeros array 2d

# import numpy as np
# arr1 = np.zeros((3,4)) + 10
# print(arr1)

# ones array 2d

# import numpy as np
# arr1 = np.ones((3,4)) * 10
# print(arr1)



# Full

# 1d
# import numpy as np
# arr = np.full((2),5)
# print(arr)

# 2d
# import numpy as np
# arr = np.full((2,3),5)
# print(arr)



# Question

# zeros array 2d

# import numpy as np
# arr1 = np.zeros((3,4)) + 6
# print(arr1)

# full for 2d

# import numpy as np
# arr = np.full((2,3),1)
# print(arr)



# Random

# 1d
# import numpy as np
# arr = np.random.random(5)
# print(arr)

# 2d
# import numpy as np
# arr = np.random.random((2,3))
# print(arr)



# Arange

# 1d
# import numpy as np
# arr = np.arange(5)
# print(arr)

# 2d
# import numpy as np
# arr = np.arange(6).reshape(2,3)
# print(arr)



# Vector 1d list

# l = [1,2,3]
# print(l)

# Vector 1d array

# import numpy as np
# arr = np.array(l)
# print(arr)



# Matrix 2d list

# l = [[1,2,3],[4,5,6]]
# print(l)

# Matrix 2d array

# import numpy as np
# arr = np.array(l)
# print(arr)



# Tensor 3d list

# l = [[[1,2],[3,4],[5,6],[7,8]]]
# print(l)

# Tensor 3d array

# import numpy as np
# arr = np.array(l)
# print(arr)



# Array Properties

# import numpy as np
# arr = np.arange(12)
# arr = np.arange(12).reshape(3,4) # for 2d
# print("shape: ",np.shape(arr))
# print("dimension: ",np.ndim(arr))
# print("size: ",np.size(arr))
# print("datatype: ",arr.dtype)



# Array reshape

# 2d
# import numpy as np
# arr = np.arange(12)
# up_arr = np.reshape(arr,(3,4))
# print(up_arr)

# Example 1

# 3d
# import numpy as np
# arr = np.arange(24)
# up_arr = np.reshape(arr,((3,2,4)))
# print(up_arr)


# example 2

# 2d
# import numpy as np
# arr = np.arange(12)
# up_arr = np.reshape(arr,(3*4))
# print(up_arr)

# 3d
# import numpy as np
# arr = np.arange(24)
# up_arr = np.reshape(arr,((3*2*4)))
# print(up_arr)



# flatten

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# up_arr = arr.flatten()
# up_arr[0] = 100
# print(up_arr)
# print(arr)

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,2,4)
# up_arr = arr.flatten()
# up_arr[0] = 100
# print(up_arr)
# print(arr)



# Ravel

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# up_arr = arr.ravel()
# up_arr[0] = 100
# print(up_arr)
# print(arr)

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,2,4)
# up_arr = arr.ravel()
# up_arr[0] = 100
# print(up_arr)
# print(arr)



# Transpose

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# up_arr = arr.T
# print(up_arr)

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,4,2)
# up_arr = arr.T
# print(up_arr)



# Slicing

# 1d
# import numpy as np
# arr = np.arange(12)
# print(arr)
# up_arr = arr[0:5]
# print(up_arr)

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr[0:2,0:3]
# print(up_arr)

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,4,2)
# print(arr)
# up_arr = arr[0:3,0:2,0:3]
# print(up_arr)
# print(arr[0,0,0])
# print(arr[2,3,1])



# while loop

# 1d
# import numpy as np
# arr = np.arange(12)
# i = 0
# while i < len(arr):
#     print(arr[i], end=" ")
#     i += 1

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# i = 0
# while i < len(arr):
#     j = 0
#     while j < len(arr[i]):
#         print(arr[i][j], end=" ")
#         j += 1
#     i += 1

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,4,2)
# i = 0
# while i < len(arr):
#     j = 0
#     while j < len(arr[i]):
#         k = 0
#         while k < len(arr[i][j]):
#             print(arr[i][j][k], end=" ")
#             k += 1
#         j += 1
#     i += 1



# for loop

# 1d
# import numpy as np
# arr = np.arange(12)
# for i in arr:
#     print(i, end=" ")

# 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# for i in arr:
#     for j in i:
#         print(j, end=" ")

# 3d
# import numpy as np
# arr = np.arange(24).reshape(3,4,2)
# for i in arr:
#     for j in i:
#         for k in j:
#             print(k, end=" ")



# sort

# 1d
# import numpy as np
# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s =np.sort()
# print(arr_s)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4]])
# print(arr)
# arr_s = np.sort(arr, axis=1)
# print(arr_s)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,55,8]]])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)



# By default sorting --> asecending | decending

# 1d
# import numpy as np
# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)
# # decending
# arr_s1 = np.sort(arr)[::-1]
# print(arr_s1)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4]])
# print(arr)
# arr_s = np.sort(arr, axis=1)
# print(arr_s)
# # decending
# arr_s1 = np.sort(arr)[:,::-1]
# print(arr_s1)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,10,18]]])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)
# # decending
# arr_s1 = np.sort(arr)[:,:,::-1]
# print(arr_s1)



# Filter

# 1d
# import numpy as np
# arr = np.array([10,20,30,60,7,9])
# print(arr)
# arr_f = arr[arr < 20]
# print(arr_f)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4],[15,35,22]])
# print(arr)
# arr_f = arr[arr < 20]
# print(arr_f)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,22,18]]])
# print(arr)
# arr_f = arr[arr < 20]
# print(arr_f)



# Example

# 1d
# import numpy as np
# arr = np.array([10,21,30,65,6,9])
# print(arr)
# arr_f = arr[arr % 2 == 0]
# print(arr_f)

# 2d
# import numpy as np
# arr = np.array([[8,35,20],[40,95,7],[15,35,22]])
# print(arr)
# arr_f = arr[arr % 2 == 0]
# print(arr_f)

# 3d
# import numpy as np
# arr = np.array([[[5,6,23],[45,90,3],[9,22,18]]])
# print(arr)
# arr_f = arr[arr % 2 == 0]
# print(arr_f)



# Fancy indexing

# 1d
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr)
# arr_f = arr[[0,2,4]]
# print(arr_f)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4],[15,35,22]])
# print(arr)
# arr_f = arr[[0,2]]
# print(arr_f)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,22,18],[15,35,22]]])
# print(arr)
# arr_f = arr[0 ,[0,2]]
# print(arr_f)



# np.where

# 1d
# import numpy as np
# arr = np.array([30,2,3,40,5,80,32])
# print(arr)
# arr_w = np.where(arr > 25,"True","False")
# print(arr_w)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4],[15,35,22]])
# print(arr)
# arr_w = np.where(arr > 25,"True","False")
# print(arr_w)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,22,18],[15,35,26]]])
# print(arr)
# arr_w = np.where(arr > 25,"True","False")
# print(arr_w)



# Example

# 1d
# import numpy as np
# arr = np.array([10,21,30,65,6,9])
# print(arr)
# arr_w = np.where(arr % 2 == 0,"True","False")
# print(arr_w)

# 2d
# import numpy as np
# arr = np.array([[5,60,20],[40,90,4],[15,35,22]])
# print(arr)
# arr_w = np.where(arr % 2 == 0,"True","False")
# print(arr_w)

# 3d
# import numpy as np
# arr = np.array([[[5,60,20],[40,90,4],[9,22,18],[15,35,22]]])
# print(arr)
# arr_w = np.where(arr % 2 == 0,"True","False")
# print(arr_w)



# Concatenate

# 1d
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([1,2,3])
# arr1_arr2 = np.concatenate((arr1, arr2))
# print(arr1_arr2)

# 2d 
# import numpy as np
# arr1 = np.array([[5,60,20],[40,90,4]])
# arr2 = np.array([[15,35,22],[9,22,18]])
# arr1_arr2 = np.concatenate((arr1, arr2), axis=1)
# print(arr1_arr2)

# 3d
# import numpy as np
# arr1 = np.array([[[5,60,20],[40,90,4]]])
# arr2 = np.array([[[15,35,22],[9,22,18]]])
# arr1_arr2 = np.concatenate((arr1, arr2), axis=1)
# print(arr1_arr2)



# np.sum

# 1d 