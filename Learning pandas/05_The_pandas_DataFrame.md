
# Chapter 5: The pandas DataFrame Object
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 5: The pandas DataFrame Object](#chapter-5-the-pandas-dataframe-object)
  * [5.1 Creating DataFrame from scratch](#51-creating-dataframe-from-scratch)
  * [5.2 Example data](#52-example-data)
    * [S&P 500](#sp-500)
    * [Monthly stock historical prices](#monthly-stock-historical-prices)
  * [5.3 Selecting columns of a DataFrame](#53-selecting-columns-of-a-dataframe)
  * [5.4 Selecting rows and values of a DataFrame using the index](#54-selecting-rows-and-values-of-a-dataframe-using-the-index)
    * [Slicing using the [] operator](#slicing-using-the-operator)
    * [Selecting rows by index label and location: .loc[] and .iloc[]](#selecting-rows-by-index-label-and-location-loc-and-iloc)
    * [Selecting rows by index label and/or location: .ix[]](#selecting-rows-by-index-label-andor-location-ix)
    * [Scalar lookup by label or location using .at[] and .iat[]](#scalar-lookup-by-label-or-location-using-at-and-iat)
  * [5.5 Selecting rows of a DataFrame by Boolean selection](#55-selecting-rows-of-a-dataframe-by-boolean-selection)
  * [5.6 Modifying the structure and content of DataFrame](#56-modifying-the-structure-and-content-of-dataframe)
    * [Renaming columns](#renaming-columns)
    * [Adding and inserting columns](#adding-and-inserting-columns)
    * [Replacing the contents of a column](#replacing-the-contents-of-a-column)
    * [Deleting columns in a DataFrame](#deleting-columns-in-a-dataframe)
    * [Adding rows to a DataFrame](#adding-rows-to-a-dataframe)
    * [Removing rows from a DataFrame](#removing-rows-from-a-dataframe)
    * [Changing scalar values in a DataFrame](#changing-scalar-values-in-a-dataframe)
  * [5.7 Arithmetic on a DataFrame](#57-arithmetic-on-a-dataframe)
  * [5.8 Resetting and reindexing](#58-resetting-and-reindexing)
  * [5.9 Hierarchical indexing](#59-hierarchical-indexing)
  * [5.10 Summarized data and descriptive statistics](#510-summarized-data-and-descriptive-statistics)
  * [5.11 Summary](#511-summary)

<!-- tocstop -->



```python
# reference NumPy and pandas
import numpy as np
import pandas as pd

# Set some pandas options
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

## 5.1 Creating DataFrame from scratch


```python
# create a DataFrame from a 2-d ndarray
pd.DataFrame(np.array([[10, 11], [20, 21]]))
```




        0   1
    0  10  11
    1  20  21




```python
# create a DataFrame for a list of Series objects
df1 = pd.DataFrame([pd.Series(np.arange(10, 15)),
                    pd.Series(np.arange(15, 20))])
df1
```




        0   1   2   3   4
    0  10  11  12  13  14
    1  15  16  17  18  19




```python
# what's the shape of this DataFrame
df1.shape  # it is two rows by 5 columns
```




    (2, 5)




```python
# specify column names
df = pd.DataFrame(np.array([[10, 11], [20, 21]]),
                  columns=['a', 'b'])
df
```




        a   b
    0  10  11
    1  20  21




```python
# what are names of the columns?
df.columns
```




    Index([u'a', u'b'], dtype='object')




```python
# retrieve just the names of the columns by position
"{0}, {1}".format(df.columns[0], df.columns[1])
```




    'a, b'




```python
# rename the columns
df.columns = ['c1', 'c2']
df
```




       c1  c2
    0  10  11
    1  20  21




```python
# create a DataFrame with named columns and rows
df = pd.DataFrame(np.array([[0, 1], [2, 3]]),
                  columns=['c1', 'c2'],
                  index=['r1', 'r2'])
df
```




        c1  c2
    r1   0   1
    r2   2   3




```python
# retrieve the index of the DataFrame
df.index
```




    Index([u'r1', u'r2'], dtype='object')




```python
# create a DataFrame with two Series objects
# and a dictionary
s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
pd.DataFrame({'c1': s1, 'c2': s2})
```




       c1  c2
    0   1   6
    1   2   7
    2   3   8
    3   4   9
    4   5  10




```python
# demonstrate alignment during creation
s3 = pd.Series(np.arange(12, 14), index=[1, 2])
df = pd.DataFrame({'c1': s1, 'c2': s2, 'c3': s3})
df
```




       c1  c2    c3
    0   1   6   NaN
    1   2   7  12.0
    2   3   8  13.0
    3   4   9   NaN
    4   5  10   NaN



## 5.2 Example data

### S&P 500


```python
# show the first three lines of the file
!head -n 3 data/sp500.csv # on mac or Linux
# type data/sp500.csv # on windows, but will show the entire file
```

    'head' is not recognized as an internal or external command,
    operable program or batch file.



```python
# read in the data and print the first five rows
# use the Symbol column as the index, and
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])
```


```python
# peek at the first 5 rows of the data using .head()
sp500.head()
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897




```python
# peek at the first 5 rows of the data using .head()
sp500.tail()
```




                            Sector   Price  Book Value
    Symbol
    YHOO    Information Technology   35.02      12.768
    YUM     Consumer Discretionary   74.77       5.147
    ZMH                Health Care  101.84      37.181
    ZION                Financials   28.43      30.191
    ZTS                Health Care   30.53       2.150




```python
# how many rows of data?
len(sp500)
```




    500




```python
# examine the index
sp500.index
```




    Index([u'MMM', u'ABT', u'ABBV', u'ACN', u'ACE', u'ACT', u'ADBE', u'AES',
           u'AET', u'AFL',
           ...
           u'XEL', u'XRX', u'XLNX', u'XL', u'XYL', u'YHOO', u'YUM', u'ZMH',
           u'ZION', u'ZTS'],
          dtype='object', name=u'Symbol', length=500)




```python
# get the columns
sp500.columns
```




    Index([u'Sector', u'Price', u'Book Value'], dtype='object')




```python
# first three lines of the file
!head -n 3 data/omh.csv # max or Linux
# type data/omh.csv # on windows, but prints the entire file
```

    Date,MSFT,AAPL

    2014-12-01,48.62,115.07

    2014-12-02,48.46,114.63



### Monthly stock historical prices


```python
# read in the data
one_mon_hist = pd.read_csv("data/omh.csv")
# examine the first three rows
one_mon_hist[:3]
```




             Date   MSFT    AAPL
    0  2014-12-01  48.62  115.07
    1  2014-12-02  48.46  114.63
    2  2014-12-03  48.08  115.93



## 5.3 Selecting columns of a DataFrame


```python
# get first and second columns (1 and 2) by location
sp500[[1, 2]].head()
```




             Price  Book Value
    Symbol
    MMM     141.14      26.668
    ABT      39.60      15.573
    ABBV     53.95       2.954
    ACN      79.79       8.326
    ACE     102.91      86.897




```python
# just the price column
sp500[[1]].head()
```




             Price
    Symbol
    MMM     141.14
    ABT      39.60
    ABBV     53.95
    ACN      79.79
    ACE     102.91




```python
# it's a DataFrame, not a Series
type(sp500[[1]].head())
```




    pandas.core.frame.DataFrame




```python
# this is an exception, hence it is commented
# this tries to find a column named '1'
# not the row at position 1
# df = sp500[1]
```


```python
# create a new DataFrame with integers as the column names
# make sure to use .copy() or change will be in-place
df = sp500.copy()
df.columns=[0, 1, 2]
df.head()
```




                                 0       1       2
    Symbol
    MMM                Industrials  141.14  26.668
    ABT                Health Care   39.60  15.573
    ABBV               Health Care   53.95   2.954
    ACN     Information Technology   79.79   8.326
    ACE                 Financials  102.91  86.897




```python
# this is not an exception
df[1]
```




    Symbol
    MMM     141.14
    ABT      39.60
    ABBV     53.95
    ACN      79.79
    ACE     102.91
             ...
    YHOO     35.02
    YUM      74.77
    ZMH     101.84
    ZION     28.43
    ZTS      30.53
    Name: 1, dtype: float64




```python
# because the column names are actually integers
# and therefore [1] is found as a column
df.columns
```




    Int64Index([0, 1, 2], dtype='int64')




```python
# this is a Series not a DataFrame
type(df[1])
```




    pandas.core.series.Series




```python
# get price column by name
# result is a Series
sp500['Price']
```




    Symbol
    MMM     141.14
    ABT      39.60
    ABBV     53.95
    ACN      79.79
    ACE     102.91
             ...
    YHOO     35.02
    YUM      74.77
    ZMH     101.84
    ZION     28.43
    ZTS      30.53
    Name: Price, dtype: float64




```python
# get Price and Sector columns
# since a list is passed, result is a DataFrame
sp500[['Price', 'Sector']]
```




             Price                  Sector
    Symbol
    MMM     141.14             Industrials
    ABT      39.60             Health Care
    ABBV     53.95             Health Care
    ACN      79.79  Information Technology
    ACE     102.91              Financials
    ...        ...                     ...
    YHOO     35.02  Information Technology
    YUM      74.77  Consumer Discretionary
    ZMH     101.84             Health Care
    ZION     28.43              Financials
    ZTS      30.53             Health Care

    [500 rows x 2 columns]




```python
# attribute access of column by name
sp500.Price
```




    Symbol
    MMM     141.14
    ABT      39.60
    ABBV     53.95
    ACN      79.79
    ACE     102.91
             ...
    YHOO     35.02
    YUM      74.77
    ZMH     101.84
    ZION     28.43
    ZTS      30.53
    Name: Price, dtype: float64




```python
# get the position of the column with value of Price
loc = sp500.columns.get_loc('Price')
loc
```




    1



## 5.4 Selecting rows and values of a DataFrame using the index

### Slicing using the [] operator


```python
# first five rows
sp500[:5]
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897




```python
# ABT through ACN labels
sp500['ABT':'ACN']
```




                            Sector  Price  Book Value
    Symbol
    ABT                Health Care  39.60      15.573
    ABBV               Health Care  53.95       2.954
    ACN     Information Technology  79.79       8.326



### Selecting rows by index label and location: .loc[] and .iloc[]


```python
# get row with label MMM
# returned as a Series
sp500.loc['MMM']
# sp500.iloc['MMM'] # not working
```




    Sector        Industrials
    Price              141.14
    Book Value         26.668
    Name: MMM, dtype: object




```python
# rows with label MMM and MSFT
# this is a DataFrame result
sp500.loc[['MMM', 'MSFT']]
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    MSFT    Information Technology   40.12      10.584




```python
# get rows in location 0 and 2
sp500.iloc[[0, 2]]
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABBV    Health Care   53.95       2.954




```python
# cf sp500.iloc[0, 2]
sp500.iloc[0, 2]
```




    26.668000000000003




```python
# get the location of MMM and A in the index
i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
"{0} {1}".format(i1, i2)
```




    '0 10'




```python
# and get the rows
sp500.iloc[[i1, i2]]
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    A       Health Care   56.18      16.928



### Selecting rows by index label and/or location: .ix[]


```python
# by label
sp500.ix[['MSFT', 'ZTS']]
```




                            Sector  Price  Book Value
    Symbol
    MSFT    Information Technology  40.12      10.584
    ZTS                Health Care  30.53       2.150




```python
# by label
sp500.loc[['MSFT', 'ZTS']]
```




                            Sector  Price  Book Value
    Symbol
    MSFT    Information Technology  40.12      10.584
    ZTS                Health Care  30.53       2.150




```python
# by location
sp500.ix[[10, 200, 450]]
```




                      Sector  Price  Book Value
    Symbol
    A            Health Care  56.18      16.928
    GIS     Consumer Staples  53.81      10.236
    TRV           Financials  92.86      73.056




```python
# by location
sp500.iloc[[10, 200, 450]]
```




                      Sector  Price  Book Value
    Symbol
    A            Health Care  56.18      16.928
    GIS     Consumer Staples  53.81      10.236
    TRV           Financials  92.86      73.056



### Scalar lookup by label or location using .at[] and .iat[]


```python
# by label in both the index and column
sp500.at['MMM', 'Price']
```




    141.13999999999999




```python
# by location.  Row 0, column 1
sp500.iat[0, 1]
```




    141.13999999999999



## 5.5 Selecting rows of a DataFrame by Boolean selection


```python
# what rows have a price < 100?
sp500.Price < 100
```




    Symbol
    MMM       False
    ABT        True
    ABBV       True
    ...
    ZMH       False
    ZION       True
    ZTS        True
    Name: Price, Length: 500, dtype: bool




```python
# now get the rows with Price < 100
sp500[sp500.Price < 100]
```




                            Sector  Price  Book Value
    Symbol
    ABT                Health Care  39.60      15.573
    ABBV               Health Care  53.95       2.954
    ACN     Information Technology  79.79       8.326
    ADBE    Information Technology  64.30      13.262
    AES                  Utilities  13.61       5.781
    ...                        ...    ...         ...
    XYL                Industrials  38.42      12.127
    YHOO    Information Technology  35.02      12.768
    YUM     Consumer Discretionary  74.77       5.147
    ZION                Financials  28.43      30.191
    ZTS                Health Care  30.53       2.150

    [407 rows x 3 columns]




```python
# get only the Price where Price is < 10 and > 0
r = sp500[(sp500.Price < 10) &
          (sp500.Price > 0)] [['Price']]
r
```




            Price
    Symbol
    FTR      5.81
    HCBK     9.80
    HBAN     9.10
    SLM      8.82
    WIN      9.38



## 5.6 Modifying the structure and content of DataFrame
### Renaming columns


```python
# rename the Book Value column to not have a space
# this returns a copy with the column renamed
df = sp500.rename(columns=
                  {'Book Value': 'BookValue'})
# print first 2 rows
df[:2]
```




                 Sector   Price  BookValue
    Symbol
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573




```python
# verify the columns in the original did not change
sp500.columns
```




    Index([u'Sector', u'Price', u'Book Value'], dtype='object')




```python
# this changes the column in-place
sp500.rename(columns=
             {'Book Value': 'BookValue'},
             inplace=True)
# we can see the column is changed
sp500.columns
```




    Index([u'Sector', u'Price', u'BookValue'], dtype='object')




```python
# and now we can use .BookValue
sp500.BookValue[:5]
```




    Symbol
    MMM       26.668
    ABT       15.573
    ABBV       2.954
    ACN        8.326
    ACE       86.897
    Name: BookValue, dtype: float64



### Adding and inserting columns


```python
# make a copy
copy = sp500.copy()
# add a new column to the copy
copy['TwicePrice'] = sp500.Price * 2
copy[:2]
```




                 Sector   Price  BookValue  TwicePrice
    Symbol
    MMM     Industrials  141.14     26.668      282.28
    ABT     Health Care   39.60     15.573       79.20




```python
copy = sp500.copy()
# insert sp500.Price * 2 as the
# second column in the DataFrame
copy.insert(1, 'TwicePrice', sp500.Price * 2)
copy[:2]
```




                 Sector  TwicePrice   Price  BookValue
    Symbol
    MMM     Industrials      282.28  141.14     26.668
    ABT     Health Care       79.20   39.60     15.573




```python
# extract the first four rows and just the Price column
rcopy = sp500[0:3][['Price']].copy()
rcopy
```




             Price
    Symbol
    MMM     141.14
    ABT      39.60
    ABBV     53.95




```python
# new create a new Series to merge as a column
# one label exists in rcopy (MSFT), and MMM does not
s = pd.Series(
              {'MMM': 'Is in the DataFrame',
               'MSFT': 'Not in the DataFrame'} )
s
```




    MMM      Is in the DataFrame
    MSFT    Not in the DataFrame
    dtype: object




```python
# add rcopy into a column named 'Comment'
rcopy['Comment'] = s
rcopy
```




             Price              Comment
    Symbol
    MMM     141.14  Is in the DataFrame
    ABT      39.60                  NaN
    ABBV     53.95                  NaN



### Replacing the contents of a column


```python
copy = sp500.copy()
# replace the Price column data with the new values
# instead of adding a new column
copy.Price = sp500.Price * 2
copy[:5]
```




                            Sector   Price  BookValue
    Symbol
    MMM                Industrials  282.28     26.668
    ABT                Health Care   79.20     15.573
    ABBV               Health Care  107.90      2.954
    ACN     Information Technology  159.58      8.326
    ACE                 Financials  205.82     86.897




```python
# copy all 500 rows
copy = sp500.copy()
# this just copies the first 2 rows of prices
prices = sp500.iloc[[3, 1, 0]].Price.copy()
# examine the extracted prices
prices
```




    Symbol
    ACN        79.79
    ABT        39.60
    MMM       141.14
    Name: Price, dtype: float64




```python
# now replace the Prices column with prices
copy.Price = prices
# it's not really simple insertion, it is alignment
# values are put in the correct place according to labels
copy
```




                            Sector   Price  BookValue
    Symbol
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care     NaN      2.954
    ACN     Information Technology   79.79      8.326
    ACE                 Financials     NaN     86.897
    ...                        ...     ...        ...
    YHOO    Information Technology     NaN     12.768
    YUM     Consumer Discretionary     NaN      5.147
    ZMH                Health Care     NaN     37.181
    ZION                Financials     NaN     30.191
    ZTS                Health Care     NaN      2.150

    [500 rows x 3 columns]



### Deleting columns in a DataFrame


```python
# Example of using del to delete a column
# make a copy of a subset of the data frame
copy = sp500[:2].copy()
copy
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573




```python
# delete the BookValue column
# deletion is in-place
del copy['BookValue']
copy
```


```python
# Example of using pop to remove a column from a DataFrame
# first make a copy of a subset of the data frame
# pop works in place
copy = sp500[:2].copy()
# this will remove Sector and return it as a series
popped = copy.pop('Sector')
# Sector column removed in-place
copy
```




             Price  Book Value
    Symbol
    MMM     141.14      26.668
    ABT      39.60      15.573




```python
# and we have the Sector column as the result of the pop
popped
```




    Symbol
    MMM    Industrials
    ABT    Health Care
    Name: Sector, dtype: object




```python
# Example of using drop to remove a column
# make a copy of a subset of the data frame
copy = sp500[:2].copy()
# this will return a new DataFrame with 'Sector’ removed
# the copy DataFrame is not modified
afterdrop = copy.drop(['Sector'], axis = 1)
afterdrop
```




             Price  Book Value
    Symbol
    MMM     141.14      26.668
    ABT      39.60      15.573



### Adding rows to a DataFrame

* Appending rows with .append()


```python
# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# append df1 and df2
appended = df1.append(df2)
# the result is the rows of the first followed by
# those of the second
appended
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954
    A       Health Care   56.18      16.928
    GAS       Utilities   52.98      32.462
    ABBV    Health Care   53.95       2.954




```python
# data frame using df1.index and just a PER column
# also a good example of using a scalar value
# to initialize multiple rows
df3 = pd.DataFrame(0.0,
                   index=df1.index,
                   columns=['PER'])
df3
```




            PER
    Symbol
    MMM     0.0
    ABT     0.0
    ABBV    0.0




```python
# append df1 and df3
# each has three rows, so 6 rows is the result
# df1 had no PER column, so NaN from for those rows
# df3 had no BookValue, Price or Sector, so NaN's
df1.append(df3)
```




            Book Value  PER   Price       Sector
    Symbol
    MMM         26.668  NaN  141.14  Industrials
    ABT         15.573  NaN   39.60  Health Care
    ABBV         2.954  NaN   53.95  Health Care
    MMM            NaN  0.0     NaN          NaN
    ABT            NaN  0.0     NaN          NaN
    ABBV           NaN  0.0     NaN          NaN




```python
# ignore index labels, create default index
df1.append(df3, ignore_index=True)
```




       Book Value  PER   Price       Sector
    0      26.668  NaN  141.14  Industrials
    1      15.573  NaN   39.60  Health Care
    2       2.954  NaN   53.95  Health Care
    3         NaN  0.0     NaN          NaN
    4         NaN  0.0     NaN          NaN
    5         NaN  0.0     NaN          NaN



* Concatenating DataFrame objects with pd.concat()


```python
# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# pass them as a list
pd.concat([df1, df2])
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954
    A       Health Care   56.18      16.928
    GAS       Utilities   52.98      32.462
    ABBV    Health Care   53.95       2.954




```python
# copy df2
df2_2 = df2.copy()
# add a column to df2_2 that is not in df1
df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
# see what it looks like
df2_2
```




                 Sector  Price  Book Value  Foo
    Symbol
    A       Health Care  56.18      16.928    0
    GAS       Utilities  52.98      32.462    0
    ABBV    Health Care  53.95       2.954    0




```python
# now concatenate
pd.concat([df1, df2_2])
```




            Book Value  Foo   Price       Sector
    Symbol
    MMM         26.668  NaN  141.14  Industrials
    ABT         15.573  NaN   39.60  Health Care
    ABBV         2.954  NaN   53.95  Health Care
    A           16.928  0.0   56.18  Health Care
    GAS         32.462  0.0   52.98    Utilities
    ABBV         2.954  0.0   53.95  Health Care




```python
# specify keys
r = pd.concat([df1, df2_2], keys=['df1', 'df2'])
r
```




                Book Value  Foo   Price       Sector
        Symbol
    df1 MMM         26.668  NaN  141.14  Industrials
        ABT         15.573  NaN   39.60  Health Care
        ABBV         2.954  NaN   53.95  Health Care
    df2 A           16.928  0.0   56.18  Health Care
        GAS         32.462  0.0   52.98    Utilities
        ABBV         2.954  0.0   53.95  Health Care




```python
# first three rows, columns 0 and 1
df3 = sp500[:3][[0, 1]]
df3
```




                 Sector   Price
    Symbol
    MMM     Industrials  141.14
    ABT     Health Care   39.60
    ABBV    Health Care   53.95




```python
# first three rows, column 2
df4 = sp500[:3][[2]]
df4
```




            Book Value
    Symbol
    MMM         26.668
    ABT         15.573
    ABBV         2.954




```python
# put them back together
pd.concat([df3, df4], axis=1)
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954




```python
# make a copy of df4
df4_2 = df4.copy()
# add a column to df4_2, that is also in df3
df4_2.insert(1, 'Sector', pd.Series(1, index=df4_2.index))
df4_2
```




            Book Value  Sector
    Symbol
    MMM         26.668       1
    ABT         15.573       1
    ABBV         2.954       1




```python
# demonstrate duplicate columns
pd.concat([df3, df4_2], axis=1)
```




                 Sector   Price  Book Value  Sector
    Symbol
    MMM     Industrials  141.14      26.668       1
    ABT     Health Care   39.60      15.573       1
    ABBV    Health Care   53.95       2.954       1




```python
# first three rows and first two columns
df5 = sp500[:3][[0, 1]]
df5
```




                 Sector   Price
    Symbol
    MMM     Industrials  141.14
    ABT     Health Care   39.60
    ABBV    Health Care   53.95




```python
# row 2 through 4 and first two columns
df6 = sp500[2:5][[0,1]]
df6
```




                            Sector   Price
    Symbol
    ABBV               Health Care   53.95
    ACN     Information Technology   79.79
    ACE                 Financials  102.91




```python
# inner join on index labels will return in only one row
pd.concat([df5, df6], join='inner', axis=1)
```




                 Sector  Price       Sector  Price
    Symbol
    ABBV    Health Care  53.95  Health Care  53.95



* Adding rows (and columns) via setting with enlargement


```python
# get a small subset of the sp500
# make sure to copy the slice to make a copy
ss = sp500[:3].copy()
# create a new row with index label FOO
# and assign some values to the columns via a list
ss.loc['FOO'] = ['the sector', 100, 110]
ss
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954
    FOO      the sector  100.00     110.000




```python
# copy of subset / slice
ss = sp500[:3].copy()
# add the new column initialized to 0
ss.loc[:,'PER'] = 0
# take a look at the results
ss
```




                 Sector   Price  Book Value  PER
    Symbol
    MMM     Industrials  141.14      26.668    0
    ABT     Health Care   39.60      15.573    0
    ABBV    Health Care   53.95       2.954    0



### Removing rows from a DataFrame

* Removing rows using .drop()


```python
# get a copy of the first 5 rows of sp500
ss = sp500[:5].copy()
ss
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897




```python
# drop rows with labels ABT and ACN
afterdrop = ss.drop(['ABT', 'ACN'])
afterdrop
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABBV    Health Care   53.95       2.954
    ACE      Financials  102.91      86.897




```python
# note that ss is not modified
ss
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897



* Removing rows using Boolean selection


```python
# determine the rows where Price > 300
selection = sp500.Price > 300
# to make output shorter, report the # of rows returned (500),
# and the sum of those where Price > 300 (which is 10)
"{0} {1}".format(len(selection), selection.sum())
```




    '500 10'




```python
# select the complement
withPriceLessThan300 = sp500[~selection]
withPriceLessThan300
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897
    ...                        ...     ...         ...
    YHOO    Information Technology   35.02      12.768
    YUM     Consumer Discretionary   74.77       5.147
    ZMH                Health Care  101.84      37.181
    ZION                Financials   28.43      30.191
    ZTS                Health Care   30.53       2.150

    [490 rows x 3 columns]



* Removing rows using a slice


```python
# get only the first three rows
onlyFirstThree = sp500[:3]
onlyFirstThree
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954




```python
# first three, but a copy of them
onlyFirstThree = sp500[:3].copy()
onlyFirstThree
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954



### Changing scalar values in a DataFrame


```python
# get a subset / copy of the data
subset = sp500[:3].copy()
subset
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABT     Health Care   39.60      15.573
    ABBV    Health Care   53.95       2.954




```python
# change scalar by label on row and column
subset.ix['MMM', 'Price'] = 0
subset
```




                 Sector  Price  Book Value
    Symbol
    MMM     Industrials   0.00      26.668
    ABT     Health Care  39.60      15.573
    ABBV    Health Care  53.95       2.954




```python
subset = sp500[:3].copy()
subset.loc['MMM', 'Price'] = 10
subset.loc['ABBV', 'Price'] = 20
subset
```




                 Sector  Price  Book Value
    Symbol
    MMM     Industrials   10.0      26.668
    ABT     Health Care   39.6      15.573
    ABBV    Health Care   20.0       2.954




```python
# subset of the first three rows
subset = sp500[:3].copy()
# get the location of the Price column
price_loc = sp500.columns.get_loc('Price')
# get the location of the MMM row
abt_row_loc = sp500.index.get_loc('ABT')
# change the price
subset.iloc[abt_row_loc, price_loc] = 1000
subset
```




                 Sector    Price  Book Value
    Symbol
    MMM     Industrials   141.14      26.668
    ABT     Health Care  1000.00      15.573
    ABBV    Health Care    53.95       2.954



## 5.7 Arithmetic on a DataFrame


```python
# set the seed to allow replicatable results
np.random.seed(123456)
# create the DataFrame
df = pd.DataFrame(np.random.randn(5, 4),
                  columns=['A', 'B', 'C', 'D'])
df
```




              A         B         C         D
    0  0.469112 -0.282863 -1.509059 -1.135632
    1  1.212112 -0.173215  0.119209 -1.044236
    2 -0.861849 -2.104569 -0.494929  1.071804
    3  0.721555 -0.706771 -1.039575  0.271860
    4 -0.424972  0.567020  0.276232 -1.087401




```python
# multiply everything by 2
df * 2
```




              A         B         C         D
    0  0.938225 -0.565727 -3.018117 -2.271265
    1  2.424224 -0.346429  0.238417 -2.088472
    2 -1.723698 -4.209138 -0.989859  2.143608
    3  1.443110 -1.413542 -2.079150  0.543720
    4 -0.849945  1.134041  0.552464 -2.174801




```python
# get first row
s = df.iloc[0]
# subtract first row from every row of the DataFrame
diff = df - s
diff
```




              A         B         C         D
    0  0.000000  0.000000  0.000000  0.000000
    1  0.743000  0.109649  1.628267  0.091396
    2 -1.330961 -1.821706  1.014129  2.207436
    3  0.252443 -0.423908  0.469484  1.407492
    4 -0.894085  0.849884  1.785291  0.048232




```python
# subtract DataFrame from Series
diff2 = s - df
diff2
```




              A         B         C         D
    0  0.000000  0.000000  0.000000  0.000000
    1 -0.743000 -0.109649 -1.628267 -0.091396
    2  1.330961  1.821706 -1.014129 -2.207436
    3 -0.252443  0.423908 -0.469484 -1.407492
    4  0.894085 -0.849884 -1.785291 -0.048232




```python
# B, C
s2 = s[1:3]
# add E
s2['E'] = 0
# see how alignment is applied in math
df + s2
```




        A         B         C   D   E
    0 NaN -0.565727 -3.018117 NaN NaN
    1 NaN -0.456078 -1.389850 NaN NaN
    2 NaN -2.387433 -2.003988 NaN NaN
    3 NaN -0.989634 -2.548633 NaN NaN
    4 NaN  0.284157 -1.232826 NaN NaN




```python
# get rows 1 through three, and only B, C columns
subframe = df[1:4][['B', 'C']]
# we have extracted a little square in the middle of df
subframe
```




              B         C
    1 -0.173215  0.119209
    2 -2.104569 -0.494929
    3 -0.706771 -1.039575




```python
# demonstrate the alignment of the subtraction
df - subframe
```




        A    B    C   D
    0 NaN  NaN  NaN NaN
    1 NaN  0.0  0.0 NaN
    2 NaN  0.0  0.0 NaN
    3 NaN  0.0  0.0 NaN
    4 NaN  NaN  NaN NaN




```python
# get the A column
a_col = df['A']
df.sub(a_col, axis=0)
```




         A         B         C         D
    0  0.0 -0.751976 -1.978171 -1.604745
    1  0.0 -1.385327 -1.092903 -2.256348
    2  0.0 -1.242720  0.366920  1.933653
    3  0.0 -1.428326 -1.761130 -0.449695
    4  0.0  0.991993  0.701204 -0.662428



## 5.8 Resetting and reindexing


```python
# reset the index, moving it into a column
reset_sp500 = sp500.reset_index()
reset_sp500
```




        Symbol                  Sector   Price  Book Value
    0      MMM             Industrials  141.14      26.668
    1      ABT             Health Care   39.60      15.573
    2     ABBV             Health Care   53.95       2.954
    3      ACN  Information Technology   79.79       8.326
    4      ACE              Financials  102.91      86.897
    ..     ...                     ...     ...         ...
    495   YHOO  Information Technology   35.02      12.768
    496    YUM  Consumer Discretionary   74.77       5.147
    497    ZMH             Health Care  101.84      37.181
    498   ZION              Financials   28.43      30.191
    499    ZTS             Health Care   30.53       2.150

    [500 rows x 4 columns]




```python
# move the Symbol column into the index
reset_sp500.set_index('Symbol')
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326
    ACE                 Financials  102.91      86.897
    ...                        ...     ...         ...
    YHOO    Information Technology   35.02      12.768
    YUM     Consumer Discretionary   74.77       5.147
    ZMH                Health Care  101.84      37.181
    ZION                Financials   28.43      30.191
    ZTS                Health Care   30.53       2.150

    [500 rows x 3 columns]




```python
# get first four rows
subset = sp500[:4].copy()
subset
```




                            Sector   Price  Book Value
    Symbol
    MMM                Industrials  141.14      26.668
    ABT                Health Care   39.60      15.573
    ABBV               Health Care   53.95       2.954
    ACN     Information Technology   79.79       8.326




```python
# reindex to have MMM, ABBV, and FOO index labels
reindexed = subset.reindex(index=['MMM', 'ABBV', 'FOO'])
# note that ABT and ACN are dropped and FOO has NaN values
reindexed
```




                 Sector   Price  Book Value
    Symbol
    MMM     Industrials  141.14      26.668
    ABBV    Health Care   53.95       2.954
    FOO             NaN     NaN         NaN




```python
# reindex columns
subset.reindex(columns=['Price',
                        'Book Value',
                        'NewCol'])
```




             Price  Book Value  NewCol
    Symbol
    MMM     141.14      26.668     NaN
    ABT      39.60      15.573     NaN
    ABBV     53.95       2.954     NaN
    ACN      79.79       8.326     NaN



## 5.9 Hierarchical indexing


```python
# first, push symbol into a column
reindexed = sp500.reset_index()
# and now index sp500 by sector and symbol
multi_fi = reindexed.set_index(['Sector', 'Symbol'])
multi_fi
```




                                    Price  Book Value
    Sector                 Symbol
    Industrials            MMM     141.14      26.668
    Health Care            ABT      39.60      15.573
                           ABBV     53.95       2.954
    Information Technology ACN      79.79       8.326
    Financials             ACE     102.91      86.897
    ...                               ...         ...
    Information Technology YHOO     35.02      12.768
    Consumer Discretionary YUM      74.77       5.147
    Health Care            ZMH     101.84      37.181
    Financials             ZION     28.43      30.191
    Health Care            ZTS      30.53       2.150

    [500 rows x 2 columns]




```python
# the index is a MultiIndex
type(multi_fi.index)
```




    pandas.indexes.multi.MultiIndex




```python
# examine the index
print (multi_fi.index)
```

    MultiIndex(levels=[['Consumer Discretionary', 'Consumer Discretionary ', 'Consumer Staples', 'Consumer Staples ', 'Energy', 'Financials', 'Health Care', 'Industrials', 'Industries', 'Information Technology', 'Materials', 'Telecommunications Services', 'Utilities'], ['A', 'AA', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 'ACT', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AKAM', 'ALL', 'ALLE', 'ALTR', 'ALXN', 'AMAT', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'AN', 'AON', 'APA', 'APC', 'APD', 'APH', 'ARG', 'ATI', 'AVB', 'AVP', 'AVY', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BCR', 'BDX', 'BEAM', 'BEN', 'BF-B', 'BHI', 'BIIB', 'BK', 'BLK', 'BLL', 'BMS', 'BMY', 'BRCM', 'BRK-B', 'BSX', 'BTU', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAM', 'CAT', 'CB', 'CBG', 'CBS', 'CCE', 'CCI', 'CCL', 'CELG', 'CERN', 'CF', 'CFN', 'CHK', 'CHRW', 'CI', 'CINF', 'CL', 'CLF', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP', 'CNX', 'COF', 'COG', 'COH', 'COL', 'COP', 'COST', 'COV', 'CPB', 'CRM', 'CSC', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'CVS', 'CVX', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DLPH', 'DLTR', 'DNB', 'DNR', 'DO', 'DOV', 'DOW', 'DPS', 'DRI', 'DTE', 'DTV', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMC', 'EMN', 'EMR', 'EOG', 'EQR', 'EQT', 'ESRX', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'F', 'FAST', 'FB', 'FCX', 'FDO', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOSL', 'FOXA', 'FRX', 'FSLR', 'FTI', 'FTR', 'GAS', 'GCI', 'GD', 'GE', 'GGP', 'GHC', 'GILD', 'GIS', 'GLW', 'GM', 'GMCR', 'GME', 'GNW', 'GOOG', 'GPC', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HCBK', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HOG', 'HON', 'HOT', 'HP', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSP', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IFF', 'IGT', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JBL', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JOY', 'JPM', 'JWN', 'K', 'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KRFT', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LLL', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC', 'LO', 'LOW', 'LRCX', 'LSI', 'LUK', 'LUV', 'LYB', 'M', 'MA', 'MAC', 'MAR', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MHFI', 'MHK', 'MJN', 'MKC', 'MMC', 'MMM', 'MNST', 'MO', 'MON', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MU', 'MUR', 'MWV', 'MYL', 'NBL', 'NBR', 'NDAQ', 'NE', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NU', 'NUE', 'NVDA', 'NWL', 'NWSA', 'OI', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PEP', 'PETM', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PLL', 'PM', 'PNC', 'PNR', 'PNW', 'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'QCOM', 'QEP', 'R', 'RAI', 'RDC', 'REGN', 'RF', 'RHI', 'RHT', 'RIG', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBUX', 'SCG', 'SCHW', 'SE', 'SEE', 'SHW', 'SIAL', 'SJM', 'SLB', 'SLM', 'SNA', 'SNDK', 'SNI', 'SO', 'SPG', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 'STT', 'STX', 'STZ', 'SWK', 'SWN', 'SWY', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDC', 'TE', 'TEG', 'TEL', 'TGT', 'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSO', 'TSS', 'TWC', 'TWX', 'TXN', 'TXT', 'TYC', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAG', 'WAT', 'WDC', 'WEC', 'WFC', 'WFM', 'WHR', 'WIN', 'WLP', 'WM', 'WMB', 'WMT', 'WU', 'WY', 'WYN', 'WYNN', 'X', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZMH', 'ZTS']],
               labels=[[7, 6, 6, 9, 5, 6, 9, 12, 6, 5, 6, 12, 10, 10, 9, 10, 6, 10, 7, 6, 9, 5, 9, 2, 0, 12, 12, 5, 5, 5, 5, 6, 9, 6, 7, 4, 9, 5, 4, 5, 9, 9, 2, 5, 11, 9, 9, 0, 0, 5, 7, 2, 4, 10, 5, 6, 6, 5, 0, 6, 0, 10, 5, 0, 6, 5, 0, 7, 0, 5, 6, 6, 9, 2, 9, 0, 4, 4, 2, 5, 6, 6, 0, 0, 7, 5, 0, 6, 12, 11, 6, 10, 7, 4, 4, 0, 5, 6, 5, 7, 9, 5, 9, 10, 2, 5, 12, 0, 2, 2, 9, 2, 0, 5, 9, 2, 4, 4, 12, 2, 7, 2, 6, 11, 7, 7, 2, 7, 0, 6, 7, 0, 7, 4, 6, 4, 4, 0, 5, 0, 0, 0, 12, 7, 10, 2, 12, 12, 7, 5, 10, 10, 7, 9, 10, 12, 6, 9, 9, 7, 4, 12, 4, 12, 5, 5, 2, 12, 0, 7, 6, 4, 9, 9, 0, 7, 7, 9, 5, 7, 12, 9, 9, 7, 7, 10, 4, 0, 6, 0, 5, 10, 11, 0, 0, 0, 0, 7, 7, 5, 2, 0, 0, 5, 6, 5, 0, 9, 0, 7, 4, 0, 0, 9, 5, 0, 5, 5, 4, 2, 4, 9, 0, 7, 2, 0, 6, 5, 5, 6, 5, 7, 7, 12, 9, 5, 0, 9, 10, 0, 10, 9, 6, 5, 7, 9, 7, 6, 0, 7, 5, 9, 7, 2, 3, 5, 2, 5, 4, 9, 0, 2, 2, 0, 7, 6, 9, 5, 0, 0, 5, 6, 5, 9, 7, 5, 2, 0, 9, 10, 5, 5, 0, 4, 4, 0, 5, 7, 9, 0, 2, 0, 5, 6, 2, 10, 6, 6, 5, 0, 9, 9, 9, 0, 2, 2, 10, 2, 5, 5, 10, 9, 4, 6, 4, 5, 4, 9, 9, 0, 4, 10, 0, 12, 8, 0, 12, 4, 4, 0, 7, 12, 5, 7, 12, 10, 9, 0, 4, 0, 12, 9, 10, 7, 7, 7, 6, 9, 4, 7, 5, 12, 2, 6, 6, 0, 6, 12, 2, 4, 12, 4, 7, 5, 5, 10, 12, 10, 7, 7, 5, 2, 5, 5, 5, 12, 5, 0, 0, 12, 9, 7, 6, 0, 4, 7, 9, 6, 5, 7, 2, 7, 7, 7, 7, 0, 4, 7, 2, 9, 9, 12, 4, 5, 0, 9, 10, 12, 0, 10, 5, 5, 2, 0, 12, 7, 4, 4, 6, 0, 0, 0, 0, 5, 7, 6, 5, 9, 2, 5, 0, 9, 12, 6, 9, 4, 9, 7, 7, 5, 4, 6, 0, 0, 0, 0, 5, 9, 1, 4, 5, 0, 0, 7, 2, 7, 7, 10, 7, 6, 5, 0, 5, 4, 6, 5, 9, 11, 6, 0, 0, 9, 5, 10, 2, 2, 0, 7, 6, 6, 5, 9, 9, 5, 0, 2, 11, 12, 0, 0, 12, 9, 9, 5, 7, 9, 0, 6, 5, 6], [303, 5, 3, 7, 6, 8, 9, 18, 19, 20, 0, 191, 40, 42, 25, 1, 29, 43, 27, 21, 13, 26, 28, 305, 35, 16, 17, 47, 22, 34, 33, 4, 31, 32, 41, 39, 10, 37, 38, 23, 2, 30, 11, 24, 429, 14, 12, 36, 48, 44, 46, 45, 60, 64, 50, 55, 51, 53, 57, 56, 52, 65, 68, 54, 61, 63, 226, 49, 71, 72, 69, 66, 67, 59, 74, 120, 105, 77, 111, 104, 76, 88, 260, 84, 78, 80, 81, 85, 102, 117, 86, 87, 90, 89, 122, 99, 79, 91, 92, 116, 114, 73, 119, 94, 95, 98, 101, 106, 261, 82, 118, 93, 97, 96, 113, 75, 108, 103, 151, 422, 199, 109, 110, 83, 115, 100, 121, 131, 142, 146, 126, 134, 124, 137, 492, 147, 138, 144, 127, 133, 128, 135, 123, 139, 140, 141, 143, 145, 136, 163, 125, 156, 164, 149, 150, 153, 166, 148, 155, 157, 162, 165, 158, 160, 152, 159, 154, 167, 169, 168, 161, 491, 177, 172, 174, 171, 175, 178, 180, 188, 176, 179, 181, 183, 182, 184, 189, 170, 187, 185, 58, 173, 190, 202, 192, 206, 207, 193, 194, 195, 198, 200, 205, 203, 197, 208, 209, 204, 196, 210, 211, 221, 212, 228, 220, 213, 217, 216, 224, 231, 219, 225, 218, 222, 227, 130, 229, 230, 215, 232, 214, 244, 241, 433, 237, 234, 240, 233, 235, 236, 239, 238, 243, 245, 242, 246, 248, 249, 247, 251, 252, 250, 266, 254, 201, 255, 258, 256, 259, 257, 265, 264, 263, 268, 272, 271, 280, 275, 269, 270, 282, 274, 277, 273, 276, 267, 278, 279, 281, 284, 314, 287, 285, 310, 308, 288, 302, 289, 286, 290, 301, 291, 298, 293, 300, 317, 296, 309, 297, 262, 292, 315, 312, 299, 430, 295, 306, 304, 294, 311, 307, 313, 316, 318, 320, 321, 331, 334, 325, 339, 326, 324, 340, 323, 329, 328, 327, 322, 319, 253, 333, 336, 335, 330, 332, 337, 338, 345, 346, 343, 342, 344, 341, 350, 367, 363, 355, 347, 70, 370, 348, 372, 357, 365, 375, 358, 359, 351, 368, 378, 371, 382, 349, 352, 369, 373, 374, 381, 354, 353, 360, 361, 362, 366, 376, 356, 377, 364, 379, 384, 383, 380, 129, 393, 397, 399, 391, 388, 389, 398, 386, 390, 394, 107, 395, 396, 387, 385, 425, 112, 411, 401, 408, 402, 412, 421, 404, 417, 405, 406, 414, 409, 407, 410, 413, 283, 424, 403, 419, 423, 415, 400, 223, 420, 416, 426, 418, 427, 428, 442, 435, 434, 432, 436, 431, 446, 450, 451, 15, 62, 481, 440, 437, 448, 449, 438, 439, 447, 444, 392, 443, 441, 186, 452, 445, 455, 456, 487, 459, 453, 454, 457, 458, 464, 461, 469, 467, 470, 468, 462, 463, 460, 466, 465, 482, 471, 132, 480, 472, 479, 475, 473, 483, 484, 477, 476, 478, 474, 485, 486, 488, 493, 490, 489, 494, 495, 496, 498, 497, 499]],
               names=['Sector', 'Symbol'])



```python
# this has two levels
len(multi_fi.index.levels)
```




    2




```python
# each index level is an index
multi_fi.index.levels[0]
```




    Index(['Consumer Discretionary', 'Consumer Discretionary ', 'Consumer Staples',
           'Consumer Staples ', 'Energy', 'Financials', 'Health Care',
           'Industrials', 'Industries', 'Information Technology', 'Materials',
           'Telecommunications Services', 'Utilities'],
          dtype='object', name='Sector')




```python
# each index level is an index
multi_fi.index.levels[1]
```




    Index(['A', 'AA', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 'ACT', 'ADBE',
           ...
           'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZMH',
           'ZTS'],
          dtype='object', name='Symbol', length=500)




```python
# values of index level 0
multi_fi.index.get_level_values(0)
```




    Index(['Industrials', 'Health Care', 'Health Care', 'Information Technology',
           'Financials', 'Health Care', 'Information Technology', 'Utilities',
           'Health Care', 'Financials',
           ...
           'Utilities', 'Information Technology', 'Information Technology',
           'Financials', 'Industrials', 'Information Technology',
           'Consumer Discretionary', 'Health Care', 'Financials', 'Health Care'],
          dtype='object', name='Sector', length=500)




```python
# get all stocks that are Industrials
# note the result drops level 0 of the index
multi_fi.xs('Industrials')
```




             Price  Book Value
    Symbol
    MMM     141.14      26.668
    ALLE     52.46       0.000
    APH      95.71      18.315
    AVY      48.20      15.616
    BA      132.41      19.870
    ...        ...         ...
    UNP     196.26      46.957
    UPS     102.73       6.790
    UTX     115.54      35.252
    WM       43.37      12.330
    XYL      38.42      12.127

    [64 rows x 2 columns]




```python
# select rows where level 1 (Symbol) is ALLE
# note that the Sector level is dropped from the result
multi_fi.xs('ALLE', level=1)
```




                 Price  Book Value
    Sector
    Industrials  52.46         0.0




```python
# Industrials, without dropping the level
multi_fi.xs('Industrials', drop_level=False)
```




                         Price  Book Value
    Sector      Symbol
    Industrials MMM     141.14      26.668
                ALLE     52.46       0.000
                APH      95.71      18.315
                AVY      48.20      15.616
                BA      132.41      19.870
    ...                    ...         ...
                UNP     196.26      46.957
                UPS     102.73       6.790
                UTX     115.54      35.252
                WM       43.37      12.330
                XYL      38.42      12.127

    [64 rows x 2 columns]




```python
# drill through the levels
multi_fi.xs('Industrials').xs('UPS')
```




    Price         102.73
    Book Value      6.79
    Name: UPS, dtype: float64




```python
# drill through using tuples
multi_fi.xs(('Industrials', 'UPS'))
```




    Price         102.73
    Book Value      6.79
    Name: (Industrials, UPS), dtype: float64



## 5.10 Summarized data and descriptive statistics


```python
# calc the mean of the values in each column
one_mon_hist.mean()
```




    MSFT     47.493182
    AAPL    112.411364
    dtype: float64




```python
# calc the mean of the values in each row
one_mon_hist.mean(axis=1)
```




    0     81.845
    1     81.545
    2     82.005
    3     82.165
    4     81.710
           ...
    17    80.075
    18    80.935
    19    80.680
    20    79.770
    21    78.415
    dtype: float64




```python
# calc the variance of the values in each column
one_mon_hist.var()
```




    MSFT    0.870632
    AAPL    5.706231
    dtype: float64




```python
# calc the median of the values in each column
one_mon_hist.median()
```




    MSFT     47.625
    AAPL    112.530
    dtype: float64




```python
# location of min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].min()
```




    MSFT     45.16
    AAPL    106.75
    dtype: float64




```python
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].max()
```




    MSFT     48.84
    AAPL    115.93
    dtype: float64




```python
# location of min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].idxmin()
```




    MSFT    11
    AAPL    11
    dtype: int64




```python
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].idxmax()
```




    MSFT    3
    AAPL    2
    dtype: int64




```python
# find the mode of this Series
s = pd.Series([1, 2, 3, 3, 5])
s.mode()
```




    0    3
    dtype: int64




```python
# there can be more than one mode
s = pd.Series([1, 2, 3, 3, 5, 1])
s.mode()
```




    0    1
    1    3
    dtype: int64




```python
# calculate a cumulative product
pd.Series([1, 2, 3, 4]).cumprod()
```




    0     1
    1     2
    2     6
    3    24
    dtype: int64




```python
# calculate a cumulative sum
pd.Series([1, 2, 3, 4]).cumsum()
```




    0     1
    1     3
    2     6
    3    10
    dtype: int64




```python
# summary statistics
one_mon_hist.describe()
```




                MSFT        AAPL
    count  22.000000   22.000000
    mean   47.493182  112.411364
    std     0.933077    2.388772
    min    45.160000  106.750000
    25%    46.967500  111.660000
    50%    47.625000  112.530000
    75%    48.125000  114.087500
    max    48.840000  115.930000




```python
# get summary stats on non-numeric data
s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
s.describe()
```




    count     4
    unique    3
    top       a
    freq      2
    dtype: object




```python
# get summary stats on non-numeric data
s.count()
```




    4




```python
# return a list of unique items
s.unique()
```




    array(['a', 'b', 'c', nan], dtype=object)




```python
# number of occurrences of each unique value
s.value_counts()
```




    a    2
    b    1
    c    1
    dtype: int64



## 5.11 Summary


```python

```
