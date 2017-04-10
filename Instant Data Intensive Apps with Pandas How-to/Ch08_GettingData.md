
# Ch08 - Getting data from the Web (Simple)


```python
import pandas as pd
```


```python
url = 'http://s3.amazonaws.com/trenthauck-public/book_data.csv'
df = pd.read_csv(url)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.768315</td>
      <td>-0.546547</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.659549</td>
      <td>0.231420</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-2.314531</td>
      <td>0.476687</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.179170</td>
      <td>1.580332</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.651118</td>
      <td>-1.597468</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 100 entries, 0 to 99
    Data columns (total 2 columns):
    a    100 non-null float64
    b    100 non-null float64
    dtypes: float64(2)
    memory usage: 1.6 KB
    


```python
df.dtypes
```




    a    float64
    b    float64
    dtype: object




```python

```
