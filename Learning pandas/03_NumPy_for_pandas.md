
# Chapter 3: NumPy for pandas
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 3: NumPy for pandas](#chapter-3-numpy-for-pandas)
  * [3.1 Installing and importing NumPy](#31-installing-and-importing-numpy)
  * [3.2 Benefits and characteristics of NumPy arrays](#32-benefits-and-characteristics-of-numpy-arrays)
  * [3.3 Creating NumPy arrays and performing basic array operations](#33-creating-numpy-arrays-and-performing-basic-array-operations)
  * [3.4 Selecting array elements](#34-selecting-array-elements)
  * [3.5 Logical operations on arrays](#35-logical-operations-on-arrays)
  * [3.6 Slicing arrays](#36-slicing-arrays)
  * [3.7 Reshaping arrays](#37-reshaping-arrays)
  * [3.8 Combining arrays](#38-combining-arrays)
  * [3.9 Splitting arrays](#39-splitting-arrays)
  * [3.10 Useful numerical methods of NumPy arrays](#310-useful-numerical-methods-of-numpy-arrays)
  * [3.11 Summary](#311-summary)

<!-- tocstop -->


## 3.1 Installing and importing NumPy


```python
# this allows us to access numpy using the
# np. prefix
import numpy as np
```

## 3.2 Benefits and characteristics of NumPy arrays


```python
# a function that squares all the values
# in a sequence
def squares(values):
    result = []
    for v in values:
        result.append(v * v)
    return result

# create 100,000 numbers using python range
to_square = range(100000)
# time how long it takes to repeatedly square them all
%timeit squares(to_square)
```

    100 loops, best of 3: 14.5 ms per loop



```python
# now lets do this with a numpy array
array_to_square = np.arange(0, 100000)
# and time using a vectorized operation
%timeit array_to_square ** 2
```

    10000 loops, best of 3: 77.6 µs per loop


## 3.3 Creating NumPy arrays and performing basic array operations


```python
# a simple array
a1 = np.array([1, 2, 3, 4, 5])
a1
```




    array([1, 2, 3, 4, 5])




```python
# what is its type?
type(a1)
```




    numpy.ndarray




```python
# how many elements?
np.size(a1)
```




    5




```python
# any floats in the sequences makes
# it an array of floats
a2 = np.array([1, 2, 3, 4.0, 5.0])
a2
```




    array([ 1.,  2.,  3.,  4.,  5.])




```python
# array is all of one type (float64 in this case)
a2.dtype
```




    dtype('float64')




```python
# shorthand to repeat a sequence 10 times
a3 = np.array([0]*10)
a3
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
# convert a python range to numpy array
np.array(range(10))
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# create a numpy array of 10 0.0's
np.zeros(10)
```




    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])




```python
# force it to be of int instead of float64
np.zeros(10, dtype=int)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
# make "a range" starting at 0 and with 10 values
np.arange(0, 10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# 0 <= x < 10 increment by two
np.arange(0, 10, 2)
```




    array([0, 2, 4, 6, 8])




```python
# 10 >= x > 0, counting down
np.arange(10, 0, -1)
```




    array([10,  9,  8,  7,  6,  5,  4,  3,  2,  1])




```python
# evenly spaced #'s between two intervals
np.linspace(0, 10, 11)
```




    array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.])




```python
# multiply numpy array by 2
a1 = np.arange(0, 10)
a1 * 2
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
# add two numpy arrays
a2 = np.arange(10, 20)
a1 + a2
```




    array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28])




```python
# create a 2- array (2x2)
np.array([[1,2], [3,4]])
```




    array([[1, 2],
           [3, 4]])




```python
# create a 1x20 array, and reshape to a 5x4 2d-array
m = np.arange(0, 20).reshape(5, 4)
m
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19]])




```python
# size of any dimensional array is the # of elements
np.size(m)
```




    20




```python
# can ask the size along a given axis (0 is rows)
np.size(m, 0)
```




    5




```python
# and 1 is the columns
np.size(m, 1)
```




    4



## 3.4 Selecting array elements


```python
# select 0-based elements 0 and 2
a1[0], a1[2]
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-6291bf204242> in <module>()
          1 # select 0-based elements 0 and 2
    ----> 2 a1[0], a1[2]


    NameError: name 'a1' is not defined



```python
# select an element in 2d array at row 1 column 2
m[1, 2]
```




    6




```python
# all items in row 1
m[1,]
```




    array([4, 5, 6, 7])




```python
m[1,:]
```




    array([4, 5, 6, 7])




```python
# all items in column 2
m[:,2]
```




    array([ 2,  6, 10, 14, 18])



## 3.5 Logical operations on arrays


```python
# which items are less than 2?
a = np.arange(5)
a < 2
```




    array([ True,  True, False, False, False], dtype=bool)




```python
# this is commented as it will cause an exception
# print (a<2 or a>3)
```


```python
# less than 2 or greater than 3?
(a<2) | (a>3)
```




    array([ True,  True, False, False,  True], dtype=bool)




```python
# create a function that is applied to all array elements
def exp (x):
    return x<3 or x>3
# np.vectorize applies the method to all items in an array
np.vectorize(exp)(a)
```




    array([ True,  True,  True, False,  True], dtype=bool)




```python
# boolean select items < 3
r = a<3
# applying the result of the expression to the [] operate
# selects just the array elements where there is a matching True
a[r]
```




    array([0, 1, 2])




```python
# np.sum treats True as 1 and False as 0
# so this is how many items are less than 3
np.sum(a < 3)
```




    3




```python
# This can be applied across two arrays
a1 = np.arange(0, 5)
a2 = np.arange(5, 0, -1)
a1 < a2
```




    array([ True,  True,  True, False, False], dtype=bool)




```python
# and even multi dimensional arrays
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9, 0 , -1).reshape(3, 3)
a1 < a2
```




    array([[ True,  True,  True],
           [ True,  True, False],
           [False, False, False]], dtype=bool)



## 3.6 Slicing arrays


```python
# get all items in the array from position 3
# up to position 8 (but not inclusive)
a1 = np.arange(1, 10)
a1[3:8]
```




    array([4, 5, 6, 7, 8])




```python
# every other item
a1[::2]
```




    array([1, 3, 5, 7, 9])




```python
# in reverse order
a1[::-1]
```




    array([9, 8, 7, 6, 5, 4, 3, 2, 1])




```python
# note that when in reverse, this does not include
# the element specified in the second component of the slice
# ie: there is no 1 printed in this
a1[9:0:-1]
```




    array([9, 8, 7, 6, 5, 4, 3, 2])




```python
# all items from position 5 onwards
a1[5:]
```




    array([6, 7, 8, 9])




```python
# the items in the first 5 positions
a1[:5]
```




    array([1, 2, 3, 4, 5])




```python
# we saw this earlier
# : in rows specifier means all rows
# so this gets items in column position 1, all rows
m[:,1]
```




    array([ 1,  5,  9, 13, 17])




```python
# in all rows, but for all columns in positions
# 1 up to but not including 3
m[:,1:3]
```




    array([[ 1,  2],
           [ 5,  6],
           [ 9, 10],
           [13, 14],
           [17, 18]])




```python
# in row positions 3 up to but not including 5, all columns
m[3:5,:]
```




    array([[12, 13, 14, 15],
           [16, 17, 18, 19]])




```python
# combined to pull out a sub matrix of the matrix
m[3:5,1:3]
```




    array([[13, 14],
           [17, 18]])




```python
# using a python array, we can select
# non-contiguous rows or columns
m[[1,3,4],:]
```




    array([[ 4,  5,  6,  7],
           [12, 13, 14, 15],
           [16, 17, 18, 19]])



## 3.7 Reshaping arrays


```python
# create a 9 element array (1x9)
a = np.arange(0, 9)
# and reshape to a 3x3 2-d array
m = a.reshape(3, 3)
m
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
# and we can reshape downward in dimensions too
reshaped = m.reshape(9)
reshaped
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8])




```python
# .ravel will array representing a flattened 2-d array
raveled = m.ravel()
raveled
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8])




```python
# it does not alter the shape of the source
m
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
# but it will be a view into the source
# so items changed in the result of the ravel
# are changed in the original object
# reshape m to an array
reshaped = m.reshape(np.size(m))
# ravel into an array
raveled = m.ravel()
# change values in either
reshaped[2] = 1000
raveled[5] = 2000
# and they show as changed in the original
m
```




    array([[   0,    1, 1000],
           [   3,    4, 2000],
           [   6,    7,    8]])




```python
# flattened is like ravel, but a copy of the data,
# not a view into the source
m2 = np.arange(0, 9).reshape(3,3)
flattened = m2.flatten()
# change in the flattened object
flattened[0] = 1000
flattened
```




    array([1000,    1,    2,    3,    4,    5,    6,    7,    8])




```python
# but not in the original
m2
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
# we can reshape by assigning  a tuple to the .shape property
# we start with this, which has one dimension
flattened.shape
```




    (9,)




```python
# and make it 3x3
flattened.shape = (3, 3)
# it is no longer flattened
flattened
```




    array([[1000,    1,    2],
           [   3,    4,    5],
           [   6,    7,    8]])




```python
# transpose a matrix
flattened.transpose()
```




    array([[1000,    3,    6],
           [   1,    4,    7],
           [   2,    5,    8]])




```python
# can also use .T property to transpose
flattened.T
```




    array([[1000,    3,    6],
           [   1,    4,    7],
           [   2,    5,    8]])




```python
# we can also use .resize, which changes shape of
# and object in-place
m = np.arange(0, 9).reshape(3,3)
m.resize(1, 9)
m # my shape has changed
```




    array([[0, 1, 2, 3, 4, 5, 6, 7, 8]])



## 3.8 Combining arrays


```python
# creating two arrays for examples
a = np.arange(9).reshape(3, 3)
b = (a + 1) * 10
a
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
b
```




    array([[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]])




```python
# horizontally stack the two arrays
# b becomes columns of a to the right of a's columns
np.hstack((a, b))
```




    array([[ 0,  1,  2, 10, 20, 30],
           [ 3,  4,  5, 40, 50, 60],
           [ 6,  7,  8, 70, 80, 90]])




```python
# identical to concatenate along axis = 1
np.concatenate((a, b), axis = 1)
```




    array([[ 0,  1,  2, 10, 20, 30],
           [ 3,  4,  5, 40, 50, 60],
           [ 6,  7,  8, 70, 80, 90]])




```python
# vertical stack, adding b as rows after a's rows
np.vstack((a, b))
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]])




```python
# concatenate along axis=0 is the same as vstack
np.concatenate((a, b), axis = 0)
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]])




```python
# dstack stacks each independent column of a and b
np.dstack((a, b))
```




    array([[[ 0, 10],
            [ 1, 20],
            [ 2, 30]],

           [[ 3, 40],
            [ 4, 50],
            [ 5, 60]],

           [[ 6, 70],
            [ 7, 80],
            [ 8, 90]]])




```python
# set up 1-d array
one_d_a = np.arange(5)
one_d_a
```




    array([0, 1, 2, 3, 4])




```python
# another 1-d array
one_d_b = (one_d_a + 1) * 10
one_d_b
```




    array([10, 20, 30, 40, 50])




```python
# stack the two columns
np.column_stack((one_d_a, one_d_b))
```




    array([[ 0, 10],
           [ 1, 20],
           [ 2, 30],
           [ 3, 40],
           [ 4, 50]])




```python
# stack along rows
np.row_stack((one_d_a, one_d_b))
```




    array([[ 0,  1,  2,  3,  4],
           [10, 20, 30, 40, 50]])



## 3.9 Splitting arrays


```python
# sample array
a = np.arange(12).reshape(3, 4)
a
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
# horiz split the 2-d array into 4 array columns
np.hsplit(a, 4)
```




    [array([[0],
            [4],
            [8]]), array([[1],
            [5],
            [9]]), array([[ 2],
            [ 6],
            [10]]), array([[ 3],
            [ 7],
            [11]])]




```python
# horiz split into two array columns
np.hsplit(a, 2)
```




    [array([[0, 1],
            [4, 5],
            [8, 9]]), array([[ 2,  3],
            [ 6,  7],
            [10, 11]])]




```python
# split at columns 1 and 3
np.hsplit(a, [1, 3])
```




    [array([[0],
            [4],
            [8]]), array([[ 1,  2],
            [ 5,  6],
            [ 9, 10]]), array([[ 3],
            [ 7],
            [11]])]




```python
# along the rows
np.split(a, 2, axis = 1)
```




    [array([[0, 1],
            [4, 5],
            [8, 9]]), array([[ 2,  3],
            [ 6,  7],
            [10, 11]])]




```python
# new array for examples
a = np.arange(12).reshape(4, 3)
a
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])




```python
# split into four rows of arrays
np.vsplit(a, 4)
```




    [array([[0, 1, 2]]),
     array([[3, 4, 5]]),
     array([[6, 7, 8]]),
     array([[ 9, 10, 11]])]




```python
# into two rows of arrays
np.vsplit(a, 2)
```




    [array([[0, 1, 2],
            [3, 4, 5]]), array([[ 6,  7,  8],
            [ 9, 10, 11]])]




```python
# split along axis=0
# row 0 of original is row 0 of new array
# rows 1 and 2 of original are row 1
np.vsplit(a, [1, 3])
```




    [array([[0, 1, 2]]), array([[3, 4, 5],
            [6, 7, 8]]), array([[ 9, 10, 11]])]




```python
# split can specify axis
np.split(a, 2, axis = 0)
```




    [array([[0, 1, 2],
            [3, 4, 5]]), array([[ 6,  7,  8],
            [ 9, 10, 11]])]




```python
# 3-d array
c = np.arange(27).reshape(3, 3, 3)
c
```




    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8]],

           [[ 9, 10, 11],
            [12, 13, 14],
            [15, 16, 17]],

           [[18, 19, 20],
            [21, 22, 23],
            [24, 25, 26]]])




```python
# split into 3
np.dsplit(c, 3)
```




    [array([[[ 0],
             [ 3],
             [ 6]],

            [[ 9],
             [12],
             [15]],

            [[18],
             [21],
             [24]]]), array([[[ 1],
             [ 4],
             [ 7]],

            [[10],
             [13],
             [16]],

            [[19],
             [22],
             [25]]]), array([[[ 2],
             [ 5],
             [ 8]],

            [[11],
             [14],
             [17]],

            [[20],
             [23],
             [26]]])]



## 3.10 Useful numerical methods of NumPy arrays


```python
# demonstrate some of the properties of NumPy arrays
m = np.arange(10, 19).reshape(3, 3)
print (a)
print ("{0} min of the entire matrix".format(m.min()))
print ("{0} max of entire matrix".format(m.max()))
print ("{0} position of the min value".format(m.argmin()))
print ("{0} position of the max value".format(m.argmax()))
print ("{0} mins down each column".format(m.min(axis = 0)))
print ("{0} mins across each row".format(m.min(axis = 1)))
print ("{0} maxs down each column".format(m.max(axis = 0)))
print ("{0} maxs across each row".format(m.max(axis = 1)))
```

    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]]
    10 min of the entire matrix
    18 max of entire matrix
    0 position of the min value
    8 position of the max value
    [10 11 12] mins down each column
    [10 13 16] mins across each row
    [16 17 18] maxs down each column
    [12 15 18] maxs across each row



```python
# demonstrate included statistical methods
a = np.arange(10)
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a.mean(), a.std(), a.var()
```




    (4.5, 2.8722813232690143, 8.25)




```python
# demonstrate sum and prod
a = np.arange(1, 6)
a
```




    array([1, 2, 3, 4, 5])




```python
a.sum(), a.prod()
```




    (15, 120)




```python
# and cumulative sum and prod
a.cumsum(), a.cumprod()
```




    (array([ 1,  3,  6, 10, 15]), array([  1,   2,   6,  24, 120]))




```python
# applying logical operators
a = np.arange(10)
(a < 5).any() # any < 5?
```




    True




```python
(a < 5).all() # all < 5?
```




    False




```python
# size is always the total number of elements
np.arange(10).reshape(2, 5).size
```




    10




```python
# .ndim will with you the total # of dimensions
np.arange(10).reshape(2,5).ndim
```




    2



## 3.11 Summary


```python

```
