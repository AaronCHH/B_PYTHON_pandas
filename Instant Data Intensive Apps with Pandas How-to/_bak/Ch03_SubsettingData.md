
# Ch03 - Subsetting data (Simple)


```python
import pandas as pd
import numpy as np
```


```python
d = {'Cost': np.random.normal(100, 5, 100),
     'Profit': np.random.normal(50, 5, 100),
     'CatA': np.random.choice(['a', 'b', 'c'], 100),
     'CatB': np.random.choice(['e', 'f', 'g'], 100)}
```


```python
df = pd.DataFrame(d)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CatA</th>
      <th>CatB</th>
      <th>Cost</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c</td>
      <td>g</td>
      <td>101.454459</td>
      <td>52.808246</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>g</td>
      <td>97.195107</td>
      <td>46.421114</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>e</td>
      <td>107.037610</td>
      <td>49.394001</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>e</td>
      <td>93.468270</td>
      <td>43.925241</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c</td>
      <td>e</td>
      <td>96.510616</td>
      <td>53.385744</td>
    </tr>
  </tbody>
</table>
</div>




```python
print (df[df.CatA == 'a'][:5])
```

       CatA CatB        Cost     Profit
    1     a    g   97.195107  46.421114
    11    a    e  102.801902  51.788275
    12    a    f   97.560271  58.403121
    13    a    e  113.309823  45.633916
    18    a    g  111.328861  52.827630
    


```python
mask = np.logical_and(df.CatA=='a', df.CatB=='e')
df[mask][:5]
a_e = ['a', 'e']
CatA_a_e = df[df.CatA.isin(a_e)]
CatA_a_e.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CatA</th>
      <th>CatB</th>
      <th>Cost</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>g</td>
      <td>97.195107</td>
      <td>46.421114</td>
    </tr>
    <tr>
      <th>11</th>
      <td>a</td>
      <td>e</td>
      <td>102.801902</td>
      <td>51.788275</td>
    </tr>
    <tr>
      <th>12</th>
      <td>a</td>
      <td>f</td>
      <td>97.560271</td>
      <td>58.403121</td>
    </tr>
    <tr>
      <th>13</th>
      <td>a</td>
      <td>e</td>
      <td>113.309823</td>
      <td>45.633916</td>
    </tr>
    <tr>
      <th>18</th>
      <td>a</td>
      <td>g</td>
      <td>111.328861</td>
      <td>52.827630</td>
    </tr>
  </tbody>
</table>
</div>




```python
only_a_e = CatA_a_e[CatA_a_e.CatB.isin(a_e)]
```


```python
print (only_a_e[:5])
```

       CatA CatB        Cost     Profit
    11    a    e  102.801902  51.788275
    13    a    e  113.309823  45.633916
    26    a    e   92.453381  55.524267
    28    a    e   91.936194  49.898428
    39    a    e   93.415774  52.785386
    


```python

```
