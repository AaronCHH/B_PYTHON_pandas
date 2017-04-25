
# Chapter 7: Tidying Up Your Data
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 7: Tidying Up Your Data](#chapter-7-tidying-up-your-data)
  * [7.1 What is tidying your data](#71-what-is-tidying-your-data)
  * [7.2 Setting up the IPython notebook](#72-setting-up-the-ipython-notebook)
  * [7.3 Working with missing data](#73-working-with-missing-data)
    * [Determining NaN values in Series and DataFrame objects](#determining-nan-values-in-series-and-dataframe-objects)
    * [Selecting out or dropping missing data](#selecting-out-or-dropping-missing-data)
    * [How pandas handles NaN values in mathematical operations](#how-pandas-handles-nan-values-in-mathematical-operations)
    * [Filling in missing data](#filling-in-missing-data)
    * [Forward and backward filling of missing values](#forward-and-backward-filling-of-missing-values)
    * [Filling using index labels](#filling-using-index-labels)
    * [Interpolation of missing values](#interpolation-of-missing-values)
  * [7.4 Handling duplicate data](#74-handling-duplicate-data)
  * [7.5 Transforming Data](#75-transforming-data)
    * [Mapping](#mapping)
    * [Replacing values](#replacing-values)
    * [Applying functions to transform data](#applying-functions-to-transform-data)
  * [7.6 Summary](#76-summary)

<!-- tocstop -->


## 7.1 What is tidying your data

## 7.2 Setting up the IPython notebook


```python
# import pandas, numpy and datetime
import numpy as np
import pandas as pd
import datetime

# Set some pandas options for controlling output
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

## 7.3 Working with missing data


```python
# create a DataFrame with 5 rows and 3 columns
df = pd.DataFrame(np.arange(0, 15).reshape(5, 3),
               index=['a', 'b', 'c', 'd', 'e'],
               columns=['c1', 'c2', 'c3'])
df
```




       c1  c2  c3
    a   0   1   2
    b   3   4   5
    c   6   7   8
    d   9  10  11
    e  12  13  14




```python
# add some columns and rows to the DataFrame
# column c4 with NaN values
df['c4'] = np.nan
# row 'f' with 15 through 18
df.loc['f'] = np.arange(15, 19)
# row 'g' will all NaN
df.loc['g'] = np.nan
# column 'C5' with NaN's
df['c5'] = np.nan
# change value in col 'c4' row 'a'
df['c4']['a'] = 20
df
```




       c1  c2  c3  c4  c5
    a   0   1   2  20 NaN
    b   3   4   5 NaN NaN
    c   6   7   8 NaN NaN
    d   9  10  11 NaN NaN
    e  12  13  14 NaN NaN
    f  15  16  17  18 NaN
    g NaN NaN NaN NaN NaN



### Determining NaN values in Series and DataFrame objects


```python
# which items are NaN?
df.isnull()
```




          c1     c2     c3     c4    c5
    a  False  False  False  False  True
    b  False  False  False   True  True
    c  False  False  False   True  True
    d  False  False  False   True  True
    e  False  False  False   True  True
    f  False  False  False  False  True
    g   True   True   True   True  True




```python
# count the number of NaN's in each column
df.isnull().sum()
```




    c1    1
    c2    1
    c3    1
    c4    5
    c5    7
    dtype: int64




```python
# total count of NaN values
df.isnull().sum().sum()
```




    15




```python
# number of non-NaN values in each column
df.count()
```




    c1    6
    c2    6
    c3    6
    c4    2
    c5    0
    dtype: int64




```python
# and this counts the number of NaN's too
(len(df) - df.count()).sum()
```




    15




```python
# which items are not null?
df.notnull()
```




          c1     c2     c3     c4     c5
    a   True   True   True   True  False
    b   True   True   True  False  False
    c   True   True   True  False  False
    d   True   True   True  False  False
    e   True   True   True  False  False
    f   True   True   True   True  False
    g  False  False  False  False  False



### Selecting out or dropping missing data


```python
# select the non-NaN items in column c4
df.c4[df.c4.notnull()]
```




    a    20
    f    18
    Name: c4, dtype: float64




```python
# .dropna will also return non NaN values
# this gets all non NaN items in column c4
df.c4.dropna()
```




    a    20
    f    18
    Name: c4, dtype: float64




```python
# dropna returns a copy with the values dropped
# the source DataFrame / column is not changed
df.c4
```




    a    20
    b   NaN
    c   NaN
    d   NaN
    e   NaN
    f    18
    g   NaN
    Name: c4, dtype: float64




```python
# on a DataFrame this will drop entire rows
# where there is at least one NaN
# in this case, that is all rows
df.dropna()
```




    Empty DataFrame
    Columns: [c1, c2, c3, c4, c5]
    Index: []




```python
# using how='all', only rows that have all values
# as NaN will be dropped
df.dropna(how = 'all')
```




       c1  c2  c3  c4  c5
    a   0   1   2  20 NaN
    b   3   4   5 NaN NaN
    c   6   7   8 NaN NaN
    d   9  10  11 NaN NaN
    e  12  13  14 NaN NaN
    f  15  16  17  18 NaN




```python
# flip to drop columns instead of rows
df.dropna(how='all', axis=1) # say goodbye to c5
```




       c1  c2  c3  c4
    a   0   1   2  20
    b   3   4   5 NaN
    c   6   7   8 NaN
    d   9  10  11 NaN
    e  12  13  14 NaN
    f  15  16  17  18
    g NaN NaN NaN NaN




```python
# make a copy of df
df2 = df.copy()

# replace two NaN cells with values
df2.ix['g'].c1 = 0
df2.ix['g'].c3 = 0

df2
```




       c1  c2  c3  c4  c5
    a   0   1   2  20 NaN
    b   3   4   5 NaN NaN
    c   6   7   8 NaN NaN
    d   9  10  11 NaN NaN
    e  12  13  14 NaN NaN
    f  15  16  17  18 NaN
    g   0 NaN   0 NaN NaN




```python
# now drop columns with any NaN values
df2.dropna(how='any', axis=1)
```




       c1  c3
    a   0   2
    b   3   5
    c   6   8
    d   9  11
    e  12  14
    f  15  17
    g   0   0




```python
# only drop columns with at least 5 NaN values
df.dropna(thresh=5, axis=1)
```




       c1  c2  c3
    a   0   1   2
    b   3   4   5
    c   6   7   8
    d   9  10  11
    e  12  13  14
    f  15  16  17
    g NaN NaN NaN



### How pandas handles NaN values in mathematical operations


```python
# create a NumPy array with one NaN value
a = np.array([1, 2, np.nan, 3])
# create a Series from the array
s = pd.Series(a)
# the mean of each is different
a.mean(), s.mean()
```




    (nan, 2.0)




```python
# demonstrate sum, mean and cumsum handling of NaN
# get one column
s = df.c4
s.sum(), # NaN's treated as 0
```




    (38.0,)




```python
s.mean() # NaN also treated as 0
```




    19.0




```python
# as 0 in the cumsum, but NaN's preserved in result Series
s.cumsum()
```




    a    20
    b   NaN
    c   NaN
    d   NaN
    e   NaN
    f    38
    g   NaN
    Name: c4, dtype: float64




```python
# in arithmetic, a NaN value will result in NaN
df.c4 + 1
```




    a    21
    b   NaN
    c   NaN
    d   NaN
    e   NaN
    f    19
    g   NaN
    Name: c4, dtype: float64



### Filling in missing data


```python
# return a new DataFrame with NaN's filled with 0
filled = df.fillna(0)
filled
```




       c1  c2  c3  c4  c5
    a   0   1   2  20   0
    b   3   4   5   0   0
    c   6   7   8   0   0
    d   9  10  11   0   0
    e  12  13  14   0   0
    f  15  16  17  18   0
    g   0   0   0   0   0




```python
# NaN's don't count as an item in calculating
# the means
df.mean()
```




    c1     7.5
    c2     8.5
    c3     9.5
    c4    19.0
    c5     NaN
    dtype: float64




```python
# having replaced NaN with 0 can make
# operations such as mean have different results
filled.mean()
```




    c1    6.428571
    c2    7.285714
    c3    8.142857
    c4    5.428571
    c5    0.000000
    dtype: float64




```python
# only fills the first two NaN's in each row with 0
df.fillna(0, limit=2)
```




       c1  c2  c3  c4  c5
    a   0   1   2  20   0
    b   3   4   5   0   0
    c   6   7   8   0 NaN
    d   9  10  11 NaN NaN
    e  12  13  14 NaN NaN
    f  15  16  17  18 NaN
    g   0   0   0 NaN NaN



### Forward and backward filling of missing values


```python
# extract the c4 column and fill NaNs forward
df.c4.fillna(method="ffill")
```




    a    20
    b    20
    c    20
    d    20
    e    20
    f    18
    g    18
    Name: c4, dtype: float64




```python
# perform a backwards fill
df.c4.fillna(method="bfill")
```




    a    20
    b    18
    c    18
    d    18
    e    18
    f    18
    g   NaN
    Name: c4, dtype: float64



### Filling using index labels


```python
# create a new Series of values to be
# used to fill NaN's where index label matches
fill_values = pd.Series([100, 101, 102], index=['a', 'e', 'g'])
fill_values
```




    a    100
    e    101
    g    102
    dtype: int64




```python
# using c4, fill using fill_values
# a, e and g will be filled with matching values
df.c4.fillna(fill_values)
```




    a     20
    b    NaN
    c    NaN
    d    NaN
    e    101
    f     18
    g    102
    Name: c4, dtype: float64




```python
# fill NaN values in each column with the
# mean of the values in that column
df.fillna(df.mean())
```




         c1    c2    c3  c4  c5
    a   0.0   1.0   2.0  20 NaN
    b   3.0   4.0   5.0  19 NaN
    c   6.0   7.0   8.0  19 NaN
    d   9.0  10.0  11.0  19 NaN
    e  12.0  13.0  14.0  19 NaN
    f  15.0  16.0  17.0  18 NaN
    g   7.5   8.5   9.5  19 NaN



### Interpolation of missing values


```python
# linear interpolate the NaN values from 1 through 2
s = pd.Series([1, np.nan, np.nan, np.nan, 2])
s.interpolate()
```




    0    1.00
    1    1.25
    2    1.50
    3    1.75
    4    2.00
    dtype: float64




```python
# create a time series, but missing one date in the Series
ts = pd.Series([1, np.nan, 2],
            index=[datetime.datetime(2014, 1, 1),
                   datetime.datetime(2014, 2, 1),
                   datetime.datetime(2014, 4, 1)])
ts
```




    2014-01-01     1
    2014-02-01   NaN
    2014-04-01     2
    dtype: float64




```python
# linear interpolate based on number of items in the Series
ts.interpolate()
```




    2014-01-01    1.0
    2014-02-01    1.5
    2014-04-01    2.0
    dtype: float64




```python
# this accounts for the fact that we don't have
# an entry for 2014-03-01
ts.interpolate(method="time")
```




    2014-01-01    1.000000
    2014-02-01    1.344444
    2014-04-01    2.000000
    dtype: float64




```python
# a Series to demonstrate index label based interpolation
s = pd.Series([0, np.nan, 100], index=[0, 1, 10])
s
```




    0       0
    1     NaN
    10    100
    dtype: float64




```python
# linear interpolate
s.interpolate()
```




    0       0
    1      50
    10    100
    dtype: float64




```python
# interpolate based upon the values in the index
s.interpolate(method="values")
```




    0       0
    1      10
    10    100
    dtype: float64



## 7.4 Handling duplicate data


```python
# a DataFrame with lots of duplicate data
data = pd.DataFrame({'a': ['x'] * 3 + ['y'] * 4,
                     'b': [1, 1, 2, 3, 3, 4, 4]})
data
```




       a  b
    0  x  1
    1  x  1
    2  x  2
    3  y  3
    4  y  3
    5  y  4
    6  y  4




```python
# reports which rows are duplicates based upon
# if the data in all columns was seen before
data.duplicated()
```




    0    False
    1     True
    2    False
    3    False
    4     True
    5    False
    6     True
    dtype: bool




```python
# drop duplicate rows retaining first row of the duplicates
data.drop_duplicates()
```




       a  b
    0  x  1
    2  x  2
    3  y  3
    5  y  4




```python
# drop duplicate rows, only keeping the first
# instance of any data
data.drop_duplicates(take_last=True)
```




       a  b
    1  x  1
    2  x  2
    4  y  3
    6  y  4




```python
# add a column c with values 0..6
# this makes .duplicated() report no duplicate rows
data['c'] = range(7)
data.duplicated()
```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6    False
    dtype: bool




```python
# but if we specify duplicates to be dropped only in columns a & b
# they will be dropped
data.drop_duplicates(['a', 'b'])
```




       a  b  c
    0  x  1  0
    2  x  2  2
    3  y  3  3
    5  y  4  5



## 7.5 Transforming Data

### Mapping


```python
# create two Series objects to demonstrate mapping
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b", 3: "c"})
x
```




    one      1
    three    3
    two      2
    dtype: int64




```python
y
```




    1    a
    2    b
    3    c
    dtype: object




```python
# map values in x to values in y
x.map(y)
```




    one      a
    three    c
    two      b
    dtype: object




```python
# three in x will not align / map to a value in y
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b"})
x.map(y)
```




    one        a
    three    NaN
    two        b
    dtype: object



### Replacing values


```python
# create a Series to demonstrate replace
s = pd.Series([0., 1., 2., 3., 2., 4.])
s
```




    0    0
    1    1
    2    2
    3    3
    4    2
    5    4
    dtype: float64




```python
# replace all items with index label 2 with value 5
s.replace(2, 5)
```




    0    0
    1    1
    2    5
    3    3
    4    5
    5    4
    dtype: float64




```python
# replace all items with new values
s.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
```




    0    4
    1    3
    2    2
    3    1
    4    2
    5    0
    dtype: float64




```python
# replace using entries in a dictionary
s.replace({0: 10, 1: 100})
```




    0     10
    1    100
    2      2
    3      3
    4      2
    5      4
    dtype: float64




```python
# DataFrame with two columns
df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})
df
```




       a  b
    0  0  5
    1  1  6
    2  2  7
    3  3  8
    4  4  9




```python
# specify different replacement values for each column
df.replace({'a': 1, 'b': 8}, 100)
```




         a    b
    0    0    5
    1  100    6
    2    2    7
    3    3  100
    4    4    9




```python
# demonstrate replacement with pad method
# set first item to 10, to have a distinct replacement value
s[0] = 10
s
```




    0    10
    1     1
    2     2
    3     3
    4     2
    5     4
    dtype: float64




```python
# replace items with index label 1, 2, 3, using fill from the
# most recent value prior to the specified labels (10)
s.replace([1, 2, 3], method='pad')
```




    0    10
    1    10
    2    10
    3    10
    4    10
    5     4
    dtype: float64



### Applying functions to transform data


```python
# demonstrate applying a function to every item of a Series
s = pd.Series(np.arange(0, 5))
s.apply(lambda v: v * 2)
```




    0    0
    1    2
    2    4
    3    6
    4    8
    dtype: int64




```python
# demonstrate applying a sum on each column
df = pd.DataFrame(np.arange(12).reshape(4, 3),
                  columns=['a', 'b', 'c'])
df
```




       a   b   c
    0  0   1   2
    1  3   4   5
    2  6   7   8
    3  9  10  11




```python
# calculate cumulative sum of items in each column
df.apply(lambda col: col.sum())
```




    a    18
    b    22
    c    26
    dtype: int64




```python
# calculate sum of items in each row
df.apply(lambda row: row.sum(), axis=1)
```




    0     3
    1    12
    2    21
    3    30
    dtype: int64




```python
# create a new column 'interim' with a * b
df['interim'] = df.apply(lambda r: r.a * r.b, axis=1)
df
```




       a   b   c  interim
    0  0   1   2        0
    1  3   4   5       12
    2  6   7   8       42
    3  9  10  11       90




```python
# and now a 'result' column with 'interim' + 'c'
df['result'] = df.apply(lambda r: r.interim + r.c, axis=1)
df
```




       a   b   c  interim  result
    0  0   1   2        0       2
    1  3   4   5       12      17
    2  6   7   8       42      50
    3  9  10  11       90     101




```python
# replace column a with the sum of columns a, b and c
df.a = df.a + df.b + df.c
df
```




        a   b   c  interim  result
    0   3   1   2        0       2
    1  12   4   5       12      17
    2  21   7   8       42      50
    3  30  10  11       90     101




```python
# create a 3x5 DataFrame
# only second row has a NaN
df = pd.DataFrame(np.arange(0, 15).reshape(3,5))
df.loc[1, 2] = np.nan
df
```




        0   1   2   3   4
    0   0   1   2   3   4
    1   5   6 NaN   8   9
    2  10  11  12  13  14




```python
# demonstrate applying a function to only rows having
# a count of 0 NaN values
df.dropna().apply(lambda x: x.sum(), axis=1)
```




    0    10
    2    60
    dtype: float64




```python
# use applymap to format all items of the DataFrame
df.applymap(lambda x: '%.2f' % x)
```




           0      1      2      3      4
    0   0.00   1.00   2.00   3.00   4.00
    1   5.00   6.00    nan   8.00   9.00
    2  10.00  11.00  12.00  13.00  14.00



## 7.6 Summary
