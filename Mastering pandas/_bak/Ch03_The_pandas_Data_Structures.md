
# Chapter 3: The pandas Data Structures

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Chapter 3: The pandas Data Structures](#chapter-3-the-pandas-data-structures)
	- [NumPy ndarrays](#numpy-ndarrays)
		- [NumPy array creation](#numpy-array-creation)
			- [NumPy arrays via numpy.array](#numpy-arrays-via-numpyarray)
			- [NumPy array via numpy.arange](#numpy-array-via-numpyarange)
			- [NumPy array via numpy.linspace](#numpy-array-via-numpylinspace)
			- [NumPy array via various other functions](#numpy-array-via-various-other-functions)
		- [NumPy datatypes](#numpy-datatypes)
		- [NumPy indexing and slicing](#numpy-indexing-and-slicing)
			- [Array slicing](#array-slicing)
			- [Array masking](#array-masking)
			- [Complex indexing](#complex-indexing)
		- [Copies and views](#copies-and-views)
		- [Operations](#operations)
			- [Basic operations](#basic-operations)
			- [Reduction operations](#reduction-operations)
			- [Statistical operators](#statistical-operators)
			- [Logical operators](#logical-operators)
		- [Broadcasting](#broadcasting)
		- [Array shape manipulation](#array-shape-manipulation)
			- [Flattening a multi-dimensional array](#flattening-a-multi-dimensional-array)
			- [Reshaping](#reshaping)
			- [Resizing](#resizing)
			- [Adding a dimension](#adding-a-dimension)
		- [Array sorting](#array-sorting)
	- [Data structures in pandas](#data-structures-in-pandas)
		- [Series](#series)
			- [Series creation](#series-creation)
			- [Operations on Series](#operations-on-series)
		- [DataFrame](#dataframe)
			- [DataFrame Creation](#dataframe-creation)
			- [Operations](#operations-1)
		- [Panel](#panel)
			- [Using 3D NumPy array with axis labels](#using-3d-numpy-array-with-axis-labels)
			- [Using a Python dictionary of DataFrame objects](#using-a-python-dictionary-of-dataframe-objects)
			- [Using the DataFrame.to_panel method](#using-the-dataframeto_panel-method)
			- [Other operations](#other-operations)
	- [Summary](#summary)

<!-- tocstop -->

## NumPy ndarrays

 ### NumPy array creation

 #### NumPy arrays via numpy.array


```python
import numpy as np
ar1=np.array([0,1,2,3]) # 1 dimensional array
ar2=np.array ([[0,3,5],[2,8,7]]) # 2D array
```


```python
ar1
```




    array([0, 1, 2, 3])




```python
ar2
```




    array([[0, 3, 5],
           [2, 8, 7]])




```python
ar2.shape
```




    (2, 3)




```python
ar2.ndim
```




    2



 #### NumPy array via numpy.arange


```python
# produces the integers from 0 to 11, not inclusive of 12
ar3=np.arange(12);
ar3
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
# start, end (exclusive), step size
ar4=np.arange(3,10,3);
ar4
```




    array([3, 6, 9])



 #### NumPy array via numpy.linspace


```python
# args - start element,end element, number of elements
ar5=np.linspace(0,2.0/3,4); ar5
```




    array([ 0.        ,  0.22222222,  0.44444444,  0.66666667])



 #### NumPy array via various other functions

* numpy.ones


```python
# Produces 2x3x2 array of 1's.
ar7=np.ones((2,3,2));
ar7
```




    array([[[ 1.,  1.],
            [ 1.,  1.],
            [ 1.,  1.]],

           [[ 1.,  1.],
            [ 1.,  1.],
            [ 1.,  1.]]])



* numpy.zeros


```python
# Produce 4x2 array of zeros.
ar8=np.zeros((4,2));
ar8
```




    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])



* numpy.eye


```python
# Produces identity matrix
ar9 = np.eye(3);
ar9
```




    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])



* numpy.diag


```python
# Create diagonal array
ar10=np.diag((2,1,4,6));
ar10
```




    array([[2, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 4, 0],
           [0, 0, 0, 6]])



* numpy.random.rand


```python
# Using the rand, randn functions
# rand(m) produces uniformly distributed random numbers with range 0 to m
np.random.seed(100) # Set seed
ar11=np.random.rand(3); ar11
```




    array([ 0.54340494,  0.27836939,  0.42451759])




```python
 # randn(m) produces m normally distributed (Gaussian) random numbers
ar12=np.random.rand(5); ar12
```




    array([ 0.84477613,  0.00471886,  0.12156912,  0.67074908,  0.82585276])



* numpy.empty


```python
ar13=np.empty((3,2)); ar13
```




    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])



* numpy.tile


```python
np.array([[1,2],[6,7]])
```




    array([[1, 2],
           [6, 7]])




```python
np.tile(np.array([[1,2],[6,7]]),3)
```




    array([[1, 2, 1, 2, 1, 2],
           [6, 7, 6, 7, 6, 7]])




```python
np.tile(np.array([[1,2],[6,7]]),(2,2))
```




    array([[1, 2, 1, 2],
           [6, 7, 6, 7],
           [1, 2, 1, 2],
           [6, 7, 6, 7]])



### NumPy datatypes


```python
ar=np.array([2,-1,6,3],dtype='float'); ar
ar.dtype
```




    dtype('float64')




```python
ar=np.array([2,4,6,8]); ar.dtype
```




    dtype('int32')




```python
ar=np.array([2.,4,6,8]); ar.dtype
```




    dtype('float64')




```python
sar=np.array(['Goodbye','Welcome','Tata','Goodnight']);
sar.dtype
```




    dtype('<U9')




```python
 bar=np.array([True, False, True]); bar.dtype
```




    dtype('bool')




```python
f_ar = np.array([3,-2,8.18])
f_ar
```




    array([ 3.  , -2.  ,  8.18])




```python
f_ar.astype(int)
```




    array([ 3, -2,  8])



### NumPy indexing and slicing


```python
# print entire array, element 0, element 1, last element.
ar = np.arange(5);
print(ar);
ar[0], ar[1], ar[-1]
```

    [0 1 2 3 4]





    (0, 1, 4)




```python
# 2nd, last and 1st elements
ar=np.arange(5); ar[1], ar[-1], ar[0]
```




    (1, 4, 0)




```python
ar=np.arange(5); ar[::-1]
```




    array([4, 3, 2, 1, 0])




```python
ar = np.array([[2,3,4],[9,8,7],[11,12,13]]);
ar
```




    array([[ 2,  3,  4],
           [ 9,  8,  7],
           [11, 12, 13]])




```python
ar[1,1]
```




    8




```python
ar[1,1]=5;
ar
```




    array([[ 2,  3,  4],
           [ 9,  5,  7],
           [11, 12, 13]])




```python
ar[2]
```




    array([11, 12, 13])




```python
ar[2,:]
```




    array([11, 12, 13])




```python
ar[:,1]
```




    array([ 3,  5, 12])




```python
ar = np.array([0,1,2])
```


```python
ar[5]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-95-8ef7e0800b7a> in <module>()
    ----> 1 ar[5]


    IndexError: index 5 is out of bounds for axis 0 with size 3


#### Array slicing


```python
ar=2*np.arange(6); ar
```




    array([ 0,  2,  4,  6,  8, 10])




```python
ar[1:5:2]
```




    array([2, 6])




```python
ar[1:6:2]
```




    array([ 2,  6, 10])




```python
ar[:4]
```




    array([0, 2, 4, 6])




```python
ar[4:]
```




    array([ 8, 10])




```python
ar[::3]
```




    array([0, 6])




```python
ar
```




    array([ 0,  2,  4,  6,  8, 10])




```python
ar[:3]=1; ar
```




    array([ 1,  1,  1,  6,  8, 10])




```python
ar[2:]=np.ones(4);ar
```




    array([1, 1, 1, 1, 1, 1])



#### Array masking


```python
np.random.seed(10)
ar=np.random.random_integers(0,25,10); ar
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:2: DeprecationWarning: This function is deprecated. Please call randint(0, 25 + 1) instead
      from ipykernel import kernelapp as app





    array([ 9,  4, 15,  0, 17, 25, 16, 17,  8,  9])




```python
evenMask=(ar % 2==0); evenMask
```




    array([False,  True, False,  True, False, False,  True, False,  True, False], dtype=bool)




```python
evenNums=ar[evenMask]; evenNums
```




    array([ 4,  0, 16,  8])




```python
ar=np.array(['Hungary','Nigeria',
             'Guatemala','','Poland',
             '','Japan']); ar
```




    array(['Hungary', 'Nigeria', 'Guatemala', '', 'Poland', '', 'Japan'],
          dtype='<U9')




```python
ar[ar=='']='USA'; ar
```




    array(['Hungary', 'Nigeria', 'Guatemala', 'USA', 'Poland', 'USA', 'Japan'],
          dtype='<U9')




```python
ar=11*np.arange(0,10); ar
```




    array([ 0, 11, 22, 33, 44, 55, 66, 77, 88, 99])




```python
ar[[1,3,4,2,7]]
```




    array([11, 33, 44, 22, 77])




```python
ar[1,3,4,2,7]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-112-adbcbe3b3cdc> in <module>()
    ----> 1 ar[1,3,4,2,7]


    IndexError: too many indices for array



```python
ar[[1,3]]=50; ar
```




    array([ 0, 50, 22, 50, 44, 55, 66, 77, 88, 99])



#### Complex indexing


```python
ar=np.arange(15); ar
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])




```python
ar2=np.arange(0,-10,-1)[::-1]; ar2
```




    array([-9, -8, -7, -6, -5, -4, -3, -2, -1,  0])




```python
ar[:10]=ar2; ar
```




    array([-9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 10, 11, 12, 13, 14])



### Copies and views


```python
ar1=np.arange(12); ar1
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
ar2=ar1[::2]; ar2
```




    array([ 0,  2,  4,  6,  8, 10])




```python
ar2[1]=-1; ar1
```




    array([ 0,  1, -1,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
ar=np.arange(8);ar
```




    array([0, 1, 2, 3, 4, 5, 6, 7])




```python
arc=ar[:3].copy(); arc
```




    array([0, 1, 2])




```python
arc[0]=-1; arc
```




    array([-1,  1,  2])




```python
ar
```




    array([0, 1, 2, 3, 4, 5, 6, 7])



### Operations

#### Basic operations


```python

```

#### Reduction operations


```python
ar=np.arange(1,5)
```


```python
ar=np.array([np.arange(1,6),np.arange(1,6)]);ar
```




    array([[1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5]])




```python
np.prod(ar,axis=0)
```




    array([ 1,  4,  9, 16, 25])




```python
np.prod(ar,axis=1)
```




    array([120, 120])




```python
ar=np.array([[2,3,4],[5,6,7],[8,9,10]]); ar.sum()
```




    54




```python
ar.mean()
```




    6.0




```python
np.median(ar)
```




    6.0



#### Statistical operators


```python
np.random.seed(10)
ar=np.random.randint(0,10, size=(4,5));ar
```




    array([[9, 4, 0, 1, 9],
           [0, 1, 8, 9, 0],
           [8, 6, 4, 3, 0],
           [4, 6, 8, 1, 8]])




```python
ar.mean()
```




    4.4500000000000002




```python
ar.std()
```




    3.4274626183227732




```python
ar.var(axis=0) # across rows
```




    array([ 12.6875,   4.1875,  11.    ,  10.75  ,  18.1875])




```python
ar.cumsum()
```




    array([ 9, 13, 13, 14, 23, 23, 24, 32, 41, 41, 49, 55, 59, 62, 62, 66, 72,
           80, 81, 89], dtype=int32)



#### Logical operators


```python
np.random.seed(100)
ar=np.random.randint(1,10, size=(4,4));ar
```




    array([[9, 9, 4, 8],
           [8, 1, 5, 3],
           [6, 3, 3, 3],
           [2, 1, 9, 5]])




```python
np.any((ar%7)==0)
```




    False




```python
np.all(ar<11)
```




    True



### Broadcasting


```python
ar=np.ones([3,2]); ar
```




    array([[ 1.,  1.],
           [ 1.,  1.],
           [ 1.,  1.]])




```python
ar2=np.array([2,3]); ar2
```




    array([2, 3])




```python
ar + ar2
```




    array([[ 3.,  4.],
           [ 3.,  4.],
           [ 3.,  4.]])




```python
ar=np.array([[23,24,25]]); ar
```




    array([[23, 24, 25]])




```python
ar.T
```




    array([[23],
           [24],
           [25]])




```python
ar.T + ar
```




    array([[46, 47, 48],
           [47, 48, 49],
           [48, 49, 50]])



### Array shape manipulation

#### Flattening a multi-dimensional array


```python
ar=np.array([np.arange(1,6), np.arange(10,15)]); ar
```




    array([[ 1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14]])




```python
ar.ravel()
```




    array([ 1,  2,  3,  4,  5, 10, 11, 12, 13, 14])




```python
ar.T.ravel()
```




    array([ 1, 10,  2, 11,  3, 12,  4, 13,  5, 14])



#### Reshaping


```python
ar = np.arange(1, 16); ar
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])




```python
ar.reshape(3,5)
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15]])



#### Resizing


```python
ar=np.arange(5); ar.resize((8,));ar
```




    array([0, 1, 2, 3, 4, 0, 0, 0])




```python
ar=np.arange(5);
```


```python
ar2=ar
```


```python
ar.resize((8,));
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-154-394f7795e2d1> in <module>()
    ----> 1 ar.resize((8,));


    ValueError: cannot resize an array that references or is referenced
    by another array in this way.  Use the resize function


#### Adding a dimension


```python
ar=np.array([14,15,16]); ar.shape
```




    (3,)




```python
ar
```




    array([14, 15, 16])




```python
ar=ar[:, np.newaxis]; ar.shape
```




    (3, 1)




```python
ar
```




    array([[14],
           [15],
           [16]])



### Array sorting


```python
ar=np.array([[3,2],[10,-1]])
ar
```




    array([[ 3,  2],
           [10, -1]])




```python
ar.sort(axis=1)
ar
```




    array([[ 2,  3],
           [-1, 10]])




```python
ar=np.array([[3,2],[10,-1]])
ar
```




    array([[ 3,  2],
           [10, -1]])




```python
ar.sort(axis=0)
ar
```




    array([[ 3, -1],
           [10,  2]])



## Data structures in pandas

### Series

#### Series creation

```py
import pandas as pd
ser=pd.Series(data, index=idx)
```

* Using numpy.ndarray


```python
import numpy as np
np.random.seed(100)
ser=pd.Series(np.random.rand(7)); ser
```




    0    0.543405
    1    0.278369
    2    0.424518
    3    0.844776
    4    0.004719
    5    0.121569
    6    0.670749
    dtype: float64




```python
import pandas as pd
import calendar as cal
monthNames = [cal.month_name[i] for i in np.arange(1,6)]
months = pd.Series(np.arange(1,6),index=monthNames);
months
```




    January     1
    February    2
    March       3
    April       4
    May         5
    dtype: int32




```python
months.index
```




    Index(['January', 'February', 'March', 'April', 'May'], dtype='object')



* Using Python dictionary


```python
currDict={'US' : 'dollar', 'UK' : 'pound',
          'Germany': 'euro', 'Mexico':'peso',
          'Nigeria':'naira',
          'China':'yuan', 'Japan':'yen'}
currSeries=pd.Series(currDict); currSeries
```




    China        yuan
    Germany      euro
    Japan         yen
    Mexico       peso
    Nigeria     naira
    UK          pound
    US         dollar
    dtype: object




```python
stockPrices = {'GOOG':1180.97,'FB':62.57,
               'TWTR': 64.50, 'AMZN':358.69,
               'AAPL':500.6}
stockPriceSeries=pd.Series(stockPrices,
                           index=['GOOG','FB','YHOO',
                                  'TWTR','AMZN','AAPL'],
                           name='stockPrices')
stockPriceSeries
```




    GOOG    1180.97
    FB        62.57
    YHOO        NaN
    TWTR      64.50
    AMZN     358.69
    AAPL     500.60
    Name: stockPrices, dtype: float64



* Using scalar values


```python
dogSeries=pd.Series('chihuahua',
                    index=['breed','countryOfOrigin',
                           'name', 'gender'])
dogSeries
```




    breed              chihuahua
    countryOfOrigin    chihuahua
    name               chihuahua
    gender             chihuahua
    dtype: object




```python
dogSeries = pd.Series('pekingese');
dogSeries
```




    0    pekingese
    dtype: object




```python
type(dogSeries)
```




    pandas.core.series.Series



#### Operations on Series

* Assignment


```python
currDict['China']
```




    'yuan'




```python
stockPriceSeries['GOOG'] = 1200.0
```


```python
stockPriceSeries['MSFT']
```


```python
stockPriceSeries.get('MSFT',np.NaN)
```




    nan



* Slicing


```python
stockPriceSeries[:4]
```




    GOOG    1200.00
    FB        62.57
    YHOO        NaN
    TWTR      64.50
    Name: stockPrices, dtype: float64




```python
stockPriceSeries[stockPriceSeries > 100]
```




    GOOG    1200.00
    AMZN     358.69
    AAPL     500.60
    Name: stockPrices, dtype: float64



* Other operations


```python
np.mean(stockPriceSeries)
```




    437.27200000000005




```python
np.std(stockPriceSeries)
```




    417.4446361087899




```python
ser
```




    0    0.543405
    1    0.278369
    2    0.424518
    3    0.844776
    4    0.004719
    5    0.121569
    6    0.670749
    dtype: float64




```python
ser*ser
```




    0    0.295289
    1    0.077490
    2    0.180215
    3    0.713647
    4    0.000022
    5    0.014779
    6    0.449904
    dtype: float64




```python
np.sqrt(ser)
```




    0    0.737160
    1    0.527607
    2    0.651550
    3    0.919117
    4    0.068694
    5    0.348668
    6    0.818993
    dtype: float64




```python
ser[1:]
```




    1    0.278369
    2    0.424518
    3    0.844776
    4    0.004719
    5    0.121569
    6    0.670749
    dtype: float64




```python
ser[1:] + ser[:-2]
```




    0         NaN
    1    0.556739
    2    0.849035
    3    1.689552
    4    0.009438
    5         NaN
    6         NaN
    dtype: float64



### DataFrame

#### DataFrame Creation

* Using dictionaries of Series


```python
stockSummaries={
    'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88],
                      index=['Closing price','EPS', 'Shares Outstanding(M)',
                             'Beta', 'P/E','Market Cap(B)']),
    'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
                      index=['Closing price','EPS','Shares Outstanding(M)',
                             'Beta','P/E','Market Cap(B)']),
    'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
                    index=['Closing price','EPS','Shares Outstanding(M)',
                           'P/E', 'Market Cap(B)']),
    'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
                      index=['Closing price','EPS','Shares Outstanding(M)',
                             'P/E','Beta', 'Market Cap(B)']),
    'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
                     index=['Closing price','EPS','Shares Outstanding(M)',
                            'Market Cap(B)']),
    'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
                     index=['Closing price','EPS','Shares Outstanding(M)',
                            'P/E','Market Cap(B)','Beta'])}
```


```python
stockDF = pd.DataFrame(stockSummaries); stockDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAPL</th>
      <th>AMZN</th>
      <th>FB</th>
      <th>GOOG</th>
      <th>TWTR</th>
      <th>YHOO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Beta</th>
      <td>0.84</td>
      <td>0.52</td>
      <td>NaN</td>
      <td>0.87</td>
      <td>NaN</td>
      <td>0.66</td>
    </tr>
    <tr>
      <th>Closing price</th>
      <td>501.53</td>
      <td>346.15</td>
      <td>61.48</td>
      <td>1133.43</td>
      <td>65.25</td>
      <td>34.90</td>
    </tr>
    <tr>
      <th>EPS</th>
      <td>40.32</td>
      <td>0.59</td>
      <td>0.59</td>
      <td>36.05</td>
      <td>-0.30</td>
      <td>1.27</td>
    </tr>
    <tr>
      <th>Market Cap(B)</th>
      <td>447.59</td>
      <td>158.88</td>
      <td>150.92</td>
      <td>380.64</td>
      <td>36.23</td>
      <td>35.36</td>
    </tr>
    <tr>
      <th>P/E</th>
      <td>12.44</td>
      <td>589.80</td>
      <td>104.93</td>
      <td>31.44</td>
      <td>NaN</td>
      <td>27.48</td>
    </tr>
    <tr>
      <th>Shares Outstanding(M)</th>
      <td>892.45</td>
      <td>459.00</td>
      <td>2450.00</td>
      <td>335.83</td>
      <td>555.20</td>
      <td>1010.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockDF=pd.DataFrame(stockSummaries,
                     index=['Closing price','EPS',
                            'Shares Outstanding(M)',
                            'P/E', 'Market Cap(B)','Beta'],
                     columns=['FB','TWTR','SCNW'])
stockDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
      <th>SCNW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Closing price</th>
      <td>61.48</td>
      <td>65.25</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>EPS</th>
      <td>0.59</td>
      <td>-0.30</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Shares Outstanding(M)</th>
      <td>2450.00</td>
      <td>555.20</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>P/E</th>
      <td>104.93</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Market Cap(B)</th>
      <td>150.92</td>
      <td>36.23</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Beta</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockDF.index
```




    Index(['Closing price', 'EPS', 'Shares Outstanding(M)', 'P/E', 'Market Cap(B)',
           'Beta'],
          dtype='object')




```python
stockDF.columns
```




    Index(['FB', 'TWTR', 'SCNW'], dtype='object')



* Using a dictionary of ndarrays/lists


```python
algos={'search':['DFS','BFS','Binary Search',
                 'Linear','ShortestPath (Djikstra)'],
       'sorting': ['Quicksort','Mergesort', 'Heapsort',
                   'Bubble Sort', 'Insertion Sort'],
       'machine learning':['RandomForest',
                           'K Nearest Neighbor',
                           'Logistic Regression',
                           'K-Means Clustering',
                           'Linear Regression']}
algoDF=pd.DataFrame(algos);
algoDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>machine learning</th>
      <th>search</th>
      <th>sorting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RandomForest</td>
      <td>DFS</td>
      <td>Quicksort</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K Nearest Neighbor</td>
      <td>BFS</td>
      <td>Mergesort</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Logistic Regression</td>
      <td>Binary Search</td>
      <td>Heapsort</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K-Means Clustering</td>
      <td>Linear</td>
      <td>Bubble Sort</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Linear Regression</td>
      <td>ShortestPath (Djikstra)</td>
      <td>Insertion Sort</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(algos,index=['algo_1','algo_2','algo_3','algo_4','algo_5'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>machine learning</th>
      <th>search</th>
      <th>sorting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>algo_1</th>
      <td>RandomForest</td>
      <td>DFS</td>
      <td>Quicksort</td>
    </tr>
    <tr>
      <th>algo_2</th>
      <td>K Nearest Neighbor</td>
      <td>BFS</td>
      <td>Mergesort</td>
    </tr>
    <tr>
      <th>algo_3</th>
      <td>Logistic Regression</td>
      <td>Binary Search</td>
      <td>Heapsort</td>
    </tr>
    <tr>
      <th>algo_4</th>
      <td>K-Means Clustering</td>
      <td>Linear</td>
      <td>Bubble Sort</td>
    </tr>
    <tr>
      <th>algo_5</th>
      <td>Linear Regression</td>
      <td>ShortestPath (Djikstra)</td>
      <td>Insertion Sort</td>
    </tr>
  </tbody>
</table>
</div>



* Using a structured array


```python
memberData = np.zeros((4,),
                      dtype=[('Name','a15'),
                             ('Age','i4'),
                             ('Weight','f4')])
memberData[:] = [('Sanjeev',37,162.4),
                 ('Yingluck',45,137.8),
                 ('Emeka',28,153.2),
                 ('Amy',67,101.3)]
memberDF = pd.DataFrame(memberData);
memberDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Sanjeev'</td>
      <td>37</td>
      <td>162.399994</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'Yingluck'</td>
      <td>45</td>
      <td>137.800003</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b'Emeka'</td>
      <td>28</td>
      <td>153.199997</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b'Amy'</td>
      <td>67</td>
      <td>101.300003</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(memberData, index=['a','b','c','d'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>b'Sanjeev'</td>
      <td>37</td>
      <td>162.399994</td>
    </tr>
    <tr>
      <th>b</th>
      <td>b'Yingluck'</td>
      <td>45</td>
      <td>137.800003</td>
    </tr>
    <tr>
      <th>c</th>
      <td>b'Emeka'</td>
      <td>28</td>
      <td>153.199997</td>
    </tr>
    <tr>
      <th>d</th>
      <td>b'Amy'</td>
      <td>67</td>
      <td>101.300003</td>
    </tr>
  </tbody>
</table>
</div>



* Using a Series structure


```python
currSeries.name='currency'
pd.DataFrame(currSeries)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>China</th>
      <td>yuan</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>euro</td>
    </tr>
    <tr>
      <th>Japan</th>
      <td>yen</td>
    </tr>
    <tr>
      <th>Mexico</th>
      <td>peso</td>
    </tr>
    <tr>
      <th>Nigeria</th>
      <td>naira</td>
    </tr>
    <tr>
      <th>UK</th>
      <td>pound</td>
    </tr>
    <tr>
      <th>US</th>
      <td>dollar</td>
    </tr>
  </tbody>
</table>
</div>



#### Operations

* Selection


```python
memberDF['Name']
```




    0     b'Sanjeev'
    1    b'Yingluck'
    2       b'Emeka'
    3         b'Amy'
    Name: Name, dtype: object



* Assignment


```python
memberDF['Height']=60;memberDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Weight</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Sanjeev'</td>
      <td>37</td>
      <td>162.399994</td>
      <td>60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'Yingluck'</td>
      <td>45</td>
      <td>137.800003</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b'Emeka'</td>
      <td>28</td>
      <td>153.199997</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b'Amy'</td>
      <td>67</td>
      <td>101.300003</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



* Deletion


```python
del memberDF['Height']; memberDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Sanjeev'</td>
      <td>37</td>
      <td>162.399994</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'Yingluck'</td>
      <td>45</td>
      <td>137.800003</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b'Emeka'</td>
      <td>28</td>
      <td>153.199997</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b'Amy'</td>
      <td>67</td>
      <td>101.300003</td>
    </tr>
  </tbody>
</table>
</div>




```python
memberDF['BloodType']='O'
bloodType=memberDF.pop('BloodType'); bloodType
```




    0    O
    1    O
    2    O
    3    O
    Name: BloodType, dtype: object




```python
memberDF.insert(2,'isSenior',memberDF['Age']>60);
memberDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>isSenior</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Sanjeev'</td>
      <td>37</td>
      <td>False</td>
      <td>162.399994</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'Yingluck'</td>
      <td>45</td>
      <td>False</td>
      <td>137.800003</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b'Emeka'</td>
      <td>28</td>
      <td>False</td>
      <td>153.199997</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b'Amy'</td>
      <td>67</td>
      <td>True</td>
      <td>101.300003</td>
    </tr>
  </tbody>
</table>
</div>



* Alignment


```python
ore1DF = pd.DataFrame(np.array([[20,35,25,20],
                                [11,28,32,29]]),
                      columns=['iron','magnesium',
                               'copper','silver'])
ore2DF = pd.DataFrame(np.array([[14,34,26,26],
                                [33,19,25,23]]),
                      columns=['iron','magnesium',
                               'gold','silver'])
ore1DF + ore2DF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>copper</th>
      <th>gold</th>
      <th>iron</th>
      <th>magnesium</th>
      <th>silver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>34</td>
      <td>69</td>
      <td>46</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>44</td>
      <td>47</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>




```python
ore1DF + pd.Series([25,25,25,25],
                   index=['iron','magnesium',
                          'copper','silver'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>iron</th>
      <th>magnesium</th>
      <th>copper</th>
      <th>silver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45</td>
      <td>60</td>
      <td>50</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>53</td>
      <td>57</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>



* Other mathematical operations


```python
np.sqrt(ore1DF)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>iron</th>
      <th>magnesium</th>
      <th>copper</th>
      <th>silver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.472136</td>
      <td>5.916080</td>
      <td>5.000000</td>
      <td>4.472136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.316625</td>
      <td>5.291503</td>
      <td>5.656854</td>
      <td>5.385165</td>
    </tr>
  </tbody>
</table>
</div>



### Panel

#### Using 3D NumPy array with axis labels


```python
stockData=np.array([[[63.03,61.48,75],
                     [62.05,62.75,46],
                     [62.74,62.19,53]],
                    [[411.90, 404.38, 2.9],
                     [405.45, 405.91, 2.6],
                     [403.15, 404.42, 2.4]]])
stockData
```




    array([[[  63.03,   61.48,   75.  ],
            [  62.05,   62.75,   46.  ],
            [  62.74,   62.19,   53.  ]],

           [[ 411.9 ,  404.38,    2.9 ],
            [ 405.45,  405.91,    2.6 ],
            [ 403.15,  404.42,    2.4 ]]])




```python
stockHistoricalPrices = pd.Panel(stockData,
                                 items=['FB', 'NFLX'],
                                 major_axis=pd.date_range('2/3/2014',
                                                          periods=3),
                                 minor_axis=['open price', 'closing price', 'volume'])
stockHistoricalPrices
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 3 (major_axis) x 3 (minor_axis)
    Items axis: FB to NFLX
    Major_axis axis: 2014-02-03 00:00:00 to 2014-02-05 00:00:00
    Minor_axis axis: open price to volume



#### Using a Python dictionary of DataFrame objects


```python
USData=pd.DataFrame(np.array([[249.62 , 8900],
                              [ 282.16,12680],
                              [309.35,14940]]),
                    columns=['Population(M)','GDP($B)'],
                    index=[1990,2000,2010])
USData
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population(M)</th>
      <th>GDP($B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1990</th>
      <td>249.62</td>
      <td>8900.0</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>282.16</td>
      <td>12680.0</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>309.35</td>
      <td>14940.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
ChinaData=pd.DataFrame(np.array([[1133.68, 390.28],
                                 [ 1266.83,1198.48],
                                 [1339.72, 6988.47]]),
                       columns=['Population(M)','GDP($B)'],
                       index=[1990,2000,2010])
ChinaData
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population(M)</th>
      <th>GDP($B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1990</th>
      <td>1133.68</td>
      <td>390.28</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>1266.83</td>
      <td>1198.48</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>1339.72</td>
      <td>6988.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
US_ChinaData={'US' : USData,
              'China': ChinaData}
pd.Panel(US_ChinaData)
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 3 (major_axis) x 2 (minor_axis)
    Items axis: China to US
    Major_axis axis: 1990 to 2010
    Minor_axis axis: Population(M) to GDP($B)



#### Using the DataFrame.to_panel method


```python
mIdx = pd.MultiIndex(levels=[['US', 'China'],
                             [1990,2000, 2010]],
                     labels=[[1,1,1,0,0,0],[0,1,2,0,1,2]])
```


```python
ChinaUSDF = pd.DataFrame({'Population(M)' : [1133.68, 1266.83,
                                             1339.72, 249.62,
                                             282.16,309.35],
                          'GDB($B)': [390.28, 1198.48, 6988.47,
                                      8900,12680, 14940]}, index=mIdx)
ChinaUSDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>GDB($B)</th>
      <th>Population(M)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">China</th>
      <th>1990</th>
      <td>390.28</td>
      <td>1133.68</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>1198.48</td>
      <td>1266.83</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>6988.47</td>
      <td>1339.72</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">US</th>
      <th>1990</th>
      <td>8900.00</td>
      <td>249.62</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>12680.00</td>
      <td>282.16</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>14940.00</td>
      <td>309.35</td>
    </tr>
  </tbody>
</table>
</div>




```python
ChinaUSDF = pd.DataFrame({'Population(M)' : [1133.68,
                                             1266.83,
                                             1339.72,
                                             249.62,
                                             282.16,
                                             309.35],
                          'GDB($B)': [390.28, 1198.48,
                                      6988.47, 8900,
                                      12680,14940]},
                         index=mIdx)
ChinaUSDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>GDB($B)</th>
      <th>Population(M)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">China</th>
      <th>1990</th>
      <td>390.28</td>
      <td>1133.68</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>1198.48</td>
      <td>1266.83</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>6988.47</td>
      <td>1339.72</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">US</th>
      <th>1990</th>
      <td>8900.00</td>
      <td>249.62</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>12680.00</td>
      <td>282.16</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>14940.00</td>
      <td>309.35</td>
    </tr>
  </tbody>
</table>
</div>




```python
ChinaUSDF.to_panel()
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 2 (major_axis) x 3 (minor_axis)
    Items axis: GDB($B) to Population(M)
    Major_axis axis: US to China
    Minor_axis axis: 1990 to 2010



#### Other operations


```python

```

## Summary
