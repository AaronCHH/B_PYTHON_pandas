
# Chapter 9: The pandas Library Architecture
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 9: The pandas Library Architecture](#chapter-9-the-pandas-library-architecture)
  * [9.1 Introduction to pandas' file hierarchy](#91-introduction-to-pandas-file-hierarchy)
  * [9.2 Description of pandas' modules and files](#92-description-of-pandas-modules-and-files)
    * [pandas/core](#pandascore)
    * [pandas/io](#pandasio)
    * [pandas/tools](#pandastools)
    * [pandas/sparse](#pandassparse)
    * [pandas/stats](#pandasstats)
    * [pandas/util](#pandasutil)
    * [pandas/rpy](#pandasrpy)
    * [pandas/tests](#pandastests)
    * [pandas/compat](#pandascompat)
    * [pandas/computation](#pandascomputation)
    * [pandas/tseries](#pandastseries)
    * [pandas/sandbox](#pandassandbox)
  * [9.3 Improving performance using Python extensions](#93-improving-performance-using-python-extensions)
  * [9.4 Summary](#94-summary)

<!-- tocstop -->


## 9.1 Introduction to pandas' file hierarchy

> For reference see: http://pandas.pydata.org/developers.html.

## 9.2 Description of pandas' modules and files
### pandas/core
### pandas/io
### pandas/tools

> Reference for the preceding information is from: http://pandas.pydata.org/pandas-docs/stable/visualization.html

> Reference for the preceding information is from: http://pandas.pydata.org/pandas-docs/stable/reshaping.html

### pandas/sparse

> For more information on this, go to http://pandas.pydata.org/pandas-docs/version/stable/sparse.html.

### pandas/stats

> For more information on vector autoregression, go to: http://en.wikipedia.org/wiki/Vector_autoregression

### pandas/util

> The Substitution and Appender classes are decorators that perform substitution and appending on function docstrings and for more information on Python decorators, go to http://bit.ly/1zj8U0o.

### pandas/rpy
### pandas/tests
### pandas/compat
### pandas/computation

> * For more information on numexpr, go to https://code.google.com/p/numexpr/.
* For information of the usage of this module, go to http://pandas.pydata.org/pandas docs/stable/computation.html.

### pandas/tseries

> The Formatter and Locator classes are used for handling ticks in matplotlib plotting.

### pandas/sandbox
## 9.3 Improving performance using Python extensions

> According to the programming benchmarks site, Python is often slower than compiled languages, such as C/C++ for many algorithms or data structure operations. An example of this would be binary tree operations. In the following reference, Python3 ran 104x slower than the fastest C++ implementation of an n-body simulation calculation: http://bit.ly/1dm4JqW.

> So, how can we solve this legitimate yet vexing problem? We can mitigate this slowness in Python while maintaining the things that we like about it—clarity and productivity—by writing the parts of our code that are performance sensitive. For example numeric processing, algorithms in C/C++ and having them called by our Python code by writing a Python extension module: http://docs.python.org/2/extending/extending.html


```python
import pandas
pandas.__file__
```




    'C:\\Anaconda3\\lib\\site-packages\\pandas\\__init__.py'




```python
import math
math.__file__
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-88a0eccf93aa> in <module>()
          1 import math
    ----> 2 math.__file__


    AttributeError: module 'math' has no attribute '__file__'



```python
def fibonacci(n):
    a,b=1,1
    for i in range(n):
        a,b=a+b,a
    return a
```


```python
fibonacci(100)
```




    927372692193078999176




```python
%timeit fibonacci(100)
```

    100000 loops, best of 3: 5.97 µs per loop



```python
%load_ext cythonmagic
```

    The cythonmagic extension is already loaded. To reload it, use:
      %reload_ext cythonmagic



```python
# %reload_ext cythonmagic  # previous to python3
%load_ext Cython
```


```python
%%cython
def cfibonacci(int n):
    cdef int i, a,b
    for i in range(n):
        a,b = a+b, a
    return a
```


```python
%timeit cfibonacci(100)
```

    The slowest run took 12.76 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 101 ns per loop



```python
18.2/0.321
```




    56.69781931464174



## 9.4 Summary

> To summarize this chapter, we took a tour of the library hierarchy of pandas in an attempt to illustrate the internal workings of the library. We also touched on the benefis of speeding up our code performance by using a Python extension module.


```python

```
