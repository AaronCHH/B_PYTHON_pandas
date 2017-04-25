
# Chapter 6: Missing Data, Time Series, and Plotting Using Matplotlib
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 6: Missing Data, Time Series, and Plotting Using Matplotlib](#chapter-6-missing-data-time-series-and-plotting-using-matplotlib)
  * [6.1 Handling missing data](#61-handling-missing-data)
    * [Handling missing values](#handling-missing-values)
  * [6.2 Handling time series](#62-handling-time-series)
    * [Reading in time series data](#reading-in-time-series-data)
    * [Time series-related instance methods](#time-series-related-instance-methods)
    * [Time series concepts and datatypes](#time-series-concepts-and-datatypes)
  * [6.3 A summary of Time Series-related objects](#63-a-summary-of-time-series-related-objects)
    * [Plotting using matplotlib](#plotting-using-matplotlib)
  * [6.4 Summary](#64-summary)

<!-- tocstop -->


## 6.1 Handling missing data


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
date_stngs = ['2014-05-01','2014-05-02',
              '2014-05-05','2014-05-06','2014-05-07']
tradeDates = pd.to_datetime(pd.Series(date_stngs))
```


```python
closingPrices=[531.35,527.93,527.81,515.14,509.96]
```


```python
googClosingPrices=pd.DataFrame(data=closingPrices,
                               columns=['closingPrice'],
                               index=tradeDates)
googClosingPrices
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>closingPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>531.35</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>527.93</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>527.81</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>515.14</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>509.96</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas.io.data as web
import datetime
googPrices = web.get_data_yahoo("GOOG",
                                start=datetime.datetime(2014, 5, 1),
                                end=datetime.datetime(2014, 5, 7))
```

    C:\Anaconda3\lib\site-packages\pandas\io\data.py:35: FutureWarning:
    The pandas.io.data module is moved to a separate package (pandas-datareader) and will be removed from pandas in a future version.
    After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
      FutureWarning)



```python
googFinalPrices=pd.DataFrame(googPrices['Close'],
                             index=tradeDates)
googFinalPrices
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>531.352435</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>527.932411</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>527.812392</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>515.142330</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>509.962321</td>
    </tr>
  </tbody>
</table>
</div>




```python
googClosingPricesCDays=googClosingPrices.asfreq('D')
googClosingPricesCDays
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>closingPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>531.35</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>527.93</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>527.81</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>515.14</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>509.96</td>
    </tr>
  </tbody>
</table>
</div>




```python
googClosingPricesCDays.isnull()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>closingPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
googClosingPricesCDays.notnull()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>closingPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>False</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>True</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
tDates=tradeDates.copy()
tDates[1]=np.NaN
tDates[4]=np.NaN
```


```python
tDates
```




    0   2014-05-01
    1          NaT
    2   2014-05-05
    3   2014-05-06
    4          NaT
    dtype: datetime64[ns]




```python
FBVolume=[82.34,54.11,45.99,55.86,78.5]
TWTRVolume=[15.74,12.71,10.39,134.62,68.84]
```


```python
socialTradingVolume=pd.concat([pd.Series(FBVolume),
                               pd.Series(TWTRVolume),
                               tradeDates], axis=1,
                              keys=['FB','TWTR','TradeDate'])
socialTradingVolume
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
      <th>TradeDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>82.34</td>
      <td>15.74</td>
      <td>2014-05-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>54.11</td>
      <td>12.71</td>
      <td>2014-05-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>45.99</td>
      <td>10.39</td>
      <td>2014-05-05</td>
    </tr>
    <tr>
      <th>3</th>
      <td>55.86</td>
      <td>134.62</td>
      <td>2014-05-06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>78.50</td>
      <td>68.84</td>
      <td>2014-05-07</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTS=socialTradingVolume.set_index('TradeDate')
socialTradingVolTS
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTSCal=socialTradingVolTS.asfreq('D')
socialTradingVolTSCal
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTSCal['FB']+socialTradingVolTSCal['TWTR']
```




    TradeDate
    2014-05-01     98.08
    2014-05-02     66.82
    2014-05-03       NaN
    2014-05-04       NaN
    2014-05-05     56.38
    2014-05-06    190.48
    2014-05-07    147.34
    Freq: D, dtype: float64




```python
pd.Series([1.0,np.NaN,5.9,6])+pd.Series([3,5,2,5.6])
```




    0     4.0
    1     NaN
    2     7.9
    3    11.6
    dtype: float64




```python
pd.Series([1.0,25.0,5.5,6])/pd.Series([3,np.NaN,2,5.6])
```




    0    0.333333
    1         NaN
    2    2.750000
    3    1.071429
    dtype: float64




```python
np.mean([1.0,np.NaN,5.9,6])
```




    nan




```python
np.sum([1.0,np.NaN,5.9,6])
```




    nan




```python
pd.Series([1.0,np.NaN,5.9,6]).sum()
```




    12.9




```python
pd.Series([1.0,np.NaN,5.9,6]).mean()
```




    4.3




```python
np.nanmean([1.0,np.NaN,5.9,6])
```




    4.2999999999999998




```python
np.nansum([1.0,np.NaN,5.9,6])
```




    12.9



### Handling missing values


```python
socialTradingVolTSCal
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTSCal.fillna(100)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTSCal.fillna(method='ffill')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
socialTradingVolTSCal.fillna(method='bfill')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>



## 6.2 Handling time series


```python
socialTradingVolTSCal.dropna()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.34</td>
      <td>15.74</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.11</td>
      <td>12.71</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.99</td>
      <td>10.39</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.86</td>
      <td>134.62</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.50</td>
      <td>68.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.precision',4)
socialTradingVolTSCal.interpolate()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FB</th>
      <th>TWTR</th>
    </tr>
    <tr>
      <th>TradeDate</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>82.3400</td>
      <td>15.7400</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>54.1100</td>
      <td>12.7100</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>51.4033</td>
      <td>11.9367</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td>48.6967</td>
      <td>11.1633</td>
    </tr>
    <tr>
      <th>2014-05-05</th>
      <td>45.9900</td>
      <td>10.3900</td>
    </tr>
    <tr>
      <th>2014-05-06</th>
      <td>55.8600</td>
      <td>134.6200</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>78.5000</td>
      <td>68.8400</td>
    </tr>
  </tbody>
</table>
</div>




```python
ibmData=pd.read_csv('./Chapter 6/ibm-common-stock-closing-prices-1959_1960.csv')
ibmData.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradeDate</th>
      <th>closingPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1959-06-29</td>
      <td>445</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1959-06-30</td>
      <td>448</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1959-07-01</td>
      <td>450</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1959-07-02</td>
      <td>447e</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1959-07-06</td>
      <td>451</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(ibmData['TradeDate'])
```




    pandas.core.series.Series




```python
type(ibmData['TradeDate'][0])
```




    pandas.tslib.Timestamp




```python
ibmData['TradeDate']=pd.to_datetime(ibmData['TradeDate'])
type(ibmData['TradeDate'][0])
```




    pandas.tslib.Timestamp




```python
#Convert DataFrame to TimeSeries
#Resampling creates NaN rows for weekend dates, hence use dropna
ibmTS = ibmData.set_index('TradeDate').resample('D')['closingPrice'].dropna()
ibmTS
```

### Reading in time series data

* DateOffset and TimeDelta objects


```python
xmasDay=pd.datetime(2014,12,25)
xmasDay
```




    datetime.datetime(2014, 12, 25, 0, 0)




```python
boxingDay=xmasDay+pd.DateOffset(days=1)
boxingDay
```




    Timestamp('2014-12-26 00:00:00')




```python
today=pd.datetime.now()
today
```




    datetime.datetime(2016, 12, 19, 23, 22, 36, 791918)




```python
today+pd.DateOffset(weeks=1)
```




    Timestamp('2016-12-26 23:22:19.143359')




```python
today+2*pd.DateOffset(years=2, months=6)
```




    Timestamp('2021-12-19 23:22:36.791918')




```python
lastDay=pd.datetime(2013,12,31)
from pandas.tseries.offsets import QuarterBegin
dtoffset=QuarterBegin()
lastDay+dtoffset
```




    Timestamp('2014-03-01 00:00:00')




```python
dtoffset.rollforward(lastDay)
```




    Timestamp('2014-03-01 00:00:00')




```python
weekDelta=datetime.timedelta(weeks=1)
weekDelta
```




    datetime.timedelta(7)




```python
today=pd.datetime.now()
today
```




    datetime.datetime(2016, 12, 19, 23, 24, 3, 839929)




```python
today+weekDelta
```




    datetime.datetime(2016, 12, 26, 23, 24, 3, 839929)



### Time series-related instance methods

* Shifting/lagging


```python
ibmTS.shift(3)
```


```python
ibmTS.shift(3, freq=pd.datetools.bday)
```

* Frequency conversion


```python
# Frequency conversion using asfreq
ibmTS.asfreq('BM')
```


```python
ibmTS.asfreq('H')
```


```python
ibmTS.asfreq('H', method='ffill')
```

* Resampling of data


```python
googTickData=pd.read_csv('./Chapter 6/GOOG_tickdata_20140527.csv')
googTickData.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Timestamp</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1401197402</td>
      <td>555.008</td>
      <td>556.41</td>
      <td>554.35</td>
      <td>556.38</td>
      <td>81100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1401197460</td>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1401197526</td>
      <td>556.730</td>
      <td>556.75</td>
      <td>556.05</td>
      <td>556.39</td>
      <td>9900</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1401197582</td>
      <td>557.480</td>
      <td>557.67</td>
      <td>556.73</td>
      <td>556.73</td>
      <td>14700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1401197642</td>
      <td>558.155</td>
      <td>558.66</td>
      <td>557.48</td>
      <td>557.59</td>
      <td>15700</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickData['tstamp']=pd.to_datetime(googTickData['Timestamp'],unit='s',utc=True)
googTickData.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Timestamp</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
      <th>tstamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1401197402</td>
      <td>555.008</td>
      <td>556.41</td>
      <td>554.35</td>
      <td>556.38</td>
      <td>81100</td>
      <td>2014-05-27 13:30:02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1401197460</td>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500</td>
      <td>2014-05-27 13:31:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1401197526</td>
      <td>556.730</td>
      <td>556.75</td>
      <td>556.05</td>
      <td>556.39</td>
      <td>9900</td>
      <td>2014-05-27 13:32:06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1401197582</td>
      <td>557.480</td>
      <td>557.67</td>
      <td>556.73</td>
      <td>556.73</td>
      <td>14700</td>
      <td>2014-05-27 13:33:02</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1401197642</td>
      <td>558.155</td>
      <td>558.66</td>
      <td>557.48</td>
      <td>557.59</td>
      <td>15700</td>
      <td>2014-05-27 13:34:02</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickTS=googTickData.set_index('tstamp')
googTickTS=googTickTS.drop('Timestamp',axis=1)
googTickTS.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 13:30:02</th>
      <td>555.008</td>
      <td>556.41</td>
      <td>554.35</td>
      <td>556.38</td>
      <td>81100</td>
    </tr>
    <tr>
      <th>2014-05-27 13:31:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500</td>
    </tr>
    <tr>
      <th>2014-05-27 13:32:06</th>
      <td>556.730</td>
      <td>556.75</td>
      <td>556.05</td>
      <td>556.39</td>
      <td>9900</td>
    </tr>
    <tr>
      <th>2014-05-27 13:33:02</th>
      <td>557.480</td>
      <td>557.67</td>
      <td>556.73</td>
      <td>556.73</td>
      <td>14700</td>
    </tr>
    <tr>
      <th>2014-05-27 13:34:02</th>
      <td>558.155</td>
      <td>558.66</td>
      <td>557.48</td>
      <td>557.59</td>
      <td>15700</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickTS.index=googTickTS.index.tz_localize('UTC').tz_convert('US/Eastern')
googTickTS.head()
```


```python
googTickTS.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 15:56:00-04:00</th>
      <td>565.4300</td>
      <td>565.48</td>
      <td>565.30</td>
      <td>565.385</td>
      <td>14300</td>
    </tr>
    <tr>
      <th>2014-05-27 15:57:00-04:00</th>
      <td>565.3050</td>
      <td>565.46</td>
      <td>565.20</td>
      <td>565.400</td>
      <td>14700</td>
    </tr>
    <tr>
      <th>2014-05-27 15:58:00-04:00</th>
      <td>565.1101</td>
      <td>565.31</td>
      <td>565.10</td>
      <td>565.310</td>
      <td>23200</td>
    </tr>
    <tr>
      <th>2014-05-27 15:59:00-04:00</th>
      <td>565.9400</td>
      <td>566.00</td>
      <td>565.08</td>
      <td>565.230</td>
      <td>55600</td>
    </tr>
    <tr>
      <th>2014-05-27 16:00:00-04:00</th>
      <td>565.9500</td>
      <td>565.95</td>
      <td>565.95</td>
      <td>565.950</td>
      <td>126000</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(googTickTS)
```




    390




```python
googTickTS.resample('5Min').head(6)
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: .resample() is now a deferred operation
    use .resample(...).mean() instead of .resample(...)
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 09:30:00-04:00</th>
      <td>556.7246</td>
      <td>557.1580</td>
      <td>555.972</td>
      <td>556.4680</td>
      <td>27980</td>
    </tr>
    <tr>
      <th>2014-05-27 09:35:00-04:00</th>
      <td>556.9365</td>
      <td>557.6480</td>
      <td>556.851</td>
      <td>557.3420</td>
      <td>24620</td>
    </tr>
    <tr>
      <th>2014-05-27 09:40:00-04:00</th>
      <td>556.4860</td>
      <td>556.7999</td>
      <td>556.277</td>
      <td>556.6068</td>
      <td>8620</td>
    </tr>
    <tr>
      <th>2014-05-27 09:45:00-04:00</th>
      <td>557.0530</td>
      <td>557.2760</td>
      <td>556.738</td>
      <td>556.9660</td>
      <td>9720</td>
    </tr>
    <tr>
      <th>2014-05-27 09:50:00-04:00</th>
      <td>556.6620</td>
      <td>556.9360</td>
      <td>556.464</td>
      <td>556.8033</td>
      <td>14560</td>
    </tr>
    <tr>
      <th>2014-05-27 09:55:00-04:00</th>
      <td>555.9658</td>
      <td>556.3540</td>
      <td>555.858</td>
      <td>556.2360</td>
      <td>12400</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickTS.resample('10Min', how=np.min).head(4)
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: how in .resample() is deprecated
    the new syntax is .resample(...)..apply(<func>)
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 09:30:00-04:00</th>
      <td>555.008</td>
      <td>556.3000</td>
      <td>554.35</td>
      <td>555.25</td>
      <td>9900</td>
    </tr>
    <tr>
      <th>2014-05-27 09:40:00-04:00</th>
      <td>556.190</td>
      <td>556.5600</td>
      <td>556.13</td>
      <td>556.35</td>
      <td>3500</td>
    </tr>
    <tr>
      <th>2014-05-27 09:50:00-04:00</th>
      <td>554.770</td>
      <td>555.5500</td>
      <td>554.77</td>
      <td>555.55</td>
      <td>3400</td>
    </tr>
    <tr>
      <th>2014-05-27 10:00:00-04:00</th>
      <td>554.580</td>
      <td>554.9847</td>
      <td>554.45</td>
      <td>554.58</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.precision',5)
googTickTS.resample('5Min', closed='right').tail(3)
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:2: FutureWarning: .resample() is now a deferred operation
    use .resample(...).mean() instead of .resample(...)
      from ipykernel import kernelapp as app





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 15:45:00-04:00</th>
      <td>564.31667</td>
      <td>564.37333</td>
      <td>564.10750</td>
      <td>564.16998</td>
      <td>12816.66667</td>
    </tr>
    <tr>
      <th>2014-05-27 15:50:00-04:00</th>
      <td>565.11275</td>
      <td>565.17250</td>
      <td>565.00900</td>
      <td>565.06500</td>
      <td>13325.00000</td>
    </tr>
    <tr>
      <th>2014-05-27 15:55:00-04:00</th>
      <td>565.51585</td>
      <td>565.60333</td>
      <td>565.30833</td>
      <td>565.41583</td>
      <td>40933.33333</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickTS[:3].resample('30s', fill_method='ffill')
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: fill_method is deprecated to .resample()
    the new syntax is .resample(...).ffill()
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 09:30:00-04:00</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-27 09:30:30-04:00</th>
      <td>555.008</td>
      <td>556.41</td>
      <td>554.35</td>
      <td>556.38</td>
      <td>81100.0</td>
    </tr>
    <tr>
      <th>2014-05-27 09:31:00-04:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500.0</td>
    </tr>
    <tr>
      <th>2014-05-27 09:31:30-04:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500.0</td>
    </tr>
    <tr>
      <th>2014-05-27 09:32:00-04:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
googTickTS[:3].resample('30s', fill_method='bfill')
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: fill_method is deprecated to .resample()
    the new syntax is .resample(...).bfill()
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 09:30:00-04:00</th>
      <td>555.008</td>
      <td>556.41</td>
      <td>554.35</td>
      <td>556.38</td>
      <td>81100</td>
    </tr>
    <tr>
      <th>2014-05-27 09:30:30-04:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500</td>
    </tr>
    <tr>
      <th>2014-05-27 09:31:00-04:00</th>
      <td>556.250</td>
      <td>556.30</td>
      <td>555.25</td>
      <td>555.25</td>
      <td>18500</td>
    </tr>
    <tr>
      <th>2014-05-27 09:31:30-04:00</th>
      <td>556.730</td>
      <td>556.75</td>
      <td>556.05</td>
      <td>556.39</td>
      <td>9900</td>
    </tr>
    <tr>
      <th>2014-05-27 09:32:00-04:00</th>
      <td>556.730</td>
      <td>556.75</td>
      <td>556.05</td>
      <td>556.39</td>
      <td>9900</td>
    </tr>
  </tbody>
</table>
</div>



* Aliases for Time Series frequencies


```python
googTickTS.resample('7T30S').head(5)
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: .resample() is now a deferred operation
    use .resample(...).mean() instead of .resample(...)
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>tstamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-27 09:30:00-04:00</th>
      <td>556.82662</td>
      <td>557.43625</td>
      <td>556.31437</td>
      <td>556.88000</td>
      <td>28075.00000</td>
    </tr>
    <tr>
      <th>2014-05-27 09:37:30-04:00</th>
      <td>556.58891</td>
      <td>556.93424</td>
      <td>556.42643</td>
      <td>556.72056</td>
      <td>11642.85714</td>
    </tr>
    <tr>
      <th>2014-05-27 09:45:00-04:00</th>
      <td>556.99214</td>
      <td>557.21854</td>
      <td>556.71714</td>
      <td>556.98711</td>
      <td>9800.00000</td>
    </tr>
    <tr>
      <th>2014-05-27 09:52:30-04:00</th>
      <td>556.18238</td>
      <td>556.53750</td>
      <td>556.03500</td>
      <td>556.38956</td>
      <td>14350.00000</td>
    </tr>
    <tr>
      <th>2014-05-27 10:00:00-04:00</th>
      <td>555.21115</td>
      <td>555.43684</td>
      <td>554.82876</td>
      <td>554.96750</td>
      <td>12512.50000</td>
    </tr>
  </tbody>
</table>
</div>



### Time series concepts and datatypes
* Period and PeriodIndex


```python
# Period representing May 2014
pd.Period('2014', freq='A-MAY')
```




    Period('2014', 'A-MAY')




```python
# Period representing specific day – June 11, 2014
pd.Period('06/11/2014')
```




    Period('2014-06-11', 'D')




```python
# Period representing 11AM, Nov 11, 1918
pd.Period('11/11/1918 11:00',freq='H')
```




    Period('1918-11-11 11:00', 'H')




```python
pd.Period('06/30/2014')+4
```




    Period('2014-07-04', 'D')




```python
pd.Period('11/11/1918 11:00',freq='H') - 48
```




    Period('1918-11-09 11:00', 'H')




```python
pd.Period('2014-04', freq='M')-pd.Period('2013-02', freq='M')
```




    14



* PeriodIndex


```python
perRng=pd.period_range('02/01/2014','02/06/2014',freq='D')
perRng
```




    PeriodIndex(['2014-02-01', '2014-02-02', '2014-02-03', '2014-02-04',
                 '2014-02-05', '2014-02-06'],
                dtype='int64', freq='D')




```python
type(perRng[:2])
```




    pandas.tseries.period.PeriodIndex




```python
perRng[:2]
```




    PeriodIndex(['2014-02-01', '2014-02-02'], dtype='int64', freq='D')




```python
JulyPeriod=pd.PeriodIndex(['07/01/2014','07/31/2014'], freq='D')
JulyPeriod
```




    PeriodIndex(['2014-07-01', '2014-07-31'], dtype='int64', freq='D')



* Conversion between Time Series datatypes


```python
worldCupFinal=pd.to_datetime('07/13/2014', errors='raise')
worldCupFinal
```




    Timestamp('2014-07-13 00:00:00')




```python
worldCupFinal.to_period('D')
```




    Period('2014-07-13', 'D')




```python
worldCupKickoff=pd.Period('06/12/2014','D')
worldCupKickoff
```




    Period('2014-06-12', 'D')




```python
worldCupKickoff.to_timestamp()
```




    Timestamp('2014-06-12 00:00:00')




```python
worldCupDays=pd.date_range('06/12/2014',periods=32, freq='D')
worldCupDays
```




    DatetimeIndex(['2014-06-12', '2014-06-13', '2014-06-14', '2014-06-15',
                   '2014-06-16', '2014-06-17', '2014-06-18', '2014-06-19',
                   '2014-06-20', '2014-06-21', '2014-06-22', '2014-06-23',
                   '2014-06-24', '2014-06-25', '2014-06-26', '2014-06-27',
                   '2014-06-28', '2014-06-29', '2014-06-30', '2014-07-01',
                   '2014-07-02', '2014-07-03', '2014-07-04', '2014-07-05',
                   '2014-07-06', '2014-07-07', '2014-07-08', '2014-07-09',
                   '2014-07-10', '2014-07-11', '2014-07-12', '2014-07-13'],
                  dtype='datetime64[ns]', freq='D')




```python
worldCupDays.to_period()
```




    PeriodIndex(['2014-06-12', '2014-06-13', '2014-06-14', '2014-06-15',
                 '2014-06-16', '2014-06-17', '2014-06-18', '2014-06-19',
                 '2014-06-20', '2014-06-21', '2014-06-22', '2014-06-23',
                 '2014-06-24', '2014-06-25', '2014-06-26', '2014-06-27',
                 '2014-06-28', '2014-06-29', '2014-06-30', '2014-07-01',
                 '2014-07-02', '2014-07-03', '2014-07-04', '2014-07-05',
                 '2014-07-06', '2014-07-07', '2014-07-08', '2014-07-09',
                 '2014-07-10', '2014-07-11', '2014-07-12', '2014-07-13'],
                dtype='int64', freq='D')



## 6.3 A summary of Time Series-related objects

### Plotting using matplotlib


```python
import matplotlib.pyplot as plt
```


```python
import numpy as np
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
f,g = np.cos(X)+np.sin(X), np.sin(X)-np.cos(X)
f_ser=pd.Series(f)
g_ser=pd.Series(g)
plotDF=pd.concat([f_ser,g_ser],axis=1)
plotDF.index=X
```


```python
plotDF.columns=['sin(x)+cos(x)','sin(x)-cos(x)']
plotDF.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sin(x)+cos(x)</th>
      <th>sin(x)-cos(x)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-3.14159</th>
      <td>-1.00000</td>
      <td>1.00000</td>
    </tr>
    <tr>
      <th>-3.11695</th>
      <td>-1.02433</td>
      <td>0.97506</td>
    </tr>
    <tr>
      <th>-3.09231</th>
      <td>-1.04805</td>
      <td>0.94953</td>
    </tr>
    <tr>
      <th>-3.06767</th>
      <td>-1.07112</td>
      <td>0.92342</td>
    </tr>
    <tr>
      <th>-3.04303</th>
      <td>-1.09355</td>
      <td>0.89675</td>
    </tr>
  </tbody>
</table>
</div>




```python
plotDF.plot()
plt.show()
```


![png](Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_files/Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_98_0.png)



```python
plotDF.columns=['f(x)','g(x)']
plotDF.plot(title='Plot of f(x)=sin(x)+cos(x), g(x)=sinx(x)-cos(x)')
plt.show()
```


![png](Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_files/Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_99_0.png)



```python
plotDF.plot(subplots=True, figsize=(6,6))
plt.show()
```


![png](Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_files/Ch06_Missing_Data%2C_Time_Series%2C_and_Plotting_Using_Matplotlib_100_0.png)


## 6.4 Summary


```python

```
