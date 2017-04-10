
# Ch06 - Combining datasets (Medium)


```python
import numpy as np
import pandas as pd
```


```python
rng = pd.date_range('2000-01-01', '2000-01-05')
```


```python
tickers = pd.DataFrame(['MSFT', 'AAPL'], columns= ['Ticker'])
```


```python
df1 = pd.DataFrame({'TickerID': [0]*5,
                   'Price': np.random.normal(100, 10, 5)}, index=rng)
```


```python
df2 = pd.DataFrame({'TickerID': [1]*5, 
                    'Price': np.random.normal(100, 10, 5)}, 
                   index=rng)
```


```python
pd.merge(df1, df2, left_index=True, right_index=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price_x</th>
      <th>TickerID_x</th>
      <th>Price_y</th>
      <th>TickerID_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>102.005288</td>
      <td>0</td>
      <td>99.777376</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>88.999480</td>
      <td>0</td>
      <td>114.273764</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>96.126734</td>
      <td>0</td>
      <td>91.647032</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>109.119551</td>
      <td>0</td>
      <td>90.568197</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>92.847688</td>
      <td>0</td>
      <td>106.449355</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, tickers, right_index=True, left_on='TickerID')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>TickerID</th>
      <th>Ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>102.005288</td>
      <td>0</td>
      <td>MSFT</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>88.999480</td>
      <td>0</td>
      <td>MSFT</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>96.126734</td>
      <td>0</td>
      <td>MSFT</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>109.119551</td>
      <td>0</td>
      <td>MSFT</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>92.847688</td>
      <td>0</td>
      <td>MSFT</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
