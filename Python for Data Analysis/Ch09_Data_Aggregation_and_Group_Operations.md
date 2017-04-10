
# Chapter 9. Data Aggregation and Group Operations


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)
```


```python
pd.options.display.notebook_repr_html = False
```


```python
%matplotlib inline
```

## 9.1 GroupBy Mechanics


```python
df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5),
                'data2' : np.random.randn(5)})
df
```


```python
grouped = df['data1'].groupby(df['key1'])
grouped
```


```python
grouped.mean()
```


```python
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
means
```


```python
means.unstack()
```


```python
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()
```


```python
df.groupby('key1').mean()
```


```python
df.groupby(['key1', 'key2']).mean()
```


```python
df.groupby(['key1', 'key2']).size()
```

### 9.1.1 Iterating Over Groups


```python
for name, group in df.groupby('key1'):
    print(name)
    print(group)
```


```python
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)
```


```python
pieces = dict(list(df.groupby('key1')))
pieces['b']
```


```python
df.dtypes
```


```python
grouped = df.groupby(df.dtypes, axis=1)
dict(list(grouped))
```

### 9.1.2 Selecting a Column or Subset of Columns
df.groupby('key1')['data1']
df.groupby('key1')[['data2']]df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])

```python
df.groupby(['key1', 'key2'])[['data2']].mean()
```


```python
s_grouped = df.groupby(['key1', 'key2'])['data2']
s_grouped
```


```python
s_grouped.mean()
```

### 9.1.3 Grouping with Dicts and Series


```python
people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.ix[2:3, ['b', 'c']] = np.nan # Add a few NA values
people
```


```python
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}
```


```python
by_column = people.groupby(mapping, axis=1)
by_column.sum()
```


```python
map_series = Series(mapping)
map_series
```


```python
people.groupby(map_series, axis=1).count()
```

### 9.1.4 Grouping with Functions


```python
people.groupby(len).sum()
```


```python
key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()
```

### 9.1.5 Grouping by Index Levels


```python
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                    [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
hier_df
```


```python
hier_df.groupby(level='cty', axis=1).count()
```

## 9.2 Data Aggregation


```python
df
```


```python
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
```


```python
def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak)
```


```python
grouped.describe()
```


```python
tips = pd.read_csv('ch08/tips.csv')
# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips[:6]
```

### 9.2.1 Column-wise and Multiple Function Application


```python
grouped = tips.groupby(['sex', 'smoker'])
```


```python
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
```


```python
grouped_pct.agg(['mean', 'std', peak_to_peak])
```


```python
grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])
```


```python
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
result
```


```python
result['tip_pct']
```


```python
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples)
```


```python
grouped.agg({'tip' : np.max, 'size' : 'sum'})
```


```python
grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],
             'size' : 'sum'})
```

### 9.2.2 Returning Aggregated Data in "unindexed" Form


```python
tips.groupby(['sex', 'smoker'], as_index=False).mean()
```

## 9.3 Group-wise Operations and Transformations


```python
df
```


```python
k1_means = df.groupby('key1').mean().add_prefix('mean_')
k1_means
```


```python
pd.merge(df, k1_means, left_on='key1', right_index=True)
```


```python
key = ['one', 'two', 'one', 'two', 'one']
people.groupby(key).mean()
```


```python
people.groupby(key).transform(np.mean)
```


```python
def demean(arr):
    return arr - arr.mean()
demeaned = people.groupby(key).transform(demean)
demeaned
```


```python
demeaned.groupby(key).mean()
```

### 9.3.1 Apply: General split-apply-combine


```python
def top(df, n=5, column='tip_pct'):
    return df.sort_index(by=column)[-n:]
top(tips, n=6)
```


```python
tips.groupby('smoker').apply(top)
```


```python
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
```


```python
result = tips.groupby('smoker')['tip_pct'].describe()
result
```


```python
result.unstack('smoker')
```
f = lambda x: x.describe()
grouped.apply(f)
* __Suppressing the group keys__


```python
tips.groupby('smoker', group_keys=False).apply(top)
```

### 9.3.2 Quantile and Bucket Analysis


```python
frame = DataFrame({'data1': np.random.randn(1000),
                   'data2': np.random.randn(1000)})
factor = pd.cut(frame.data1, 4)
factor[:10]
```


```python
def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}

grouped = frame.data2.groupby(factor)
grouped.apply(get_stats).unstack()

#ADAPT the output is not sorted in the book while this is the case now (swap first two lines)
```


```python
# Return quantile numbers
grouping = pd.qcut(frame.data1, 10, labels=False)

grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()
```

### 9.3.3 Example: Filling Missing Values with Group-specific Values


```python
s = Series(np.random.randn(6))
s[::2] = np.nan
s
```


```python
s.fillna(s.mean())
```


```python
states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
data
```


```python
data.groupby(group_key).mean()
```


```python
fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)
```


```python
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])

data.groupby(group_key).apply(fill_func)
```

### 9.3.4 Example: Random Sampling and Permutation


```python
# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (range(1, 11) + [10] * 3) * 4
base_names = ['A'] + range(2, 11) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)

deck = Series(card_val, index=cards)
```


```python
deck[:13]
```


```python
def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])
draw(deck)
```


```python
get_suit = lambda card: card[-1] # last letter is suit
deck.groupby(get_suit).apply(draw, n=2)
```


```python
# alternatively
deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
```

### 9.3.5 Example: Group Weighted Average and Correlation


```python
df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                'data': np.random.randn(8),
                'weights': np.random.rand(8)})
df
```


```python
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)
```


```python
close_px = pd.read_csv('ch09/stock_px.csv', parse_dates=True, index_col=0)
close_px.info()
```


```python
close_px[-4:]
```


```python
rets = close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x['SPX'])
by_year = rets.groupby(lambda x: x.year)
by_year.apply(spx_corr)
```


```python
# Annual correlation of Apple with Microsoft
by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))
```

### 9.3.6 Example: Group-wise Linear Regression


```python
import statsmodels.api as sm
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params
```


```python
by_year.apply(regress, 'AAPL', ['SPX'])
```

## 9.4 Pivot Tables and Cross-Tabulation


```python
tips.pivot_table(index=['sex', 'smoker'])
```


```python
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker')
```


```python
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker', margins=True)
```


```python
tips.pivot_table('tip_pct', index=['sex', 'smoker'], columns='day',
                 aggfunc=len, margins=True)
```


```python
tips.pivot_table('size', index=['time', 'sex', 'smoker'],
                 columns='day', aggfunc='sum', fill_value=0)
```

### 9.4.1 Cross-Tabulations: Crosstab


```python
from StringIO import StringIO
data = """\
Sample    Gender    Handedness
1    Female    Right-handed
2    Male    Left-handed
3    Female    Right-handed
4    Male    Right-handed
5    Male    Left-handed
6    Male    Right-handed
7    Female    Right-handed
8    Female    Left-handed
9    Male    Right-handed
10    Female    Right-handed"""
data = pd.read_table(StringIO(data), sep='\s+')
```


```python
data
```


```python
pd.crosstab(data.Gender, data.Handedness, margins=True)
```


```python
pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)
```

## 9.5 Example: 2012 Federal Election Commission Database


```python
fec = pd.read_csv('ch09/P00000001-ALL.csv')
```


```python
fec.info()
```


```python
fec.ix[123456]
```


```python
unique_cands = fec.cand_nm.unique()
unique_cands
```


```python
unique_cands[2]
```


```python
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}
```


```python
fec.cand_nm[123456:123461]
```


```python
fec.cand_nm[123456:123461].map(parties)
```


```python
# Add it as a column
fec['party'] = fec.cand_nm.map(parties)
```


```python
fec['party'].value_counts()
```


```python
(fec.contb_receipt_amt > 0).value_counts()
```


```python
fec = fec[fec.contb_receipt_amt > 0]
```


```python
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
```

### 9.5.1 Donation Statistics by Occupation and Employer


```python
fec.contbr_occupation.value_counts()[:10]
```


```python
occ_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED',
   'C.E.O.': 'CEO'
}

# If no mapping provided, return x
f = lambda x: occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(f)
```


```python
emp_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'SELF' : 'SELF-EMPLOYED',
   'SELF EMPLOYED' : 'SELF-EMPLOYED',
}

# If no mapping provided, return x
f = lambda x: emp_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)
```


```python
by_occupation = fec.pivot_table('contb_receipt_amt',
                                index='contbr_occupation',
                                columns='party', aggfunc='sum')
```


```python
over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
over_2mm
```


```python
over_2mm.plot(kind='barh')
```


```python
def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()

    # Order totals by key in descending order
    return totals.order(ascending=False)[-n:]
```


```python
grouped = fec_mrbo.groupby('cand_nm')
grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
```


```python
grouped.apply(get_top_amounts, 'contbr_employer', n=10)
```

### 9.5.2 Bucketing Donation Amounts


```python
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
labels
```


```python
grouped = fec_mrbo.groupby(['cand_nm', labels])
grouped.size().unstack(0)
```


```python
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
bucket_sums
```


```python
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
normed_sums
```


```python
normed_sums[:-2].plot(kind='barh', stacked=True)
```

### 9.5.3 Donation Statistics by State 


```python
grouped = fec_mrbo.groupby(['cand_nm', 'contbr_st'])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1) > 100000]
totals[:10]
```


```python
percent = totals.div(totals.sum(1), axis=0)
percent[:10]
```
