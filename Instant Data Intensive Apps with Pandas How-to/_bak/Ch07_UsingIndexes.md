
# Ch07 - Using indexes to manipulate objects (Medium)


```python
import numpy as np
import pandas as pd
from pandas.io.data import DataReader
```

    C:\Anaconda3\lib\site-packages\pandas\io\data.py:35: FutureWarning: 
    The pandas.io.data module is moved to a separate package (pandas-datareader) and will be removed from pandas in a future version.
    After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
      FutureWarning)
    


```python
tickers = ['gs', 'ibm', 'f', 'ba', 'axp']
dfs = {}
for ticker in tickers:
    dfs[ticker] = DataReader(ticker, "yahoo", '2006-01-01')
```


```python
# a yet undiscussed data structure, in the same way the a         # DataFrame is a collection of Series, a Panel is a collection of # DataFrames
pan = pd.Panel(dfs)
pan
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 5 (items) x 2761 (major_axis) x 6 (minor_axis)
    Items axis: axp to ibm
    Major_axis axis: 2006-01-03 00:00:00 to 2016-12-19 00:00:00
    Minor_axis axis: Open to Adj Close




```python
pan.items
```




    Index(['axp', 'ba', 'f', 'gs', 'ibm'], dtype='object')




```python
pan.minor_axis
```




    Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], dtype='object')




```python
pan.major_axis
pan.minor_xs('Open').mean()
```




    axp     57.033343
    ba      91.009290
    f       11.162771
    gs     159.183694
    ibm    144.339345
    dtype: float64




```python
# major axis is sliceable as well
day_slice = pan.major_axis[1]
pan.major_xs(day_slice)[['gs', 'ba']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gs</th>
      <th>ba</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Open</th>
      <td>1.273500e+02</td>
      <td>7.008000e+01</td>
    </tr>
    <tr>
      <th>High</th>
      <td>1.289100e+02</td>
      <td>7.127000e+01</td>
    </tr>
    <tr>
      <th>Low</th>
      <td>1.263800e+02</td>
      <td>6.986000e+01</td>
    </tr>
    <tr>
      <th>Close</th>
      <td>1.270900e+02</td>
      <td>7.117000e+01</td>
    </tr>
    <tr>
      <th>Volume</th>
      <td>4.861600e+06</td>
      <td>3.165000e+06</td>
    </tr>
    <tr>
      <th>Adj Close</th>
      <td>1.118300e+02</td>
      <td>5.461842e+01</td>
    </tr>
  </tbody>
</table>
</div>




```python
for df in pan:
    print([df])
```

    ['axp']
    ['ba']
    ['f']
    ['gs']
    ['ibm']
    


```python
dfs = []
for df in pan:
    idx = pan.major_axis
    print(idx)
    print(idx.shape[0])
#     idx = pd.MultiIndex.from_tuples(zip([dfs]*len(idx), idx))
    idx = pd.MultiIndex.from_tuples(zip([df]*idx.shape[0], idx))
    idx.names = ['ticker', 'timestamp']
    dfs.append(pd.DataFrame(pan[df].values, index=idx,  columns=pan.minor_axis))
```


```python
df = pd.concat(dfs)
```


```python
print df
```


```python
print df.ix['gs':'ibm']
print df['Open']
```


```python

```
