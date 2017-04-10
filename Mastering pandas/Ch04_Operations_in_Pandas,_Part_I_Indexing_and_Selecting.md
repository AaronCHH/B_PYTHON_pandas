
# Chapter 4: Operations in Pandas, Part I – Indexing and Selecting

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Chapter 4: Operations in Pandas, Part I – Indexing and Selecting](#chapter-4-operations-in-pandas-part-i-indexing-and-selecting)
	- [Basic indexing](#basic-indexing)
		- [Accessing attributes using dot operator](#accessing-attributes-using-dot-operator)
		- [Range slicing](#range-slicing)
	- [Label, integer, and mixed indexing](#label-integer-and-mixed-indexing)
		- [Label-oriented indexing](#label-oriented-indexing)
			- [Selection using a Boolean array](#selection-using-a-boolean-array)
		- [Integer-oriented indexing](#integer-oriented-indexing)
		- [The .iat and .at operators](#the-iat-and-at-operators)
		- [Mixed indexing with the .ix operator](#mixed-indexing-with-the-ix-operator)
		- [Multi-indexing](#multi-indexing)
		- [Swapping and re-ordering levels](#swapping-and-re-ordering-levels)
		- [Cross-sections](#cross-sections)
	- [Boolean indexing](#boolean-indexing)
		- [The is in and any all methods](#the-is-in-and-any-all-methods)
		- [Using the where() method](#using-the-where-method)
		- [Operations on indexes](#operations-on-indexes)
	- [Summary](#summary)

<!-- tocstop -->

## Basic indexing


```python
import pandas as pd
SpotCrudePrices_2013_Data={
    'U.K. Brent' : {'2013-Q1':112.9, '2013-Q2':103.0,
                    '2013-Q3':110.1, '2013-Q4':109.4},
    'Dubai':{'2013-Q1':108.1, '2013-Q2':100.8,
             '2013-Q3':106.1,'2013-Q4':106.7},
    'West Texas Intermediate':{'2013-Q1':94.4, '2013-Q2':94.2,
                               '2013-Q3':105.8,'2013-Q4':97.4}}
SpotCrudePrices_2013=pd.DataFrame.from_dict(SpotCrudePrices_2013_Data)
SpotCrudePrices_2013
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>U.K. Brent</th>
      <th>West Texas Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>108.1</td>
      <td>112.9</td>
      <td>94.4</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>100.8</td>
      <td>103.0</td>
      <td>94.2</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>106.1</td>
      <td>110.1</td>
      <td>105.8</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>106.7</td>
      <td>109.4</td>
      <td>97.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
 dubaiPrices=SpotCrudePrices_2013['Dubai']; dubaiPrices
```




    2013-Q1    108.1
    2013-Q2    100.8
    2013-Q3    106.1
    2013-Q4    106.7
    Name: Dubai, dtype: float64




```python
SpotCrudePrices_2013[['West Texas Intermediate','U.K. Brent']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>West Texas Intermediate</th>
      <th>U.K. Brent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>94.4</td>
      <td>112.9</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>94.2</td>
      <td>103.0</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>105.8</td>
      <td>110.1</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>97.4</td>
      <td>109.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013['Brent Blend']
```


```python
SpotCrudePrices_2013.get('Brent Blend','N/A')
```




    'N/A'




```python
:SpotCrudePrices_2013['2013-Q1']
```

### Accessing attributes using dot operator


```python
SpotCrudePrices_2013.Dubai
```




    2013-Q1    108.1
    2013-Q2    100.8
    2013-Q3    106.1
    2013-Q4    106.7
    Name: Dubai, dtype: float64




```python
SpotCrudePrices_2013."West Texas Intermediate"
```


      File "<ipython-input-12-2a782563c15a>", line 1
        SpotCrudePrices_2013."West Texas Intermediate"
                                                     ^
    SyntaxError: invalid syntax




```python
SpotCrudePrices_2013
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>U.K. Brent</th>
      <th>West Texas Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>108.1</td>
      <td>112.9</td>
      <td>94.4</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>100.8</td>
      <td>103.0</td>
      <td>94.2</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>106.1</td>
      <td>110.1</td>
      <td>105.8</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>106.7</td>
      <td>109.4</td>
      <td>97.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013.columns=['Dubai','UK_Brent',
                              'West_Texas_Intermediate']
```


```python
SpotCrudePrices_2013.West_Texas_Intermediate
```




    2013-Q1     94.4
    2013-Q2     94.2
    2013-Q3    105.8
    2013-Q4     97.4
    Name: West_Texas_Intermediate, dtype: float64




```python
SpotCrudePrices_2013[[1]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UK_Brent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>112.9</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>103.0</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>110.1</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>109.4</td>
    </tr>
  </tbody>
</table>
</div>



### Range slicing


```python
SpotCrudePrices_2013[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>UK_Brent</th>
      <th>West_Texas_Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>108.1</td>
      <td>112.9</td>
      <td>94.4</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>100.8</td>
      <td>103.0</td>
      <td>94.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013[2:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>UK_Brent</th>
      <th>West_Texas_Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q3</th>
      <td>106.1</td>
      <td>110.1</td>
      <td>105.8</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>106.7</td>
      <td>109.4</td>
      <td>97.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013[::2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>UK_Brent</th>
      <th>West_Texas_Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>108.1</td>
      <td>112.9</td>
      <td>94.4</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>106.1</td>
      <td>110.1</td>
      <td>105.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013[::-1]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dubai</th>
      <th>UK_Brent</th>
      <th>West_Texas_Intermediate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q4</th>
      <td>106.7</td>
      <td>109.4</td>
      <td>97.4</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>106.1</td>
      <td>110.1</td>
      <td>105.8</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>100.8</td>
      <td>103.0</td>
      <td>94.2</td>
    </tr>
    <tr>
      <th>2013-Q1</th>
      <td>108.1</td>
      <td>112.9</td>
      <td>94.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
dubaiPrices=SpotCrudePrices_2013['Dubai']
```


```python
dubaiPrices[1:]
```




    2013-Q2    100.8
    2013-Q3    106.1
    2013-Q4    106.7
    Name: Dubai, dtype: float64




```python
dubaiPrices[:-1]
```




    2013-Q1    108.1
    2013-Q2    100.8
    2013-Q3    106.1
    Name: Dubai, dtype: float64




```python
dubaiPrices[::-1]
```




    2013-Q4    106.7
    2013-Q3    106.1
    2013-Q2    100.8
    2013-Q1    108.1
    Name: Dubai, dtype: float64



## Label, integer, and mixed indexing

### Label-oriented indexing


```python
NYC_SnowAvgsData={'Months' :
                  ['January','February','March',
                   'April', 'November', 'December'],
                  'Avg SnowDays' : [4.0,2.7,1.7,0.2,0.2,2.3],
                  'Avg Precip. (cm)' : [17.8,22.4,9.1,1.5,0.8,12.2],
                  'Avg Low Temp. (F)' : [27,29,35,45,42,32] }
```


```python
NYC_SnowAvgsData
```




    {'Avg Low Temp. (F)': [27, 29, 35, 45, 42, 32],
     'Avg Precip. (cm)': [17.8, 22.4, 9.1, 1.5, 0.8, 12.2],
     'Avg SnowDays': [4.0, 2.7, 1.7, 0.2, 0.2, 2.3],
     'Months': ['January', 'February', 'March', 'April', 'November', 'December']}




```python
NYC_SnowAvgs=pd.DataFrame(NYC_SnowAvgsData,
                          index=NYC_SnowAvgsData['Months'],
                          columns=['Avg SnowDays','Avg Precip. (cm)',
                                   'Avg Low Temp. (F)'])
```


```python
NYC_SnowAvgs
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg SnowDays</th>
      <th>Avg Precip. (cm)</th>
      <th>Avg Low Temp. (F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>January</th>
      <td>4.0</td>
      <td>17.8</td>
      <td>27</td>
    </tr>
    <tr>
      <th>February</th>
      <td>2.7</td>
      <td>22.4</td>
      <td>29</td>
    </tr>
    <tr>
      <th>March</th>
      <td>1.7</td>
      <td>9.1</td>
      <td>35</td>
    </tr>
    <tr>
      <th>April</th>
      <td>0.2</td>
      <td>1.5</td>
      <td>45</td>
    </tr>
    <tr>
      <th>November</th>
      <td>0.2</td>
      <td>0.8</td>
      <td>42</td>
    </tr>
    <tr>
      <th>December</th>
      <td>2.3</td>
      <td>12.2</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_SnowAvgs.loc['January']
```




    Avg SnowDays          4.0
    Avg Precip. (cm)     17.8
    Avg Low Temp. (F)    27.0
    Name: January, dtype: float64




```python
NYC_SnowAvgs.loc[['January','April']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg SnowDays</th>
      <th>Avg Precip. (cm)</th>
      <th>Avg Low Temp. (F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>January</th>
      <td>4.0</td>
      <td>17.8</td>
      <td>27</td>
    </tr>
    <tr>
      <th>April</th>
      <td>0.2</td>
      <td>1.5</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_SnowAvgs.loc['January':'March']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg SnowDays</th>
      <th>Avg Precip. (cm)</th>
      <th>Avg Low Temp. (F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>January</th>
      <td>4.0</td>
      <td>17.8</td>
      <td>27</td>
    </tr>
    <tr>
      <th>February</th>
      <td>2.7</td>
      <td>22.4</td>
      <td>29</td>
    </tr>
    <tr>
      <th>March</th>
      <td>1.7</td>
      <td>9.1</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
NYC_SnowAvgs.loc['Avg SnowDays']
```


```python
NYC_SnowAvgs.loc[:,'Avg SnowDays']
```




    January     4.0
    February    2.7
    March       1.7
    April       0.2
    November    0.2
    December    2.3
    Name: Avg SnowDays, dtype: float64




```python
NYC_SnowAvgs.loc['March','Avg SnowDays']
```




    1.7




```python
NYC_SnowAvgs.loc['March']['Avg SnowDays']
```




    1.7




```python
NYC_SnowAvgs['Avg SnowDays']['March']
```




    1.7




```python
NYC_SnowAvgs['March']['Avg SnowDays']
```


```python
NYC_SnowAvgs['March']
```


```python
NYC_SnowAvgs.loc['March']
```




    Avg SnowDays          1.7
    Avg Precip. (cm)      9.1
    Avg Low Temp. (F)    35.0
    Name: March, dtype: float64



#### Selection using a Boolean array


```python
NYC_SnowAvgs.loc[NYC_SnowAvgs['Avg SnowDays']<1,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg SnowDays</th>
      <th>Avg Precip. (cm)</th>
      <th>Avg Low Temp. (F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>April</th>
      <td>0.2</td>
      <td>1.5</td>
      <td>45</td>
    </tr>
    <tr>
      <th>November</th>
      <td>0.2</td>
      <td>0.8</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013.loc[:,SpotCrudePrices_2013.loc['2013-Q1']>110]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UK_Brent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-Q1</th>
      <td>112.9</td>
    </tr>
    <tr>
      <th>2013-Q2</th>
      <td>103.0</td>
    </tr>
    <tr>
      <th>2013-Q3</th>
      <td>110.1</td>
    </tr>
    <tr>
      <th>2013-Q4</th>
      <td>109.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
SpotCrudePrices_2013.loc['2013-Q1']>110
```




    Dubai                      False
    UK_Brent                    True
    West_Texas_Intermediate    False
    Name: 2013-Q1, dtype: bool



### Integer-oriented indexing


```python
import scipy.constants as phys
import math
```


```python
sci_values=pd.DataFrame([[math.pi, math.sin(math.pi),
                          math.cos(math.pi)],
                         [math.e,math.log(math.e),
                          phys.golden],
                         [phys.c,phys.g,phys.e],
                         [phys.m_e,phys.m_p,phys.m_n]],
                        index=list(range(0,20,5)))
```


```python
sci_values
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.141593e+00</td>
      <td>1.224647e-16</td>
      <td>-1.000000e+00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.718282e+00</td>
      <td>1.000000e+00</td>
      <td>1.618034e+00</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2.997925e+08</td>
      <td>9.806650e+00</td>
      <td>1.602177e-19</td>
    </tr>
    <tr>
      <th>15</th>
      <td>9.109384e-31</td>
      <td>1.672622e-27</td>
      <td>1.674927e-27</td>
    </tr>
  </tbody>
</table>
</div>




```python
sci_values.iloc[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.141593</td>
      <td>1.224647e-16</td>
      <td>-1.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.718282</td>
      <td>1.000000e+00</td>
      <td>1.618034</td>
    </tr>
  </tbody>
</table>
</div>




```python
sci_values.iloc[2,0:2]
```




    0    2.997925e+08
    1    9.806650e+00
    Name: 10, dtype: float64




```python
sci_values.iloc[10]
```


```python
sci_values.loc[10]
```




    0    2.997925e+08
    1    9.806650e+00
    2    1.602177e-19
    Name: 10, dtype: float64




```python
sci_values.iloc[2:3,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>299792458.0</td>
      <td>9.80665</td>
      <td>1.602177e-19</td>
    </tr>
  </tbody>
</table>
</div>




```python
sci_values.iloc[3]
```




    0    9.109384e-31
    1    1.672622e-27
    2    1.674927e-27
    Name: 15, dtype: float64




```python
sci_values.iloc[6,:]
```

### The .iat and .at operators


```python
sci_values.iloc[3,0]
```




    9.1093835599999998e-31




```python
sci_values.iat[3,0]
```




    9.1093835599999998e-31




```python
%timeit sci_values.iloc[3,0]
```

    10000 loops, best of 3: 88 µs per loop



```python
%timeit sci_values.iat[3,0]
```

    The slowest run took 7.07 times longer than the fastest. This could mean that an intermediate result is being cached.
    100000 loops, best of 3: 6.24 µs per loop


### Mixed indexing with the .ix operator


```python
stockIndexDataDF=pd.read_csv('./Chapter 4/stock_index_data.csv')
```


```python
stockIndexDataDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/02/05</td>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/02/06</td>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF=stockIndexDataDF.set_index('TradingDate')
```


```python
stockIndexDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2014/02/03</th>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
    <tr>
      <th>2014/02/04</th>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>2014/02/05</th>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
    </tr>
    <tr>
      <th>2014/02/06</th>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.ix['2014/01/30']
```




    Nasdaq          4123.13
    S&P 500         1794.19
    Russell 2000    1139.36
    Name: 2014/01/30, dtype: float64




```python
stockIndexDF.ix[['2014/01/30']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.ix[['2014/01/30','2014/01/31']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(stockIndexDF.ix['2014/01/30'])
```




    pandas.core.series.Series




```python
type(stockIndexDF.ix[['2014/01/30']])
```




    pandas.core.frame.DataFrame




```python
tradingDates=stockIndexDataDF.TradingDate
```


```python
stockIndexDF.ix[tradingDates[:3]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2014/02/03</th>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.ix[0]
```




    Nasdaq          4123.13
    S&P 500         1794.19
    Russell 2000    1139.36
    Name: 2014/01/30, dtype: float64




```python
stockIndexDF.ix[[0,2]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/02/03</th>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.ix[1:3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2014/02/03</th>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.ix[stockIndexDF['Russell 2000']>1100]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2014/02/04</th>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>2014/02/06</th>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>



### Multi-indexing


```python
sharesIndexDataDF=pd.read_csv('./Chapter 4/stock_index_prices.csv')
sharesIndexDataDF.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/02/21</td>
      <td>open</td>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/02/21</td>
      <td>close</td>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/21</td>
      <td>high</td>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/24</td>
      <td>open</td>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/02/24</td>
      <td>close</td>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
sharesIndexDF=sharesIndexDataDF.set_index(['TradingDate','PriceType'])
```


```python
mIndex=sharesIndexDF.index; mIndex
```




    MultiIndex(levels=[['2014/02/21', '2014/02/24', '2014/02/25', '2014/02/26', '2014/02/27', '2014/02/28'], ['close', 'high', 'open']],
               labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]],
               names=['TradingDate', 'PriceType'])




```python
sharesIndexDF.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">2014/02/21</th>
      <th>open</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>close</th>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>high</th>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2014/02/24</th>
      <th>open</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>close</th>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
mIndex.get_level_values(0)
```




    Index(['2014/02/21', '2014/02/21', '2014/02/21', '2014/02/24', '2014/02/24',
           '2014/02/24', '2014/02/25', '2014/02/25', '2014/02/25', '2014/02/26',
           '2014/02/26', '2014/02/26', '2014/02/27', '2014/02/27', '2014/02/27',
           '2014/02/28', '2014/02/28', '2014/02/28'],
          dtype='object', name='TradingDate')




```python
mIndex.get_level_values(1)
```




    Index(['open', 'close', 'high', 'open', 'close', 'high', 'open', 'close',
           'high', 'open', 'close', 'high', 'open', 'close', 'high', 'open',
           'close', 'high'],
          dtype='object', name='PriceType')




```python
 mIndex.get_level_values(2)
```


```python
sharesIndexDF.ix['2014/02/21','open']
```




    Nasdaq          4282.17
    S&P 500         1841.07
    Russell 2000    1166.25
    Name: (2014/02/21, open), dtype: float64




```python
sharesIndexDF.ix['2014/02/21':'2014/02/24']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">2014/02/21</th>
      <th>open</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>close</th>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>high</th>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2014/02/24</th>
      <th>open</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>close</th>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
    <tr>
      <th>high</th>
      <td>4311.13</td>
      <td>1858.71</td>
      <td>1180.29</td>
    </tr>
  </tbody>
</table>
</div>




```python
sharesIndexDF.ix[('2014/02/21','open'):('2014/02/24','open')]
```


```python
sharesIndexDF.sortlevel(0).ix[('2014/02/21','open'):('2014/02/24','open')]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/02/21</th>
      <th>open</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2014/02/24</th>
      <th>close</th>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
    <tr>
      <th>high</th>
      <td>4311.13</td>
      <td>1858.71</td>
      <td>1180.29</td>
    </tr>
    <tr>
      <th>open</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
sharesIndexDF.ix[[('2014/02/21','close'),('2014/02/24','open')]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/02/21</th>
      <th>close</th>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>2014/02/24</th>
      <th>open</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
  </tbody>
</table>
</div>



### Swapping and re-ordering levels


```python
swappedDF=sharesIndexDF[:7].swaplevel(0, 1, axis=0)
swappedDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>PriceType</th>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>open</th>
      <th>2014/02/21</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>close</th>
      <th>2014/02/21</th>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>high</th>
      <th>2014/02/21</th>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
    <tr>
      <th>open</th>
      <th>2014/02/24</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>close</th>
      <th>2014/02/24</th>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
    <tr>
      <th>high</th>
      <th>2014/02/24</th>
      <td>4311.13</td>
      <td>1858.71</td>
      <td>1180.29</td>
    </tr>
    <tr>
      <th>open</th>
      <th>2014/02/25</th>
      <td>4298.48</td>
      <td>1847.66</td>
      <td>1176.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
reorderedDF=sharesIndexDF[:7].reorder_levels(['PriceType',
                                              'TradingDate'],
                                             axis=0)
reorderedDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>PriceType</th>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>open</th>
      <th>2014/02/21</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>close</th>
      <th>2014/02/21</th>
      <td>4263.41</td>
      <td>1836.25</td>
      <td>1164.63</td>
    </tr>
    <tr>
      <th>high</th>
      <th>2014/02/21</th>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
    <tr>
      <th>open</th>
      <th>2014/02/24</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>close</th>
      <th>2014/02/24</th>
      <td>4292.97</td>
      <td>1847.61</td>
      <td>1174.55</td>
    </tr>
    <tr>
      <th>high</th>
      <th>2014/02/24</th>
      <td>4311.13</td>
      <td>1858.71</td>
      <td>1180.29</td>
    </tr>
    <tr>
      <th>open</th>
      <th>2014/02/25</th>
      <td>4298.48</td>
      <td>1847.66</td>
      <td>1176.00</td>
    </tr>
  </tbody>
</table>
</div>



### Cross-sections


```python
sharesIndexDF.xs('open',level='PriceType')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/02/21</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>2014/02/24</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>2014/02/25</th>
      <td>4298.48</td>
      <td>1847.66</td>
      <td>1176.00</td>
    </tr>
    <tr>
      <th>2014/02/26</th>
      <td>4300.45</td>
      <td>1845.79</td>
      <td>1176.11</td>
    </tr>
    <tr>
      <th>2014/02/27</th>
      <td>4291.47</td>
      <td>1844.90</td>
      <td>1179.28</td>
    </tr>
    <tr>
      <th>2014/02/28</th>
      <td>4323.52</td>
      <td>1855.12</td>
      <td>1189.19</td>
    </tr>
  </tbody>
</table>
</div>




```python
sharesIndexDF.swaplevel(0, 1, axis=0).ix['open']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/02/21</th>
      <td>4282.17</td>
      <td>1841.07</td>
      <td>1166.25</td>
    </tr>
    <tr>
      <th>2014/02/24</th>
      <td>4273.32</td>
      <td>1836.78</td>
      <td>1166.74</td>
    </tr>
    <tr>
      <th>2014/02/25</th>
      <td>4298.48</td>
      <td>1847.66</td>
      <td>1176.00</td>
    </tr>
    <tr>
      <th>2014/02/26</th>
      <td>4300.45</td>
      <td>1845.79</td>
      <td>1176.11</td>
    </tr>
    <tr>
      <th>2014/02/27</th>
      <td>4291.47</td>
      <td>1844.90</td>
      <td>1179.28</td>
    </tr>
    <tr>
      <th>2014/02/28</th>
      <td>4323.52</td>
      <td>1855.12</td>
      <td>1189.19</td>
    </tr>
  </tbody>
</table>
</div>



## Boolean indexing


```python
sharesIndexDataDF.ix[(sharesIndexDataDF['PriceType']=='close')
                     & (sharesIndexDataDF['Nasdaq']>4300) ]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>2014/02/27</td>
      <td>close</td>
      <td>4318.93</td>
      <td>1854.29</td>
      <td>1187.94</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2014/02/28</td>
      <td>close</td>
      <td>4308.12</td>
      <td>1859.45</td>
      <td>1183.03</td>
    </tr>
  </tbody>
</table>
</div>




```python
highSelection=sharesIndexDataDF['PriceType']=='high'
NasdaqHigh=sharesIndexDataDF['Nasdaq']<4300
sharesIndexDataDF.ix[highSelection & NasdaqHigh]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>PriceType</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>2014/02/21</td>
      <td>high</td>
      <td>4284.85</td>
      <td>1846.13</td>
      <td>1168.43</td>
    </tr>
  </tbody>
</table>
</div>



### The is in and any all methods


```python
stockSeries=pd.Series(['NFLX','AMZN','GOOG','FB','TWTR'])
stockSeries.isin(['AMZN','FB'])
```




    0    False
    1     True
    2    False
    3     True
    4    False
    dtype: bool




```python
stockSeries[stockSeries.isin(['AMZN','FB'])]
```




    1    AMZN
    3      FB
    dtype: object




```python
 australianMammals = {
        'kangaroo': {'Subclass':'marsupial',
                     'Species Origin':'native'},
        'flying fox' : {'Subclass':'placental',
                        'Species Origin':'native'},
        'black rat': {'Subclass':'placental',
                      'Species Origin':'invasive'},
        'platypus' : {'Subclass':'monotreme',
                      'Species Origin':'native'},
        'wallaby' : {'Subclass':'marsupial',
                     'Species Origin':'native'},
        'palm squirrel' : {'Subclass':'placental',
                           'Origin':'invasive'},
        'anteater': {'Subclass':'monotreme', 'Origin':'native'},
        'koala': {'Subclass':'marsupial', 'Origin':'native'}
    }
```


```python
ozzieMammalsDF=pd.DataFrame(australianMammals)
aussieMammalsDF=ozzieMammalsDF.T; aussieMammalsDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Origin</th>
      <th>Species Origin</th>
      <th>Subclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>anteater</th>
      <td>native</td>
      <td>NaN</td>
      <td>monotreme</td>
    </tr>
    <tr>
      <th>black rat</th>
      <td>NaN</td>
      <td>invasive</td>
      <td>placental</td>
    </tr>
    <tr>
      <th>flying fox</th>
      <td>NaN</td>
      <td>native</td>
      <td>placental</td>
    </tr>
    <tr>
      <th>kangaroo</th>
      <td>NaN</td>
      <td>native</td>
      <td>marsupial</td>
    </tr>
    <tr>
      <th>koala</th>
      <td>native</td>
      <td>NaN</td>
      <td>marsupial</td>
    </tr>
    <tr>
      <th>palm squirrel</th>
      <td>invasive</td>
      <td>NaN</td>
      <td>placental</td>
    </tr>
    <tr>
      <th>platypus</th>
      <td>NaN</td>
      <td>native</td>
      <td>monotreme</td>
    </tr>
    <tr>
      <th>wallaby</th>
      <td>NaN</td>
      <td>native</td>
      <td>marsupial</td>
    </tr>
  </tbody>
</table>
</div>




```python
aussieMammalsDF.isin({'Subclass':['marsupial'],'Origin':['native']})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Origin</th>
      <th>Species Origin</th>
      <th>Subclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>anteater</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>black rat</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>flying fox</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>kangaroo</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>koala</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>palm squirrel</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>platypus</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>wallaby</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
nativeMarsupials={'Mammal Subclass':['marsupial'],
                  'Species Origin':['native']}
nativeMarsupialMask = aussieMammalsDF.isin(nativeMarsupials).all(True)
aussieMammalsDF[nativeMarsupialMask]
```

### Using the where() method


```python
import numpy as np
np.random.seed(100)
normvals=pd.Series([np.random.normal() for i in np.arange(10)])
normvals
```




    0   -1.749765
    1    0.342680
    2    1.153036
    3   -0.252436
    4    0.981321
    5    0.514219
    6    0.221180
    7   -1.070043
    8   -0.189496
    9    0.255001
    dtype: float64




```python
normvals[normvals>0]
```




    1    0.342680
    2    1.153036
    4    0.981321
    5    0.514219
    6    0.221180
    9    0.255001
    dtype: float64




```python
normvals.where(normvals>0)
```




    0         NaN
    1    0.342680
    2    1.153036
    3         NaN
    4    0.981321
    5    0.514219
    6    0.221180
    7         NaN
    8         NaN
    9    0.255001
    dtype: float64




```python
np.random.seed(100)
normDF=pd.DataFrame([[round(np.random.normal(),3) for i in np.arange(5)] for j in range(3)], columns=['0','30','60','90','120'])
```


```python
normDF[normDF>0]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>30</th>
      <th>60</th>
      <th>90</th>
      <th>120</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>0.343</td>
      <td>1.153</td>
      <td>NaN</td>
      <td>0.981</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.514</td>
      <td>0.221</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.255</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>0.435</td>
      <td>NaN</td>
      <td>0.817</td>
      <td>0.673</td>
    </tr>
  </tbody>
</table>
</div>




```python
normDF.where(normDF>0)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>30</th>
      <th>60</th>
      <th>90</th>
      <th>120</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>0.343</td>
      <td>1.153</td>
      <td>NaN</td>
      <td>0.981</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.514</td>
      <td>0.221</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.255</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>0.435</td>
      <td>NaN</td>
      <td>0.817</td>
      <td>0.673</td>
    </tr>
  </tbody>
</table>
</div>




```python
normDF.mask(normDF>0)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>30</th>
      <th>60</th>
      <th>90</th>
      <th>120</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.750</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.252</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1.070</td>
      <td>-0.189</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.458</td>
      <td>NaN</td>
      <td>-0.584</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Operations on indexes


```python
stockIndexDataDF=pd.read_csv('./Chapter 4/stock_index_data.csv')
stockIndexDataDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/02/05</td>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/02/06</td>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF=stockIndexDataDF.set_index('TradingDate')
stockIndexDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
    <tr>
      <th>TradingDate</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014/01/30</th>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>2014/01/31</th>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2014/02/03</th>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
    <tr>
      <th>2014/02/04</th>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>2014/02/05</th>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
    </tr>
    <tr>
      <th>2014/02/06</th>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockIndexDF.reset_index()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/02/05</td>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/02/06</td>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

## Summary
