
# Ch02 - Slicing pandas objects (Simple)


```python
import numpy as np
import pandas as pd
```


```python
dim = (10, 3)
df = pd.DataFrame(np.random.normal(0, 1, dim), columns=['one', 'two', 'three'])
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
      <td>0.443203</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.104274</td>
      <td>-0.770589</td>
      <td>-0.291118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.170701</td>
      <td>1.764555</td>
      <td>-1.093696</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.338280</td>
      <td>0.814837</td>
      <td>0.050361</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.217414</td>
      <td>-1.335033</td>
      <td>0.205164</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['one'][:2]
```




    0   -0.307193
    1    1.104274
    Name: one, dtype: float64




```python
df[['one', 'two']][:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.104274</td>
      <td>-0.770589</td>
    </tr>
  </tbody>
</table>
</div>



* Use .loc


```python
df.loc[:2, ['one', 'two']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.104274</td>
      <td>-0.770589</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.170701</td>
      <td>1.764555</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.ix[:2, ['one', 'two']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.104274</td>
      <td>-0.770589</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.170701</td>
      <td>1.764555</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['one', 'two']][-3:-2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>-0.385934</td>
      <td>0.023691</td>
    </tr>
  </tbody>
</table>
</div>



* Use iloc


```python
df.iloc[-3:-2, 0:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>-0.385934</td>
      <td>0.023691</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[::5]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
      <td>0.443203</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.284679</td>
      <td>0.179049</td>
      <td>-1.465171</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.307193</td>
      <td>-0.153684</td>
      <td>0.443203</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.104274</td>
      <td>-0.770589</td>
      <td>-0.291118</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
