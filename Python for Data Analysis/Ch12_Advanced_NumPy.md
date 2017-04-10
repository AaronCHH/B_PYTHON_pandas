
# Chapter 12. Advanced NumPy


```python
from __future__ import division
from numpy.random import randn
from pandas import Series
import numpy as np
np.set_printoptions(precision=4)
import sys
```

## 12.1 ndarray Object Internals

### 12.1.1 NumPy dtype Hierarchy


```python
ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)
np.issubdtype(ints.dtype, np.integer)
np.issubdtype(floats.dtype, np.floating)
```


```python
np.float64.mro()
```

## 12.2 Advanced Array Manipulation

### 12.2.1 Reshaping Arrays


```python
arr = np.arange(8)
arr
arr.reshape((4, 2))
```


```python
arr.reshape((4, 2)).reshape((2, 4))
```


```python
arr = np.arange(15)
arr.reshape((5, -1))
```


```python
other_arr = np.ones((3, 5))
other_arr.shape
arr.reshape(other_arr.shape)
```


```python
arr = np.arange(15).reshape((5, 3))
arr
arr.ravel()
```


```python
arr.flatten()
```

### 12.2.2 C versus Fortran Order


```python
arr = np.arange(12).reshape((3, 4))
arr
arr.ravel()
arr.ravel('F')
```

### 12.2.3 Concatenating and Splitting Arrays


```python
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
np.concatenate([arr1, arr2], axis=0)
np.concatenate([arr1, arr2], axis=1)
```


```python
np.vstack((arr1, arr2))
np.hstack((arr1, arr2))
```


```python
from numpy.random import randn
arr = randn(5, 2)
arr
first, second, third = np.split(arr, [1, 3])
first
second
third
```

* __Stacking helpers: r_ and c___


```python
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = randn(3, 2)
np.r_[arr1, arr2]
np.c_[np.r_[arr1, arr2], arr]
```


```python
np.c_[1:6, -10:-5]
```

### 12.2.4 Repeating Elements: Tile and Repeat


```python
arr = np.arange(3)
arr.repeat(3)
```


```python
arr.repeat([2, 3, 4])
```


```python
arr = randn(2, 2)
arr
arr.repeat(2, axis=0)
```


```python
arr.repeat([2, 3], axis=0)
arr.repeat([2, 3], axis=1)
```


```python
arr
np.tile(arr, 2)
```


```python
arr
np.tile(arr, (2, 1))
np.tile(arr, (3, 2))
```

### 12.2.5 Fancy Indexing Equivalents: Take and Put


```python
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
arr[inds]
```


```python
arr.take(inds)
arr.put(inds, 42)
arr
arr.put(inds, [40, 41, 42, 43])
arr
```


```python
inds = [2, 0, 2, 1]
arr = randn(2, 4)
arr
arr.take(inds, axis=1)
```

## 12.3 Broadcasting


```python
arr = np.arange(5)
arr
arr * 4
```


```python
arr = randn(4, 3)
arr.mean(0)
demeaned = arr - arr.mean(0)
demeaned
demeaned.mean(0)
```


```python
arr
row_means = arr.mean(1)
row_means.reshape((4, 1))
demeaned = arr - row_means.reshape((4, 1))
demeaned.mean(1)
```

### 12.3.1 Broadcasting Over Other Axes


```python
arr - arr.mean(1)
```


```python
arr - arr.mean(1).reshape((4, 1))
```


```python
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
arr_3d.shape
```


```python
arr_1d = np.random.normal(size=3)
arr_1d[:, np.newaxis]
arr_1d[np.newaxis, :]
```


```python
arr = randn(3, 4, 5)
depth_means = arr.mean(2)
depth_means
demeaned = arr - depth_means[:, :, np.newaxis]
demeaned.mean(2)
```


```python
def demean_axis(arr, axis=0):
    means = arr.mean(axis)

    # This generalized things like [:, :, np.newaxis] to N dimensions
    indexer = [slice(None)] * arr.ndim
    indexer[axis] = np.newaxis
    return arr - means[indexer]
```

### 12.3.2 Setting Array Values by Broadcasting


```python
arr = np.zeros((4, 3))
arr[:] = 5
arr
```


```python
col = np.array([1.28, -0.42, 0.44, 1.6])
arr[:] = col[:, np.newaxis]
arr
arr[:2] = [[-1.37], [0.509]]
arr
```

## 12.4 Advanced ufunc Usage

### 12.4.1 ufunc Instance Methods


```python
arr = np.arange(10)
np.add.reduce(arr)
arr.sum()
```


```python
np.random.seed(12346)
```


```python
arr = randn(5, 5)
arr[::2].sort(1) # sort a few rows
arr[:, :-1] < arr[:, 1:]
np.logical_and.reduce(arr[:, :-1] < arr[:, 1:], axis=1)
```


```python
arr = np.arange(15).reshape((3, 5))
np.add.accumulate(arr, axis=1)
```


```python
arr = np.arange(3).repeat([1, 2, 2])
arr
np.multiply.outer(arr, np.arange(5))
```


```python
result = np.subtract.outer(randn(3, 4), randn(5))
result.shape
```


```python
arr = np.arange(10)
np.add.reduceat(arr, [0, 5, 8])
```


```python
arr = np.multiply.outer(np.arange(4), np.arange(5))
arr
np.add.reduceat(arr, [0, 2, 4], axis=1)
```

### 12.4.2 Custom ufuncs


```python
def add_elements(x, y):
    return x + y
add_them = np.frompyfunc(add_elements, 2, 1)
add_them(np.arange(8), np.arange(8))
```


```python
add_them = np.vectorize(add_elements, otypes=[np.float64])
add_them(np.arange(8), np.arange(8))
```


```python
arr = randn(10000)
%timeit add_them(arr, arr)
%timeit np.add(arr, arr)
```

## 12.5 Structured and Record Arrays


```python
dtype = [('x', np.float64), ('y', np.int32)]
sarr = np.array([(1.5, 6), (np.pi, -2)], dtype=dtype)
sarr
```


```python
sarr[0]
sarr[0]['y']
```


```python
sarr['x']
```

### 12.5.1 Nested dtypes and Multidimensional Fields


```python
dtype = [('x', np.int64, 3), ('y', np.int32)]
arr = np.zeros(4, dtype=dtype)
arr
```


```python
arr[0]['x']
```


```python
arr['x']
```


```python
dtype = [('x', [('a', 'f8'), ('b', 'f4')]), ('y', np.int32)]
data = np.array([((1, 2), 5), ((3, 4), 6)], dtype=dtype)
data['x']
data['y']
data['x']['a']
```

### 12.5.2 Why Use Structured Arrays

### 12.5.3 Structured Array Manipulations: numpy.lib.recfunctions

## 12.6 More About Sorting


```python
arr = randn(6)
arr.sort()
arr
```


```python
arr = randn(3, 5)
arr
arr[:, 0].sort()  # Sort first column values in-place
arr
```


```python
arr = randn(5)
arr
np.sort(arr)
arr
```


```python
arr = randn(3, 5)
arr
arr.sort(axis=1)
arr
```


```python
arr[:, ::-1]
```

### 12.6.1 Indirect Sorts: argsort and lexsort


```python
values = np.array([5, 0, 1, 3, 2])
indexer = values.argsort()
indexer
values[indexer]
```


```python
arr = randn(3, 5)
arr[0] = values
arr
arr[:, arr[0].argsort()]
```


```python
first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])
last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
sorter = np.lexsort((first_name, last_name))
zip(last_name[sorter], first_name[sorter])
```

### 12.6.2 Alternate Sort Algorithms


```python
values = np.array(['2:first', '2:second', '1:first', '1:second', '1:third'])
key = np.array([2, 2, 1, 1, 1])
indexer = key.argsort(kind='mergesort')
indexer
values.take(indexer)
```

### 12.6.3 numpy.searchsorted: Finding elements in a Sorted Array


```python
arr = np.array([0, 1, 7, 12, 15])
arr.searchsorted(9)
```


```python
arr.searchsorted([0, 8, 11, 16])
```


```python
arr = np.array([0, 0, 0, 1, 1, 1, 1])
arr.searchsorted([0, 1])
arr.searchsorted([0, 1], side='right')
```


```python
data = np.floor(np.random.uniform(0, 10000, size=50))
bins = np.array([0, 100, 1000, 5000, 10000])
data
```


```python
labels = bins.searchsorted(data)
labels
```


```python
Series(data).groupby(labels).mean()
```


```python
np.digitize(data, bins)
```

## 12.7 NumPy Matrix Class


```python
X =  np.array([[ 8.82768214,  3.82222409, -1.14276475,  2.04411587],
               [ 3.82222409,  6.75272284,  0.83909108,  2.08293758],
               [-1.14276475,  0.83909108,  5.01690521,  0.79573241],
               [ 2.04411587,  2.08293758,  0.79573241,  6.24095859]])
X[:, 0]  # one-dimensional
y = X[:, :1]  # two-dimensional by slicing
X
y
```


```python
np.dot(y.T, np.dot(X, y))
```


```python
Xm = np.matrix(X)
ym = Xm[:, 0]
Xm
ym
ym.T * Xm * ym
```


```python
Xm.I * X
```

## 12.8 Advanced Array Input and Output

### 12.8.1 Memory-mapped Files


```python
mmap = np.memmap('mymmap', dtype='float64', mode='w+', shape=(10000, 10000))
mmap
```


```python
section = mmap[:5]
```


```python
section[:] = np.random.randn(5, 10000)
mmap.flush()
mmap
del mmap
```


```python
mmap = np.memmap('mymmap', dtype='float64', shape=(10000, 10000))
mmap
```


```python
%xdel mmap
!rm mymmap
```

### 12.8.2 HDF5 and Other Array Storage Options

## 12.9 Performance Tips

### 12.9.1 The Importance of Contiguous Memory


```python
arr_c = np.ones((1000, 1000), order='C')
arr_f = np.ones((1000, 1000), order='F')
arr_c.flags
arr_f.flags
arr_f.flags.f_contiguous
```


```python
%timeit arr_c.sum(1)
%timeit arr_f.sum(1)
```


```python
arr_f.copy('C').flags
```


```python
arr_c[:50].flags.contiguous
arr_c[:, :50].flags
```


```python
%xdel arr_c
%xdel arr_f
%cd ..
```

### 12.9.2 Other Speed Options: Cython, f2py, C

```cython
from numpy cimport ndarray, float64_t

def sum_elements(ndarray[float64_t] arr):
    cdef Py_ssize_t i, n = len(arr)
    cdef float64_t result = 0

    for i in range(n):
        result += arr[i]

    return result
```
