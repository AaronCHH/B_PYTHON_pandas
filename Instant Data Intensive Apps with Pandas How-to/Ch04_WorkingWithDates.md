
# Ch04 - Working with dates (Medium)


```python
import pandas as pd
import numpy as np
```


```python
Y2K = pd.date_range('2000-01-01', '2000-12-31')
Y2K
```




    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
                   '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08',
                   '2000-01-09', '2000-01-10',
                   ...
                   '2000-12-22', '2000-12-23', '2000-12-24', '2000-12-25',
                   '2000-12-26', '2000-12-27', '2000-12-28', '2000-12-29',
                   '2000-12-30', '2000-12-31'],
                  dtype='datetime64[ns]', length=366, freq='D')




```python
Y2K_hourly = pd.date_range('2000-01-01', '2000-12-31', freq='H')
Y2K_temp = pd.Series(np.random.normal(75, 10, len(Y2K)), index=Y2K)
```


```python
Y2K_temp['2000-01-01':'2000-01-02']
from datetime import date
Y2K_temp[date(2000, 1, 1):date(2000, 1, 2)]
Y2K_temp.resample('H', fill_method='pad')[:1]
Y2K_temp.head()
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:4: FutureWarning: fill_method is deprecated to .resample()
    the new syntax is .resample(...).pad()
    




    2000-01-01    71.338515
    2000-01-02    72.811898
    2000-01-03    87.707299
    2000-01-04    84.367695
    2000-01-05    57.571880
    Freq: D, dtype: float64




```python

```
