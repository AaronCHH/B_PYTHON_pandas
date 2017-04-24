Creating a DataFrame from scratch

```
# reference NumPy and pandas
import numpy as np
import pandas as pd

# Set some pandas options
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10) 
```


```
# create a DataFrame from a 2-d ndarray
pd.DataFrame(np.array([[10, 11], [20, 21]]))
```




        0   1
    0  10  11
    1  20  21




```
# create a DataFrame for a list of Series objects
df1 = pd.DataFrame([pd.Series(np.arange(10, 15)), 
                    pd.Series(np.arange(15, 20))])
df1
```




        0   1   2   3   4
    0  10  11  12  13  14
    1  15  16  17  18  19




```
# what's the shape of this DataFrame
df1.shape  # it is two rows by 5 columns
```




    (2, 5)




```
# specify column names
df = pd.DataFrame(np.array([[10, 11], [20, 21]]), 
                  columns=['a', 'b'])
df
```




        a   b
    0  10  11
    1  20  21




```
# what are names of the columns?
df.columns
```




    Index([u'a', u'b'], dtype='object')




```
# retrieve just the names of the columns by position
"{0}, {1}".format(df.columns[0], df.columns[1])
```




    'a, b'




```
# rename the columns
df.columns = ['c1', 'c2']
df
```




       c1  c2
    0  10  11
    1  20  21




```
# create a DataFrame with named columns and rows
df = pd.DataFrame(np.array([[0, 1], [2, 3]]), 
                  columns=['c1', 'c2'], 
                  index=['r1', 'r2'])
df
```




        c1  c2
    r1   0   1
    r2   2   3




```
# retrieve the index of the DataFrame
df.index
```




    Index([u'r1', u'r2'], dtype='object')




```
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




```
# demonstrate alignment during creation
s3 = pd.Series(np.arange(12, 14), index=[1, 2])
df = pd.DataFrame({'c1': s1, 'c2': s2, 'c3': s3})
df
```




       c1  c2  c3
    0   1   6 NaN
    1   2   7  12
    2   3   8  13
    3   4   9 NaN
    4   5  10 NaN



# Loading sample data for demonstrate DataFrame capabilities

## S&P 500


```
# show the first three lines of the file
!head -n 3 data/sp500.csv # on mac or Linux
# type data/sp500.csv # on windows, but will show the entire file
```

    
    
    



```
# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])
```


```
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




```
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




```
# how many rows of data?
len(sp500)
```




    500




```
# examine the index
sp500.index
```




    Index([u'MMM', u'ABT', u'ABBV', u'ACN', u'ACE', u'ACT', u'ADBE', u'AES', u'AET', u'AFL', u'A', u'GAS', u'APD', u'ARG', u'AKAM', u'AA', u'ALXN', u'ATI', u'ALLE', u'AGN', u'ADS', u'ALL', u'ALTR', u'MO', u'AMZN', u'AEE', u'AEP', u'AXP', u'AIG', u'AMT', u'AMP', u'ABC', u'AME', u'AMGN', u'APH', u'APC', u'ADI', u'AON', u'APA', u'AIV', u'AAPL', u'AMAT', u'ADM', u'AIZ', u'T', u'ADSK', u'ADP', u'AN', u'AZO', u'AVB', u'AVY', u'AVP', u'BHI', u'BLL', u'BAC', u'BCR', u'BAX', u'BBT', u'BEAM', u'BDX', u'BBBY', u'BMS', u'BRK-B', u'BBY', u'BIIB', u'BLK', u'HRB', u'BA', u'BWA', u'BXP', u'BSX', u'BMY', u'BRCM', u'BF-B', u'CA', u'CVC', u'COG', u'CAM', u'CPB', u'COF', u'CAH', u'CFN', u'KMX', u'CCL', u'CAT', u'CBG', u'CBS', u'CELG', u'CNP', u'CTL', u'CERN', u'CF', u'CHRW', u'CHK', u'CVX', u'CMG', u'CB', u'CI', u'CINF', u'CTAS', ...], dtype='object')




```
# get the columns
sp500.columns
```




    Index([u'Sector', u'Price', u'Book Value'], dtype='object')



## Monthly stock historical prices


```
# first three lines of the file
!head -n 3 data/omh.csv # max or Linux
# type data/omh.csv # on windows, but prints the entire file
```

    Date,MSFT,AAPL
    2014-12-01,48.62,115.07
    2014-12-02,48.46,114.63



```
# read in the data
one_mon_hist = pd.read_csv("data/omh.csv")
# examine the first three rows
one_mon_hist[:3]
```




             Date   MSFT    AAPL
    0  2014-12-01  48.62  115.07
    1  2014-12-02  48.46  114.63
    2  2014-12-03  48.08  115.93



# Selecting columns of a DataFrame


```
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




```
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




```
# it's a DataFrame, not a Series
type(sp500[[1]].head())
```




    pandas.core.frame.DataFrame




```
# this is an exception, hence it is commented
# this tries to find a column named '1'
# not the row at position 1
# df = sp500[1]
```


```
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




```
# this is not an exception
df[1]
```




    Symbol
    MMM       141.14
    ABT        39.60
    ABBV       53.95
    ...
    ZMH       101.84
    ZION       28.43
    ZTS        30.53
    Name: 1, Length: 500, dtype: float64




```
# because the column names are actually integers
# and therefore [1] is found as a column
df.columns
```




    Int64Index([0, 1, 2], dtype='int64')




```
# this is a Series not a DataFrame
type(df[1])
```




    pandas.core.series.Series




```
# get price column by name
# result is a Series
sp500['Price']
```




    Symbol
    MMM       141.14
    ABT        39.60
    ABBV       53.95
    ...
    ZMH       101.84
    ZION       28.43
    ZTS        30.53
    Name: Price, Length: 500, dtype: float64




```
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




```
# attribute access of column by name
sp500.Price
```




    Symbol
    MMM       141.14
    ABT        39.60
    ABBV       53.95
    ...
    ZMH       101.84
    ZION       28.43
    ZTS        30.53
    Name: Price, Length: 500, dtype: float64




```
# get the position of the column with value of Price
loc = sp500.columns.get_loc('Price')
loc
```




    1



# Selecting rows of a DataFrame

## Slicing using the [] operator


```
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




```
# ABT through ACN labels
sp500['ABT':'ACN']
```




                            Sector  Price  Book Value
    Symbol                                           
    ABT                Health Care  39.60      15.573
    ABBV               Health Care  53.95       2.954
    ACN     Information Technology  79.79       8.326



## Selecting rows by index label and location: .loc[] and .iloc[]


```
# get row with label MMM
# returned as a Series
sp500.loc['MMM']
```




    Sector        Industrials
    Price              141.14
    Book Value         26.668
    Name: MMM, dtype: object




```
# rows with label MMM and MSFT
# this is a DataFrame result
sp500.loc[['MMM', 'MSFT']]
```




                            Sector   Price  Book Value
    Symbol                                            
    MMM                Industrials  141.14      26.668
    MSFT    Information Technology   40.12      10.584




```
# get rows in location 0 and 2
sp500.iloc[[0, 2]]
```




                 Sector   Price  Book Value
    Symbol                                 
    MMM     Industrials  141.14      26.668
    ABBV    Health Care   53.95       2.954




```
# get the location of MMM and A in the index
i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
"{0} {1}".format(i1, i2)
```




    '0 10'




```
# and get the rows
sp500.iloc[[i1, i2]]
```




                 Sector   Price  Book Value
    Symbol                                 
    MMM     Industrials  141.14      26.668
    A       Health Care   56.18      16.928



## Selecting rows by index label and/or location: .ix[]


```
# by label
sp500.ix[['MSFT', 'ZTS']]
```




                            Sector  Price  Book Value
    Symbol                                           
    MSFT    Information Technology  40.12      10.584
    ZTS                Health Care  30.53       2.150




```
# by location
sp500.ix[[10, 200, 450]]
```




                      Sector  Price  Book Value
    Symbol                                     
    A            Health Care  56.18      16.928
    GIS     Consumer Staples  53.81      10.236
    TRV           Financials  92.86      73.056



## Scalar lookup by label or location using .at[] and .iat[] 


```
# by label in both the index and column
sp500.at['MMM', 'Price']
```




    141.13999999999999




```
# by location.  Row 0, column 1
sp500.iat[0, 1]
```




    141.13999999999999



## Selecting rows by Boolean selection


```
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




```
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




```
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



# Modifying the structure and contents of a DataFrame

## Renaming Columns


```
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




```
# verify the columns in the original did not change
sp500.columns
```




    Index([u'Sector', u'Price', u'Book Value'], dtype='object')




```
# this changes the column in-place
sp500.rename(columns=                  
             {'Book Value': 'BookValue'},                   
             inplace=True)
# we can see the column is changed
sp500.columns
```




    Index([u'Sector', u'Price', u'BookValue'], dtype='object')




```
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



## Adding and inserting columns	


```
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




```
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




```
# extract the first four rows and just the Price column
rcopy = sp500[0:3][['Price']].copy()
rcopy
```




             Price
    Symbol        
    MMM     141.14
    ABT      39.60
    ABBV     53.95




```
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




```
# add rcopy into a column named 'Comment'
rcopy['Comment'] = s
rcopy
```




             Price              Comment
    Symbol                             
    MMM     141.14  Is in the DataFrame
    ABT      39.60                  NaN
    ABBV     53.95                  NaN



## Replacing the contents of a column


```
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




```
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




```
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



## Deleting columns in a DataFrame


```
# Example of using del to delete a column
# make a copy of a subset of the data frame
copy = sp500[:2].copy()
copy
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573




```
# delete the BookValue column
# deletion is in-place
del copy['BookValue']
copy
```




                 Sector   Price
    Symbol                     
    MMM     Industrials  141.14
    ABT     Health Care   39.60




```
# Example of using pop to remove a column from a DataFrame
# first make a copy of a subset of the data frame
# pop works in place
copy = sp500[:2].copy()
# this will remove Sector and return it as a series
popped = copy.pop('Sector')
# Sector column removed in-place
copy
```




             Price  BookValue
    Symbol                   
    MMM     141.14     26.668
    ABT      39.60     15.573




```
# and we have the Sector column as the result of the pop
popped
```




    Symbol
    MMM       Industrials
    ABT       Health Care
    Name: Sector, dtype: object




```
# Example of using drop to remove a column 
# make a copy of a subset of the data frame
copy = sp500[:2].copy()
# this will return a new DataFrame with 'Sector’ removed
# the copy DataFrame is not modified
afterdrop = copy.drop(['Sector'], axis = 1)
afterdrop
```




             Price  BookValue
    Symbol                   
    MMM     141.14     26.668
    ABT      39.60     15.573



## Adding rows to a DataFrame

### Appending rows with .append()


```
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




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954
    A       Health Care   56.18     16.928
    GAS       Utilities   52.98     32.462
    ABBV    Health Care   53.95      2.954




```
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
    MMM       0
    ABT       0
    ABBV      0




```
# append df1 and df3
# each has three rows, so 6 rows is the result
# df1 had no PER column, so NaN from for those rows
# df3 had no BookValue, Price or Sector, so NaN's
df1.append(df3)
```




            BookValue  PER   Price       Sector
    Symbol                                     
    MMM        26.668  NaN  141.14  Industrials
    ABT        15.573  NaN   39.60  Health Care
    ABBV        2.954  NaN   53.95  Health Care
    MMM           NaN    0     NaN          NaN
    ABT           NaN    0     NaN          NaN
    ABBV          NaN    0     NaN          NaN




```
# ignore index labels, create default index
df1.append(df3, ignore_index=True)
```




       BookValue  PER   Price       Sector
    0     26.668  NaN  141.14  Industrials
    1     15.573  NaN   39.60  Health Care
    2      2.954  NaN   53.95  Health Care
    3        NaN    0     NaN          NaN
    4        NaN    0     NaN          NaN
    5        NaN    0     NaN          NaN



### Concatenating DataFrame objects with pd.concat()


```
# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# pass them as a list
pd.concat([df1, df2])
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954
    A       Health Care   56.18     16.928
    GAS       Utilities   52.98     32.462
    ABBV    Health Care   53.95      2.954




```
# copy df2
df2_2 = df2.copy()
# add a column to df2_2 that is not in df1
df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
# see what it looks like
df2_2
```




                 Sector  Price  BookValue  Foo
    Symbol                                    
    A       Health Care  56.18     16.928    0
    GAS       Utilities  52.98     32.462    0
    ABBV    Health Care  53.95      2.954    0




```
# now concatenate
pd.concat([df1, df2_2])
```




            BookValue  Foo   Price       Sector
    Symbol                                     
    MMM        26.668  NaN  141.14  Industrials
    ABT        15.573  NaN   39.60  Health Care
    ABBV        2.954  NaN   53.95  Health Care
    A          16.928    0   56.18  Health Care
    GAS        32.462    0   52.98    Utilities
    ABBV        2.954    0   53.95  Health Care




```
# specify keys
r = pd.concat([df1, df2_2], keys=['df1', 'df2'])
r
```




                BookValue  Foo   Price       Sector
        Symbol                                     
    df1 MMM        26.668  NaN  141.14  Industrials
        ABT        15.573  NaN   39.60  Health Care
        ABBV        2.954  NaN   53.95  Health Care
    df2 A          16.928    0   56.18  Health Care
        GAS        32.462    0   52.98    Utilities
        ABBV        2.954    0   53.95  Health Care




```
# first three rows, columns 0 and 1
df3 = sp500[:3][[0, 1]]
df3
```




                 Sector   Price
    Symbol                     
    MMM     Industrials  141.14
    ABT     Health Care   39.60
    ABBV    Health Care   53.95




```
# first three rows, column 2
df4 = sp500[:3][[2]]
df4
```




            BookValue
    Symbol           
    MMM        26.668
    ABT        15.573
    ABBV        2.954




```
# put them back together
pd.concat([df3, df4], axis=1)
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954




```
# make a copy of df4
df4_2 = df4.copy()
# add a column to df4_2, that is also in df3
df4_2.insert(1, 'Sector', pd.Series(1, index=df4_2.index))
df4_2
```




            BookValue  Sector
    Symbol                   
    MMM        26.668       1
    ABT        15.573       1
    ABBV        2.954       1




```
# demonstrate duplicate columns
pd.concat([df3, df4_2], axis=1)
```




                 Sector   Price  BookValue  Sector
    Symbol                                        
    MMM     Industrials  141.14     26.668       1
    ABT     Health Care   39.60     15.573       1
    ABBV    Health Care   53.95      2.954       1




```
# first three rows and first two columns
df5 = sp500[:3][[0, 1]]
df5
```




                 Sector   Price
    Symbol                     
    MMM     Industrials  141.14
    ABT     Health Care   39.60
    ABBV    Health Care   53.95




```
# row 2 through 4 and first two columns
df6 = sp500[2:5][[0,1]]
df6
```




                            Sector   Price
    Symbol                                
    ABBV               Health Care   53.95
    ACN     Information Technology   79.79
    ACE                 Financials  102.91




```
# inner join on index labels will return in only one row
pd.concat([df5, df6], join='inner', axis=1)
```




                 Sector  Price       Sector  Price
    Symbol                                        
    ABBV    Health Care  53.95  Health Care  53.95



### Adding rows via setting with enlargement


```
# get a small subset of the sp500 
# make sure to copy the slice to make a copy
ss = sp500[:3].copy()
# create a new row with index label FOO
# and assign some values to the columns via a list
ss.loc['FOO'] = ['the sector', 100, 110]
ss
```




               Sector   Price  BookValue
    MMM   Industrials  141.14     26.668
    ABT   Health Care   39.60     15.573
    ABBV  Health Care   53.95      2.954
    FOO    the sector  100.00    110.000




```
# copy of subset / slice
ss = sp500[:3].copy()
# add the new column initialized to 0
ss.loc[:,'PER'] = 0
# take a look at the results
ss
```




                 Sector   Price  BookValue  PER
    Symbol                                     
    MMM     Industrials  141.14     26.668    0
    ABT     Health Care   39.60     15.573    0
    ABBV    Health Care   53.95      2.954    0



## Removing rows from a DataFrame


```
# get a copy of the first 5 rows of sp500
ss = sp500[:5].copy()
ss
```




                            Sector   Price  BookValue
    Symbol                                           
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care   53.95      2.954
    ACN     Information Technology   79.79      8.326
    ACE                 Financials  102.91     86.897




```
# drop rows with labels ABT and ACN
afterdrop = ss.drop(['ABT', 'ACN'])
afterdrop
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABBV    Health Care   53.95      2.954
    ACE      Financials  102.91     86.897




```
# note that ss is not modified
ss
```




                            Sector   Price  BookValue
    Symbol                                           
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care   53.95      2.954
    ACN     Information Technology   79.79      8.326
    ACE                 Financials  102.91     86.897



### Removing rows using Boolean selection


```
# determine the rows where Price > 300
selection = sp500.Price > 300
# to make output shorter, report the # of rows returned (500), 
# and the sum of those where Price > 300 (which is 10)
"{0} {1}".format(len(selection), selection.sum())
```




    '500 10'




```
# select the complement
withPriceLessThan300 = sp500[~selection]
withPriceLessThan300
```




                            Sector   Price  BookValue
    Symbol                                           
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care   53.95      2.954
    ACN     Information Technology   79.79      8.326
    ACE                 Financials  102.91     86.897
    ...                        ...     ...        ...
    YHOO    Information Technology   35.02     12.768
    YUM     Consumer Discretionary   74.77      5.147
    ZMH                Health Care  101.84     37.181
    ZION                Financials   28.43     30.191
    ZTS                Health Care   30.53      2.150
    
    [490 rows x 3 columns]



### Removing rows using a slice


```
# get only the first three rows
onlyFirstThree = sp500[:3]
onlyFirstThree
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954




```
# first three, but a copy of them
onlyFirstThree = sp500[:3].copy()
onlyFirstThree
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954



## Changing scalar values in a DataFrame


```
# get a subset / copy of the data
subset = sp500[:3].copy()
subset
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABT     Health Care   39.60     15.573
    ABBV    Health Care   53.95      2.954




```
# change scalar by label on row and column
subset.ix['MMM', 'Price'] = 0
subset
```




                 Sector  Price  BookValue
    Symbol                               
    MMM     Industrials   0.00     26.668
    ABT     Health Care  39.60     15.573
    ABBV    Health Care  53.95      2.954




```
subset = sp500[:3].copy()
subset.loc['MMM', 'Price'] = 10
subset.loc['ABBV', 'Price'] = 20
subset
```




                 Sector  Price  BookValue
    Symbol                               
    MMM     Industrials   10.0     26.668
    ABT     Health Care   39.6     15.573
    ABBV    Health Care   20.0      2.954




```
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




                 Sector    Price  BookValue
    Symbol                                 
    MMM     Industrials   141.14     26.668
    ABT     Health Care  1000.00     15.573
    ABBV    Health Care    53.95      2.954



# Arithmetic on a DataFrame


```
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




```
# multiply everything by 2
df * 2
```




              A         B         C         D
    0  0.938225 -0.565727 -3.018117 -2.271265
    1  2.424224 -0.346429  0.238417 -2.088472
    2 -1.723698 -4.209138 -0.989859  2.143608
    3  1.443110 -1.413542 -2.079150  0.543720
    4 -0.849945  1.134041  0.552464 -2.174801




```
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




```
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




```
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




```
# get rows 1 through three, and only B, C columns
subframe = df[1:4][['B', 'C']]
# we have extracted a little square in the middle of df
subframe
```




              B         C
    1 -0.173215  0.119209
    2 -2.104569 -0.494929
    3 -0.706771 -1.039575




```
# demonstrate the alignment of the subtraction
df - subframe
```




        A   B   C   D
    0 NaN NaN NaN NaN
    1 NaN   0   0 NaN
    2 NaN   0   0 NaN
    3 NaN   0   0 NaN
    4 NaN NaN NaN NaN




```
# get the A column
a_col = df['A']
df.sub(a_col, axis=0)
```




       A         B         C         D
    0  0 -0.751976 -1.978171 -1.604745
    1  0 -1.385327 -1.092903 -2.256348
    2  0 -1.242720  0.366920  1.933653
    3  0 -1.428326 -1.761130 -0.449695
    4  0  0.991993  0.701204 -0.662428



# Resetting and reindexing


```
# reset the index, moving it into a column
reset_sp500 = sp500.reset_index()
reset_sp500
```




        Symbol                  Sector   Price  BookValue
    0      MMM             Industrials  141.14     26.668
    1      ABT             Health Care   39.60     15.573
    2     ABBV             Health Care   53.95      2.954
    3      ACN  Information Technology   79.79      8.326
    4      ACE              Financials  102.91     86.897
    ..     ...                     ...     ...        ...
    495   YHOO  Information Technology   35.02     12.768
    496    YUM  Consumer Discretionary   74.77      5.147
    497    ZMH             Health Care  101.84     37.181
    498   ZION              Financials   28.43     30.191
    499    ZTS             Health Care   30.53      2.150
    
    [500 rows x 4 columns]




```
# move the Symbol column into the index
reset_sp500.set_index('Symbol')
```




                            Sector   Price  BookValue
    Symbol                                           
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care   53.95      2.954
    ACN     Information Technology   79.79      8.326
    ACE                 Financials  102.91     86.897
    ...                        ...     ...        ...
    YHOO    Information Technology   35.02     12.768
    YUM     Consumer Discretionary   74.77      5.147
    ZMH                Health Care  101.84     37.181
    ZION                Financials   28.43     30.191
    ZTS                Health Care   30.53      2.150
    
    [500 rows x 3 columns]




```
# get first four rows
subset = sp500[:4].copy()
subset
```




                            Sector   Price  BookValue
    Symbol                                           
    MMM                Industrials  141.14     26.668
    ABT                Health Care   39.60     15.573
    ABBV               Health Care   53.95      2.954
    ACN     Information Technology   79.79      8.326




```
# reindex to have MMM, ABBV, and FOO index labels
reindexed = subset.reindex(index=['MMM', 'ABBV', 'FOO'])
# note that ABT and ACN are dropped and FOO has NaN values
reindexed
```




                 Sector   Price  BookValue
    Symbol                                
    MMM     Industrials  141.14     26.668
    ABBV    Health Care   53.95      2.954
    FOO             NaN     NaN        NaN




```
# reindex columns
subset.reindex(columns=['Price', 
                        'Book Value', 
                        'NewCol'])
```




             Price  Book Value  NewCol
    Symbol                            
    MMM     141.14         NaN     NaN
    ABT      39.60         NaN     NaN
    ABBV     53.95         NaN     NaN
    ACN      79.79         NaN     NaN



# Hierarchical indexing


```
# first, push symbol into a column
reindexed = sp500.reset_index()
# and now index sp500 by sector and symbol
multi_fi = reindexed.set_index(['Sector', 'Symbol'])
multi_fi
```




                                    Price  BookValue
    Sector                 Symbol                   
    Industrials            MMM     141.14     26.668
    Health Care            ABT      39.60     15.573
                           ABBV     53.95      2.954
    Information Technology ACN      79.79      8.326
    Financials             ACE     102.91     86.897
    ...                               ...        ...
    Information Technology YHOO     35.02     12.768
    Consumer Discretionary YUM      74.77      5.147
    Health Care            ZMH     101.84     37.181
    Financials             ZION     28.43     30.191
    Health Care            ZTS      30.53      2.150
    
    [500 rows x 2 columns]




```
# the index is a MultiIndex
type(multi_fi.index)
```




    pandas.core.index.MultiIndex




```
# examine the index
print (multi_fi.index)
```

    Sector                       Symbol
    Industrials                  MMM   
    Health Care                  ABT   
                                 ABBV  
    Information Technology       ACN   
                    ...                
    Information Technology       YHOO  
    Consumer Discretionary       YUM   
    Health Care                  ZMH   
    Financials                   ZION  
    Health Care                  ZTS   
    


```
# this has two levels
len(multi_fi.index.levels)
```




    2




```
# each index level is an index
multi_fi.index.levels[0]
```




    Index([u'Consumer Discretionary', u'Consumer Discretionary ', u'Consumer Staples', u'Consumer Staples ', u'Energy', u'Financials', u'Health Care', u'Industrials', u'Industries', u'Information Technology', u'Materials', u'Telecommunications Services', u'Utilities'], dtype='object')




```
# each index level is an index
multi_fi.index.levels[1]
```




    Index([u'A', u'AA', u'AAPL', u'ABBV', u'ABC', u'ABT', u'ACE', u'ACN', u'ACT', u'ADBE', u'ADI', u'ADM', u'ADP', u'ADS', u'ADSK', u'ADT', u'AEE', u'AEP', u'AES', u'AET', u'AFL', u'AGN', u'AIG', u'AIV', u'AIZ', u'AKAM', u'ALL', u'ALLE', u'ALTR', u'ALXN', u'AMAT', u'AME', u'AMGN', u'AMP', u'AMT', u'AMZN', u'AN', u'AON', u'APA', u'APC', u'APD', u'APH', u'ARG', u'ATI', u'AVB', u'AVP', u'AVY', u'AXP', u'AZO', u'BA', u'BAC', u'BAX', u'BBBY', u'BBT', u'BBY', u'BCR', u'BDX', u'BEAM', u'BEN', u'BF-B', u'BHI', u'BIIB', u'BK', u'BLK', u'BLL', u'BMS', u'BMY', u'BRCM', u'BRK-B', u'BSX', u'BTU', u'BWA', u'BXP', u'C', u'CA', u'CAG', u'CAH', u'CAM', u'CAT', u'CB', u'CBG', u'CBS', u'CCE', u'CCI', u'CCL', u'CELG', u'CERN', u'CF', u'CFN', u'CHK', u'CHRW', u'CI', u'CINF', u'CL', u'CLF', u'CLX', u'CMA', u'CMCSA', u'CME', u'CMG', ...], dtype='object')




```
# values of index level 0
multi_fi.index.get_level_values(0)
```




    Index([u'Industrials', u'Health Care', u'Health Care', u'Information Technology', u'Financials', u'Health Care', u'Information Technology', u'Utilities', u'Health Care', u'Financials', u'Health Care', u'Utilities', u'Materials', u'Materials', u'Information Technology', u'Materials', u'Health Care', u'Materials', u'Industrials', u'Health Care', u'Information Technology', u'Financials', u'Information Technology', u'Consumer Staples', u'Consumer Discretionary', u'Utilities', u'Utilities', u'Financials', u'Financials', u'Financials', u'Financials', u'Health Care', u'Information Technology', u'Health Care', u'Industrials', u'Energy', u'Information Technology', u'Financials', u'Energy', u'Financials', u'Information Technology', u'Information Technology', u'Consumer Staples', u'Financials', u'Telecommunications Services', u'Information Technology', u'Information Technology', u'Consumer Discretionary', u'Consumer Discretionary', u'Financials', u'Industrials', u'Consumer Staples', u'Energy', u'Materials', u'Financials', u'Health Care', u'Health Care', u'Financials', u'Consumer Discretionary', u'Health Care', u'Consumer Discretionary', u'Materials', u'Financials', u'Consumer Discretionary', u'Health Care', u'Financials', u'Consumer Discretionary', u'Industrials', u'Consumer Discretionary', u'Financials', u'Health Care', u'Health Care', u'Information Technology', u'Consumer Staples', u'Information Technology', u'Consumer Discretionary', u'Energy', u'Energy', u'Consumer Staples', u'Financials', u'Health Care', u'Health Care', u'Consumer Discretionary', u'Consumer Discretionary', u'Industrials', u'Financials', u'Consumer Discretionary', u'Health Care', u'Utilities', u'Telecommunications Services', u'Health Care', u'Materials', u'Industrials', u'Energy', u'Energy', u'Consumer Discretionary', u'Financials', u'Health Care', u'Financials', u'Industrials', ...], dtype='object')




```
# get all stocks that are Industrials
# note the result drops level 0 of the index
multi_fi.xs('Industrials')
```




             Price  BookValue
    Symbol                   
    MMM     141.14     26.668
    ALLE     52.46      0.000
    APH      95.71     18.315
    AVY      48.20     15.616
    BA      132.41     19.870
    ...        ...        ...
    UNP     196.26     46.957
    UPS     102.73      6.790
    UTX     115.54     35.252
    WM       43.37     12.330
    XYL      38.42     12.127
    
    [64 rows x 2 columns]




```
# select rows where level 1 (Symbol) is ALLE
# note that the Sector level is dropped from the result
multi_fi.xs('ALLE', level=1)
```




                 Price  BookValue
    Sector                       
    Industrials  52.46          0




```
# Industrials, without dropping the level
multi_fi.xs('Industrials', drop_level=False)
```




                         Price  BookValue
    Sector      Symbol                   
    Industrials MMM     141.14     26.668
                ALLE     52.46      0.000
                APH      95.71     18.315
                AVY      48.20     15.616
                BA      132.41     19.870
    ...                    ...        ...
                UNP     196.26     46.957
                UPS     102.73      6.790
                UTX     115.54     35.252
                WM       43.37     12.330
                XYL      38.42     12.127
    
    [64 rows x 2 columns]




```
# drill through the levels
multi_fi.xs('Industrials').xs('UPS')
```




    Price        102.73
    BookValue      6.79
    Name: UPS, dtype: float64




```
# drill through using tuples
multi_fi.xs(('Industrials', 'UPS'))
```




    Price        102.73
    BookValue      6.79
    Name: (Industrials, UPS), dtype: float64



# Summarized data and descriptive statistics


```
# calc the mean of the values in each column
one_mon_hist.mean()
```




    MSFT     47.493182
    AAPL    112.411364
    dtype: float64




```
# calc the mean of the values in each row
one_mon_hist.mean(axis=1)
```




    0    81.845
    1    81.545
    2    82.005
    ...
    19    80.680
    20    79.770
    21    78.415
    Length: 22, dtype: float64




```
# calc the variance of the values in each column
one_mon_hist.var()
```




    MSFT    0.870632
    AAPL    5.706231
    dtype: float64




```
# calc the median of the values in each column
one_mon_hist.median()
```




    MSFT     47.625
    AAPL    112.530
    dtype: float64




```
# location of min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].min()
```




    MSFT     45.16
    AAPL    106.75
    dtype: float64




```
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].max()
```




    MSFT     48.84
    AAPL    115.93
    dtype: float64




```
# location of min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].idxmin()
```




    MSFT    11
    AAPL    11
    dtype: int64




```
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].idxmax()
```




    MSFT    3
    AAPL    2
    dtype: int64




```
# find the mode of this Series
s = pd.Series([1, 2, 3, 3, 5])
s.mode()
```




    0    3
    dtype: int64




```
# there can be more than one mode
s = pd.Series([1, 2, 3, 3, 5, 1])
s.mode()
```




    0    1
    1    3
    dtype: int64




```
# calculate a cumulative product
pd.Series([1, 2, 3, 4]).cumprod()
```




    0     1
    1     2
    2     6
    3    24
    dtype: int64




```
# calculate a cumulative sum
pd.Series([1, 2, 3, 4]).cumsum()
```




    0     1
    1     3
    2     6
    3    10
    dtype: int64




```
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




```
# get summary stats on non-numeric data
s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
s.describe()
```




    count     4
    unique    3
    top       a
    freq      2
    dtype: object




```
# get summary stats on non-numeric data
s.count()
```




    4




```
# return a list of unique items
s.unique()
```




    array(['a', 'b', 'c', nan], dtype=object)




```
# number of occurrences of each unique value
s.value_counts()
```




    a    2
    b    1
    c    1
    dtype: int64


