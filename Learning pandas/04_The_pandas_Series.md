
# Chapter 4: The pandas Series Object
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 4: The pandas Series Object](#chapter-4-the-pandas-series-object)
  * [4.1 The Series object](#41-the-series-object)
  * [4.2 Importing pandas](#42-importing-pandas)
  * [4.3 Creating Series](#43-creating-series)
  * [4.4 Size, shape, uniqueness, and counts of values](#44-size-shape-uniqueness-and-counts-of-values)
  * [4.5 Peeking at data with heads, tails, and take](#45-peeking-at-data-with-heads-tails-and-take)
  * [4.6 Looking up values in Series](#46-looking-up-values-in-series)
    * [Alignment via index labels](#alignment-via-index-labels)
  * [4.7 Arithmetic operations](#47-arithmetic-operations)
  * [4.8 The special case of Not-A-Number (NaN)](#48-the-special-case-of-not-a-number-nan)
  * [4.9 Boolean selection](#49-boolean-selection)
  * [4.10 Reindexing a Series](#410-reindexing-a-series)
    * [Modifying a Series in-place](#modifying-a-series-in-place)
  * [4.11 Slicing a Series](#411-slicing-a-series)
  * [4.12 Summary](#412-summary)

<!-- tocstop -->



```python
# bring in NumPy and pandas
import numpy as np
import pandas as pd
```


```python
# Set some pandas options for controlling output display
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

## 4.1 The Series object

## 4.2 Importing pandas

## 4.3 Creating Series


```python
# create one item Series
s1 = pd.Series(2)
s1
```




    0    2
    dtype: int64




```python
# get value with label 0
s1[0]
```




    2




```python
# create a series of multiple items from a list
s2 = pd.Series([1, 2, 3, 4, 5])
s2
```




    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64




```python
# get the values in the Series
s2.values
```




    array([1, 2, 3, 4, 5], dtype=int64)




```python
# get the index of the Series
s2.index
```




    Int64Index([0, 1, 2, 3, 4], dtype='int64')




```python
# explicitly create an index
# index is alpha, not integer
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s3
```




    a    1
    b    2
    c    3
    dtype: int64




```python
s3.index
```




    Index(['a', 'b', 'c'], dtype='object')




```python
# lookup by label value, not integer position
s3['c']
```




    3




```python
# create Series from an existing index
# scalar value with be copied at each index label
s4 = pd.Series(2, index=s2.index)
s4
```




    0    2
    1    2
    2    2
    3    2
    4    2
    dtype: int64




```python
# generate a Series from 5 normal random numbers
np.random.seed(123456)
pd.Series(np.random.randn(5))
```




    0    0.469112
    1   -0.282863
    2   -1.509059
    3   -1.135632
    4    1.212112
    dtype: float64




```python
# 0 through 9
pd.Series(np.linspace(0, 9, 10))
```




    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    6    6
    7    7
    8    8
    9    9
    dtype: float64




```python
# 0 through 8
pd.Series(np.arange(0, 9))
```




    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    6    6
    7    7
    8    8
    dtype: int32




```python
# create Series from dict
s6 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
s6
```




    a    1
    b    2
    c    3
    d    4
    dtype: int64



## 4.4 Size, shape, uniqueness, and counts of values


```python
# example series, which also contains a NaN
s = pd.Series([0, 1, 1, 2, 3, 4, 5, 6, 7, np.nan])
s
```




    0     0
    1     1
    2     1
    3     2
    4     3
    5     4
    6     5
    7     6
    8     7
    9   NaN
    dtype: float64




```python
# length of the Series
len(s)
```




    10




```python
# .size is also the # of items in the Series
s.size
```




    10




```python
# .shape is a tuple with one value
s.shape
```




    (10,)




```python
# count() returns the number of non-NaN values
s.count()
```




    9




```python
# all unique values
s.unique()
```




    array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,  nan])




```python
# count of non-NaN values, returned max to min order
s.value_counts()
```




    1    2
    7    1
    6    1
    5    1
    4    1
    3    1
    2    1
    0    1
    dtype: int64



## 4.5 Peeking at data with heads, tails, and take


```python
# first five
s.head()
```




    0    0
    1    1
    2    1
    3    2
    4    3
    dtype: float64




```python
# first three
s.head(n = 3) # s.head(3) is equivalent
```




    0    0
    1    1
    2    1
    dtype: float64




```python
# last five
s.tail()
```




    5     4
    6     5
    7     6
    8     7
    9   NaN
    dtype: float64




```python
# last 3
s.tail(n = 3) # equivalent to s.tail(3)
```




    7     6
    8     7
    9   NaN
    dtype: float64




```python
# only take specific items
s.take([0, 3, 9])
```




    0     0
    3     2
    9   NaN
    dtype: float64



## 4.6 Looking up values in Series


```python
# single item lookup
s3['a']
```




    1




```python
# lookup by position since the index is not integer
s3[1]
```




    2




```python
# multiple items
s3[['a', 'c']]
```




    a    1
    c    3
    dtype: int64




```python
# series with integer index, but not starting with 0
s5 = pd.Series([1, 2, 3], index=[10, 11, 12])
s5
```




    10    1
    11    2
    12    3
    dtype: int64




```python
# by value as value passed and index are both integer
s5[11]
```




    2




```python
# force lookup by index label
s5.loc[12]
```




    3




```python
# forced lookup by location / position
s5.iloc[1]
```




    2




```python
# multiple items by label (loc)
s5.loc[[12, 10]]
```




    12    3
    10    1
    dtype: int64




```python
# multiple items by location / position (iloc)
s5.iloc[[0, 2]]
```




    10    1
    12    3
    dtype: int64




```python
# -1 and 15 will be NaN
s5.loc[[12, -1, 15]]
```




     12     3
    -1    NaN
     15   NaN
    dtype: float64




```python
# reminder of the contents of s3
s3
```




    a    1
    b    2
    c    3
    dtype: int64




```python
# label based lookup
s3.ix[['a', 'c']]
```




    a    1
    c    3
    dtype: int64




```python
# position based lookup
s3.ix[[1, 2]]
```




    b    2
    c    3
    dtype: int64




```python
# this looks up by label and not position
# note that 1,2 have NaN as those labels do not exist
# in the index
s5.ix[[1, 2, 10, 11]]
```




    1    NaN
    2    NaN
    10     1
    11     2
    dtype: float64



### Alignment via index labels


```python
s6 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s6
```




    a    1
    b    2
    c    3
    d    4
    dtype: int64




```python
s7 = pd.Series([4, 3, 2, 1], index=['d', 'c', 'b', 'a'])
s7
```




    d    4
    c    3
    b    2
    a    1
    dtype: int64




```python
# add them
s6 + s7
```




    a    2
    b    4
    c    6
    d    8
    dtype: int64




```python
# see how different from adding numpy arrays
a1 = np.array([1, 2, 3, 4])
a2 = np.array([4, 3, 2, 1])
a1 + a2
```




    array([5, 5, 5, 5])



## 4.7 Arithmetic operations


```python
# multiply all values in s3 by 2
s3 * 2
```




    a    2
    b    4
    c    6
    dtype: int64




```python
# scalar series using s3's index
t = pd.Series(2, s3.index)
s3 * t
```




    a    2
    b    4
    c    6
    dtype: int64




```python
# we will add this to s9
s8 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 5})
s8
```




    a    1
    b    2
    c    3
    d    5
    dtype: int64




```python
# going to add this to s8
s9 = pd.Series({'b': 6, 'c': 7, 'd': 9, 'e': 10})
s9
```




    b     6
    c     7
    d     9
    e    10
    dtype: int64




```python
# NaN's result for a and e
# demonstrates alignment
s8 + s9
```




    a   NaN
    b     8
    c    10
    d    14
    e   NaN
    dtype: float64




```python
# going to add this to s11
s10 = pd.Series([1.0, 2.0, 3.0], index=['a', 'a', 'b'])
s10
```




    a    1
    a    2
    b    3
    dtype: float64




```python
# going to add this to s10
s11 = pd.Series([4.0, 5.0, 6.0], index=['a', 'a', 'c'])
s11
```




    a    4
    a    5
    c    6
    dtype: float64




```python
# will result in four 'a' index labels
s10 + s11
```




    a     5
    a     6
    a     6
    a     7
    b   NaN
    c   NaN
    dtype: float64



## 4.8 The special case of Not-A-Number (NaN)


```python
# mean of numpy array values
nda = np.array([1, 2, 3, 4, 5])
nda.mean()
```




    3.0




```python
# mean of numpy array values with a NaN
nda = np.array([1, 2, 3, 4, np.NaN])
nda.mean()
```




    nan




```python
# ignores NaN's
s = pd.Series(nda)
s.mean()
```




    2.5




```python
# handle nan's like NumPy
s.mean(skipna=False)
```




    nan



## 4.9 Boolean selection


```python
# which rows have values that are > 5?
s = pd.Series(np.arange(0, 10))
s > 5
```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6     True
    7     True
    8     True
    9     True
    dtype: bool




```python
# select rows where values are > 5
logicalResults = s > 5
s[logicalResults]
```




    6    6
    7    7
    8    8
    9    9
    dtype: int32




```python
# a little shorter version
s[s > 5]
```




    6    6
    7    7
    8    8
    9    9
    dtype: int32




```python
# commented as it throws an exception
# s[s > 5 and s < 8]
```


```python
# correct syntax
s[(s > 5) & (s < 8)]
```




    6    6
    7    7
    dtype: int32




```python
# are all items >= 0?
(s >= 0).all()
```




    True




```python
# any items < 2?
s[s < 2].any()
```




    True




```python
# how many values < 2?
(s < 2).sum()
```




    2



## 4.10 Reindexing a Series


```python
# sample series of five items
s = pd.Series(np.random.randn(5))
s
```




    0   -0.173215
    1    0.119209
    2   -1.044236
    3   -0.861849
    4   -2.104569
    dtype: float64




```python
# change the index
s.index = ['a', 'b', 'c', 'd', 'e']
s
```




    a   -0.173215
    b    0.119209
    c   -1.044236
    d   -0.861849
    e   -2.104569
    dtype: float64




```python
# concat copies index values verbatim,
# potentially making duplicates
np.random.seed(123456)
s1 = pd.Series(np.random.randn(3))
s2 = pd.Series(np.random.randn(3))
combined = pd.concat([s1, s2])
combined
```




    0    0.469112
    1   -0.282863
    2   -1.509059
    0   -1.135632
    1    1.212112
    2   -0.173215
    dtype: float64




```python
# reset the index
combined.index = np.arange(0, len(combined))
combined
```




    0    0.469112
    1   -0.282863
    2   -1.509059
    3   -1.135632
    4    1.212112
    5   -0.173215
    dtype: float64




```python
np.random.seed(123456)
s1 = pd.Series(np.random.randn(4), ['a', 'b', 'c', 'd'])
# reindex with different number of labels
# results in dropped rows and/or NaN's
s2 = s1.reindex(['a', 'c', 'g'])
s2
```




    a    0.469112
    c   -1.509059
    g         NaN
    dtype: float64




```python
# s2 is a different Series than s1
s2['a'] = 0
s2
```




    a    0.000000
    c   -1.509059
    g         NaN
    dtype: float64




```python
# this did not modify s1
s1
```




    a    0.469112
    b   -0.282863
    c   -1.509059
    d   -1.135632
    dtype: float64




```python
# different types for the same values of labels
# causes big trouble
s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([3, 4, 5], index=['0', '1', '2'])
s1 + s2
```




    0   NaN
    1   NaN
    2   NaN
    0   NaN
    1   NaN
    2   NaN
    dtype: float64




```python
# reindex by casting the label types
# and we will get the desired result
s2.index = s2.index.values.astype(int)
s1 + s2
```




    0    3
    1    5
    2    7
    dtype: int64




```python
# fill with 0 instead of NaN
s2 = s.copy()
s2.reindex(['a', 'f'], fill_value=0)
```




    a   -0.173215
    f    0.000000
    dtype: float64




```python
# create example to demonstrate fills
s3 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
s3
```




    0      red
    3    green
    5     blue
    dtype: object




```python
# forward fill example
s3.reindex(np.arange(0,7), method='ffill')
```




    0      red
    1      red
    2      red
    3    green
    4    green
    5     blue
    6     blue
    dtype: object




```python
# backwards fill example
s3.reindex(np.arange(0,7), method='bfill')
```




    0      red
    1    green
    2    green
    3    green
    4     blue
    5     blue
    6      NaN
    dtype: object



### Modifying a Series in-place


```python
# generate a Series to play with
np.random.seed(123456)
s = pd.Series(np.random.randn(3), index=['a', 'b', 'c'])
s
```




    a    0.469112
    b   -0.282863
    c   -1.509059
    dtype: float64




```python
# change a value in the Series
# this is done in-place
# a new Series is not returned that has a modified value
s['d'] = 100
s
```




    a      0.469112
    b     -0.282863
    c     -1.509059
    d    100.000000
    dtype: float64




```python
# modify the value at 'd' in-place
s['d'] = -100
s
```




    a      0.469112
    b     -0.282863
    c     -1.509059
    d   -100.000000
    dtype: float64




```python
# remove a row / item
del(s['a'])
s
```




    b     -0.282863
    c     -1.509059
    d   -100.000000
    dtype: float64



## 4.11 Slicing a Series


```python
# a Series to use for slicing
# using index labels not starting at 0 to demonstrate
# position based slicing
s = pd.Series(np.arange(100, 110), index=np.arange(10, 20))
s
```




    10    100
    11    101
    12    102
    13    103
    14    104
    15    105
    16    106
    17    107
    18    108
    19    109
    dtype: int32




```python
# items at position 0, 2, 4
s[0:6:2]
```




    10    100
    12    102
    14    104
    dtype: int32




```python
# equivalent to
s.iloc[[0, 2, 4]]
```




    10    100
    12    102
    14    104
    dtype: int32




```python
# first five by slicing, same as .head(5)
s[:5]
```




    10    100
    11    101
    12    102
    13    103
    14    104
    dtype: int32




```python
# fourth position to the end
s[4:]
```




    14    104
    15    105
    16    106
    17    107
    18    108
    19    109
    dtype: int32




```python
# every other item in the first five positions
s[:5:2]
```




    10    100
    12    102
    14    104
    dtype: int32




```python
# every other item starting at the fourth position
s[4::2]
```




    14    104
    16    106
    18    108
    dtype: int32




```python
# reverse the Series
s[::-1]
```




    19    109
    18    108
    17    107
    16    106
    15    105
    14    104
    13    103
    12    102
    11    101
    10    100
    dtype: int32




```python
# every other starting at position 4, in reverse
s[4::-2]
```




    14    104
    12    102
    10    100
    dtype: int32




```python
# :-2, which means positions 0 through (10-2) [8]
s[:-2]
```




    10    100
    11    101
    12    102
    13    103
    14    104
    15    105
    16    106
    17    107
    dtype: int32




```python
# last three items of the series
s[-3:]
```




    17    107
    18    108
    19    109
    dtype: int32




```python
# equivalent to s.tail(4).head(3)
s[-4:-1]
```




    16    106
    17    107
    18    108
    dtype: int32




```python
copy = s.copy() # preserve s
slice = copy[:2] # slice with first two rows
slice
```




    10    100
    11    101
    dtype: int32




```python
# change item with label 10 to 1000
slice[11] = 1000
# and see it in the source
copy
```




    10     100
    11    1000
    12     102
    13     103
    14     104
    15     105
    16     106
    17     107
    18     108
    19     109
    dtype: int32




```python
# used to demonstrate the next two slices
s = pd.Series(np.arange(0, 5),
              index=['a', 'b', 'c', 'd', 'e'])
s
```




    a    0
    b    1
    c    2
    d    3
    e    4
    dtype: int32




```python
# slices by position as the index is characters
s[1:3]
```




    b    1
    c    2
    dtype: int32




```python
# this slices by the strings in the index
s['b':'d']
```




    b    1
    c    2
    d    3
    dtype: int32



## 4.12 Summary


```python

```
