
# Chapter 2. Introductory Examples

## 2.1 1.usa.gov data from bit.ly


```python
%pwd
```


```python
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
```


```python
open(path).readline()
```


```python
import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
```


```python
records[0]
```


```python
records[0]['tz']
```


```python
print(records[0]['tz'])
```

### 2.1.1 Counting Time Zones in Pure Python


```python
time_zones = [rec['tz'] for rec in records]
```


```python
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
```


```python
time_zones[:10]
```


```python
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
```


```python
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts
```


```python
counts = get_counts(time_zones)
```


```python
counts['America/New_York']
```


```python
len(time_zones)
```


```python
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
```


```python
top_counts(counts)
```


```python
from collections import Counter
```


```python
counts = Counter(time_zones)
```


```python
counts.most_common(10)
```

### 2.1.2 Counting Time Zones with pandas


```python
%matplotlib inline
```


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)
```


```python
import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]
```


```python
from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)
frame
```


```python
frame['tz'][:10]
```


```python
tz_counts = frame['tz'].value_counts()
tz_counts[:10]
```


```python
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
```


```python
plt.figure(figsize=(10, 4))
```


```python
tz_counts[:10].plot(kind='barh', rot=0)
```


```python
frame['a'][1]
```


```python
frame['a'][50]
```


```python
frame['a'][51]
```


```python
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
```


```python
results.value_counts()[:8]
```


```python
cframe = frame[frame.a.notnull()]
```


```python
operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'Windows', 'Not Windows')
operating_system[:5]
```


```python
by_tz_os = cframe.groupby(['tz', operating_system])
```


```python
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
```


```python
# Use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
indexer[:10]
```


```python
count_subset = agg_counts.take(indexer)[-10:]
count_subset
```


```python
plt.figure()
```


```python
count_subset.plot(kind='barh', stacked=True)
```


```python
plt.figure()
```


```python
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
```

## 2.2 MovieLens 1M Data Set


```python
import pandas as pd
import os
encoding = 'latin1'

upath = os.path.expanduser('ch02/movielens/users.dat')
rpath = os.path.expanduser('ch02/movielens/ratings.dat')
mpath = os.path.expanduser('ch02/movielens/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)
```


```python
users[:5]
```


```python
ratings[:5]
```


```python
movies[:5]
```


```python
ratings
```


```python
data = pd.merge(pd.merge(ratings, users), movies)
data
```


```python
data.ix[0]
```


```python
mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')
mean_ratings[:5]
```


```python
ratings_by_title = data.groupby('title').size()
```


```python
ratings_by_title[:5]
```


```python
active_titles = ratings_by_title.index[ratings_by_title >= 250]
```


```python
active_titles[:10]
```


```python
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings
```


```python
mean_ratings = mean_ratings.rename(index={'Seven Samurai (The Magnificent Seven) (Shichinin no samurai) (1954)':
                           'Seven Samurai (Shichinin no samurai) (1954)'})
```


```python
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]
```

### 2.2.1 Measuring rating disagreement


```python
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
```


```python
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:15]
```


```python
# Reverse order of rows, take first 15 rows
sorted_by_diff[::-1][:15]
```


```python
# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# Order Series by value in descending order
rating_std_by_title.order(ascending=False)[:10]
```

## 2.3 US Baby Names 1880-2010


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 5))
np.set_printoptions(precision=4)
%pwd
```

http://www.ssa.gov/oact/babynames/limits.html


```python
!head -n 10 ch02/names/yob1880.txt
```


```python
import pandas as pd
names1880 = pd.read_csv('ch02/names/yob1880.txt', names=['name', 'sex', 'births'])
names1880
```


```python
names1880.groupby('sex').births.sum()
```


```python
# 2010 is the last available year right now
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)
```


```python
total_births = names.pivot_table('births', index='year',
                                 columns='sex', aggfunc=sum)
```


```python
total_births.tail()
```


```python
total_births.plot(title='Total births by sex and year')
```


```python
def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)

    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)
```


```python
names
```


```python
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)
```


```python
def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
```


```python
pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
```


```python
top1000.index = np.arange(len(top1000))
```


```python
top1000
```

### 2.3.1 Analyzing Naming Trends


```python
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
```


```python
total_births = top1000.pivot_table('births', index='year', columns='name',
                                   aggfunc=sum)
total_births
```


```python
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False,
            title="Number of births per year")
```

* __Measuring the increase in naming diversity__


```python
plt.figure()
```


```python
table = top1000.pivot_table('prop', index='year',
                            columns='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex',
           yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
```


```python
df = boys[boys.year == 2010]
df
```


```python
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
prop_cumsum[:10]
```


```python
prop_cumsum.values.searchsorted(0.5)
```


```python
df = boys[boys.year == 1900]
in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()
in1900.values.searchsorted(0.5) + 1
```


```python
def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
```


```python
def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.head()
```


```python
diversity.plot(title="Number of popular names in top 50%")
```

* __The "Last letter" Revolution__


```python
# extract last letter from name column
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index=last_letters,
                          columns=['sex', 'year'], aggfunc=sum)
```


```python
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
subtable.head()

```


```python
subtable.sum()
```


```python
letter_prop = subtable / subtable.sum().astype(float)
```


```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',
                      legend=False)
```


```python
plt.subplots_adjust(hspace=0.25)
```


```python
letter_prop = table / table.sum().astype(float)

dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
dny_ts.head()
```


```python
plt.close('all')
```


```python
dny_ts.plot()
```

* __Boy names that became girl names (and vice versa__


```python
all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
lesley_like
```


```python
filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()
```


```python
table = filtered.pivot_table('births', index='year',
                             columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
table.tail()
```


```python
plt.close('all')
```


```python
table.plot(style={'M': 'k-', 'F': 'k--'})
```

## 2.4 Conclusions and The Path Ahead 

The examples in this chapter are rather simple, but they’re here to give you a bit of a flavor of what sorts of things you can expect in the upcoming chapters.  
The focus of this book is on tools as opposed to presenting more sophisticated analytical methods.  
Mastering the techniques in this book will enable you to implement your own analyses (assuming you know what you want to do!) in short order.  

