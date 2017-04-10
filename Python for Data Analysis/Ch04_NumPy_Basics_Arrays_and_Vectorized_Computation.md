
# Chapter 4. NumPy Basics: Arrays and Vectorized Computation


```python
%matplotlib inline
```


```python
from __future__ import division
from numpy.random import randn
import numpy as np
np.set_printoptions(precision=4, suppress=True)
```

## 4.1 The NumPy ndarray: A Multidimensional Array Object


```python
data = randn(2, 3)
```


```python
data
data * 10
data + data
```




    array([[ 1.5904,  1.4627,  1.3321],
           [-0.1838,  0.2379, -4.6895]])




```python
data.shape
data.dtype
```




    dtype('float64')



### 4.1.1 Creating ndarrays


```python
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1
```




    array([ 6. ,  7.5,  8. ,  0. ,  1. ])




```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape
```




    (2, 4)




```python
arr1.dtype
arr2.dtype
```




    dtype('int32')




```python
np.zeros(10)
np.zeros((3, 6))
np.empty((2, 3, 2))
```




    array([[[ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.]],
    
           [[ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.]]])




```python
np.arange(15)
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])



### 4.1.2 Data Types for ndarrays


```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr1.dtype
arr2.dtype
```




    dtype('int32')




```python
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype
```




    dtype('float64')




```python
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
arr.astype(np.int32)
```




    array([ 3, -1, -2,  0, 12, 10])




```python
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
```




    array([  1.25,  -9.6 ,  42.  ])




```python
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])




```python
empty_uint32 = np.empty(8, dtype='u4')
empty_uint32
```




    array([1, 2, 3, 4, 5, 6, 7, 8], dtype=uint32)



### 4.1.3 Operations between Arrays and Scalars


```python
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
arr * arr
arr - arr
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
1 / arr
arr ** 0.5
```




    array([[ 1.    ,  1.4142,  1.7321],
           [ 2.    ,  2.2361,  2.4495]])



### 4.1.4 Basic Indexing and Slicing


```python
arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8] = 12
arr
```




    array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])




```python
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr
arr_slice[:] = 64
arr
```




    array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])




```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
```




    array([7, 8, 9])




```python
arr2d[0][2]
arr2d[0, 2]
```




    3




```python
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[0]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d
arr3d[0] = old_values
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[1, 0]
```




    array([7, 8, 9])



* __Indexing with slices__


```python
arr[1:6]
```




    array([ 1,  2,  3,  4, 64])




```python
arr2d
arr2d[:2]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
arr2d[:2, 1:]
```




    array([[2, 3],
           [5, 6]])




```python
arr2d[1, :2]
arr2d[2, :1]
```




    array([7])




```python
arr2d[:, :1]
```




    array([[1],
           [4],
           [7]])




```python
arr2d[:2, 1:] = 0
```

### 4.1.5 Boolean Indexing  


```python
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)
names
data
```




    array([[ 0.4857, -2.3062,  0.0509, -0.6884],
           [ 0.4555, -0.7382,  1.5596, -0.0532],
           [-0.2162, -0.9184,  0.7882, -0.8907],
           [ 1.7107,  0.0374, -0.531 ,  1.6703],
           [ 1.2692, -0.2151,  1.8235,  1.1778],
           [ 1.6432, -0.6106, -1.3099,  0.4819],
           [-0.1313, -2.0218,  0.6414, -1.2997]])




```python
names == 'Bob'
```




    array([ True, False, False,  True, False, False, False], dtype=bool)




```python
data[names == 'Bob']
```




    array([[ 0.4857, -2.3062,  0.0509, -0.6884],
           [ 1.7107,  0.0374, -0.531 ,  1.6703]])




```python
data[names == 'Bob', 2:]
data[names == 'Bob', 3]
```




    array([-0.6884,  1.6703])




```python
names != 'Bob'
data[-(names == 'Bob')]
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:2: DeprecationWarning: numpy boolean negative, the `-` operator, is deprecated, use the `~` operator or the logical_not function instead.
      from ipykernel import kernelapp as app
    




    array([[ 0.4555, -0.7382,  1.5596, -0.0532],
           [-0.2162, -0.9184,  0.7882, -0.8907],
           [ 1.2692, -0.2151,  1.8235,  1.1778],
           [ 1.6432, -0.6106, -1.3099,  0.4819],
           [-0.1313, -2.0218,  0.6414, -1.2997]])




```python
mask = (names == 'Bob') | (names == 'Will')
mask
data[mask]
```




    array([[ 0.4857, -2.3062,  0.0509, -0.6884],
           [-0.2162, -0.9184,  0.7882, -0.8907],
           [ 1.7107,  0.0374, -0.531 ,  1.6703],
           [ 1.2692, -0.2151,  1.8235,  1.1778]])




```python
data[data < 0] = 0
data
```




    array([[ 0.4857,  0.    ,  0.0509,  0.    ],
           [ 0.4555,  0.    ,  1.5596,  0.    ],
           [ 0.    ,  0.    ,  0.7882,  0.    ],
           [ 1.7107,  0.0374,  0.    ,  1.6703],
           [ 1.2692,  0.    ,  1.8235,  1.1778],
           [ 1.6432,  0.    ,  0.    ,  0.4819],
           [ 0.    ,  0.    ,  0.6414,  0.    ]])




```python
data[names != 'Joe'] = 7
data
```




    array([[ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 0.4555,  0.    ,  1.5596,  0.    ],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 1.6432,  0.    ,  0.    ,  0.4819],
           [ 0.    ,  0.    ,  0.6414,  0.    ]])



### 4.1.6 Fancy Indexing


```python
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
arr
```




    array([[ 0.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  1.],
           [ 2.,  2.,  2.,  2.],
           [ 3.,  3.,  3.,  3.],
           [ 4.,  4.,  4.,  4.],
           [ 5.,  5.,  5.,  5.],
           [ 6.,  6.,  6.,  6.],
           [ 7.,  7.,  7.,  7.]])




```python
arr[[4, 3, 0, 6]]
```




    array([[ 4.,  4.,  4.,  4.],
           [ 3.,  3.,  3.,  3.],
           [ 0.,  0.,  0.,  0.],
           [ 6.,  6.,  6.,  6.]])




```python
arr[[-3, -5, -7]]
```




    array([[ 5.,  5.,  5.,  5.],
           [ 3.,  3.,  3.,  3.],
           [ 1.,  1.,  1.,  1.]])




```python
# more on reshape in Chapter 12
arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
```




    array([ 4, 23, 29, 10])




```python
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
```




    array([[ 4,  7,  5,  6],
           [20, 23, 21, 22],
           [28, 31, 29, 30],
           [ 8, 11,  9, 10]])




```python
arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
```

### 4.1.7 Transposing Arrays and Swapping Axes


```python
arr = np.arange(15).reshape((3, 5))
arr
arr.T
```


```python
arr = np.random.randn(6, 3)
np.dot(arr.T, arr)
```


```python
arr = np.arange(16).reshape((2, 2, 4))
arr
arr.transpose((1, 0, 2))
```


```python
arr
arr.swapaxes(1, 2)
```

## 4.2 Universal Functions: Fast Element-wise Array Functions


```python
arr = np.arange(10)
np.sqrt(arr)
np.exp(arr)
```


```python
x = randn(8)
y = randn(8)
x
y
np.maximum(x, y) # element-wise maximum
```


```python
arr = randn(7) * 5
np.modf(arr)
```

## 4.3 Data Processing Using Arrays


```python
points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
ys
```


```python
from matplotlib.pyplot import imshow, title
```


```python
import matplotlib.pyplot as plt
z = np.sqrt(xs ** 2 + ys ** 2)
z
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
```


```python
plt.draw()
```

### 4.3.1 Expressing Conditional Logic as Array Operations


```python
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
```


```python
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
result
```


```python
result = np.where(cond, xarr, yarr)
result
```


```python
arr = randn(4, 4)
arr
np.where(arr > 0, 2, -2)
np.where(arr > 0, 2, arr) # set only positive values to 2
```


```python
# Not to be executed

result = []
for i in range(n):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)
```


```python
# Not to be executed

np.where(cond1 & cond2, 0,
         np.where(cond1, 1,
                  np.where(cond2, 2, 3)))
```


```python
# Not to be executed

result = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)
```

### 4.3.2 Mathematical and Statistical Methods


```python
arr = np.random.randn(5, 4) # normally-distributed data
arr.mean()
np.mean(arr)
arr.sum()
```


```python
arr.mean(axis=1)
arr.sum(0)
```


```python
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr.cumsum(0)
arr.cumprod(1)
```

### 4.3.3 Methods for Boolean Arrays


```python
arr = randn(100)
(arr > 0).sum() # Number of positive values
```


```python
bools = np.array([False, False, True, False])
bools.any()
bools.all()
```

### 4.3.4 Sorting


```python
arr = randn(8)
arr
arr.sort()
arr
```


```python
arr = randn(5, 3)
arr
arr.sort(1)
arr
```


```python
large_arr = randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))] # 5% quantile
```

### 4.3.5 Unique and Other Set Logic


```python
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)
```


```python
sorted(set(names))
```


```python
values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])
```

## 4.4 File Input and Output with Arrays

### 4.4.1 Storing Arrays on Disk in Binary Format


```python
arr = np.arange(10)
np.save('some_array', arr)
```


```python
np.load('some_array.npy')
```


```python
np.savez('array_archive.npz', a=arr, b=arr)
```


```python
arch = np.load('array_archive.npz')
arch['b']
```


```python
!rm some_array.npy
!rm array_archive.npz
```

### 4.4.2 Saving and Loading Text Files


```python
!cat array_ex.txt
```


```python
arr = np.loadtxt('array_ex.txt', delimiter=',')
arr
```

## 4.5 Linear Algebra


```python
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
x
y
x.dot(y)  # equivalently np.dot(x, y)
```


```python
np.dot(x, np.ones(3))
```


```python
np.random.seed(12345)
```


```python
from numpy.linalg import inv, qr
X = randn(5, 5)
mat = X.T.dot(X)
inv(mat)
mat.dot(inv(mat))
q, r = qr(mat)
r
```

## 4.6 Random Number Generation


```python
samples = np.random.normal(size=(4, 4))
samples
```


```python
from random import normalvariate
N = 1000000
%timeit samples = [normalvariate(0, 1) for _ in xrange(N)]
%timeit np.random.normal(size=N)
```

## 4.7 Example: Random Walks
import random
position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

```python
np.random.seed(12345)
```


```python
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
```


```python
walk.min()
walk.max()
```


```python
(np.abs(walk) >= 10).argmax()
```

### 4.7.1 Simulating Many Random Walks at Once 


```python
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks
```


```python
walks.max()
walks.min()
```


```python
hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum() # Number that hit 30 or -30
```


```python
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
```


```python
steps = np.random.normal(loc=0, scale=0.25,
                         size=(nwalks, nsteps))
```
