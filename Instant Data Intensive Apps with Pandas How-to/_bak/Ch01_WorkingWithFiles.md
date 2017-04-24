
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
    n   8.437420  10.735015
    a  11.851225  10.897672
    m  11.663746  10.762064
    e   9.140417   9.761845
    


```python
print(df.A)
```

    a
    n     8.437420
    a    11.851225
    m    11.663746
    e     9.140417
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
print df.to_string()
```


```python
pd.read_csv('df.csv')
```


```python
with open('df.json', 'w') as f:
    json.dump(df.to_dict(),to_dict f)
```


```python
with open(‘df.json’) as f:
    df_json = json.load(f)
```
