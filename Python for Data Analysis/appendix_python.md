
# Appendix. Python Language Essentials


```python
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import *
import pandas
np.set_printoptions(precision=4)

```

## A.1 The Python Interpreter

```
$ python
Python 2.7.2 (default, Oct  4 2011, 20:06:09)
[GCC 4.6.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 5
>>> print a
5
```


```python
%%writefile hello_world.py
print 'Hello world'
```

```
$ ipython
Python 2.7.2 |EPD 7.1-2 (64-bit)| (default, Jul  3 2011, 15:17:51)
Type "copyright", "credits" or "license" for more information.

IPython 0.12 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: %run hello_world.py
Hello world

In [2]:
```

## A.2 The Basics

### A.2.1 Language Semantics

* __for loops__

* __Indentation, not braces__
for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)for x in array {
        if x < pivot {
            less.append(x)
        } else {
            greater.append(x)
        }
    }for x in array
    {
      if x < pivot
      {
        less.append(x)
      }
      else
      {
        greater.append(x)
      }
    }a = 5; b = 6; c = 7
* __Everything is an object__

* __Comments__


```python
results = []
for line in file_handle:
    # keep the empty lines for now
    # if len(line) == 0:
    #   continue
    results.append(line.replace('foo', 'bar'))
```

* __Function and object method calls__


```python
result = f(x, y, z)
g()
```


```python
obj.some_method(x, y, z)
```


```python
result = f(a, b, c, d=5, e='foo')
```

* __Variables and pass-by-reference__


```python
a = [1, 2, 3]
```


```python
b = a
```


```python
a.append(4)
b
```


```python
def append_element(some_list, element):
    some_list.append(element)
```


```python
data = [1, 2, 3]

append_element(data, 4)

In [4]: data
Out[4]: [1, 2, 3, 4]
```

* __Dynamic references, strong types__


```python
a = 5
type(a)
a = 'foo'
type(a)
```


```python
'5' + 5
```


```python
a = 4.5
b = 2
# String formatting, to be visited later
print 'a is %s, b is %s' % (type(a), type(b))
a / b
```


```python
a = 5
isinstance(a, int)
```


```python
a = 5; b = 4.5
isinstance(a, (int, float))
isinstance(b, (int, float))
```

* __Attributes and methods__
In [1]: a = 'foo'

In [2]: a.<Tab>
a.capitalize  a.format      a.isupper     a.rindex      a.strip
a.center      a.index       a.join        a.rjust       a.swapcase
a.count       a.isalnum     a.ljust       a.rpartition  a.title
a.decode      a.isalpha     a.lower       a.rsplit      a.translate
a.encode      a.isdigit     a.lstrip      a.rstrip      a.upper
a.endswith    a.islower     a.partition   a.split       a.zfill
a.expandtabs  a.isspace     a.replace     a.splitlines
a.find        a.istitle     a.rfind       a.startswith>>> getattr(a, 'split')
<function split>

* __"Duck" typing__


```python
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
```


```python
isiterable('a string')
isiterable([1, 2, 3])
isiterable(5)
```
if not isinstance(x, list) and isiterable(x):
    x = list(x)
* __Imports__


```python
# some_module.py
PI = 3.14159

def f(x):
    return x + 2

def g(a, b):
    return a + b
```


```python
import some_module
result = some_module.f(5)
pi = some_module.PI
```


```python
from some_module import f, g, PI
result = g(5, PI)
```


```python
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)
```

* __Binary operators and comparisons__


```python
5 - 7
12 + 21.5
5 <= 2
```


```python
a = [1, 2, 3]
b = a
# Note, the list function always creates a new list
c = list(a)
a is b
a is not c
```


```python
a == c
```


```python
a = None
a is None
```

* __Strictness versus laziness__


```python
a = b = c = 5
d = a + b * c
```

* __Mutable and immutable objects__


```python
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list
```


```python
a_tuple = (3, 5, (4, 5))
a_tuple[1] = 'four'
```

### A.2.2 Scalar Types

* __Numeric types__


```python
ival = 17239871
ival ** 6
```


```python
fval = 7.243
fval2 = 6.78e-5
```


```python
3 / 2
```


```python
from __future__ import division
```


```python
3 / float(2)
```


```python
3 // 2
```


```python
cval = 1 + 2j
cval * (1 - 2j)
```

* __Strings__


```python
a = 'one way of writing a string'
b = "another way"
```


```python
c = """
This is a longer string that
spans multiple lines
"""
```


```python
a = 'this is a string'
a[10] = 'f'
b = a.replace('string', 'longer string')
b
```


```python
a = 5.6
s = str(a)
s
```


```python
s = 'python'
list(s)
s[:3]
```


```python
s = '12\\34'
print s
```


```python
s = r'this\has\no\special\characters'
s
```


```python
a = 'this is the first half '
b = 'and this is the second half'
a + b
```


```python
template = '%.2f %s are worth $%d'
```


```python
template % (4.5560, 'Argentine Pesos', 1)
```

* __Booleans__


```python
True and True
False or True
```


```python
a = [1, 2, 3]
if a:
    print 'I found something!'

b = []
if not b:
    print 'Empty!'
```


```python
bool([]), bool([1, 2, 3])
bool('Hello world!'), bool('')
bool(0), bool(1)
```

* __Type casting__


```python
s = '3.14159'
fval = float(s)
type(fval)
int(fval)
bool(fval)
bool(0)
```

* __None__


```python
a = None
a is None
b = 5
b is not None
```


```python
def add_and_maybe_multiply(a, b, c=None):
    result = a + b

    if c is not None:
        result = result * c

    return result
```

* __Dates and times__


```python
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day
dt.minute
```


```python
dt.date()
dt.time()
```


```python
dt.strftime('%m/%d/%Y %H:%M')

```


```python
datetime.strptime('20091031', '%Y%m%d')

```


```python
dt.replace(minute=0, second=0)
```


```python
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
delta
type(delta)
```


```python
dt
dt + delta
```

### A.2.3 Control Flow

* __if, elif, and else__


```python
if x < 0:
    print 'It's negative'
```


```python
if x < 0:
    print 'It's negative'
elif x == 0:
    print 'Equal to zero'
elif 0 < x < 5:
    print 'Positive but smaller than 5'
else:
    print 'Positive and larger than 5'
```


```python
a = 5; b = 7
c = 8; d = 4
if a < b or c > d:
    print 'Made it'
```


```python
for value in collection:
    # do something with value
```


```python
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
```


```python
sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value
```


```python
for a, b, c in iterator:
    # do something
```

* __while loops__


```python
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
```

* __pass__


```python
if x < 0:
    print 'negative!'
elif x == 0:
    # TODO: put something smart here
    pass
else:
    print 'positive!'
```


```python
def f(x, y, z):
    # TODO: implement this function!
    pass

```

* __Exception handling__


```python
float('1.2345')
float('something')
```


```python
def attempt_float(x):
    try:
        return float(x)
    except:
        return x
```


```python
attempt_float('1.2345')
attempt_float('something')
```


```python
float((1, 2))
```


```python
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x
```


```python
attempt_float((1, 2))
```


```python
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
```


```python
f = open(path, 'w')

try:
    write_to_file(f)
finally:
    f.close()
```


```python
f = open(path, 'w')

try:
    write_to_file(f)
except:
    print 'Failed'
else:
    print 'Succeeded'
finally:
    f.close()
```

* __range and xrange__


```python
range(10)
```


```python
range(0, 20, 2)
```


```python
seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
```


```python
sum = 0
for i in xrange(10000):
    # % is the modulo operator
    if i % 3 == 0 or i % 5 == 0:
        sum += i

```

* __Ternary Expressions__


```python
x = 5
value = 'Non-negative' if x >= 0 else 'Negative'
```

## A.3 Data Structures and Sequences

### A.6.1 Tuple


```python
tup = 4, 5, 6
tup
```


```python
nested_tup = (4, 5, 6), (7, 8)
nested_tup
```


```python
tuple([4, 0, 2])
tup = tuple('string')
tup
```


```python
tup[0]
```


```python
tup = tuple(['foo', [1, 2], True])
tup[2] = False

# however
tup[1].append(3)
tup
```


```python
(4, None, 'foo') + (6, 0) + ('bar',)
```


```python
('foo', 'bar') * 4
```

* __Unpacking tuples__


```python
tup = (4, 5, 6)
a, b, c = tup
b
```


```python
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d
```
tmp = a
a = b
b = tmpb, a = a, b
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    pass
* __Tuple methods__


```python
a = (1, 2, 2, 2, 3, 4, 2)
a.count(2)
```

### A.6.2 List


```python
a_list = [2, 3, 7, None]

tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list
b_list[1] = 'peekaboo'
b_list
```

* __Adding and removing elements__


```python
b_list.append('dwarf')
b_list
```


```python
b_list.insert(1, 'red')
b_list
```


```python
b_list.pop(2)
b_list
```


```python
b_list.append('foo')
b_list.remove('foo')
b_list
```


```python
'dwarf' in b_list
```

* __Concatenating and combining lists__


```python
[4, None, 'foo'] + [7, 8, (2, 3)]

```


```python
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
x
```


```python
everything = []
for chunk in list_of_lists:
    everything.extend(chunk)

```


```python
everything = []
for chunk in list_of_lists:
    everything = everything + chunk
```

* __Sorting__


```python
a = [7, 2, 5, 1, 3]
a.sort()
a
```


```python
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
b
```

* __Binary search and maintaining a sorted list__


```python
import bisect
c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)
bisect.bisect(c, 5)
bisect.insort(c, 6)
c
```

* __Slicing__


```python
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]
```


```python
seq[3:4] = [6, 3]
seq
```


```python
seq[:5]
seq[3:]
```


```python
seq[-4:]
seq[-6:-2]
```


```python
seq[::2]
```


```python
seq[::-1]
```

### A.6.3 Built-in Sequence Functions
* __enumerate__


```python

i = 0
for value in collection:
   # do something with value
   i += 1
```


```python
for i, value in enumerate(collection):
   # do something with value
```


```python
some_list = ['foo', 'bar', 'baz']
mapping = dict((v, i) for i, v in enumerate(some_list))
mapping
```

* __sorted__


```python
sorted([7, 1, 2, 6, 0, 3, 2])
sorted('horse race')
```


```python
sorted(set('this is just some string'))
```

* __zip__


```python
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zip(seq1, seq2)
```


```python
seq3 = [False, True]
zip(seq1, seq2, seq3)
```


```python
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('%d: %s, %s' % (i, a, b))
```


```python
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
            ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
first_names
last_names
```


```python
zip(seq[0], seq[1], ..., seq[len(seq) - 1])
```

* __reversed__


```python
list(reversed(range(10)))
```

### A.6.4 Dict


```python
empty_dict = {}
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1
```


```python
d1[7] = 'an integer'
d1
d1['b']
```


```python
'b' in d1
```


```python
d1[5] = 'some value'
d1['dummy'] = 'another value'
del d1[5]
ret = d1.pop('dummy')
ret
```


```python
d1.keys()
d1.values()
```


```python
d1.update({'b' : 'foo', 'c' : 12})
d1
```

* __Creating dicts from sequences__


```python
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
```


```python
mapping = dict(zip(range(5), reversed(range(5))))
mapping
```

* __Default values__


```python
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value
```


```python
value = some_dict.get(key, default_value)
```


```python
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

by_letter
```
by_letter.setdefault(letter, []).append(word)

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

```


```python
counts = defaultdict(lambda: 4)
```

* __Valid dict key types__


```python
hash('string')
hash((1, 2, (2, 3)))
hash((1, 2, [2, 3])) # fails because lists are mutable
```


```python
d = {}
d[tuple([1, 2, 3])] = 5
d
```

### A.6.5 Set


```python
set([2, 2, 2, 1, 3, 3])
{2, 2, 2, 1, 3, 3}
```


```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a | b  # union (or)
a & b  # intersection (and)
a - b  # difference
a ^ b  # symmetric difference (xor)
```


```python
a_set = {1, 2, 3, 4, 5}
{1, 2, 3}.issubset(a_set)
a_set.issuperset({1, 2, 3})
```


```python
{1, 2, 3} == {3, 2, 1}
```

### A.6.6 List, Set, and Dict Comprehensions


```python
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]
```


```python
unique_lengths = {len(x) for x in strings}
unique_lengths
```


```python
loc_mapping = {val : index for index, val in enumerate(strings)}
loc_mapping
```
loc_mapping = dict((val, idx) for idx, val in enumerate(strings)}
* __Nested list comprehensions__


```python
all_data = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
            ['Susie', 'Casey', 'Jill', 'Ana', 'Eva', 'Jennifer', 'Stephanie']]

```


```python
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') > 2]
    names_of_interest.extend(enough_es)
```


```python
result = [name for names in all_data for name in names
          if name.count('e') >= 2]
result

```


```python
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened
```


```python
flattened = []

for tup in some_tuples:
    for x in tup:
        flattened.append(x)
```


```python
In [229]: [[x for x in tup] for tup in some_tuples]
```

## A.4 Functions


```python
def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
```


```python
my_function(5, 6, z=0.7)
my_function(3.14, 7, 3.5)
```

### A.4.1 Namespaces, Scope, and Local Functions


```python
def func():
    a = []
    for i in range(5):
        a.append(i)
```


```python
a = []
def func():
    for i in range(5):
        a.append(i)

```


```python
a = None
def bind_a_variable():
    global a
    a = []
bind_a_variable()
print a
```


```python
def outer_function(x, y, z):
    def inner_function(a, b, c):
        pass
    pass
```

### A.4.2 Returning Multiple Values


```python
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()
```


```python
return_value = f()
```


```python
def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}
```

### A.4.3 Functions Are Objects


```python

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']
```


```python
import re  # Regular expression module

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value) # remove punctuation
        value = value.title()
        result.append(value)
    return result
```


```python
In [15]: clean_strings(states)
Out[15]:
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South Carolina',
 'West Virginia']
```


```python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```


```python
In [22]: clean_strings(states, clean_ops)
Out[22]:
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South Carolina',
 'West Virginia']
```


```python
In [23]: map(remove_punctuation, states)
Out[23]:
['   Alabama ',
 'Georgia',
 'Georgia',
 'georgia',
 'FlOrIda',
 'south   carolina',
 'West virginia']
```

### A.4.4 Anonymous (lambda) Functions


```python
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2
```


```python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```


```python
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```


```python
strings.sort(key=lambda x: len(set(list(x))))
strings
```

### A.4.5 Closures: Functions that Return Functions


```python
def make_closure(a):
    def closure():
        print('I know the secret: %d' % a)
    return closure

closure = make_closure(5)
```


```python
def make_watcher():
    have_seen = {}

    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False

    return has_been_seen
```


```python
watcher = make_watcher()
vals = [5, 6, 1, 5, 1, 6, 3, 5]
[watcher(x) for x in vals]
```
def make_counter():
    count = [0]
    def counter():
        # increment and return the current count
        count[0] += 1
        return count[0]
    return counter

counter = make_counter()

```python
def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)

    return formatter
```


```python
fmt = format_and_pad('%.4f', 15)
fmt(1.756)
```

### A.4.6 Extended Call Syntax with *args, **kwargs


```python
a, b, c = args
d = kwargs.get('d', d_default_value)
e = kwargs.get('e', e_default_value)
```


```python
def say_hello_then_call_f(f, *args, **kwargs):
    print 'args is', args
    print 'kwargs is', kwargs
    print("Hello! Now I'm going to call %s" % f)
    return f(*args, **kwargs)

def g(x, y, z=1):
    return (x + y) / z
```


```python
In [8]:  say_hello_then_call_f(g, 1, 2, z=5.)
args is (1, 2)
kwargs is {'z': 5.0}
Hello! Now I'm going to call <function g at 0x2dd5cf8>
Out[8]: 0.6
```

### A.4.7 Currying: Partial Argument Application


```python
def add_numbers(x, y):
    return x + y
```


```python
add_five = lambda y: add_numbers(5, y)
```


```python
from functools import partial
add_five = partial(add_numbers, 5)
```


```python
# compute 60-day moving average of time series x
ma60 = lambda x: pandas.rolling_mean(x, 60)

# Take the 60-day moving average of of all time series in data
data.apply(ma60)
```

### A.4.8 Generators


```python
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print key,
```


```python
dict_iterator = iter(some_dict)
dict_iterator
```


```python
list(dict_iterator)
```


```python
def squares(n=10):
    for i in xrange(1, n + 1):
        print 'Generating squares from 1 to %d' % (n ** 2)
        yield i ** 2
```


```python
In [2]: gen = squares()

In [3]: gen
Out[3]: <generator object squares at 0x34c8280>
```


```python
In [4]: for x in gen:
   ...:     print x,
   ...:
Generating squares from 0 to 100
1 4 9 16 25 36 49 64 81 100
```


```python
def make_change(amount, coins=[1, 5, 10, 25], hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        # ensures we don't give too much change, and combinations are unique
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue

        for result in make_change(amount - coin, coins=coins,
                                  hand=hand + [coin]):
            yield result
```


```python
for way in make_change(100, coins=[10, 25, 50]):
    print way
len(list(make_change(100)))
```

* __Generator expresssions__


```python
gen = (x ** 2 for x in xrange(100))
gen
```


```python
def _make_gen():
    for x in xrange(100):
        yield x ** 2
gen = _make_gen()
```


```python
sum(x ** 2 for x in xrange(100))
dict((i, i **2) for i in xrange(5))
```

* __itertools module__


```python
import itertools
first_letter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, first_letter):
    print letter, list(names) # names is a generator
```

## A.5 Files and the operating system


```python
path = 'ch13/segismundo.txt'
f = open(path)
```


```python
for line in f:
    pass
```


```python
lines = [x.rstrip() for x in open(path)]
lines
```


```python
with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)

open('tmp.txt').readlines()
```


```python
os.remove('tmp.txt')
```
