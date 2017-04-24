
# Chapter 6. Data Loading, Storage, and File Formats


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)
```


```python
%pwd
```

## 6.1 Reading and Writing Data in Text Format


```python
!cat ch06/ex1.csv
```


```python
df = pd.read_csv('ch06/ex1.csv')
df
```


```python
pd.read_table('ch06/ex1.csv', sep=',')
```


```python
!cat ch06/ex2.csv
```


```python
pd.read_csv('ch06/ex2.csv', header=None)
pd.read_csv('ch06/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
```


```python
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('ch06/ex2.csv', names=names, index_col='message')
```


```python
!cat ch06/csv_mindex.csv
parsed = pd.read_csv('ch06/csv_mindex.csv', index_col=['key1', 'key2'])
parsed
```


```python
list(open('ch06/ex3.txt'))
```


```python
result = pd.read_table('ch06/ex3.txt', sep='\s+')
result
```


```python
!cat ch06/ex4.csv
pd.read_csv('ch06/ex4.csv', skiprows=[0, 2, 3])
```


```python
!cat ch06/ex5.csv
result = pd.read_csv('ch06/ex5.csv')
result
pd.isnull(result)
```


```python
result = pd.read_csv('ch06/ex5.csv', na_values=['NULL'])
result
```


```python
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ch06/ex5.csv', na_values=sentinels)
```

### 6.1.1 Reading Text Files in Pieces


```python
result = pd.read_csv('ch06/ex6.csv')
result
```


```python
pd.read_csv('ch06/ex6.csv', nrows=5)
```


```python
chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)
chunker
```


```python
chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)

tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.order(ascending=False)
```


```python
tot[:10]
```

### 6.1.2 Writing Data Out to Text Format


```python
!cat ch06/ex7.csv
```


```python
import csv
f = open('ch06/ex7.csv')

reader = csv.reader(f)
```


```python
for line in reader:
    print(line)
```


```python
lines = list(csv.reader(open('ch06/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict
```


```python
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
```


```python
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
```


```python
%cat mydata.csv
```

### 6.1.3 Manually Working with Delimited Formats


```python
data = pd.read_csv('ch06/ex5.csv')
data
```


```python
data.to_csv('ch06/out.csv')
!cat ch06/out.csv
```


```python
data.to_csv(sys.stdout, sep='|')
```


```python
data.to_csv(sys.stdout, na_rep='NULL')
```


```python
data.to_csv(sys.stdout, index=False, header=False)
```


```python
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
```


```python
dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv('ch06/tseries.csv')
!cat ch06/tseries.csv
```


```python
Series.from_csv('ch06/tseries.csv', parse_dates=True)
```

### 6.1.4 JSON Data


```python
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
```


```python
import json
result = json.loads(obj)
result
```


```python
asjson = json.dumps(result)
```


```python
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
siblings
```

### 6.1.5 XML and HTML: Web Scraping

**NB. The Yahoo! Finance API has changed and this example no longer works**


```python
from lxml.html import parse
from urllib2 import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

doc = parsed.getroot()
```


```python
links = doc.findall('.//a')
links[15:20]
```


```python
lnk = links[28]
lnk
lnk.get('href')
lnk.text_content()
```


```python
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
urls[-10:]
```


```python
tables = doc.findall('.//table')
calls = tables[9]
puts = tables[13]
```


```python
rows = calls.findall('.//tr')
```


```python
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]
```


```python
_unpack(rows[0], kind='th')
_unpack(rows[1], kind='td')
```


```python
from pandas.io.parsers import TextParser

def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()
```


```python
call_data = parse_options_data(calls)
put_data = parse_options_data(puts)
call_data[:10]
```

* __Parsing XML with lxml.objectify__


```python
%cd ch06/mta_perf/Performance_XML_Data
```


```python
!head -21 Performance_MNR.xml
```


```python
from lxml import objectify
```


```python
path = 'Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()
```


```python
data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
```


```python
perf = DataFrame(data)
perf
```


```python
root
```


```python
root.get('href')
```


```python
root.text
```

## 6.2 Binary Data Formats


```python
cd ../..
```


```python
frame = pd.read_csv('ch06/ex1.csv')
frame
frame.to_pickle('ch06/frame_pickle')
```


```python
pd.read_pickle('ch06/frame_pickle')
```

### 6.2.1 Using HDF5 Format


```python
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
store
```


```python
store['obj1']
```


```python
store.close()
os.remove('mydata.h5')
```

### 6.2.2 Reading Microsoft Excel Files

## 6.3 Interacting with HTML and Web APIs


```python
import requests
url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(url)
resp
```


```python
data[:5]
```


```python
issue_labels = DataFrame(data)
issue_labels
```

## 6.4 Interacting with Databases


```python
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()
```


```python
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()
```


```python
cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows
```


```python
cursor.description
```


```python
DataFrame(rows, columns=zip(*cursor.description)[0])
```


```python
import pandas.io.sql as sql
sql.read_sql('select * from test', con)
```

### 6.4.1 Storing and Loading Data in MongoDB 


```python
import pymongo
con = pymongo.Connection('localhost', port=27017)
```


```python
tweets = con.db.tweets
```


```python
import requests, json
url = 'http://search.twitter.com/search.json?q=python%20pandas'
data = json.loads(requests.get(url).text)
for tweet in data['results']:
    tweets.save(tweet)
```


```python
cursor = tweets.find({'from_user': 'wesmckinn'})
```


```python
tweet_fields = ['created_at', 'from_user', 'id', 'text']
result = DataFrame(list(cursor), columns=tweet_fields)
```
