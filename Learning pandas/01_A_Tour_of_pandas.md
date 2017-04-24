
# Chapter 1: A Tour of pandas
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 1: A Tour of pandas](#chapter-1-a-tour-of-pandas)
  * [1.1 pandas and why it is important](#11-pandas-and-why-it-is-important)
  * [1.2 pandas and IPython Notebooks](#12-pandas-and-ipython-notebooks)
  * [1.3 Referencing pandas in the application](#13-referencing-pandas-in-the-application)
  * [1.4 Primary pandas objects](#14-primary-pandas-objects)
    * [The pandas Series object](#the-pandas-series-object)
      * [Practice](#practice)
    * [The pandas DataFrame object](#the-pandas-dataframe-object)
  * [1.5 Loading data from files and the Web](#15-loading-data-from-files-and-the-web)
    * [Loading CSV data from files](#loading-csv-data-from-files)
    * [Loading data from the Web](#loading-data-from-the-web)
  * [1.6 Simplicity of visualization of pandas data](#16-simplicity-of-visualization-of-pandas-data)
  * [1.7 Summary](#17-summary)

<!-- tocstop -->



```python
# import numpy and pandas, and DataFrame / Series
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# Set some pandas options7
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

# And some items for matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'
```

## 1.1 pandas and why it is important
## 1.2 pandas and IPython Notebooks
## 1.3 Referencing pandas in the application

## 1.4 Primary pandas objects

### The pandas Series object


```python
# create a four item Series
s = Series([1, 2, 3, 4])
s
```

#### Practice


```python
s2 = Series([1,2,3,4])
s2
```


```python
# return a Series with the row with labels 1 and 3
s[[1, 3]]
```


```python
# create a series using an explicit index
s = Series([1, 2, 3, 4],
           index = ['a', 'b', 'c', 'd'])
s
```


```python
# look up items the series having index 'a' and 'd'
s[['a', 'd']]
```


```python
# passing a list of integers to a Series that has
# non-integer index labels will look up based upon
# 0-based index like an array
s[[1, 2]]
```


```python
# get only the index of the Series
s.index
```


```python
# create a Series who's index is a series of dates
# between the two specified dates (inclusive)
dates = pd.date_range('2014-07-01', '2014-07-06')
dates
```


```python
# create a Series with values (representing temperatures)
# for each date in the index
temps1 = Series([80, 82, 85, 90, 83, 87],
                index = dates)
temps1
```


```python
# calculate the mean of the values in the Series
temps1.mean()
```


```python
# create a second series of values using the same index
temps2 = Series([70, 75, 69, 83, 79, 77],
                index = dates)
# the following aligns the two by their index values
# and calculates the difference at those matching labels
temp_diffs = temps1 - temps2
temp_diffs
```


```python
# lookup a value by date using the index
temp_diffs['2014-07-03']
```


```python
# and also possible by integer position as if the
# series was an array
temp_diffs[2]
```

### The pandas DataFrame object


```python
# create a DataFrame from the two series objects temp1 and temp2
# and give them column names
temps_df = DataFrame(
            {'Missoula': temps1,
             'Philadelphia': temps2})
temps_df
```


```python
# get the column with the name Missoula
temps_df['Missoula']
```


```python
# likewise we can get just the Philadelphia column
temps_df['Philadelphia']
```


```python
# return both columns in a different order
temps_df[['Philadelphia', 'Missoula']]
```


```python
# retrieve the Missoula column through property syntax
temps_df.Missoula
```


```python
# calculate the temperature difference between the two cities
temps_df.Missoula - temps_df.Philadelphia
```


```python
# add a column to temp_df which contains the difference in temps
temps_df['Difference'] = temp_diffs
temps_df
```


```python
# get the columns, which is also an Index object
temps_df.columns
```


```python
# slice the temp differences column for the rows at
# location 1 through 4 (as though it is an array)
temps_df.Difference[1:4]
```


```python
# get the row at array position 1
temps_df.iloc[1]
```


```python
# the names of the columns have become the index
# they have been 'pivoted'
temps_df.ix[1].index
```


```python
# retrieve row by index label using .loc
temps_df.loc['2014-07-03']
```


```python
# get the values in the Differences column in tows 1, 3 and 5
# using 0-based location
temps_df.iloc[[1, 3, 5]].Difference
```


```python
# which values in the Missoula column are > 82?
temps_df.Missoula > 82
```


```python
# return the rows where the temps for Missoula > 82
temps_df[temps_df.Missoula > 82]
```

## 1.5 Loading data from files and the Web

### Loading CSV data from files


```python
# display the contents of test1.csv
# which command to use depends on your OS
!cat data/test1.csv # on non-windows systems
#!type data/test1.csv # on windows systems
```


```python
# read the contents of the file into a DataFrame
df = pd.read_csv('data/test1.csv')
df
```


```python
# the contents of the date column
df.date
```


```python
# we can get the first value in the date column
df.date[0]
```


```python
# it is a string
type(df.date[0])
```


```python
# read the data and tell pandas the date column should be
# a date in the resulting DataFrame
df = pd.read_csv('data/test1.csv', parse_dates=['date'])
df
```


```python
# verify the type now is date
# in pandas, this is actually a Timestamp
type(df.date[0])
```


```python
# unfortunately the index is numeric which makes
# accessing data by date more complicated
df.index
```


```python
# read in again, now specity the data column as being the
# index of the resulting DataFrame
df = pd.read_csv('data/test1.csv',
                 parse_dates=['date'],
                 index_col='date')
df
```


```python
# and the index is now a DatetimeIndex
df.index
```

### Loading data from the Web


```python
# imports for reading data from Yahoo!
from pandas.io.data import DataReader
from datetime import date
from dateutil.relativedelta import relativedelta

# read the last three months of data for GOOG
goog = DataReader("GOOG",  "yahoo",
                  date.today() +
                  relativedelta(months=-3))

# the result is a DataFrame
#and this gives us the 5 most recent prices
goog.tail()
```

## 1.6 Simplicity of visualization of pandas data


```python
# plot the Adj Close values we just read in
goog.plot(y='Adj Close', figsize=(12,8));
plt.savefig('5128OS_01_02.png', bbox_inches='tight', dpi=300)
```

## 1.7 Summary


```python

```
