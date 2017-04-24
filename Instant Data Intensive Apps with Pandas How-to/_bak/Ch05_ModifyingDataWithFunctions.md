
# Ch05 - Modifying data with functions (Simple)


```python
import pandas as pd
import numpy as np
```


```python
data = {'Open': np.random.normal(100, 5, 366),
        'Close': np.random.normal(100, 5, 366)}
```


```python
df = pd.DataFrame(data)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close</th>
      <th>Open</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>104.392516</td>
      <td>106.029530</td>
    </tr>
    <tr>
      <th>1</th>
      <td>97.335476</td>
      <td>96.547402</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101.226359</td>
      <td>102.022804</td>
    </tr>
    <tr>
      <th>3</th>
      <td>99.953867</td>
      <td>102.783661</td>
    </tr>
    <tr>
      <th>4</th>
      <td>106.126685</td>
      <td>102.484453</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.apply(np.mean, axis=1).head(3)
```




    0    105.211023
    1     96.941439
    2    101.624581
    dtype: float64




```python
#passing a lambda is a common pattern
df.apply(lambda x: (x['Open'] - x['Close']), axis=1).head(3)
#define a more complex function
def percent_change(x):
    return (x['Open'] - x['Close']) / x['Open']
```


```python
df.apply(percent_change, axis=1).head(3)
```




    0    0.015439
    1   -0.008163
    2    0.007807
    dtype: float64




```python
#change axis, axis = 0 is default
df.apply(np.mean, axis=0)
```




    Close     99.986877
    Open     100.103914
    dtype: float64




```python
def greater_than_x(element, x):
    return element > x
```


```python
df.Open.apply(greater_than_x, args=(100,)).head(3)
```




    0     True
    1    False
    2     True
    Name: Open, dtype: bool




```python
#This can be used as in conjunction with subset capabilities
mask = df.Open.apply(greater_than_x, args=(100,))
```


```python
df.Open[mask].head()
```




    0    106.029530
    2    102.022804
    3    102.783661
    4    102.484453
    9    101.685135
    Name: Open, dtype: float64




```python
pd.rolling_apply(df.Close, 5, np.mean).head()
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: pd.rolling_apply is deprecated for Series and will be removed in a future version, replace with 
    	Series.rolling(center=False,window=5).apply(kwargs=<dict>,func=<function>,args=<tuple>)
      if __name__ == '__main__':
    




    0           NaN
    1           NaN
    2           NaN
    3           NaN
    4    101.806981
    Name: Close, dtype: float64




```python
#There are actually a several built-in rolling functions
pd.rolling_corr(df.Close, df.Open, 5)[:5]
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:2: FutureWarning: pd.rolling_corr is deprecated for Series and will be removed in a future version, replace with 
    	Series.rolling(window=5).corr(other=<Series>)
      from ipykernel import kernelapp as app
    




    0         NaN
    1         NaN
    2         NaN
    3         NaN
    4    0.738859
    dtype: float64


