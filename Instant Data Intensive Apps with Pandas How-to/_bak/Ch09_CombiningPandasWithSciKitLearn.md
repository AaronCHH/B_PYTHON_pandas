
# Ch09 - Combining pandas with scikit-learn (Advanced)


```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
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
```


```python
close = pan.minor_xs('Close')
```


```python
close.plot()
plt.show()
```


![png](Ch09_CombiningPandasWithSciKitLearn_files/Ch09_CombiningPandasWithSciKitLearn_5_0.png)



```python
diff = (close - close.shift(1))
diff = diff[diff < 0].fillna(0)
diff = diff[diff >= 0].fillna(1)
diff.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>axp</th>
      <th>ba</th>
      <th>f</th>
      <th>gs</th>
      <th>ibm</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-03</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-01-04</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2006-01-05</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-01-06</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-01-09</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
x = diff[['axp', 'ba', 'ibm', 'gs']]
y = diff['f']
obj = svm.SVC()
ft = obj.fit(x, y)
ft
```




    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
      max_iter=-1, probability=False, random_state=None, shrinking=True,
      tol=0.001, verbose=False)




```python
#so given the fit, we can then look at predictions
#all stocks up
ft.predict([1,1,1,1])
```

    C:\Anaconda3\lib\site-packages\sklearn\utils\validation.py:386: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and willraise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
      DeprecationWarning)
    




    array([ 1.])




```python
#all stocks down
ft.predict([0,0,0,0])
```

    C:\Anaconda3\lib\site-packages\sklearn\utils\validation.py:386: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and willraise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
      DeprecationWarning)
    




    array([ 0.])


