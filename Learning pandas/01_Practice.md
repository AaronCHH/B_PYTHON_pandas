

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->



<!-- tocstop -->
```python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# Set some pandas options
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

# And some items for matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'
```


```python
# read the contents of the file into a DataFrame
df = pd.read_csv('data/test1.csv')
df
```




                      date         0         1         2
    0  2000-01-01 00:00:00  1.103763 -1.909979 -0.808956
    1  2000-01-02 00:00:00  1.188917  0.581120  0.861597
    2  2000-01-03 00:00:00 -0.964200  0.779764  1.829062
    3  2000-01-04 00:00:00  0.782130 -1.720670 -1.108242
    4  2000-01-05 00:00:00 -1.867017 -0.528368 -2.488309
    5  2000-01-06 00:00:00  2.569280 -0.471901 -0.835033
    6  2000-01-07 00:00:00 -0.399323 -0.676427 -0.011256
    7  2000-01-08 00:00:00  1.642993  1.013420  1.435667
    8  2000-01-09 00:00:00  1.147308  2.138000  0.554171
    9  2000-01-10 00:00:00  0.933766  1.387155 -0.560143




```python
# read the contents of the file into a DataFrame
df = pd.read_csv('data/test3.csv')
df
```




                      date        欄0        欄1        欄2
    0  2000-01-01 00:00:00  1.103763 -1.909979 -0.808956
    1  2000-01-02 00:00:00  1.188917  0.581120  0.861597
    2  2000-01-03 00:00:00 -0.964200  0.779764  1.829062
    3  2000-01-04 00:00:00  0.782130 -1.720670 -1.108242
    4  2000-01-05 00:00:00 -1.867017 -0.528368 -2.488309
    5  2000-01-06 00:00:00  2.569280 -0.471901 -0.835033
    6  2000-01-07 00:00:00 -0.399323 -0.676427 -0.011256
    7  2000-01-08 00:00:00  1.642993  1.013420  1.435667
    8  2000-01-09 00:00:00  1.147308  2.138000  0.554171
    9  2000-01-10 00:00:00  0.933766  1.387155 -0.560143




```python

```
