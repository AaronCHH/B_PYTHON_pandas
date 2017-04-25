
# Chapter 10: R and pandas Compared
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: R and pandas Compared](#chapter-10-r-and-pandas-compared)
  * [10.1 R data types](#101-r-data-types)
    * [R lists](#r-lists)
    * [R DataFrames](#r-dataframes)
  * [10.2 Slicing and selection](#102-slicing-and-selection)
    * [R-matrix and Numpy array compared](#r-matrix-and-numpy-array-compared)
    * [R lists and pandas series compared](#r-lists-and-pandas-series-compared)
      * [Specifying column name in R](#specifying-column-name-in-r)
      * [Specifying column name in pandas](#specifying-column-name-in-pandas)
    * [R DataFrames versus pandas DataFrames](#r-dataframes-versus-pandas-dataframes)
      * [Multi-column selection in R](#multi-column-selection-in-r)
      * [Multi-column selection in pandas](#multi-column-selection-in-pandas)
  * [10.3 Arithmetic operations on columns](#103-arithmetic-operations-on-columns)
  * [10.4 Aggregation and GroupBy](#104-aggregation-and-groupby)
    * [Aggregation in R](#aggregation-in-r)
    * [The pandas' GroupBy operator](#the-pandas-groupby-operator)
  * [10.5 Comparing matching operators in R and pandas](#105-comparing-matching-operators-in-r-and-pandas)
    * [R %in% operator](#r-in-operator)
    * [The pandas isin() function](#the-pandas-isin-function)
  * [10.6 Logical subsetting](#106-logical-subsetting)
    * [Logical subsetting in R](#logical-subsetting-in-r)
    * [Logical subsetting in pandas](#logical-subsetting-in-pandas)
  * [10.7 Split-apply-combine](#107-split-apply-combine)
    * [Implementation in R](#implementation-in-r)
    * [Implementation in pandas](#implementation-in-pandas)
  * [10.8 Reshaping using Melt](#108-reshaping-using-melt)
    * [The R melt() function](#the-r-melt-function)
    * [The pandas melt() function](#the-pandas-melt-function)
  * [10.9 Factors/categorical data](#109-factorscategorical-data)
    * [An R example using cut()](#an-r-example-using-cut)
    * [The pandas solution](#the-pandas-solution)
  * [10.10 Summary](#1010-summary)

<!-- tocstop -->


## 10.1 R data types

* Character
* Numeric
* Integer
* Complex
* Logical/Boolean
---
* Vector
* List
* DataFrame
* Matrix

> For more information on R data types, refer to the following document at: http://www.statmethods.net/input/datatypes.html.
For NumPy data types, refer to the following document at: http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html and http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html.

### R lists

```{r id:"j1x4x7fx"}
h_lst <- list(23,'donkey',5.6,1+4i,TRUE)
h_lst
typeof(h_lst)
```

* **Python**


```python
h_list = [23, 'donkey', 5.6,1+4j, True]
import pandas as pd
h_ser = pd.Series(h_list)
h_ser
```




    0        23
    1    donkey
    2       5.6
    3    (1+4j)
    4      True
    dtype: object




```python
type(h_ser)
```




    pandas.core.series.Series



### R DataFrames

```r
stocks_table<- data.frame(Symbol=c('GOOG','AMZN','FB','AAPL',
                                   'TWTR','NFLX','LINKD'),
                          Price=c(518.7,307.82,74.9,109.7,37.1,
                                  334.48,219.9),
                          MarketCap=c(352.8,142.29,216.98,643.55,23.54,20.15,27.31))
stocks_table
```

* **Python**


```python
stocks_df=pd.DataFrame({'Symbol':['GOOG','AMZN','FB','AAPL',
                                  'TWTR','NFLX','LNKD'],
                        'Price':[518.7,307.82,74.9,109.7,37.1,
                                 334.48,219.9],
                        'MarketCap($B)' : [352.8,142.29,216.98,643.55,
                                           23.54,20.15,27.31]
                       })

stocks_df = stocks_df.reindex_axis(sorted(stocks_df.columns,reverse=True),axis=1)
stocks_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Symbol</th>
      <th>Price</th>
      <th>MarketCap($B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>518.70</td>
      <td>352.80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AMZN</td>
      <td>307.82</td>
      <td>142.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FB</td>
      <td>74.90</td>
      <td>216.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AAPL</td>
      <td>109.70</td>
      <td>643.55</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TWTR</td>
      <td>37.10</td>
      <td>23.54</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NFLX</td>
      <td>334.48</td>
      <td>20.15</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LNKD</td>
      <td>219.90</td>
      <td>27.31</td>
    </tr>
  </tbody>
</table>
</div>



## 10.2 Slicing and selection

> In R, we slice objects in the following three ways:
• [: This always returns an object of the same type as the original and can be used to select more than one element.
• [[: This is used to extract elements of list or DataFrame; and can only be used to extract a single element,: the type of the returned element will not necessarily be a list or DataFrame.
• $: This is used to extract elements of a list or DataFrame by name and is similar to [[.
Here are some slicing examples in R and their equivalents in pandas:

### R-matrix and Numpy array compared

```r
r_mat<- matrix(2:13,4,3)
r_mat
r_mat[1,]
r_mat[,2]
```

* **Python**


```python
import numpy as np
a = np.array(range(2,6))
b = np.array(range(6,10))
c = np.array(range(10,14))

np_ar = np.column_stack([a,b,c])
np_ar
```




    array([[ 2,  6, 10],
           [ 3,  7, 11],
           [ 4,  8, 12],
           [ 5,  9, 13]])




```python
np_ar[0,]
```




    array([ 2,  6, 10])



> Indexing is different in R and pandas/NumPy. In R, indexing starts at 1, while in pandas/NumPy, it starts at 0. Hence, we have to subtract 1 from all indexes when making the translation from R to pandas/NumPy.


```python
# To select second column, write the following command:
np_ar[:,1]
```




    array([6, 7, 8, 9])




```python
# Another option is to transpose the array fist and then select the column, as follows:
np_ar.T[1,]
```




    array([6, 7, 8, 9])



### R lists and pandas series compared

```r
cal_lst<- list(weekdays=1:8, mth='jan')
cal_lst
cal_lst[1]
cal_lst[[1]]
cal_lst[2]
```

* **Python**


```python
cal_df= pd.Series({'weekdays':range(1,8), 'mth':'jan'})
cal_df
```




    mth                           jan
    weekdays    (1, 2, 3, 4, 5, 6, 7)
    dtype: object




```python
cal_df[0]
```




    'jan'




```python
cal_df[1]
```




    range(1, 8)




```python
cal_df[[1]]
```




    weekdays    (1, 2, 3, 4, 5, 6, 7)
    dtype: object



```
In the case of R, the []  operator produces a container type, that is, a list containing the string, while the [[]]  produces an atomic type: in this case, a character as follows:

>typeof(cal_lst[2])
[1] "list"
>typeof(cal_lst[[2]])
[1] "character"
```

```
In the case of pandas, the opposite is true: []  produces the atomic type, while [[]] results in a complex type, that is, a series as follows:

In [99]: type(cal_df[0])
Out[99]: str
In [101]: type(cal_df[[0]])
Out[101]: pandas.core.series.Series
```

#### Specifying column name in R

```
In R, this can be done with the column name preceded by the $ operator as follows:
> cal_lst$mth
[1] "jan"
> cal_lst$'mth'
[1] "jan"
```

#### Specifying column name in pandas


```python
cal_df['mth']
```




    'jan'



```
One area where R and pandas differ is in the subsetting of nested elements. For example, to obtain day 4 from weekdays, we have to use the [[]]  operator in R:
> cal_lst[[1]][[4]]
[1] 4
> cal_lst[[c(1,4)]]
[1] 4
```

```
However, in the case of pandas, we can just use a double [] :
In [132]: cal_df[1][3]
Out[132]: 4
```

### R DataFrames versus pandas DataFrames

#### Multi-column selection in R

```
In R, we specify the multiple columns to select by stating them in a vector within square brackets:

>stocks_table[c('Symbol','Price')]
Symbol Price
1 GOOG 518.70
2 AMZN 307.82
3 FB 74.90
4 AAPL 109.70
5 TWTR 37.10
6 NFLX 334.48
7 LINKD 219.90

>stocks_table[,c('Symbol','Price')]
Symbol Price
1 GOOG 518.70
2 AMZN 307.82
3 FB 74.90
4 AAPL 109.70
5 TWTR 37.10
6 NFLX 334.48
7 LINKD 219.90
```

#### Multi-column selection in pandas


```python
stocks_df[['Symbol','Price']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Symbol</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>518.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AMZN</td>
      <td>307.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FB</td>
      <td>74.90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AAPL</td>
      <td>109.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TWTR</td>
      <td>37.10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NFLX</td>
      <td>334.48</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LNKD</td>
      <td>219.90</td>
    </tr>
  </tbody>
</table>
</div>




```python
stocks_df.loc[:,['Symbol','Price']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Symbol</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>518.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AMZN</td>
      <td>307.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FB</td>
      <td>74.90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AAPL</td>
      <td>109.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TWTR</td>
      <td>37.10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NFLX</td>
      <td>334.48</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LNKD</td>
      <td>219.90</td>
    </tr>
  </tbody>
</table>
</div>



## 10.3 Arithmetic operations on columns

```
Here, we construct a DataFrame in R with columns labeled x and y, and subtract column y from column x:

> norm_df<- data.frame(x=rnorm(7,0,1), y=rnorm(7,0,1))
> norm_df$x - norm_df$y
[1] -1.3870730 2.4681458 -4.6991395 0.2978311 -0.8492245 1.5851009
-1.4620324

The with operator in R also has the same effect as arithmetic operations:
> with(norm_df,x-y)
[1] -1.3870730 2.4681458 -4.6991395 0.2978311 -0.8492245 1.5851009
-1.4620324
```

* **Python**


```python
import pandas as pd
import numpy as np
df = pd.DataFrame({'x': np.random.normal(0,1,size=7), 'y': np.random.normal(0,1,size=7)})
df.x - df.y
```




    0   -0.508194
    1    1.374298
    2    1.583775
    3    1.795601
    4   -0.988068
    5    1.458116
    6    2.558691
    dtype: float64




```python
df.eval('x-y')
```




    0   -0.508194
    1    1.374298
    2    1.583775
    3    1.795601
    4   -0.988068
    5    1.458116
    6    2.558691
    dtype: float64



## 10.4 Aggregation and GroupBy

### Aggregation in R

```{r id:"j1x4x7g0"}
goal_stats=read.csv('champ_league_stats_semifinalists.csv')
goal_stats

goal_stats$GoalsPerGame <- goal_stats$Goals/goal_stats$GamesPlayed
goal_stats

aggregate(x=goal_stats[,c('GoalsPerGame')], by=list(goal_stats$Club),FUN=max)

tapply(goal_stats$GoalsPerGame,goal_stats$Club,max)
```

### The pandas' GroupBy operator


```python
import pandas as pd
import numpy as np

goal_stats_df=pd.read_csv('champ_league_stats_semifinalists.csv')

goal_stats_df['GoalsPerGame']= goal_stats_df['Goals']/goal_stats_df['GamesPlayed']

goal_stats_df

grouped = goal_stats_df.groupby('Club')

grouped['GoalsPerGame'].aggregate(np.max)

grouped['GoalsPerGame'].apply(np.max)
```

## 10.5 Comparing matching operators in R and pandas

### R %in% operator

```{r id:"j1x4x7g0"}
stock_symbols=stocks_table$Symbol
stock_symbols

stock_symbols %in% c('GOOG','NFLX')
```

### The pandas isin() function


```python
stock_symbols = stocks_df.Symbol
stock_symbols
```




    0    GOOG
    1    AMZN
    2      FB
    3    AAPL
    4    TWTR
    5    NFLX
    6    LNKD
    Name: Symbol, dtype: object




```python
stock_symbols.isin(['GOOG','NFLX'])
```




    0     True
    1    False
    2    False
    3    False
    4    False
    5     True
    6    False
    Name: Symbol, dtype: bool



## 10.6 Logical subsetting
### Logical subsetting in R

• Via a logical slice:

```{R id:"j1x4x7g1"}
goaml_stats[goal_stats$GoalsPerGame>=0.5,]
```

• Via the subset()  function:

```{r id:"j1x4x7g1"}
subset(goal_stats,GoalsPerGame>=0.5)
```

### Logical subsetting in pandas

• Via a logical slice:


```python
goal_stats_df[goal_stats_df['GoalsPerGame']>=0.5]
```

• Via the subset()  function:


```python
goal_stats_df.query('GoalsPerGame>= 0.5')
```

## 10.7 Split-apply-combine

> For more information on ddply, you can refer to the following: http://www.inside-r.org/packages/cran/plyr/docs/ddply

> To illustrate, let us consider a subset of a recently created dataset in R, which contains data on flghts departing NYC in 2013: http://cran.r-project.org/web/packages/nycflights13/index.html.

### Implementation in R

```{r id:"j1x4x7g2"}
install.packages('nycflights13')
...

library('nycflights13')
dim(flights)
head(flights,3)

flights.data=na.omit(flights[,c('year','month','dep_delay','arr_delay','distance')])
flights.sample<- flights.data[sample(1:nrow(flights.data),100,replace=FALSE),]
head(flights.sample,5)

ddply(flights.sample,.(year,month),summarize, mean_dep_delay=round(mean(dep_delay),2), s_dep_delay=round(sd(dep_delay),2))

write.csv(flights.sample,file='nycflights13_sample.csv', quote=FALSE,row.names=FALSE)
```

### Implementation in pandas


```python
flights_sample=pd.read_csv('nycflights13_sample.csv')

flights_sample.head()

pd.set_option('precision',3)
grouped = flights_sample_df.groupby(['year','month'])
grouped['dep_delay'].agg([np.mean, np.std])
```

## 10.8 Reshaping using Melt

### The R melt() function

```{r id:"j1x4x7g2"}
sample4=head(flights.sample,4)[c('year','month','dep_delay','arr_delay')]
sample4

melt(sample4,id=c('year','month'))
```

> For more information, you can refer to the following: http://www.statmethods.net/management/reshape.html.

### The pandas melt() function


```python
sample_4_df=flights_sample_df[['year','month','dep_delay', 'arr_delay']].head(4)
sample_4_df
```


```python
pd.melt(sample_4_df,id_vars=['year','month'])
```

> The reference for this information is from: http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-by-melt.

## 10.9 Factors/categorical data

### An R example using cut()

```{R id:"j1x4x7g3"}
clinical.trial<- data.frame(patient = 1:1000,
                            age = rnorm(1000, mean = 50, sd = 5),
                            year.enroll = sample(paste("19", 80:99, sep = ""),
                                                 1000, replace = TRUE))
summary(clinical.trial)

ctcut<- cut(clinical.trial$age, breaks = 5)> table(ctcut)
ctcut
```

> The reference for the preceding data can be found at: http://www.r-bloggers.com/r-function-of-the-day-cut/.

### The pandas solution


```python
pd.set_option('precision',4)
clinical_trial=pd.DataFrame({'patient':range(1,1001),
                             'age' : np.random.normal(50,5,size=1000),
                             'year_enroll': [str(x) for x in np.random.choice(range(1980,2000),size=1000,replace=True)]})

clinical_trial.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>patient</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1000.0000</td>
      <td>1000.0000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>50.3431</td>
      <td>500.5000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.9643</td>
      <td>288.8204</td>
    </tr>
    <tr>
      <th>min</th>
      <td>30.7673</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>46.9517</td>
      <td>250.7500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>50.4489</td>
      <td>500.5000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>53.7125</td>
      <td>750.2500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>67.9728</td>
      <td>1000.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
clinical_trial.describe(include=['O'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year_enroll</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>20</td>
    </tr>
    <tr>
      <th>top</th>
      <td>1991</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
clinical_trial.year_enroll.value_counts()[:6]
```




    1991    60
    1995    59
    1993    57
    1987    55
    1988    54
    1997    53
    Name: year_enroll, dtype: int64




```python
ctcut=pd.cut(clinical_trial['age'], 5)
ctcut.head()
```




    0     (45.65, 53.0906]
    1    (53.0906, 60.532]
    2     (45.65, 53.0906]
    3     (45.65, 53.0906]
    4     (45.65, 53.0906]
    Name: age, dtype: category
    Categories (5, object): [(30.73, 38.208] < (38.208, 45.65] < (45.65, 53.0906] < (53.0906, 60.532] < (60.532, 67.973]]




```python
ctcut.value_counts().sort_index()
```




    (30.73, 38.208]        6
    (38.208, 45.65]      162
    (45.65, 53.0906]     545
    (53.0906, 60.532]    268
    (60.532, 67.973]      19
    Name: age, dtype: int64



## 10.10 Summary

> In this chapter, we have attempted to compare key features in R with their pandas equivalents in order to achieve the following objectives:
• To assist R users who may wish to replicate the same functionality in pandas
• To assist any users who upon reading some R code may wish to rewrite the code in pandas

> In the next chapter, we will conclude the book by giving a brief introduction to the scikit-learn library for doing machine learning and show how pandas fis within that framework. The reference documentation for this chapter can be found here: http://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html.


```python

```
