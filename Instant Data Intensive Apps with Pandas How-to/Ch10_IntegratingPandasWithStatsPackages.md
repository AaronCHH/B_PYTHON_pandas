
# Ch10 - Integrating pandas with statistics packages (Advanced)


```python
import numpy as np
from pandas.io.data import DataReader
import pandas as pd
import statsmodels.api as sm
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
pan = pd.Panel(dfs)
```


```python
close = pan.minor_xs('Close')
```


```python
x = close[['axp', 'ba', 'gs', 'ibm']]
y = close['f']
ols_model = sm.OLS(y,x)
fit = ols_model.fit()
```


```python
fit
```




    <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x592f88f6a0>




```python
fit.tvalues
```




    axp     9.653511
    ba     10.084249
    gs     -4.929902
    ibm    38.821898
    dtype: float64




```python
fit.t()
```


```python
fit.conf_int()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>axp</th>
      <td>0.043758</td>
      <td>0.066066</td>
    </tr>
    <tr>
      <th>ba</th>
      <td>0.024589</td>
      <td>0.036460</td>
    </tr>
    <tr>
      <th>gs</th>
      <td>-0.006876</td>
      <td>-0.002963</td>
    </tr>
    <tr>
      <th>ibm</th>
      <td>0.040146</td>
      <td>0.044417</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
