
# Chapter 6: Accessing Data
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 6: Accessing Data](#chapter-6-accessing-data)
  * [6.1 Setting up the IPython notebook](#61-setting-up-the-ipython-notebook)
    * [CSV and Text/Tabular format](#csv-and-texttabular-format)
  * [The sample CSV data set](#the-sample-csv-data-set)
    * [General field-delimited data](#general-field-delimited-data)
    * [Reading and writing data in an Excel format](#reading-and-writing-data-in-an-excel-format)
  * [6.2 Reading and writing JSON files](#62-reading-and-writing-json-files)
    * [Reading HTML data from the Web](#reading-html-data-from-the-web)
    * [Reading and writing HDF5 format files](#reading-and-writing-hdf5-format-files)
  * [6.3 Accessing data on the web and in the cloud](#63-accessing-data-on-the-web-and-in-the-cloud)
  * [6.4 Reading and writing from/to SQL databases](#64-reading-and-writing-fromto-sql-databases)
  * [6.5 Reading data from remote data services](#65-reading-data-from-remote-data-services)
    * [Reading stock data from Yahoo! and Google Finance](#reading-stock-data-from-yahoo-and-google-finance)
  * [6.6 Summary](#66-summary)

<!-- tocstop -->


## 6.1 Setting up the IPython notebook


```python
# import pandas and numpy
import numpy as np
import pandas as pd

# Set some pandas options for controlling output
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

### CSV and Text/Tabular format

## The sample CSV data set

* The sample CSV data set


```python
# view the first five lines of data/msft.csv
!head -n 5 data/msft.csv # mac or Linux
# type data/msft.csv # on windows, but shows the entire file
```

    'head' is not recognized as an internal or external command,
    operable program or batch file.


* Reading a CSV file into a DataFrame


```python
# read in msft.csv into a DataFrame
msft = pd.read_csv("data/msft.csv")
msft.head()
```




             Date   Open   High    Low  Close   Volume  Adj Close
    0  2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    1  2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    2  2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63
    3  2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91
    4  2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58



* Specifying the index column when reading CSV file


```python
# use column 0 as the index
msft = pd.read_csv("data/msft.csv", index_col=0)
msft.head()
```




                 Open   High    Low  Close   Volume  Adj Close
    Date
    2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63
    2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91
    2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58



* Data type inference and specification


```python
# examine the types of the columns in this DataFrame
msft.dtypes
```




    Open         float64
    High         float64
    Low          float64
    Close        float64
    Volume         int64
    Adj Close    float64
    dtype: object




```python
# specify that the Volume column should be a float64
msft = pd.read_csv("data/msft.csv",
                   dtype = { 'Volume' : np.float64})
msft.dtypes
```




    Date          object
    Open         float64
    High         float64
    Low          float64
    Close        float64
    Volume       float64
    Adj Close    float64
    dtype: object



* Specifying column names


```python
# specify a new set of names for the columns
# all lower case, remove space in Adj Close
# also, header=0 skips the header row
df = pd.read_csv("data/msft.csv",
                 header=0,
                 names=['open', 'high', 'low',
                        'close', 'volume', 'adjclose'])
df.head()
```




                 open   high    low  close   volume  adjclose
    2014-07-21  83.46  83.53  81.81  81.93  2359300     81.93
    2014-07-18  83.30  83.40  82.52  83.35  4020800     83.35
    2014-07-17  84.35  84.63  83.33  83.63  1974000     83.63
    2014-07-16  83.77  84.91  83.66  84.91  1755600     84.91
    2014-07-15  84.30  84.38  83.20  83.58  1874700     83.58



* Specifying specific columns to load


```python
# read in data only in the Date and Close columns
# and index by the Date column
df2 = pd.read_csv("data/msft.csv",
                  usecols=['Date', 'Close'],
                  index_col=['Date'])
df2.head()
```




                Close
    Date
    2014-07-21  81.93
    2014-07-18  83.35
    2014-07-17  83.63
    2014-07-16  84.91
    2014-07-15  83.58



* Saving DataFrame to a CSV file


```python
# save df2 to a new csv file
# also specify naming the index as date
df2.to_csv("data/msft_modified.csv", index_label='date')
```


```python
# view the start of the file just saved
!head data/msft_modified.csv
#type data/msft_modified.csv # windows
```

    date,Close

    2014-07-21,81.93

    2014-07-18,83.35

    2014-07-17,83.63

    2014-07-16,84.91

    2014-07-15,83.58

    2014-07-14,84.4

    2014-07-11,83.35

    2014-07-10,83.42

    2014-07-09,85.5



### General field-delimited data


```python
# use read_table with sep=',' to read a CSV
df = pd.read_table("data/msft.csv", sep=',')
df.head()
```




             Date   Open   High    Low  Close   Volume  Adj Close
    0  2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    1  2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    2  2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63
    3  2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91
    4  2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58




```python
# save as pipe delimited
df.to_csv("data/msft_piped.txt", sep='|')
# check that it worked
!head -n 5 data/msft_piped.txt # osx or Linux
# type data/psft_piped.txt # on windows
```

    |Date|Open|High|Low|Close|Volume|Adj Close

    0|2014-07-21|83.46|83.53|81.81|81.93|2359300|81.93

    1|2014-07-18|83.3|83.4|82.52|83.35|4020800|83.35

    2|2014-07-17|84.35|84.63|83.33|83.63|1974000|83.63

    3|2014-07-16|83.77|84.91|83.66|84.91|1755600|84.91



* Handling noise rows in field-delimited data


```python
# messy file
!head data/msft2.csv # osx or Linux
# type data/msft2.csv # windows
```

    This is fun because the data does not start on the first line

    Date,Open,High,Low,Close,Volume,Adj Close



    And there is space between the header row and data

    2014-07-21,83.46,83.53,81.81,81.93,2359300,81.93

    2014-07-18,83.30,83.40,82.52,83.35,4020800,83.35

    2014-07-17,84.35,84.63,83.33,83.63,1974000,83.63

    2014-07-16,83.77,84.91,83.66,84.91,1755600,84.91

    2014-07-15,84.30,84.38,83.20,83.58,1874700,83.58

    2014-07-14,83.66,84.64,83.11,84.40,1432100,84.40




```python
# read, but skip rows 0, 2 and 3
df = pd.read_csv("data/msft2.csv", skiprows=[0, 2, 3])
df
```




             Date   Open   High    Low  Close   Volume  Adj Close
    0         NaN    NaN    NaN    NaN    NaN      NaN        NaN
    1  2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    2  2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    3  2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63
    4  2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91
    5  2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58
    6  2014-07-14  83.66  84.64  83.11  84.40  1432100      84.40
    7  2014-07-11  83.55  83.98  82.85  83.35  2001400      83.35
    8  2014-07-10  85.20  85.57  83.36  83.42  2713300      83.42
    9  2014-07-09  84.83  85.79  84.76  85.50  1540700      85.50




```python
# another messy file, with the mess at the end
!cat data/msft_with_footer.csv # osx or Linux
# type data/msft_with_footer.csv # windows
```

    Date,Open,High,Low,Close,Volume,Adj Close

    2014-07-21,83.46,83.53,81.81,81.93,2359300,81.93

    2014-07-18,83.30,83.40,82.52,83.35,4020800,83.35



    Uh oh, there is stuff at the end.


```python
# skip only two lines at the end
df = pd.read_csv("data/msft_with_footer.csv",
                 skip_footer=2,
                 engine = 'python')
df
```




             Date   Open   High    Low  Close   Volume  Adj Close
    0  2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    1  2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35




```python
# only process the first three rows
pd.read_csv("data/msft.csv", nrows=3)
```




             Date   Open   High    Low  Close   Volume  Adj Close
    0  2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    1  2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    2  2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63




```python
# skip 100 lines, then only process the next five
pd.read_csv("data/msft.csv", skiprows=100, nrows=5,
            header=0,
            names=['open', 'high', 'low', 'close', 'vol',
                   'adjclose'])
```




                 open   high    low  close      vol  adjclose
    2014-03-03  80.35  81.31  79.91  79.97  5004100     77.40
    2014-02-28  82.40  83.42  82.17  83.42  2853200     80.74
    2014-02-27  84.06  84.63  81.63  82.00  3676800     79.36
    2014-02-26  82.92  84.03  82.43  83.81  2623600     81.12
    2014-02-25  83.80  83.80  81.72  83.08  3579100     80.41



### Reading and writing data in an Excel format


```python
# read excel file
# only reads first sheet (msft in this case)
df = pd.read_excel("data/stocks.xlsx")
df.head()
```




            Date   Open   High    Low  Close   Volume  Adj Close
    0 2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93
    1 2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35
    2 2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63
    3 2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91
    4 2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58




```python
# read from the aapl worksheet
aapl = pd.read_excel("data/stocks.xlsx", sheetname='aapl')
aapl.head()
```




            Date   Open   High    Low  Close    Volume  Adj Close
    0 2014-07-21  94.99  95.00  93.72  93.94  38887700      93.94
    1 2014-07-18  93.62  94.74  93.02  94.43  49898600      94.43
    2 2014-07-17  95.03  95.28  92.57  93.09  57152000      93.09
    3 2014-07-16  96.97  97.10  94.74  94.78  53396300      94.78
    4 2014-07-15  96.80  96.85  95.03  95.32  45477900      95.32




```python
# save to an .XLS file, in worksheet 'Sheet1'
df.to_excel("data/stocks2.xls")
```


```python
# write making the worksheet name MSFT
df.to_excel("data/stocks_msft.xls", sheet_name='MSFT')
```


```python
# write multiple sheets
# requires use of the ExcelWriter class
from pandas import ExcelWriter
with ExcelWriter("data/all_stocks.xls") as writer:
    aapl.to_excel(writer, sheet_name='AAPL')
    df.to_excel(writer, sheet_name='MSFT')
```


```python
# write to xlsx
df.to_excel("data/msft2.xlsx")
```

## 6.2 Reading and writing JSON files


```python
# wirite the excel data to a JSON file
df.head().to_json("data/stocks.json")
!cat data/stocks.json # osx or Linux
#type data/stocks.json # windows
```

    {"Date":{"0":1405900800000,"1":1405641600000,"2":1405555200000,"3":1405468800000,"4":1405382400000},"Open":{"0":83.46,"1":83.3,"2":84.35,"3":83.77,"4":84.3},"High":{"0":83.53,"1":83.4,"2":84.63,"3":84.91,"4":84.38},"Low":{"0":81.81,"1":82.52,"2":83.33,"3":83.66,"4":83.2},"Close":{"0":81.93,"1":83.35,"2":83.63,"3":84.91,"4":83.58},"Volume":{"0":2359300,"1":4020800,"2":1974000,"3":1755600,"4":1874700},"Adj Close":{"0":81.93,"1":83.35,"2":83.63,"3":84.91,"4":83.58}}


```python
# read data in from JSON
df_from_json = pd.read_json("data/stocks.json")
df_from_json.head(5)
```




       Adj Close  Close       Date   High    Low   Open   Volume
    0      81.93  81.93 2014-07-21  83.53  81.81  83.46  2359300
    1      83.35  83.35 2014-07-18  83.40  82.52  83.30  4020800
    2      83.63  83.63 2014-07-17  84.63  83.33  84.35  1974000
    3      84.91  84.91 2014-07-16  84.91  83.66  83.77  1755600
    4      83.58  83.58 2014-07-15  84.38  83.20  84.30  1874700



### Reading HTML data from the Web


```python
# the URL to read
url = "http://www.fdic.gov/bank/individual/failed/banklist.html"
# read it
banks = pd.read_html(url)
# examine a subset of the first table read
banks[0][0:5].ix[:,0:4]
```




                               Bank Name       City  ST   CERT
    0               Doral BankEn Espanol   San Juan  PR  32102
    1  Capitol City Bank & Trust Company    Atlanta  GA  33938
    2            Highland Community Bank    Chicago  IL  20290
    3   First National Bank of Crestview  Crestview  FL  17557
    4                 Northern Star Bank    Mankato  MN  34983




```python
# read the stock data
df = pd.read_excel("data/stocks.xlsx")
# write the first two rows to HTML
df.head(2).to_html("data/stocks.html")
# check the first 28 lines of the output
!head -n 28 data/stocks.html # max or Linux
# type data/stocks.html # window, but prints the entire file
```

    <table border="1" class="dataframe">

      <thead>

        <tr style="text-align: right;">

          <th></th>

          <th>Date</th>

          <th>Open</th>

          <th>High</th>

          <th>Low</th>

          <th>Close</th>

          <th>Volume</th>

          <th>Adj Close</th>

        </tr>

      </thead>

      <tbody>

        <tr>

          <th>0</th>

          <td>2014-07-21</td>

          <td> 83.46</td>

          <td> 83.53</td>

          <td> 81.81</td>

          <td> 81.93</td>

          <td> 2359300</td>

          <td> 81.93</td>

        </tr>

        <tr>

          <th>1</th>

          <td>2014-07-18</td>

          <td> 83.30</td>



### Reading and writing HDF5 format files


```python
# seed for replication
np.random.seed(123456)
# create a DataFrame of dates and random numbers in three columns
df = pd.DataFrame(np.random.randn(8, 3),
                  index=pd.date_range('1/1/2000', periods=8),
                  columns=['A', 'B', 'C'])

# create HDF5 store
store = pd.HDFStore('data/store.h5')
store['df'] = df # persisting happened here
store
```




    <class 'pandas.io.pytables.HDFStore'>
    File path: data/store.h5
    /df            frame        (shape->[8,3])




```python
# read in data from HDF5
store = pd.HDFStore("data/store.h5")
df = store['df']
df
```




                       A         B         C
    2000-01-01  0.469112 -0.282863 -1.509059
    2000-01-02 -1.135632  1.212112 -0.173215
    2000-01-03  0.119209 -1.044236 -0.861849
    2000-01-04 -2.104569 -0.494929  1.071804
    2000-01-05  0.721555 -0.706771 -1.039575
    2000-01-06  0.271860 -0.424972  0.567020
    2000-01-07  0.276232 -1.087401 -0.673690
    2000-01-08  0.113648 -1.478427  0.524988




```python
# this changes the DataFrame, but did not persist
df.ix[0].A = 1

# to persist the change, assign the DataFrame to the
# HDF5 store object
store['df'] = df
# it is now persisted

# the following loads the store and
# shows the first two rows, demonstrating
# the the persisting was done
pd.HDFStore("data/store.h5")['df'].head(2) # it's now in there
```




                       A         B         C
    2000-01-01  1.000000 -0.282863 -1.509059
    2000-01-02 -1.135632  1.212112 -0.173215



## 6.3 Accessing data on the web and in the cloud


```python
# read csv directly from Yahoo! Finance from a URL
df = pd.read_csv("http://ichart.yahoo.com/table.csv?s=MSFT&" +
                 "a=5&b=1&c=2014&" +
                 "d=5&e=30&f=2014&" +
                 "g=d&ignore=.csv")
df[:5]
```




             Date   Open   High    Low  Close    Volume  Adj Close
    0  2014-06-30  42.17  42.21  41.70  41.70  30805500      40.89
    1  2014-06-27  41.61  42.29  41.51  42.25  74640000      41.43
    2  2014-06-26  41.93  41.94  41.43  41.72  23604400      40.91
    3  2014-06-25  41.70  42.05  41.46  42.03  20049100      41.21
    4  2014-06-24  41.83  41.94  41.56  41.75  26509100      40.94



## 6.4 Reading and writing from/to SQL databases


```python
# reference SQLite
import sqlite3

# read in the stock data from CSV
msft = pd.read_csv("data/msft.csv")
msft["Symbol"]="MSFT"
aapl = pd.read_csv("data/aapl.csv")
aapl["Symbol"]="AAPL"

# create connection
connection = sqlite3.connect("data/stocks.sqlite")
# .to_sql() will create SQL to store the DataFrame
# in the specified table.  if_exists specifies
# what to do if the table already exists
msft.to_sql("STOCK_DATA", connection, if_exists="replace")
aapl.to_sql("STOCK_DATA", connection, if_exists="append")

# commit the SQL and close the connection
connection.commit()
connection.close()
```

    /Users/michaelheydt/anaconda/lib/python2.7/site-packages/pandas/io/sql.py:1309: UserWarning: The spaces in these column names will not be changed. In pandas versions < 0.14, spaces were converted to underscores.
      warnings.warn(_SAFE_NAMES_WARNING)



```python
# connect to the database file
connection = sqlite3.connect("data/stocks.sqlite")

# query all records in STOCK_DATA
# returns a DataFrame
# inde_col specifies which column to make the DataFrame index
stocks = pd.io.sql.read_sql("SELECT * FROM STOCK_DATA;",
                             connection, index_col='index')

# close the connection
connection.close()

# report the head of the data retrieved
stocks.head()
```




                 Date   Open   High    Low  Close   Volume  Adj Close Symbol
    index
    0      2014-07-21  83.46  83.53  81.81  81.93  2359300      81.93   MSFT
    1      2014-07-18  83.30  83.40  82.52  83.35  4020800      83.35   MSFT
    2      2014-07-17  84.35  84.63  83.33  83.63  1974000      83.63   MSFT
    3      2014-07-16  83.77  84.91  83.66  84.91  1755600      84.91   MSFT
    4      2014-07-15  84.30  84.38  83.20  83.58  1874700      83.58   MSFT




```python
# open the connection
connection = sqlite3.connect("data/stocks.sqlite")

# construct the query string
query = "SELECT * FROM STOCK_DATA WHERE Volume>29200100 AND Symbol='MSFT';"

# execute and close connection
items = pd.io.sql.read_sql(query, connection, index_col='index')
connection.close()

# report the query result
items
```




                 Date   Open   High    Low  Close    Volume  Adj Close Symbol
    index
    1081   2010-05-21  42.22  42.35  40.99  42.00  33610800      36.48   MSFT
    1097   2010-04-29  46.80  46.95  44.65  45.92  47076200      38.41   MSFT
    1826   2007-06-15  89.80  92.10  89.55  92.04  30656400      35.87   MSFT
    3455   2001-03-16  47.00  47.80  46.10  45.33  40806400      17.66   MSFT
    3712   2000-03-17  49.50  50.00  48.29  50.00  50860500      19.48   MSFT



## 6.5 Reading data from remote data services

### Reading stock data from Yahoo! and Google Finance


```python
# import pandas.io.data namespace, alias as web
import pandas.io.data as web
# and datetime for the dates
import datetime

# start end end dates
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2014, 1, 27)

# read the MSFT stock data from yahoo! and view the head
yahoo = web.DataReader('MSFT', 'yahoo', start, end)
yahoo.head()
```




                 Open   High    Low  Close    Volume  Adj Close
    Date
    2012-01-03  26.55  26.96  26.39  26.77  64731500      24.42
    2012-01-04  26.82  27.47  26.78  27.40  80516100      25.00
    2012-01-05  27.38  27.73  27.29  27.68  56081400      25.25
    2012-01-06  27.53  28.19  27.53  28.11  99455500      25.64
    2012-01-09  28.05  28.10  27.72  27.74  59706800      25.31




```python
# read from google and display the head of the data
goog = web.DataReader("MSFT", 'google', start, end)
goog.head()
```




                 Open   High    Low  Close    Volume
    ﻿Date
    2012-01-03  26.55  26.96  26.39  26.76  64735391
    2012-01-04  26.82  27.47  26.78  27.40  80519402
    2012-01-05  27.38  27.73  27.29  27.68  56082205
    2012-01-06  27.53  28.19  27.52  28.10  99459469
    2012-01-09  28.05  28.10  27.72  27.74  59708266



* Retrieving data from Yahoo! Finance Options


```python
# specify we want all yahoo options data for AAPL
# this can take a little time...
aapl = pd.io.data.Options('AAPL', 'yahoo')
# read all the data
data = aapl.get_all_data()
# examine the first six rows and four columns
data.iloc[0:6, 0:4]
```




                                                 Last  Bid  Ask  Chg
    Strike Expiry     Type Symbol
    34.29  2016-01-15 call AAPL160115C00034290  92.00    0    0    0
                      put  AAPL160115P00034290   0.03    0    0    0
    35.71  2016-01-15 call AAPL160115C00035710  90.00    0    0    0
                      put  AAPL160115P00035710   0.04    0    0    0
    37.14  2016-01-15 call AAPL160115C00037140  72.55    0    0    0
                      put  AAPL160115P00037140   0.04    0    0    0




```python
# get all puts at strike price of $80 (first four columns only)
data.loc[(80, slice(None), 'put'), :].iloc[0:5, 0:4]
```




                                                Last  Bid  Ask  Chg
    Strike Expiry     Type Symbol
    80     2015-04-17 put  AAPL150417P00080000  0.01    0    0    0
           2015-05-15 put  AAPL150515P00080000  0.02    0    0    0
           2015-07-17 put  AAPL150717P00080000  0.12    0    0    0
           2015-10-16 put  AAPL151016P00080000  0.34    0    0    0
           2016-01-15 put  AAPL160115P00080000  0.69    0    0    0




```python
# put options at strike of $80, between 2015-01-17 and 2015-04-17
data.loc[(80, slice('20150117','20150417'),
          'put'), :].iloc[:, 0:4]
```




                                                Last  Bid  Ask  Chg
    Strike Expiry     Type Symbol
    80     2015-04-17 put  AAPL150417P00080000  0.01    0    0    0




```python
# msft calls expiring on 2015-01-05
expiry = datetime.date(2015, 1, 5)
msft_calls = pd.io.data.Options('MSFT', 'yahoo').get_call_data(
                                                    expiry=expiry)
msft_calls.iloc[0:5, 0:5]
```




                                                Last  Bid  Ask  Chg PctChg
    Strike Expiry     Type Symbol
    26     2015-04-17 call MSFT150417C00026000  17.0    0    0    0  0.00%
    29     2015-04-17 call MSFT150417C00029000  12.9    0    0    0  0.00%
    30     2015-04-17 call MSFT150417C00030000  11.2    0    0    0  0.00%
    31     2015-04-17 call MSFT150417C00031000  18.6    0    0    0  0.00%
    32     2015-04-17 call MSFT150417C00032000   9.5    0    0    0  0.00%




```python
# msft calls expiring on 2015-01-05
expiry = datetime.date(2015, 1, 17)
aapl_calls = aapl.get_call_data(expiry=expiry)
aapl_calls.iloc[0:5, 0:4]
```




                                                 Last  Bid  Ask  Chg
    Strike Expiry     Type Symbol
    45.71  2015-04-17 call AAPL150417C00045710  80.18    0    0    0
    46.43  2015-04-17 call AAPL150417C00046430  62.42    0    0    0
    47.86  2015-04-17 call AAPL150417C00047860  69.39    0    0    0
    48.57  2015-04-17 call AAPL150417C00048570  71.50    0    0    0
    49.29  2015-04-17 call AAPL150417C00049290  77.25    0    0    0



* Reading economic data from the Federal Reserve Bank of St. Louis


```python
# read GDP data from FRED
gdp = web.DataReader("GDP", "fred",
                     datetime.date(2012, 1, 1),
                     datetime.date(2014, 1, 27))
gdp
```




                    GDP
    DATE
    2012-01-01  15956.5
    2012-04-01  16094.7
    2012-07-01  16268.9
    2012-10-01  16332.5
    2013-01-01  16502.4
    2013-04-01  16619.2
    2013-07-01  16872.3
    2013-10-01  17078.3
    2014-01-01  17044.0




```python
# Get Compensation of employees: Wages and salaries
web.DataReader("A576RC1A027NBEA",
               "fred",
               datetime.date(1929, 1, 1),
               datetime.date(2013, 1, 1))
```




                A576RC1A027NBEA
    DATE
    1929-01-01             50.5
    1930-01-01             46.2
    1931-01-01             39.2
    1932-01-01             30.5
    1933-01-01             29.0
    ...                     ...
    2009-01-01           6251.4
    2010-01-01           6377.5
    2011-01-01           6633.2
    2012-01-01           6932.1
    2013-01-01           7124.7

    [85 rows x 1 columns]



* Accessing Kenneth French's data


```python
# read from Kenneth French fama global factors data set
factors = web.DataReader("Global_Factors", "famafrench")
factors
```




    {3:         1 Mkt-RF  2 SMB  3 HML  4 WML  5 RF
     199007      0.79   0.07   0.24 -99.99  0.68
     199008    -10.76  -1.56   0.42 -99.99  0.66
     199009    -12.24   1.68   0.34 -99.99  0.60
     199010      9.58  -8.11  -3.29 -99.99  0.68
     199011     -3.87   1.62   0.68  -0.32  0.57
     ...          ...    ...    ...    ...   ...
     201411      1.67  -2.14  -1.92   0.65  0.00
     201412     -1.45   1.89  -0.33   1.06  0.00
     201501     -1.75   0.04  -2.78   4.50  0.00
     201502      5.93  -0.17  -0.30  -1.93  0.00
     201503     -1.20   1.54  -0.89   2.07  0.00

     [297 rows x 5 columns]}



* Reading from the World Bank


```python
# make referencing pandas.io.wb a little less typing
import pandas.io.wb as wb
# get all indicators
all_indicators = wb.get_indicators()
```


```python
# examine some of the indicators
all_indicators.ix[:,0:1]
```




                                      id
    0                 1.0.HCount.1.25usd
    1                   1.0.HCount.10usd
    2                  1.0.HCount.2.5usd
    3               1.0.HCount.Mid10to50
    4                    1.0.HCount.Ofcl
    ...                              ...
    12546      per_sionl.overlap_pop_urb
    12547  per_sionl.overlap_q1_preT_tot
    12548       per_sionl.overlap_q1_rur
    12549       per_sionl.overlap_q1_tot
    12550       per_sionl.overlap_q1_urb

    [12551 rows x 1 columns]




```python
# search of life expectancy indicators
le_indicators = wb.search("life expectancy")
# report first three rows, first two columns
le_indicators.iloc[:3,:2]
```




                         id                                      name
    7793  SP.DYN.LE00.FE.IN  Life expectancy at birth, female (years)
    7794     SP.DYN.LE00.IN   Life expectancy at birth, total (years)
    7795  SP.DYN.LE00.MA.IN    Life expectancy at birth, male (years)




```python
# get countries and show the 3 digit code and name
countries = wb.get_countries()
# show a subset of the country data
countries.iloc[0:10].ix[:,['name', 'capitalCity', 'iso2c']]
```




                       name       capitalCity iso2c
    0                 Aruba        Oranjestad    AW
    1           Afghanistan             Kabul    AF
    2                Africa                      A9
    3                Angola            Luanda    AO
    4               Albania            Tirane    AL
    5               Andorra  Andorra la Vella    AD
    6         Andean Region                      L5
    7            Arab World                      1A
    8  United Arab Emirates         Abu Dhabi    AE
    9             Argentina      Buenos Aires    AR




```python
# get life expectancy at birth for all countries from 1980 to 2014
le_data_all = wb.download(indicator="SP.DYN.LE00.IN",
                          start='1980',
                          end='2014')
le_data_all
```




                        SP.DYN.LE00.IN
    country       year
    Canada        2014             NaN
                  2013             NaN
                  2012       81.238049
                  2011       81.068317
                  2010       80.893488
    ...                            ...
    United States 1984       74.563415
                  1983       74.463415
                  1982       74.360976
                  1981       74.007317
                  1980       73.658537

    [105 rows x 1 columns]




```python
# only US, CAN, and MEX are returned by default
le_data_all.index.levels[0]
```




    Index([u'Canada', u'Mexico', u'United States'], dtype='object')




```python
# retrieve life expectancy at birth for all countries
# from 1980 to 2014
le_data_all = wb.download(indicator="SP.DYN.LE00.IN",
                          country = countries['iso2c'],
                          start='1980',
                          end='2012')
le_data_all
```

    /Users/michaelheydt/anaconda/lib/python2.7/site-packages/pandas/io/wb.py:128: UserWarning: Non-standard ISO country codes: 1A, 1W, 4E, 7E, 8S, A4, A5, A9, B8, C4, C5, C6, C7, C8, C9, EU, F1, JG, KV, L4, L5, L6, L7, M2, OE, S1, S2, S3, S4, XC, XD, XE, XJ, XL, XM, XN, XO, XP, XQ, XR, XS, XT, XU, XY, Z4, Z7, ZF, ZG, ZJ, ZQ
      warnings.warn('Non-standard ISO country codes: %s' % tmp)





                   SP.DYN.LE00.IN
    country  year
    Aruba    2012       75.206756
             2011       75.080390
             2010       74.952024
             2009       74.816146
             2008       74.674220
    ...                       ...
    Zimbabwe 1984       61.217561
             1983       60.902854
             1982       60.466171
             1981       59.944951
             1980       59.377610

    [8151 rows x 1 columns]




```python
#le_data_all.pivot(index='country', columns='year')
le_data = le_data_all.reset_index().pivot(index='country',
                                          columns='year')
# examine pivoted data
le_data.ix[:,0:3]
```




                       SP.DYN.LE00.IN
    year                         1980       1981       1982
    country
    Afghanistan             41.233659  41.760634  42.335610
    Albania                 70.235976  70.454463  70.685122
    Algeria                 58.164024  59.486756  60.786341
    American Samoa                NaN        NaN        NaN
    Andorra                       NaN        NaN        NaN
    ...                           ...        ...        ...
    West Bank and Gaza            NaN        NaN        NaN
    World                   63.186868  63.494118  63.798264
    Yemen, Rep.             50.559537  51.541341  52.492707
    Zambia                  51.148951  50.817707  50.350805
    Zimbabwe                59.377610  59.944951  60.466171

    [247 rows x 3 columns]




```python
# ask what is the name of country for each year
# with the least life expectancy
country_with_least_expectancy = le_data.idxmin(axis=0)
country_with_least_expectancy
```




                    year
    SP.DYN.LE00.IN  1980       Cambodia
                    1981       Cambodia
                    1982    Timor-Leste
    ...
    SP.DYN.LE00.IN  2010    Sierra Leone
                    2011    Sierra Leone
                    2012    Sierra Leone
    Length: 33, dtype: object




```python
# and what is the minimum life expectancy for each year
expectancy_for_least_country = le_data.min(axis=0)
expectancy_for_least_country
```




                    year
    SP.DYN.LE00.IN  1980    29.613537
                    1981    35.856341
                    1982    38.176220
    ...
    SP.DYN.LE00.IN  2010    44.838951
                    2011    45.102585
                    2012    45.329049
    Length: 33, dtype: float64




```python
# this merges the two frames together and gives us
# year, country and expectancy where there minimum exists
least = pd.DataFrame(
    data = {'Country': country_with_least_expectancy.values,
            'Expectancy': expectancy_for_least_country.values},
    index = country_with_least_expectancy.index.levels[1])
least
```




               Country  Expectancy
    year
    1980      Cambodia   29.613537
    1981      Cambodia   35.856341
    1982   Timor-Leste   38.176220
    1983   South Sudan   39.676488
    1984   South Sudan   40.011024
    ...            ...         ...
    2008  Sierra Leone   44.067463
    2009  Sierra Leone   44.501439
    2010  Sierra Leone   44.838951
    2011  Sierra Leone   45.102585
    2012  Sierra Leone   45.329049

    [33 rows x 2 columns]



## 6.6 Summary


```python

```
