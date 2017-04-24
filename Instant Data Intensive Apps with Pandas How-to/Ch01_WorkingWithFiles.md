
# Ch01 - Working with files (Simple)


```python
import pandas as pd #standard convention throughout the book
import numpy as np
```


```python
#Create a simple DataFrame
my_df = pd.DataFrame([1,2,3])
print(my_df)
```

       0
    0  1
    1  2
    2  3
    


```python
cols = ['A', 'B']
idx = pd.Index(list('name'), name='a')
data = np.random.normal(10, 1, (4, 2))
df = pd.DataFrame(data, columns=cols, index=idx)
```


```python
print(df)
```

               A          B
    a                      
    n   9.860958   8.843439
    a   9.632312  11.135734
    m   8.762392  10.922028
    e  10.502465  10.054965
    


```python
print(df.A)
```

    a
    n     9.860958
    a     9.632312
    m     8.762392
    e    10.502465
    Name: A, dtype: float64
    


```python
pan = pd.Panel({'df1': df, 'df2': df})
print(pan)
```

    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 4 (major_axis) x 2 (minor_axis)
    Items axis: df1 to df2
    Major_axis axis: n to e
    Minor_axis axis: A to B
    


```python
df.to_csv('df.csv')
df.to_latex('df.tex') #useful with Pweave
df.to_excel('df.xlsx') #requires extra packages
df.to_html('df.html')
print(df.to_string())
```

               A          B
    a                      
    n   9.860958   8.843439
    a   9.632312  11.135734
    m   8.762392  10.922028
    e  10.502465  10.054965
    


```python
pd.read_csv('df.csv')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>n</td>
      <td>9.860958</td>
      <td>8.843439</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>9.632312</td>
      <td>11.135734</td>
    </tr>
    <tr>
      <th>2</th>
      <td>m</td>
      <td>8.762392</td>
      <td>10.922028</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e</td>
      <td>10.502465</td>
      <td>10.054965</td>
    </tr>
  </tbody>
</table>
</div>




```python
import json
```


```python
with open('df.json', 'w') as f:
    json.dump(df.to_dict(), f)
```


```python
with open('df.json') as f:
    df_json = json.load(f)
```


```python
df_json
```




    {'A': {'a': 9.632312190738741,
      'e': 10.50246514841397,
      'm': 8.762391711061914,
      'n': 9.86095810726794},
     'B': {'a': 11.135734396151403,
      'e': 10.054964686167159,
      'm': 10.92202788643155,
      'n': 8.843438663762372}}




```python

```
