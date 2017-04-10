
# Chapter 5. Getting Started with pandas

## 5.1 Introduction to pandas Data Structures


```python
from pandas import Series, DataFrame
import pandas as pd
```


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
```


```python
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)
```


```python
%pwd
```

### 5.1.1 Series


```python
obj = Series([4, 7, -5, 3])
obj
```


```python
obj.values
obj.index
```


```python
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
```


```python
obj2.index
```


```python
obj2['a']
```


```python
obj2['d'] = 6
obj2[['c', 'a', 'd']]
```


```python
obj2[obj2 > 0]
```


```python
obj2 * 2
```


```python
np.exp(obj2)
```


```python
'b' in obj2
```


```python
'e' in obj2
```


```python
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3
```


```python
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4
```


```python
pd.isnull(obj4)
```


```python
pd.notnull(obj4)
```


```python
obj4.isnull()
```


```python
obj3
```


```python
obj4
```


```python
obj3 + obj4
```


```python
obj4.name = 'population'
obj4.index.name = 'state'
obj4
```


```python
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj
```

### 5.1.2 DataFrame


```python
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
```


```python
frame
```


```python
DataFrame(data, columns=['year', 'state', 'pop'])
```


```python
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
```


```python
frame2.columns
```


```python
frame2['state']
```


```python
frame2.year
```


```python
frame2.ix['three']
```


```python
frame2['debt'] = 16.5
frame2
```


```python
frame2['debt'] = np.arange(5.)
frame2
```


```python
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2
```


```python
frame2['eastern'] = frame2.state == 'Ohio'
frame2
```


```python
del frame2['eastern']
frame2.columns
```


```python
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
```


```python
frame3 = DataFrame(pop)
frame3
```


```python
frame3.T
```


```python
DataFrame(pop, index=[2001, 2002, 2003])
```


```python
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata)
```


```python
frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
```


```python
frame3.values
```


```python
frame2.values
```

### 5.1.3 Index Objects


```python
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index
```


```python
index[1:]
```


```python
index[1] = 'd'
```


```python
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index
```


```python
frame3
```


```python
'Ohio' in frame3.columns
```


```python
2003 in frame3.index
```

## 5.2 Essential Functionality

### 5.2.1 Reindexing


```python
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
```


```python
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
```


```python
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
```


```python
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')
```


```python
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
frame
```


```python
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2
```


```python
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)
```


```python
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',
              columns=states)
```


```python
frame.ix[['a', 'b', 'c', 'd'], states]
```

### 5.2.2 Dropping entries from an axis


```python
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj
```


```python
obj.drop(['d', 'c'])
```


```python
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
```


```python
data.drop(['Colorado', 'Ohio'])
```


```python
data.drop('two', axis=1)
```


```python
data.drop(['two', 'four'], axis=1)
```

### 5.2.3 Indexing, selection, and filtering


```python
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj['b']
```


```python
obj[1]
```


```python
obj[2:4]
```


```python
obj[['b', 'a', 'd']]
```


```python
obj[[1, 3]]
```


```python
obj[obj < 2]
```


```python
obj['b':'c']
```


```python
obj['b':'c'] = 5
obj
```


```python
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data
```


```python
data['two']
```


```python
data[['three', 'one']]
```


```python
data[:2]
```


```python
data[data['three'] > 5]
```


```python
data < 5
```


```python
data[data < 5] = 0
```


```python
data
```


```python
data.ix['Colorado', ['two', 'three']]
```


```python
data.ix[['Colorado', 'Utah'], [3, 0, 1]]
```


```python
data.ix[2]
```


```python
data.ix[:'Utah', 'two']
```


```python
data.ix[data.three > 5, :3]
```

### 5.2.4 Arithmetic and data alignment


```python
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
```


```python
s1
```


```python
s2
```


```python
s1 + s2
```


```python
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
```


```python
df2
```


```python
df1 + df2
```

* __Arithmetic methods with fill values__


```python
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1
```


```python
df2
```


```python
df1 + df2
```


```python
df1.add(df2, fill_value=0)
```


```python
df1.reindex(columns=df2.columns, fill_value=0)
```

* __Operations between DataFrame and Series__


```python
arr = np.arange(12.).reshape((3, 4))
arr
```


```python
arr[0]
```


```python
arr - arr[0]
```


```python
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
frame
```


```python
series
```


```python
frame - series
```


```python
series2 = Series(range(3), index=['b', 'e', 'f'])
frame + series2
```


```python
series3 = frame['d']
frame
```


```python
series3
```


```python
frame.sub(series3, axis=0)
```

### 5.2.5 Function application and mapping


```python
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
```


```python
frame
```


```python
np.abs(frame)
```


```python
f = lambda x: x.max() - x.min()
```


```python
frame.apply(f)
```


```python
frame.apply(f, axis=1)
```


```python
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)
```


```python
format = lambda x: '%.2f' % x
frame.applymap(format)
```


```python
frame['e'].map(format)
```

### 5.2.6 Sorting and ranking


```python
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
```


```python
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
frame.sort_index()
```


```python
frame.sort_index(axis=1)
```


```python
frame.sort_index(axis=1, ascending=False)
```


```python
obj = Series([4, 7, -3, 2])
obj.order()
```


```python
obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj.order()
```


```python
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
```


```python
frame.sort_index(by='b')
```


```python
frame.sort_index(by=['a', 'b'])
```


```python
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()
```


```python
obj.rank(method='first')
```


```python
obj.rank(ascending=False, method='max')
```


```python
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame
```


```python
frame.rank(axis=1)
```

### 5.2.7 Axis indexes with duplicate values


```python
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
```


```python
obj.index.is_unique
```


```python
obj['a']
```


```python
obj['c']
```


```python
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
```


```python
df.ix['b']
```

## 5.3 Summarizing and Computing Descriptive Statistics


```python
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
df
```


```python
df.sum()
```


```python
df.sum(axis=1)
```


```python
df.mean(axis=1, skipna=False)
```


```python
df.idxmax()
```


```python
df.cumsum()
```


```python
df.describe()
```


```python
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()
```

### 5.3.1 Correlation and Covariance


```python
import pandas.io.data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker)

price = DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.iteritems()})
```


```python
returns = price.pct_change()
returns.tail()
```


```python
returns.MSFT.corr(returns.IBM)
```


```python
returns.MSFT.cov(returns.IBM)
```


```python
returns.corr()
```


```python
returns.cov()
```


```python
returns.corrwith(returns.IBM)
```


```python
returns.corrwith(volume)
```

### 5.3.2 Unique Values, Value Counts, and Membership


```python
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
```


```python
uniques = obj.unique()
uniques
```


```python
obj.value_counts()
```


```python
pd.value_counts(obj.values, sort=False)
```


```python
mask = obj.isin(['b', 'c'])
mask
```


```python
obj[mask]
```


```python
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
data
```


```python
result = data.apply(pd.value_counts).fillna(0)
result
```

## 5.4 Handling Missing Data


```python
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data
```


```python
string_data.isnull()
```


```python
string_data[0] = None
string_data.isnull()
```

### 5.4.1 Filtering Out Missing Data


```python
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data.dropna()
```


```python
data[data.notnull()]
```


```python
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
data
```


```python
cleaned
```


```python
data.dropna(how='all')
```


```python
data[4] = NA
data
```


```python
data.dropna(axis=1, how='all')
```


```python
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA; df.ix[:2, 2] = NA
df
```


```python
df.dropna(thresh=3)
```

### 5.4.2 Filling in Missing Data


```python
df.fillna(0) 
```


```python
df.fillna({1: 0.5, 3: -1})
```


```python
# always returns a reference to the filled object
_ = df.fillna(0, inplace=True)
df
```


```python
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
df
```


```python
df.fillna(method='ffill')
```


```python
df.fillna(method='ffill', limit=2)
```


```python
data = Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())
```

## 5.5 Hierarchical Indexing


```python
data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data
```


```python
data.index
```


```python
data['b']
```


```python
data['b':'c']
```


```python
data.ix[['b', 'd']]
```


```python
data[:, 2]
```


```python
data.unstack()
```


```python
data.unstack().stack()
```


```python
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])
frame
```


```python
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
```


```python
frame['Ohio']
```
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                       names=['state', 'color'])
### 5.5.1 Reordering and Sorting Levels


```python
frame.swaplevel('key1', 'key2')
```


```python
frame.sortlevel(1)
```


```python
frame.swaplevel(0, 1).sortlevel(0)
```

### 5.5.2 Summary Statistics by Level


```python
frame.sum(level='key2')
```


```python
frame.sum(level='color', axis=1)
```

### 5.5.3 Using a DataFrame’s Columns


```python
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
frame
```


```python
frame2 = frame.set_index(['c', 'd'])
frame2
```


```python
frame.set_index(['c', 'd'], drop=False)
```


```python
frame2.reset_index()
```

## 5.6 Other pandas Topics

### 5.6.1 Integer Indexing


```python
ser = Series(np.arange(3.))
ser.iloc[-1]
```


```python
ser
```


```python
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]
```


```python
ser.ix[:1]
```


```python
ser3 = Series(range(3), index=[-5, 1, 3])
ser3.iloc[2]
```


```python
frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
frame.iloc[0]
```

### 5.6.2 Panel Data 


```python
import pandas.io.data as web

pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk))
                       for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))
```


```python
pdata
```


```python
pdata = pdata.swapaxes('items', 'minor')
pdata['Adj Close']
```


```python
pdata.ix[:, '6/1/2012', :]
```


```python
pdata.ix['Adj Close', '5/22/2012':, :]
```


```python
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
stacked
```


```python
stacked.to_panel()
```
