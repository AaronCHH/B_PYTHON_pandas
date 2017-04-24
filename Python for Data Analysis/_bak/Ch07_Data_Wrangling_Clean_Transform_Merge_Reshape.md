
# Chapter 7. Data Wrangling: Clean, Transform, Merge, Reshape


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas
import pandas as pd
np.set_printoptions(precision=4, threshold=500)
pd.options.display.max_rows = 100
```


```python
%matplotlib inline
```

## 7.1 Combining and Merging Data Sets

### 7.1.1 Database-style DataFrame Merges


```python
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
df1
```


```python
df2
```


```python
pd.merge(df1, df2)
```


```python
pd.merge(df1, df2, on='key')
```


```python
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')
```


```python
pd.merge(df1, df2, how='outer')
```


```python
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
```


```python
df1
```


```python
df2
```


```python
pd.merge(df1, df2, on='key', how='left')
```


```python
pd.merge(df1, df2, how='inner')
```


```python
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')
```


```python
pd.merge(left, right, on='key1')
```


```python
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
```

### 7.1.2 Merging on Index


```python
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                  'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
```


```python
left1
```


```python
right1
```


```python
pd.merge(left1, right1, left_on='key', right_index=True)
```


```python
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
```


```python
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])
lefth
```


```python
righth
```


```python
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
```


```python
pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True, how='outer')
```


```python
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                 columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
```


```python
left2
```


```python
right2
```


```python
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
```


```python
left2.join(right2, how='outer')
```


```python
left1.join(right1, on='key')
```


```python
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
```


```python
left2.join([right2, another])
```


```python
left2.join([right2, another], how='outer')
```

### 7.1.3 Concatenating Along an Axis


```python
arr = np.arange(12).reshape((3, 4))
```


```python
arr
```


```python
np.concatenate([arr, arr], axis=1)
```


```python
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
```


```python
pd.concat([s1, s2, s3])
```


```python
pd.concat([s1, s2, s3], axis=1)
```


```python
s4 = pd.concat([s1 * 5, s3])
```


```python
pd.concat([s1, s4], axis=1)
```


```python
pd.concat([s1, s4], axis=1, join='inner')
```


```python
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
```


```python
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
```


```python
result
```


```python
# Much more on the unstack function later
result.unstack()
```


```python
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])
```


```python
df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
```


```python
pd.concat({'level1': df1, 'level2': df2}, axis=1)
```


```python
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])
```


```python
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
```


```python
df1
```


```python
df2
```


```python
pd.concat([df1, df2], ignore_index=True)
```

### 7.1.4 Combining Data with Overlap


```python
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
```


```python
a
```


```python
b
```


```python
np.where(pd.isnull(a), b, a)
```


```python
b[:-2].combine_first(a[2:])
```


```python
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
df1.combine_first(df2)
```

## 7.2 Reshaping and Pivoting

### 7.2.1 Reshaping with Hierarchical Indexing


```python
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
data
```


```python
result = data.stack()
result
```


```python
result.unstack()
```


```python
result.unstack(0)
```


```python
result.unstack('state')
```


```python
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2.unstack()
```


```python
data2.unstack().stack()
```


```python
data2.unstack().stack(dropna=False)
```


```python
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))
df
```


```python
df.unstack('state')
```


```python
df.unstack('state').stack('side')
```

### 7.2.2 Pivoting "long" to "wide" Format


```python
data = pd.read_csv('ch07/macrodata.csv')
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
data = DataFrame(data.to_records(),
                 columns=pd.Index(['realgdp', 'infl', 'unemp'], name='item'),
                 index=periods.to_timestamp('D', 'end'))

ldata = data.stack().reset_index().rename(columns={0: 'value'})
wdata = ldata.pivot('date', 'item', 'value')
```


```python
ldata[:10]
```


```python
pivoted = ldata.pivot('date', 'item', 'value')
pivoted.head()
```


```python
ldata['value2'] = np.random.randn(len(ldata))
ldata[:10]
```


```python
pivoted = ldata.pivot('date', 'item')
pivoted[:5]
```


```python
pivoted['value'][:5]
```


```python
unstacked = ldata.set_index(['date', 'item']).unstack('item')
unstacked[:7]
```

## 7.3 Data Transformation

### 7.3.1 Removing Duplicates


```python
data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
data
```


```python
data.duplicated()
```


```python
data.drop_duplicates()
```


```python
data['v1'] = range(7)
data.drop_duplicates(['k1'])
```


```python
data.drop_duplicates(['k1', 'k2'], take_last=True)
```

### 7.3.2 Transforming Data Using a Function or Mapping


```python
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data
```


```python
meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}
```


```python
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data
```


```python
data['food'].map(lambda x: meat_to_animal[x.lower()])
```

### 7.3.3 Replacing Values


```python
data = Series([1., -999., 2., -999., -1000., 3.])
data
```


```python
data.replace(-999, np.nan)
```


```python
data.replace([-999, -1000], np.nan)
```


```python
data.replace([-999, -1000], [np.nan, 0])
```


```python
data.replace({-999: np.nan, -1000: 0})
```

### 7.3.4 Renaming Axis Indexes


```python
data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
```


```python
data.index.map(str.upper)
```


```python
data.index = data.index.map(str.upper)
data
```


```python
data.rename(index=str.title, columns=str.upper)
```


```python
data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})
```


```python
# Always returns a reference to a DataFrame
_ = data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
data
```

### 7.3.5 Discretization and Binning


```python
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
```


```python
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats
```


```python
cats.labels
```


```python
cats.levels
```


```python
pd.value_counts(cats)
```


```python
pd.cut(ages, [18, 26, 36, 61, 100], right=False)
```


```python
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)
```


```python
data = np.random.rand(20)
pd.cut(data, 4, precision=2)
```


```python
data = np.random.randn(1000) # Normally distributed
cats = pd.qcut(data, 4) # Cut into quartiles
cats
```


```python
pd.value_counts(cats)
```


```python
pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
```

### 7.3.6 Detecting and Filtering Outliers


```python
np.random.seed(12345)
data = DataFrame(np.random.randn(1000, 4))
data.describe()
```


```python
col = data[3]
col[np.abs(col) > 3]
```


```python
data[(np.abs(data) > 3).any(1)]
```


```python
data[np.abs(data) > 3] = np.sign(data) * 3
data.describe()
```

### 7.3.7 Permutation and Random Sampling


```python
df = DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
sampler
```


```python
df
```


```python
df.take(sampler)
```


```python
df.take(np.random.permutation(len(df))[:3])
```


```python
bag = np.array([5, 7, -1, 6, 4])
sampler = np.random.randint(0, len(bag), size=10)
```


```python
sampler
```


```python
draws = bag.take(sampler)
draws
```

### 7.3.8 Computing Indicator/Dummy Variables


```python
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
pd.get_dummies(df['key'])
```


```python
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy
```


```python
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ch02/movielens/movies.dat', sep='::', header=None,
                        names=mnames)
movies[:10]
```


```python
genre_iter = (set(x.split('|')) for x in movies.genres)
genres = sorted(set.union(*genre_iter))
```


```python
dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
```


```python
for i, gen in enumerate(movies.genres):
    dummies.ix[i, gen.split('|')] = 1
```


```python
movies_windic = movies.join(dummies.add_prefix('Genre_'))
movies_windic.ix[0]
```


```python
np.random.seed(12345)
```


```python
values = np.random.rand(10)
values
```


```python
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.get_dummies(pd.cut(values, bins))
```

## 7.4 String Manipulation

### 7.4.1 String Object Methods


```python
val = 'a,b,  guido'
val.split(',')
```


```python
pieces = [x.strip() for x in val.split(',')]
pieces
```


```python
first, second, third = pieces
first + '::' + second + '::' + third
```


```python
'::'.join(pieces)
```


```python
'guido' in val
```


```python
val.index(',')
```


```python
val.find(':')
```


```python
val.index(':')
```


```python
val.count(',')
```


```python
val.replace(',', '::')
```


```python
val.replace(',', '')
```

### 7.4.2 Regular expressions


```python
import re
text = "foo    bar\t baz  \tqux"
re.split('\s+', text)
```


```python
regex = re.compile('\s+')
regex.split(text)
```


```python
regex.findall(text)
```


```python
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
```


```python
regex.findall(text)
```


```python
m = regex.search(text)
m
```


```python
text[m.start():m.end()]
```


```python
print(regex.match(text))
```


```python
print(regex.sub('REDACTED', text))
```


```python
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
```


```python
m = regex.match('wesm@bright.net')
m.groups()
```


```python
regex.findall(text)
```


```python
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))
```


```python
regex = re.compile(r"""
    (?P<username>[A-Z0-9._%+-]+)
    @
    (?P<domain>[A-Z0-9.-]+)
    \.
    (?P<suffix>[A-Z]{2,4})""", flags=re.IGNORECASE|re.VERBOSE)
```


```python
m = regex.match('wesm@bright.net')
m.groupdict()
```

### 7.4.3 Vectorized string functions in pandas


```python
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = Series(data)
```


```python
data
```


```python
data.isnull()
```


```python
data.str.contains('gmail')
```


```python
pattern
```


```python
data.str.findall(pattern, flags=re.IGNORECASE)
```


```python
matches = data.str.match(pattern, flags=re.IGNORECASE)
matches
```


```python
matches.str.get(1)
```


```python
matches.str[0]
```


```python
data.str[:5]
```

## 7.5 Example: USDA Food Database 
{
  "id": 21441,
  "description": "KENTUCKY FRIED CHICKEN, Fried Chicken, EXTRA CRISPY,
Wing, meat and skin with breading",
  "tags": ["KFC"],
  "manufacturer": "Kentucky Fried Chicken",
  "group": "Fast Foods",
  "portions": [
    {
      "amount": 1,
      "unit": "wing, with skin",
      "grams": 68.0
    },

    ...
  ],
  "nutrients": [
    {
      "value": 20.8,
      "units": "g",
      "description": "Protein",
      "group": "Composition"
    },

    ...
  ]
}

```python
import json
db = json.load(open('ch07/foods-2011-10-03.json'))
len(db)
```


```python
db[0].keys()
```


```python
db[0]['nutrients'][0]
```


```python
nutrients = DataFrame(db[0]['nutrients'])
nutrients[:7]
```


```python
info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)
```


```python
info[:5]
```


```python
info
```


```python
pd.value_counts(info.group)[:10]
```


```python
nutrients = []

for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)
```


```python
nutrients
```


```python
nutrients.duplicated().sum()
```


```python
nutrients = nutrients.drop_duplicates()
```


```python
col_mapping = {'description' : 'food',
               'group'       : 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
info
```


```python
col_mapping = {'description' : 'nutrient',
               'group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
nutrients
```


```python
ndata = pd.merge(nutrients, info, on='id', how='outer')
```


```python
ndata
```


```python
ndata.ix[30000]
```


```python
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].order().plot(kind='barh')
```


```python
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])

get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())

max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]

# make the food a little smaller
max_foods.food = max_foods.food.str[:50]
```


```python
max_foods.ix['Amino Acids']['food']
```
