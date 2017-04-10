
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Setting up the notebook](#setting-up-the-notebook)
- [Concatenating data](#concatenating-data)
- [Merging and Joining Data](#merging-and-joining-data)
	- [Overview of merges](#overview-of-merges)
	- [Specifying the join semantics of a merge operation](#specifying-the-join-semantics-of-a-merge-operation)
- [Pivoting](#pivoting)
- [Stacking and Unstacking](#stacking-and-unstacking)
	- [Stacking using non-hierarchical indexes](#stacking-using-non-hierarchical-indexes)
	- [Unstacking using hierarchical indexes](#unstacking-using-hierarchical-indexes)
- [Melting](#melting)
- [A note on the performance benefits of stacked data](#a-note-on-the-performance-benefits-of-stacked-data)

<!-- tocstop -->


# Setting up the notebook
{python}

```
# import pandas, numpy and datetime
import numpy as np
import pandas as pd
import datetime

# Set some pandas options for controlling output
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

# Concatenating data


```{python}
# two Series objects to concatenate
s1 = pd.Series(np.arange(0, 3))
s2 = pd.Series(np.arange(5, 8))
s1
```




    0    0
    1    1
    2    2
    dtype: int64




```{python}
s2
```




    0    5
    1    6
    2    7
    dtype: int64




```{python}
# concatenate them
pd.concat([s1, s2])
```




    0    0
    1    1
    2    2
    0    5
    1    6
    2    7
    dtype: int64




```{python}
# create two DataFrame objects to concatenate
# using the same index labels and column names,
# but different values
df1 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=['a', 'b', 'c'])
#df2 has 9 .. 18
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3),
                   columns=['a', 'b', 'c'])
df1
```




       a  b  c
    0  0  1  2
    1  3  4  5
    2  6  7  8




```{python}
df2
```




        a   b   c
    0   9  10  11
    1  12  13  14
    2  15  16  17




```{python}
# do the concat
pd.concat([df1, df2])
```




        a   b   c
    0   0   1   2
    1   3   4   5
    2   6   7   8
    0   9  10  11
    1  12  13  14
    2  15  16  17




```{python}
# demonstrate concatenating two DataFrame objects with
# different columns
df1 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=['a', 'b', 'c'])
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3),
                   columns=['a', 'c', 'd'])
df1
```




       a  b  c
    0  0  1  2
    1  3  4  5
    2  6  7  8




```{python}
df2
```




        a   c   d
    0   9  10  11
    1  12  13  14
    2  15  16  17




```{python}
# do the concat, NaN's will be filled in for
# the d column for df1 and b column for df2
pd.concat([df1, df2])
```




        a   b   c   d
    0   0   1   2 NaN
    1   3   4   5 NaN
    2   6   7   8 NaN
    0   9 NaN  10  11
    1  12 NaN  13  14
    2  15 NaN  16  17




```{python}
# concat the two objects, but create an index using the
# given keys
c = pd.concat([df1, df2], keys=['df1', 'df2'])
# note in the labeling of the rows in the output
c
```




            a   b   c   d
    df1 0   0   1   2 NaN
        1   3   4   5 NaN
        2   6   7   8 NaN
    df2 0   9 NaN  10  11
        1  12 NaN  13  14
        2  15 NaN  16  17




```{python}
# we can extract the data originating from
# the first or second source DataFrame
c.ix['df2']
```




        a   b   c   d
    0   9 NaN  10  11
    1  12 NaN  13  14
    2  15 NaN  16  17




```{python}
# concat df1 and df2 along columns
# aligns on row labels, has duplicate columns
pd.concat([df1, df2], axis=1)
```




       a  b  c   a   c   d
    0  0  1  2   9  10  11
    1  3  4  5  12  13  14
    2  6  7  8  15  16  17




```{python}
# a new DataFrame to merge with df1
# this has two common row labels (2, 3)
# common columns (a) and one disjoint column
# in each (b in df1 and d in df2)
df3 = pd.DataFrame(np.arange(20, 26).reshape(3, 2),
                   columns=['a', 'd'],
                   index=[2, 3, 4])
df3
```




        a   d
    2  20  21
    3  22  23
    4  24  25




```{python}
# concat them. Alignment is along row labels
# columns first from df1 and then df3, with duplicates.
# NaN filled in where those columns do not exist in the source
pd.concat([df1, df3], axis=1)
```




        a   b   c   a   d
    0   0   1   2 NaN NaN
    1   3   4   5 NaN NaN
    2   6   7   8  20  21
    3 NaN NaN NaN  22  23
    4 NaN NaN NaN  24  25




```{python}
# do an inner join instead of outer
# results in one row
pd.concat([df1, df3], axis=1, join='inner')
```




       a  b  c   a   d
    2  6  7  8  20  21




```{python}
# add keys to the columns
df = pd.concat([df1, df2],
               axis=1,
               keys=['df1', 'df2'])
df
```




      df1       df2        
        a  b  c   a   c   d
    0   0  1  2   9  10  11
    1   3  4  5  12  13  14
    2   6  7  8  15  16  17




```{python}
# retrieve the data that originated from the
# DataFrame with key 'df2'
df.ix[:, 'df2']
```




        a   c   d
    0   9  10  11
    1  12  13  14
    2  15  16  17




```{python}
# append does a concatenate along axis=0
# duplicate row index labels can result
df1.append(df2)
```




        a   b   c   d
    0   0   1   2 NaN
    1   3   4   5 NaN
    2   6   7   8 NaN
    0   9 NaN  10  11
    1  12 NaN  13  14
    2  15 NaN  16  17




```{python}
# remove duplicates in the result index by ignoring the
# index labels in the source DataFrame objects
df1.append(df2, ignore_index=True)
```




        a   b   c   d
    0   0   1   2 NaN
    1   3   4   5 NaN
    2   6   7   8 NaN
    3   9 NaN  10  11
    4  12 NaN  13  14
    5  15 NaN  16  17



# Merging and Joining Data

## Overview of merges


```{python}
# these are our customers
customers = {'CustomerID': [10, 11],
             'Name': ['Mike', 'Marcia'],
             'Address': ['Address for Mike',
                         'Address for Marcia']}
customers = pd.DataFrame(customers)
customers
```




                  Address  CustomerID    Name
    0    Address for Mike          10    Mike
    1  Address for Marcia          11  Marcia




```{python}
# and these are the orders made by our customers
# they are related to customers by CustomerID
orders = {'CustomerID': [10, 11, 10],
          'OrderDate': [datetime.date(2014, 12, 1),
                        datetime.date(2014, 12, 1),
                        datetime.date(2014, 12, 1)]}
orders = pd.DataFrame(orders)
orders
```




       CustomerID   OrderDate
    0          10  2014-12-01
    1          11  2014-12-01
    2          10  2014-12-01




```{python}
# merge customers and orders so we can ship the items
customers.merge(orders)
```




                  Address  CustomerID    Name   OrderDate
    0    Address for Mike          10    Mike  2014-12-01
    1    Address for Mike          10    Mike  2014-12-01
    2  Address for Marcia          11  Marcia  2014-12-01




```{python}
# data to be used in the remainder of this section's examples
left_data = {'key1': ['a', 'b', 'c'],
            'key2': ['x', 'y', 'z'],
            'lval1': [ 0, 1, 2]}
right_data = {'key1': ['a', 'b', 'c'],
              'key2': ['x', 'a', 'z'],
              'rval1': [ 6, 7, 8 ]}
left = pd.DataFrame(left_data, index=[0, 1, 2])
right = pd.DataFrame(right_data, index=[1, 2, 3])
left
```




      key1 key2  lval1
    0    a    x      0
    1    b    y      1
    2    c    z      2




```{python}
right
```




      key1 key2  rval1
    1    a    x      6
    2    b    a      7
    3    c    z      8




```{python}
# demonstrate merge without specifying columns to merge
# this will implicitly merge on all common columns
left.merge(right)
```




      key1 key2  lval1  rval1
    0    a    x      0      6
    1    c    z      2      8




```{python}
# demonstrate merge using an explicit column
# on needs the value to be in both DataFrame objects
left.merge(right, on='key1')
```




      key1 key2_x  lval1 key2_y  rval1
    0    a      x      0      x      6
    1    b      y      1      a      7
    2    c      z      2      z      8




```{python}
# merge explicitly using two columns
left.merge(right, on=['key1', 'key2'])
```




      key1 key2  lval1  rval1
    0    a    x      0      6
    1    c    z      2      8




```{python}
# join on the row indices of both matrices
pd.merge(left, right, left_index=True, right_index=True)
```




      key1_x key2_x  lval1 key1_y key2_y  rval1
    1      b      y      1      a      x      6
    2      c      z      2      b      a      7



## Specifying the join semantics of a merge operation


```{python}
# outer join, merges all matched data,
# and fills unmatched items with NaN
left.merge(right, how='outer')
```




      key1 key2  lval1  rval1
    0    a    x      0      6
    1    b    y      1    NaN
    2    c    z      2      8
    3    b    a    NaN      7




```{python}
# left join, merges all matched data, and only fills unmatched
# items from the left dataframe with NaN filled for the
# unmatched items in the result
# rows with labels 0 and 2
# match on key1 and key2 the row with label 1 is from left

left.merge(right, how='left')
```




      key1 key2  lval1  rval1
    0    a    x      0      6
    1    b    y      1    NaN
    2    c    z      2      8




```{python}
# right join, merges all matched data, and only fills unmatched
# item from the right with NaN filled for the unmatched items
# in the result
# rows with labels 0 and 2 match on key1 and key2
# the row with label 1 is from right
left.merge(right, how='right')
```




      key1 key2  lval1  rval1
    0    a    x      0      6
    1    c    z      2      8
    2    b    a    NaN      7




```{python}
# join left with right (default method is outer)
# and since these DataFrame objects have duplicate column names
# we just specify lsuffix and rsuffix
left.join(right, lsuffix='_left', rsuffix='_right')
```




      key1_left key2_left  lval1 key1_right key2_right  rval1
    0         a         x      0        NaN        NaN    NaN
    1         b         y      1          a          x      6
    2         c         z      2          b          a      7




```{python}
# join left with right with an inner join
left.join(right, lsuffix='_left', rsuffix='_right', how='inner')
```




      key1_left key2_left  lval1 key1_right key2_right  rval1
    1         b         y      1          a          x      6
    2         c         z      2          b          a      7



# Pivoting


```{python}
# read in accellerometer data
sensor_readings = pd.read_csv("data/accel.csv")
sensor_readings
```




        interval axis  reading
    0          0    X      0.0
    1          0    Y      0.5
    2          0    Z      1.0
    3          1    X      0.1
    4          1    Y      0.4
    ..       ...  ...      ...
    7          2    Y      0.3
    8          2    Z      0.8
    9          3    X      0.3
    10         3    Y      0.2
    11         3    Z      0.7

    [12 rows x 3 columns]




```{python}
# extract X-axis readings
sensor_readings[sensor_readings['axis'] == 'X']
```




       interval axis  reading
    0         0    X      0.0
    3         1    X      0.1
    6         2    X      0.2
    9         3    X      0.3




```{python}
# pivot the data.  Interval becomes the index, the columns are
# the current axes values, and use the readings as values
sensor_readings.pivot(index='interval',
                     columns='axis',
                     values='reading')
```




    axis        X    Y    Z
    interval               
    0         0.0  0.5  1.0
    1         0.1  0.4  0.9
    2         0.2  0.3  0.8
    3         0.3  0.2  0.7



# Stacking and Unstacking

## Stacking using non-hierarchical indexes


```{python}
# simple DataFrame with one column
df = pd.DataFrame({'a': [1, 2]}, index={'one', 'two'})
df
```




         a
    two  1
    one  2




```{python}
# push the column to another level of the index
# the result is a Series where values are looked up through
# a multi-index
stacked1 = df.stack()
stacked1
```




    two  a    1
    one  a    2
    dtype: int64




```{python}
# lookup one / a using just the index via a tuple
stacked1[('one', 'a')]
```




    2




```{python}
# DataFrame with two columns
df = pd.DataFrame({'a': [1, 2],
                   'b': [3, 4]},
                  index={'one', 'two'})
df
```




         a  b
    two  1  3
    one  2  4




```{python}
# push the two columns into a single level of the index
stacked2 = df.stack()
stacked2
```




    two  a    1
         b    3
    one  a    2
         b    4
    dtype: int64




```{python}
# lookup value with index of one / b
stacked2[('one', 'b')]
```




    4



## Unstacking using hierarchical indexes


```{python}
# make two copies of the sensor data, one for each user
user1 = sensor_readings.copy()
user2 = sensor_readings.copy()
# add names to the two copies
user1['who'] = 'Mike'
user2['who'] = 'Mikael'
# for demonstration, lets scale user2's readings
user2['reading'] *= 100
# and reorganize this to have a hierarchical row index
multi_user_sensor_data = pd.concat([user1, user2]) \
            .set_index(['who', 'interval', 'axis'])
multi_user_sensor_data
```




                          reading
    who    interval axis         
    Mike   0        X         0.0
                    Y         0.5
                    Z         1.0
           1        X         0.1
                    Y         0.4
    ...                       ...
    Mikael 2        Y        30.0
                    Z        80.0
           3        X        30.0
                    Y        20.0
                    Z        70.0

    [24 rows x 1 columns]




```{python}
# lookup user data for Mike using just the index
multi_user_sensor_data.ix['Mike']
```




                   reading
    interval axis         
    0        X         0.0
             Y         0.5
             Z         1.0
    1        X         0.1
             Y         0.4
    ...                ...
    2        Y         0.3
             Z         0.8
    3        X         0.3
             Y         0.2
             Z         0.7

    [12 rows x 1 columns]




```{python}
# readings for all users and axes at interval 1
multi_user_sensor_data.xs(1, level='interval')
```




                 reading
    who    axis         
    Mike   X         0.1
           Y         0.4
           Z         0.9
    Mikael X        10.0
           Y        40.0
           Z        90.0




```{python}
# unstack the who level
multi_user_sensor_data.unstack()
```




                    reading             
    axis                  X     Y      Z
    who    interval                     
    Mikael 0            0.0  50.0  100.0
           1           10.0  40.0   90.0
           2           20.0  30.0   80.0
           3           30.0  20.0   70.0
    Mike   0            0.0   0.5    1.0
           1            0.1   0.4    0.9
           2            0.2   0.3    0.8
           3            0.3   0.2    0.7




```{python}
# unstack at level=0
multi_user_sensor_data.unstack(level=0)
```




                  reading     
    who            Mikael Mike
    interval axis             
    0        X          0  0.0
             Y         50  0.5
             Z        100  1.0
    1        X         10  0.1
             Y         40  0.4
    ...               ...  ...
    2        Y         30  0.3
             Z         80  0.8
    3        X         30  0.3
             Y         20  0.2
             Z         70  0.7

    [12 rows x 2 columns]




```{python}
# unstack who and axis levels
unstacked = multi_user_sensor_data.unstack(['who', 'axis'])
unstacked
```




             reading                          
    who         Mike           Mikael         
    axis           X    Y    Z      X   Y    Z
    interval                                  
    0            0.0  0.5  1.0      0  50  100
    1            0.1  0.4  0.9     10  40   90
    2            0.2  0.3  0.8     20  30   80
    3            0.3  0.2  0.7     30  20   70




```{python}
# and we can of course stack what we have unstacked
# this re-stacks who
unstacked.stack(level='who')
```




                    reading             
    axis                  X     Y      Z
    interval who                        
    0        Mikael     0.0  50.0  100.0
             Mike       0.0   0.5    1.0
    1        Mikael    10.0  40.0   90.0
             Mike       0.1   0.4    0.9
    2        Mikael    20.0  30.0   80.0
             Mike       0.2   0.3    0.8
    3        Mikael    30.0  20.0   70.0
             Mike       0.3   0.2    0.7



# Melting


```{python}
# we will demonstrate melting with this DataFrame
data = pd.DataFrame({'Name' : ['Mike', 'Mikael'],
                     'Height' : [6.1, 6.0],
                     'Weight' : [220, 185]})
data
```




       Height    Name  Weight
    0     6.1    Mike     220
    1     6.0  Mikael     185




```{python}
# melt it, use Name as the id's,
# Height and Weight columns as the variables
pd.melt(data,
        id_vars=['Name'],
        value_vars=['Height', 'Weight'])
```




         Name variable  value
    0    Mike   Height    6.1
    1  Mikael   Height    6.0
    2    Mike   Weight  220.0
    3  Mikael   Weight  185.0



# A note on the performance benefits of stacked data


```{python}
# stacked scalar access can be a lot faster than
# column access

# time the different methods
import timeit
t = timeit.Timer("stacked1[('one', 'a')]",
                 "from __main__ import stacked1, df")
r1 = timeit.timeit(lambda: stacked1.loc[('one', 'a')],
                   number=10000)
r2 = timeit.timeit(lambda: df.loc['one']['a'],
                   number=10000)
r3 = timeit.timeit(lambda: df.iloc[1, 0],
                   number=10000)

# and the results are...  Yes, it's the fastest of the three
r1, r2, r3
```




    (0.5667150020599365, 0.9489731788635254, 1.2142961025238037)
