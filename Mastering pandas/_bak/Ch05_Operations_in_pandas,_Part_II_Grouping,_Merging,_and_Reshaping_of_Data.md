
# Chapter 5: Operations in pandas, Part II – Grouping, Merging, and Reshaping of Data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Chapter 5: Operations in pandas, Part II – Grouping, Merging, and Reshaping of Data](#chapter-5-operations-in-pandas-part-ii-grouping-merging-and-reshaping-of-data)
	- [Grouping of data](#grouping-of-data)
		- [The groupby operation](#the-groupby-operation)
			- [Using groupby with a MultiIndex](#using-groupby-with-a-multiindex)
			- [Using the aggregate method](#using-the-aggregate-method)
			- [Applying multiple functions](#applying-multiple-functions)
			- [The transform() method](#the-transform-method)
			- [Filtering](#filtering)
	- [Merging and joining](#merging-and-joining)
		- [The concat function](#the-concat-function)
		- [Using append](#using-append)
		- [Appending a single row to a DataFrame](#appending-a-single-row-to-a-dataframe)
		- [SQL-like merging/joining of DataFrame objects](#sql-like-mergingjoining-of-dataframe-objects)
			- [The join function](#the-join-function)
	- [Pivots and reshaping data](#pivots-and-reshaping-data)
		- [Stacking and unstacking](#stacking-and-unstacking)
			- [The stack() function](#the-stack-function)
		- [Other methods to reshape DataFrames](#other-methods-to-reshape-dataframes)
			- [Using the melt function](#using-the-melt-function)
	- [Summary](#summary)

<!-- tocstop -->

## Grouping of data

### The groupby operation


```python
import pandas as pd
uefaDF=pd.read_csv('./Chapter 5/euro_winners.csv')
uefaDF.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Season</th>
      <th>Nation</th>
      <th>Winners</th>
      <th>Score</th>
      <th>Runners-up</th>
      <th>Runner-UpNation</th>
      <th>Venue</th>
      <th>Attendance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1955–56</td>
      <td>Spain</td>
      <td>Real Madrid</td>
      <td>4–3</td>
      <td>Stade de Reims</td>
      <td>France</td>
      <td>Parc des Princes,Paris</td>
      <td>38239</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1956–57</td>
      <td>Spain</td>
      <td>Real Madrid</td>
      <td>2–0</td>
      <td>Fiorentina</td>
      <td>Italy</td>
      <td>Santiago Bernabéu Stadium, Madrid</td>
      <td>124000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1957–58</td>
      <td>Spain</td>
      <td>Real Madrid</td>
      <td>3–2</td>
      <td>Milan</td>
      <td>Italy</td>
      <td>Heysel Stadium,Brussels</td>
      <td>67000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1958–59</td>
      <td>Spain</td>
      <td>Real Madrid</td>
      <td>2–0</td>
      <td>Stade de Reims</td>
      <td>France</td>
      <td>Neckarstadion,Stuttgart</td>
      <td>72000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1959–60</td>
      <td>Spain</td>
      <td>Real Madrid</td>
      <td>7–3</td>
      <td>Eintracht Frankfurt</td>
      <td>Germany</td>
      <td>Hampden Park,Glasgow</td>
      <td>127621</td>
    </tr>
  </tbody>
</table>
</div>




```python
nationsGrp =uefaDF.groupby('Nation');
type(nationsGrp)
```




    pandas.core.groupby.DataFrameGroupBy




```python
nationsGrp.groups
```




    {'England': [12, 21, 22, 23, 24, 25, 26, 28, 43, 49, 52, 56],
     'France': [37],
     'Germany': [18, 19, 20, 27, 41, 45, 57],
     'Italy': [7, 8, 9, 13, 29, 33, 34, 38, 40, 47, 51, 54],
     'Netherlands': [14, 15, 16, 17, 32, 39],
     'Portugal': [5, 6, 31, 48],
     'Romania': [30],
     'Scotland': [11],
     'Spain': [0, 1, 2, 3, 4, 10, 36, 42, 44, 46, 50, 53, 55],
     'Yugoslavia': [35]}




```python
len(nationsGrp.groups)
```




    10




```python
nationWins=nationsGrp.size()
```


```python
nationWins.sort(ascending=False)
nationWins
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: sort is deprecated, use sort_values(inplace=True) for INPLACE sorting
      if __name__ == '__main__':





    Nation
    Spain          13
    Italy          12
    England        12
    Germany         7
    Netherlands     6
    Portugal        4
    Yugoslavia      1
    Scotland        1
    Romania         1
    France          1
    dtype: int64




```python
winnersGrp =uefaDF.groupby(['Nation','Winners'])
clubWins=winnersGrp.size()
clubWins.sort(ascending=False)
clubWins
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:3: FutureWarning: sort is deprecated, use sort_values(inplace=True) for INPLACE sorting
      app.launch_new_instance()





    Nation       Winners          
    Spain        Real Madrid          9
    Italy        Milan                7
    Germany      Bayern Munich        5
    England      Liverpool            5
    Spain        Barcelona            4
    Netherlands  Ajax                 4
    England      Manchester United    3
    Italy        Internazionale       3
                 Juventus             2
    Portugal     Porto                2
                 Benfica              2
    England      Nottingham Forest    2
                 Chelsea              1
    France       Marseille            1
    Yugoslavia   Red Star Belgrade    1
    Germany      Borussia Dortmund    1
                 Hamburg              1
    Netherlands  Feyenoord            1
                 PSV Eindhoven        1
    Romania      Steaua Bucure?ti     1
    Scotland     Celtic               1
    England      Aston Villa          1
    dtype: int64




```python
goalStatsDF=pd.read_csv('./Chapter 5/goal_stats_euro_leagues_2012-13.csv')
goalStatsDF.head(3)
goalStatsDF.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Month</th>
      <th>Stat</th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19</th>
      <td>04/01/2013</td>
      <td>GoalsScored</td>
      <td>105.0</td>
      <td>127</td>
      <td>102.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>05/01/2013</td>
      <td>GoalsScored</td>
      <td>96.0</td>
      <td>109</td>
      <td>102.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>06/01/2013</td>
      <td>GoalsScored</td>
      <td>NaN</td>
      <td>80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalStatsDF=pd.read_csv('./Chapter 5/goal_stats_euro_leagues_2012-13.csv', index_col = 'Month')
goalStatsDF.head(3)
goalStatsDF.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Stat</th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>04/01/2013</th>
      <td>GoalsScored</td>
      <td>105.0</td>
      <td>127</td>
      <td>102.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>05/01/2013</th>
      <td>GoalsScored</td>
      <td>96.0</td>
      <td>109</td>
      <td>102.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>06/01/2013</th>
      <td>GoalsScored</td>
      <td>NaN</td>
      <td>80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalStatsGroupedByYear = goalStatsDF.groupby(lambda Month: Month.split('/')[2])
```


```python
for name, group in goalStatsGroupedByYear:
    print(name)
    print(group)
```

    2012
                         Stat    EPL  La Liga  Serie A  Bundesliga
    Month                                                         
    08/01/2012  MatchesPlayed   20.0       20     10.0        10.0
    09/01/2012  MatchesPlayed   38.0       39     50.0        44.0
    10/01/2012  MatchesPlayed   31.0       31     39.0        27.0
    11/01/2012  MatchesPlayed   50.0       41     42.0        46.0
    12/01/2012  MatchesPlayed   59.0       39     39.0        26.0
    08/01/2012    GoalsScored   57.0       60     21.0        23.0
    09/01/2012    GoalsScored  111.0      112    133.0       135.0
    10/01/2012    GoalsScored   95.0       88     97.0        77.0
    11/01/2012    GoalsScored  121.0      116    120.0       137.0
    12/01/2012    GoalsScored  183.0      109    125.0        72.0
    2013
                         Stat    EPL  La Liga  Serie A  Bundesliga
    Month                                                         
    01/01/2013  MatchesPlayed   42.0       40     40.0        18.0
    02/01/2013  MatchesPlayed   30.0       40     40.0        36.0
    03/01/2013  MatchesPlayed   35.0       38     39.0        36.0
    04/01/2013  MatchesPlayed   42.0       42     41.0        36.0
    05/01/2013  MatchesPlayed   33.0       40     40.0        27.0
    06/02/2013  MatchesPlayed    NaN       10      NaN         NaN
    01/01/2013    GoalsScored  117.0      121    104.0        51.0
    02/01/2013    GoalsScored   87.0      110    100.0       101.0
    03/01/2013    GoalsScored   91.0      101     99.0       106.0
    04/01/2013    GoalsScored  105.0      127    102.0       104.0
    05/01/2013    GoalsScored   96.0      109    102.0        92.0
    06/01/2013    GoalsScored    NaN       80      NaN         NaN



```python
goalStatsGroupedByMonth = goalStatsDF.groupby(level=0)
```


```python
for name, group in goalStatsGroupedByMonth:
    print(name)
    print(group)
    print("\n")
```


```python
goalStatsDF=goalStatsDF.reset_index()
goalStatsDF=goalStatsDF.set_index(['Month','Stat'])
```


```python
monthStatGroup=goalStatsDF.groupby(level=['Month','Stat'])
```


```python
for name, group in monthStatGroup:
    print(name)
    print(group)
```

#### Using groupby with a MultiIndex


```python
goalStatsDF2=pd.read_csv('./Chapter 5/goal_stats_euro_leagues_2012-13.csv')
goalStatsDF2=goalStatsDF2.set_index(['Month','Stat'])
```


```python
print(goalStatsDF2.head(3))
print(goalStatsDF2.tail(3))
```

                               EPL  La Liga  Serie A  Bundesliga
    Month      Stat                                             
    08/01/2012 MatchesPlayed  20.0       20     10.0        10.0
    09/01/2012 MatchesPlayed  38.0       39     50.0        44.0
    10/01/2012 MatchesPlayed  31.0       31     39.0        27.0
                              EPL  La Liga  Serie A  Bundesliga
    Month      Stat                                            
    04/01/2013 GoalsScored  105.0      127    102.0       104.0
    05/01/2013 GoalsScored   96.0      109    102.0        92.0
    06/01/2013 GoalsScored    NaN       80      NaN         NaN



```python
grouped2=goalStatsDF2.groupby(level='Stat')
grouped2.sum()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Stat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsScored</th>
      <td>1063.0</td>
      <td>1133</td>
      <td>1003.0</td>
      <td>898.0</td>
    </tr>
    <tr>
      <th>MatchesPlayed</th>
      <td>380.0</td>
      <td>380</td>
      <td>380.0</td>
      <td>306.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalStatsDF2.sum(level='Stat')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Stat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsScored</th>
      <td>1063.0</td>
      <td>1133</td>
      <td>1003.0</td>
      <td>898.0</td>
    </tr>
    <tr>
      <th>MatchesPlayed</th>
      <td>380.0</td>
      <td>380</td>
      <td>380.0</td>
      <td>306.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
totalsDF=grouped2.sum()
```


```python
 totalsDF.ix['GoalsScored']/totalsDF.ix['MatchesPlayed']
```




    EPL           2.797368
    La Liga       2.981579
    Serie A       2.639474
    Bundesliga    2.934641
    dtype: float64




```python
gpg=totalsDF.ix['GoalsScored']/totalsDF.ix['MatchesPlayed']
goalsPerGameDF=pd.DataFrame(gpg).T
```


```python
goalsPerGameDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.797368</td>
      <td>2.981579</td>
      <td>2.639474</td>
      <td>2.934641</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalsPerGameDF=goalsPerGameDF.rename(index={0:'GoalsPerGame'})
```


```python
goalsPerGameDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsPerGame</th>
      <td>2.797368</td>
      <td>2.981579</td>
      <td>2.639474</td>
      <td>2.934641</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.options.display.float_format='{:.2f}'.format
totalsDF.append(goalsPerGameDF)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Stat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsScored</th>
      <td>1063.00</td>
      <td>1133.00</td>
      <td>1003.00</td>
      <td>898.00</td>
    </tr>
    <tr>
      <th>MatchesPlayed</th>
      <td>380.00</td>
      <td>380.00</td>
      <td>380.00</td>
      <td>306.00</td>
    </tr>
    <tr>
      <th>GoalsPerGame</th>
      <td>2.80</td>
      <td>2.98</td>
      <td>2.64</td>
      <td>2.93</td>
    </tr>
  </tbody>
</table>
</div>



#### Using the aggregate method


```python
import numpy as np
pd.options.display.float_format=None
grouped2.aggregate(np.sum)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Stat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsScored</th>
      <td>1063.0</td>
      <td>1133</td>
      <td>1003.0</td>
      <td>898.0</td>
    </tr>
    <tr>
      <th>MatchesPlayed</th>
      <td>380.0</td>
      <td>380</td>
      <td>380.0</td>
      <td>306.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Applying multiple functions


```python
grouped2.agg([np.sum, np.mean,np.size])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">EPL</th>
      <th colspan="3" halign="left">La Liga</th>
      <th colspan="3" halign="left">Serie A</th>
      <th colspan="3" halign="left">Bundesliga</th>
    </tr>
    <tr>
      <th></th>
      <th>sum</th>
      <th>mean</th>
      <th>size</th>
      <th>sum</th>
      <th>mean</th>
      <th>size</th>
      <th>sum</th>
      <th>mean</th>
      <th>size</th>
      <th>sum</th>
      <th>mean</th>
      <th>size</th>
    </tr>
    <tr>
      <th>Stat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GoalsScored</th>
      <td>1063.0</td>
      <td>106.3</td>
      <td>11.0</td>
      <td>1133</td>
      <td>103.000000</td>
      <td>11</td>
      <td>1003.0</td>
      <td>100.3</td>
      <td>11.0</td>
      <td>898.0</td>
      <td>89.8</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>MatchesPlayed</th>
      <td>380.0</td>
      <td>38.0</td>
      <td>11.0</td>
      <td>380</td>
      <td>34.545455</td>
      <td>11</td>
      <td>380.0</td>
      <td>38.0</td>
      <td>11.0</td>
      <td>306.0</td>
      <td>30.6</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
nationsGrp['Attendance'].agg({'Total':np.sum, 'Average':np.mean, 'Deviation':np.std})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Deviation</th>
      <th>Total</th>
      <th>Average</th>
    </tr>
    <tr>
      <th>Nation</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>England</th>
      <td>17091.309877</td>
      <td>798411</td>
      <td>66534.250000</td>
    </tr>
    <tr>
      <th>France</th>
      <td>NaN</td>
      <td>64400</td>
      <td>64400.000000</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>13783.830076</td>
      <td>473083</td>
      <td>67583.285714</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>17443.516494</td>
      <td>789135</td>
      <td>65761.250000</td>
    </tr>
    <tr>
      <th>Netherlands</th>
      <td>16048.580972</td>
      <td>404934</td>
      <td>67489.000000</td>
    </tr>
    <tr>
      <th>Portugal</th>
      <td>15632.863259</td>
      <td>198542</td>
      <td>49635.500000</td>
    </tr>
    <tr>
      <th>Romania</th>
      <td>NaN</td>
      <td>70000</td>
      <td>70000.000000</td>
    </tr>
    <tr>
      <th>Scotland</th>
      <td>NaN</td>
      <td>45000</td>
      <td>45000.000000</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>27457.531064</td>
      <td>955203</td>
      <td>73477.153846</td>
    </tr>
    <tr>
      <th>Yugoslavia</th>
      <td>NaN</td>
      <td>56000</td>
      <td>56000.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### The transform() method


```python
goalStatsDF3=pd.read_csv('./Chapter 5/goal_stats_euro_leagues_2012-13.csv')
goalStatsDF3=goalStatsDF3.set_index(['Month'])
goalsScoredDF=goalStatsDF3.ix[goalStatsDF3['Stat']=='GoalsScored']
goalsScoredDF.iloc[:,1:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>08/01/2012</th>
      <td>57.0</td>
      <td>60</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>09/01/2012</th>
      <td>111.0</td>
      <td>112</td>
      <td>133.0</td>
      <td>135.0</td>
    </tr>
    <tr>
      <th>10/01/2012</th>
      <td>95.0</td>
      <td>88</td>
      <td>97.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>11/01/2012</th>
      <td>121.0</td>
      <td>116</td>
      <td>120.0</td>
      <td>137.0</td>
    </tr>
    <tr>
      <th>12/01/2012</th>
      <td>183.0</td>
      <td>109</td>
      <td>125.0</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>01/01/2013</th>
      <td>117.0</td>
      <td>121</td>
      <td>104.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>02/01/2013</th>
      <td>87.0</td>
      <td>110</td>
      <td>100.0</td>
      <td>101.0</td>
    </tr>
    <tr>
      <th>03/01/2013</th>
      <td>91.0</td>
      <td>101</td>
      <td>99.0</td>
      <td>106.0</td>
    </tr>
    <tr>
      <th>04/01/2013</th>
      <td>105.0</td>
      <td>127</td>
      <td>102.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>05/01/2013</th>
      <td>96.0</td>
      <td>109</td>
      <td>102.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>06/01/2013</th>
      <td>NaN</td>
      <td>80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalsScoredPerYearGrp = goalsScoredDF.groupby(lambda Month: Month.split('/')[2])
goalsScoredPerYearGrp.mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>113.4</td>
      <td>97</td>
      <td>99.2</td>
      <td>88.8</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>99.2</td>
      <td>108</td>
      <td>101.4</td>
      <td>90.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalsScoredPerYearGrp.count()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Stat</th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
fill_fcn = lambda x: x.fillna(x.mean())
trans = goalsScoredPerYearGrp.transform(fill_fcn)
tGroupedStats = trans.groupby(lambda Month: Month.split('/')[2])
tGroupedStats.mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>113.4</td>
      <td>97</td>
      <td>99.2</td>
      <td>88.8</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>99.2</td>
      <td>108</td>
      <td>101.4</td>
      <td>90.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
tGroupedStats.count()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



#### Filtering


```python
goalsScoredDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Stat</th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>08/01/2012</th>
      <td>GoalsScored</td>
      <td>57.0</td>
      <td>60</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>09/01/2012</th>
      <td>GoalsScored</td>
      <td>111.0</td>
      <td>112</td>
      <td>133.0</td>
      <td>135.0</td>
    </tr>
    <tr>
      <th>10/01/2012</th>
      <td>GoalsScored</td>
      <td>95.0</td>
      <td>88</td>
      <td>97.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>11/01/2012</th>
      <td>GoalsScored</td>
      <td>121.0</td>
      <td>116</td>
      <td>120.0</td>
      <td>137.0</td>
    </tr>
    <tr>
      <th>12/01/2012</th>
      <td>GoalsScored</td>
      <td>183.0</td>
      <td>109</td>
      <td>125.0</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>01/01/2013</th>
      <td>GoalsScored</td>
      <td>117.0</td>
      <td>121</td>
      <td>104.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>02/01/2013</th>
      <td>GoalsScored</td>
      <td>87.0</td>
      <td>110</td>
      <td>100.0</td>
      <td>101.0</td>
    </tr>
    <tr>
      <th>03/01/2013</th>
      <td>GoalsScored</td>
      <td>91.0</td>
      <td>101</td>
      <td>99.0</td>
      <td>106.0</td>
    </tr>
    <tr>
      <th>04/01/2013</th>
      <td>GoalsScored</td>
      <td>105.0</td>
      <td>127</td>
      <td>102.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>05/01/2013</th>
      <td>GoalsScored</td>
      <td>96.0</td>
      <td>109</td>
      <td>102.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>06/01/2013</th>
      <td>GoalsScored</td>
      <td>NaN</td>
      <td>80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalsScoredDF.drop('Stat', axis = 1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EPL</th>
      <th>La Liga</th>
      <th>Serie A</th>
      <th>Bundesliga</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>08/01/2012</th>
      <td>57.0</td>
      <td>60</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>09/01/2012</th>
      <td>111.0</td>
      <td>112</td>
      <td>133.0</td>
      <td>135.0</td>
    </tr>
    <tr>
      <th>10/01/2012</th>
      <td>95.0</td>
      <td>88</td>
      <td>97.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>11/01/2012</th>
      <td>121.0</td>
      <td>116</td>
      <td>120.0</td>
      <td>137.0</td>
    </tr>
    <tr>
      <th>12/01/2012</th>
      <td>183.0</td>
      <td>109</td>
      <td>125.0</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>01/01/2013</th>
      <td>117.0</td>
      <td>121</td>
      <td>104.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>02/01/2013</th>
      <td>87.0</td>
      <td>110</td>
      <td>100.0</td>
      <td>101.0</td>
    </tr>
    <tr>
      <th>03/01/2013</th>
      <td>91.0</td>
      <td>101</td>
      <td>99.0</td>
      <td>106.0</td>
    </tr>
    <tr>
      <th>04/01/2013</th>
      <td>105.0</td>
      <td>127</td>
      <td>102.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>05/01/2013</th>
      <td>96.0</td>
      <td>109</td>
      <td>102.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>06/01/2013</th>
      <td>NaN</td>
      <td>80</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
goalsScoredDF.groupby(level='Month')
```




    <pandas.core.groupby.DataFrameGroupBy object at 0x0000000A97760908>




```python
for col in goalsScoredDF.columns:
    print(col)
```

    Stat
    EPL
    La Liga
    Serie A
    Bundesliga



```python
import numpy as np
goalsScoredDF.groupby(level='Month').filter(lambda x: np.all([x[col] > 100 for col in goalsScoredDF.columns]))
```

## Merging and joining

### The concat function


```python
stockDataDF=pd.read_csv('./Chapter 5/tech_stockprices.csv').set_index(['Symbol']);stockDataDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>Shares Outstanding(M)</th>
      <th>Beta</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
      <td>459.00</td>
      <td>0.52</td>
      <td>589.80</td>
      <td>158.88</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
      <td>335.83</td>
      <td>0.87</td>
      <td>31.44</td>
      <td>380.64</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>2450.00</td>
      <td>NaN</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>1010.00</td>
      <td>27.48</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>65.25</td>
      <td>-0.30</td>
      <td>555.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.23</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>501.53</td>
      <td>40.32</td>
      <td>892.45</td>
      <td>12.44</td>
      <td>447.59</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
A=stockDataDF.ix[:4, ['Closing price', 'EPS']]; A
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
B=stockDataDF.ix[2:-2, ['P/E']];B
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>P/E</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>104.93</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>0.66</td>
    </tr>
  </tbody>
</table>
</div>




```python
C=stockDataDF.ix[1:5, ['Market Cap(B)']];C
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GOOG</th>
      <td>380.64</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>35.36</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>36.23</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([A,B,C],axis=1) # outer join
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
      <td>NaN</td>
      <td>380.64</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.23</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([A,B,C],axis=1, join='inner') # Inner join
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([A,B,C], axis=1, join_axes=[stockDataDF.index])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
      <td>NaN</td>
      <td>380.64</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.23</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
normDF=pd.DataFrame(np.random.randn(3,4));normDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.006398</td>
      <td>-1.079097</td>
      <td>-1.443114</td>
      <td>-0.378780</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-2.778138</td>
      <td>-0.503359</td>
      <td>-0.228286</td>
      <td>-1.538284</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.232718</td>
      <td>0.787588</td>
      <td>-0.008145</td>
      <td>0.756178</td>
    </tr>
  </tbody>
</table>
</div>




```python
binomDF=pd.DataFrame(np.random.binomial(100,0.5,(3,4)));binomDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>41</td>
      <td>42</td>
      <td>64</td>
    </tr>
    <tr>
      <th>1</th>
      <td>52</td>
      <td>56</td>
      <td>56</td>
      <td>48</td>
    </tr>
    <tr>
      <th>2</th>
      <td>44</td>
      <td>54</td>
      <td>51</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
poissonDF=pd.DataFrame(np.random.poisson(100,(3,4)));poissonDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>91</td>
      <td>96</td>
      <td>96</td>
    </tr>
    <tr>
      <th>1</th>
      <td>99</td>
      <td>106</td>
      <td>115</td>
      <td>106</td>
    </tr>
    <tr>
      <th>2</th>
      <td>102</td>
      <td>82</td>
      <td>100</td>
      <td>82</td>
    </tr>
  </tbody>
</table>
</div>




```python
rand_distribs=[normDF,binomDF,poissonDF]
```


```python
rand_distribsDF=pd.concat(rand_distribs,keys=['Normal','Binomial', 'Poisson']);
rand_distribsDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Normal</th>
      <th>0</th>
      <td>2.006398</td>
      <td>-1.079097</td>
      <td>-1.443114</td>
      <td>-0.378780</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-2.778138</td>
      <td>-0.503359</td>
      <td>-0.228286</td>
      <td>-1.538284</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.232718</td>
      <td>0.787588</td>
      <td>-0.008145</td>
      <td>0.756178</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Binomial</th>
      <th>0</th>
      <td>56.000000</td>
      <td>41.000000</td>
      <td>42.000000</td>
      <td>64.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>52.000000</td>
      <td>56.000000</td>
      <td>56.000000</td>
      <td>48.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>44.000000</td>
      <td>54.000000</td>
      <td>51.000000</td>
      <td>60.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Poisson</th>
      <th>0</th>
      <td>100.000000</td>
      <td>91.000000</td>
      <td>96.000000</td>
      <td>96.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>99.000000</td>
      <td>106.000000</td>
      <td>115.000000</td>
      <td>106.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>102.000000</td>
      <td>82.000000</td>
      <td>100.000000</td>
      <td>82.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Using append


```python
stockDataA = stockDataDF.ix[:2,:3]
stockDataA
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>Shares Outstanding(M)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
      <td>459.00</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
      <td>335.83</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockDataB = stockDataDF[2:]
stockDataB
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>Shares Outstanding(M)</th>
      <th>Beta</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>2450.00</td>
      <td>NaN</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>1010.00</td>
      <td>27.48</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>65.25</td>
      <td>-0.30</td>
      <td>555.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.23</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>501.53</td>
      <td>40.32</td>
      <td>892.45</td>
      <td>12.44</td>
      <td>447.59</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockDataA.append(stockDataB)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Beta</th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>Market Cap(B)</th>
      <th>P/E</th>
      <th>Shares Outstanding(M)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>NaN</td>
      <td>346.15</td>
      <td>0.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>459.00</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>NaN</td>
      <td>1133.43</td>
      <td>36.05</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>335.83</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>NaN</td>
      <td>61.48</td>
      <td>0.59</td>
      <td>150.92</td>
      <td>104.93</td>
      <td>2450.00</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>27.48</td>
      <td>34.90</td>
      <td>1.27</td>
      <td>35.36</td>
      <td>0.66</td>
      <td>1010.00</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>NaN</td>
      <td>65.25</td>
      <td>-0.30</td>
      <td>36.23</td>
      <td>NaN</td>
      <td>555.20</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>12.44</td>
      <td>501.53</td>
      <td>40.32</td>
      <td>0.84</td>
      <td>447.59</td>
      <td>892.45</td>
    </tr>
  </tbody>
</table>
</div>




```python
stockDataA.append(stockDataB).reindex_axis(stockDataDF.columns,axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Closing price</th>
      <th>EPS</th>
      <th>Shares Outstanding(M)</th>
      <th>Beta</th>
      <th>P/E</th>
      <th>Market Cap(B)</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMZN</th>
      <td>346.15</td>
      <td>0.59</td>
      <td>459.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>1133.43</td>
      <td>36.05</td>
      <td>335.83</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>61.48</td>
      <td>0.59</td>
      <td>2450.00</td>
      <td>NaN</td>
      <td>104.93</td>
      <td>150.92</td>
    </tr>
    <tr>
      <th>YHOO</th>
      <td>34.90</td>
      <td>1.27</td>
      <td>1010.00</td>
      <td>27.48</td>
      <td>0.66</td>
      <td>35.36</td>
    </tr>
    <tr>
      <th>TWTR</th>
      <td>65.25</td>
      <td>-0.30</td>
      <td>555.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.23</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>501.53</td>
      <td>40.32</td>
      <td>892.45</td>
      <td>12.44</td>
      <td>447.59</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
</div>



### Appending a single row to a DataFrame


```python
algos={'search':['DFS','BFS','Binary Search','Linear'],
       'sorting': ['Quicksort','Mergesort','Heapsort','Bubble Sort'],
       'machine learning':['RandomForest','K Nearest Neighbor','Logistic Regression','K-Means Clustering']}
algoDF=pd.DataFrame(algos);algoDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>machine learning</th>
      <th>search</th>
      <th>sorting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RandomForest</td>
      <td>DFS</td>
      <td>Quicksort</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K Nearest Neighbor</td>
      <td>BFS</td>
      <td>Mergesort</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Logistic Regression</td>
      <td>Binary Search</td>
      <td>Heapsort</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K-Means Clustering</td>
      <td>Linear</td>
      <td>Bubble Sort</td>
    </tr>
  </tbody>
</table>
</div>




```python
moreAlgos={'search': 'ShortestPath' , 'sorting': 'Insertion Sort',
           'machine learning': 'Linear Regression'}
algoDF.append(moreAlgos,ignore_index=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>machine learning</th>
      <th>search</th>
      <th>sorting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RandomForest</td>
      <td>DFS</td>
      <td>Quicksort</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K Nearest Neighbor</td>
      <td>BFS</td>
      <td>Mergesort</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Logistic Regression</td>
      <td>Binary Search</td>
      <td>Heapsort</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K-Means Clustering</td>
      <td>Linear</td>
      <td>Bubble Sort</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Linear Regression</td>
      <td>ShortestPath</td>
      <td>Insertion Sort</td>
    </tr>
  </tbody>
</table>
</div>



### SQL-like merging/joining of DataFrame objects


```python
USIndexDataDF=pd.read_csv('./Chapter 5/us_index_data.csv')
USIndexDataDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
      <td>15372.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
      <td>15445.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/02/05</td>
      <td>4011.55</td>
      <td>1751.64</td>
      <td>1093.59</td>
      <td>15440.23</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/02/06</td>
      <td>4057.12</td>
      <td>1773.43</td>
      <td>1103.93</td>
      <td>15628.53</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice1=USIndexDataDF.ix[:1,:3]
slice1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice2=USIndexDataDF.ix[:1,[0,3,4]]
slice2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice3=USIndexDataDF.ix[[1,2],:3]
slice3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(slice1,slice2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(slice3,slice2,how='inner')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(slice3,slice2,how='outer')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/01/30</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(slice3,slice2,how='left')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(slice3,slice2,how='right')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/30</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
  </tbody>
</table>
</div>



#### The join function


```python
slice_NASD_SP=USIndexDataDF.ix[:3,:3]
slice_NASD_SP
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice_Russ_DJIA=USIndexDataDF.ix[:3,3:]
slice_Russ_DJIA
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1094.58</td>
      <td>15372.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1102.84</td>
      <td>15445.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice_NASD_SP.join(slice_Russ_DJIA)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/02/03</td>
      <td>3996.96</td>
      <td>1741.89</td>
      <td>1094.58</td>
      <td>15372.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/02/04</td>
      <td>4031.52</td>
      <td>1755.20</td>
      <td>1102.84</td>
      <td>15445.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
slice1.join(slice2)
```

## Pivots and reshaping data


```python
plantGrowthRawDF=pd.read_csv('./Chapter 5/PlantGrowth.csv')
plantGrowthRawDF.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>observation</th>
      <th>weight</th>
      <th>group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4.17</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5.58</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>5.18</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>6.11</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.50</td>
      <td>ctrl</td>
    </tr>
  </tbody>
</table>
</div>




```python
plantGrowthRawDF[plantGrowthRawDF['group']=='ctrl']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>observation</th>
      <th>weight</th>
      <th>group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4.17</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5.58</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>5.18</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>6.11</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.50</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>4.61</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>5.17</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>4.53</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>5.33</td>
      <td>ctrl</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>5.14</td>
      <td>ctrl</td>
    </tr>
  </tbody>
</table>
</div>




```python
plantGrowthRawDF.pivot(index='observation',columns='group',values='weight')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>group</th>
      <th>ctrl</th>
      <th>trt1</th>
      <th>trt2</th>
    </tr>
    <tr>
      <th>observation</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4.17</td>
      <td>4.81</td>
      <td>6.31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.58</td>
      <td>4.17</td>
      <td>5.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.18</td>
      <td>4.41</td>
      <td>5.54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.11</td>
      <td>3.59</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.50</td>
      <td>5.87</td>
      <td>5.37</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.61</td>
      <td>3.83</td>
      <td>5.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.17</td>
      <td>6.03</td>
      <td>4.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.53</td>
      <td>4.89</td>
      <td>6.15</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.33</td>
      <td>4.32</td>
      <td>5.80</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.14</td>
      <td>4.69</td>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(plantGrowthRawDF, values='weight', index='observation', columns=['group'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>group</th>
      <th>ctrl</th>
      <th>trt1</th>
      <th>trt2</th>
    </tr>
    <tr>
      <th>observation</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4.17</td>
      <td>4.81</td>
      <td>6.31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.58</td>
      <td>4.17</td>
      <td>5.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.18</td>
      <td>4.41</td>
      <td>5.54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.11</td>
      <td>3.59</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.50</td>
      <td>5.87</td>
      <td>5.37</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.61</td>
      <td>3.83</td>
      <td>5.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.17</td>
      <td>6.03</td>
      <td>4.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.53</td>
      <td>4.89</td>
      <td>6.15</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.33</td>
      <td>4.32</td>
      <td>5.80</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.14</td>
      <td>4.69</td>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(plantGrowthRawDF, values='weight', columns=['group'], aggfunc=np.mean)
```




    group
    ctrl    5.032
    trt1    4.661
    trt2    5.526
    Name: weight, dtype: float64



### Stacking and unstacking

#### The stack() function


```python
plantGrowthStackedDF = plantGrowthRawDF.set_index(['group','observation'])
```


```python
plantGrowthStackedDF.unstack(level='group')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">weight</th>
    </tr>
    <tr>
      <th>group</th>
      <th>ctrl</th>
      <th>trt1</th>
      <th>trt2</th>
    </tr>
    <tr>
      <th>observation</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4.17</td>
      <td>4.81</td>
      <td>6.31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.58</td>
      <td>4.17</td>
      <td>5.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.18</td>
      <td>4.41</td>
      <td>5.54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.11</td>
      <td>3.59</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.50</td>
      <td>5.87</td>
      <td>5.37</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.61</td>
      <td>3.83</td>
      <td>5.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.17</td>
      <td>6.03</td>
      <td>4.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.53</td>
      <td>4.89</td>
      <td>6.15</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.33</td>
      <td>4.32</td>
      <td>5.80</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.14</td>
      <td>4.69</td>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
plantGrowthStackedDF.index
```




    MultiIndex(levels=[['ctrl', 'trt1', 'trt2'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
               labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
               names=['group', 'observation'])




```python
plantGrowthStackedDF.columns
```




    Index(['weight'], dtype='object')




```python
plantGrowthStackedDF.unstack(level='group').index
```




    Int64Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='int64', name='observation')




```python
plantGrowthStackedDF.unstack(level='group').columns
```




    MultiIndex(levels=[['weight'], ['ctrl', 'trt1', 'trt2']],
               labels=[[0, 0, 0], [0, 1, 2]],
               names=[None, 'group'])




```python
plantGrowthStackedDF.unstack(level=0).stack('group')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>weight</th>
    </tr>
    <tr>
      <th>observation</th>
      <th>group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">1</th>
      <th>ctrl</th>
      <td>4.17</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.81</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>6.31</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2</th>
      <th>ctrl</th>
      <td>5.58</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.17</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.12</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">3</th>
      <th>ctrl</th>
      <td>5.18</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.41</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.54</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">4</th>
      <th>ctrl</th>
      <td>6.11</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>3.59</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.50</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">5</th>
      <th>ctrl</th>
      <td>4.50</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>5.87</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.37</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">6</th>
      <th>ctrl</th>
      <td>4.61</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>3.83</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.29</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">7</th>
      <th>ctrl</th>
      <td>5.17</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>6.03</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>4.92</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">8</th>
      <th>ctrl</th>
      <td>4.53</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.89</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>6.15</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">9</th>
      <th>ctrl</th>
      <td>5.33</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.32</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.80</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">10</th>
      <th>ctrl</th>
      <td>5.14</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.69</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
plantGrowthStackedDF.unstack()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="10" halign="left">weight</th>
    </tr>
    <tr>
      <th>observation</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
    </tr>
    <tr>
      <th>group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ctrl</th>
      <td>4.17</td>
      <td>5.58</td>
      <td>5.18</td>
      <td>6.11</td>
      <td>4.50</td>
      <td>4.61</td>
      <td>5.17</td>
      <td>4.53</td>
      <td>5.33</td>
      <td>5.14</td>
    </tr>
    <tr>
      <th>trt1</th>
      <td>4.81</td>
      <td>4.17</td>
      <td>4.41</td>
      <td>3.59</td>
      <td>5.87</td>
      <td>3.83</td>
      <td>6.03</td>
      <td>4.89</td>
      <td>4.32</td>
      <td>4.69</td>
    </tr>
    <tr>
      <th>trt2</th>
      <td>6.31</td>
      <td>5.12</td>
      <td>5.54</td>
      <td>5.50</td>
      <td>5.37</td>
      <td>5.29</td>
      <td>4.92</td>
      <td>6.15</td>
      <td>5.80</td>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
plantGrowthStackedDF.unstack().stack()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>weight</th>
    </tr>
    <tr>
      <th>group</th>
      <th>observation</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="10" valign="top">ctrl</th>
      <th>1</th>
      <td>4.17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6.11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.50</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.61</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.17</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.53</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.33</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.14</td>
    </tr>
    <tr>
      <th rowspan="10" valign="top">trt1</th>
      <th>1</th>
      <td>4.81</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.41</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.87</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3.83</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6.03</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.89</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.32</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.69</td>
    </tr>
    <tr>
      <th rowspan="10" valign="top">trt2</th>
      <th>1</th>
      <td>6.31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.37</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4.92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6.15</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.80</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.26</td>
    </tr>
  </tbody>
</table>
</div>



### Other methods to reshape DataFrames

#### Using the melt function


```python
from pandas.core.reshape import melt
USIndexDataDF[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Nasdaq</th>
      <th>S&amp;P 500</th>
      <th>Russell 2000</th>
      <th>DJIA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>4123.13</td>
      <td>1794.19</td>
      <td>1139.36</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>4103.88</td>
      <td>1782.59</td>
      <td>1130.88</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
 melt(USIndexDataDF[:2], id_vars=['TradingDate'], var_name='Index Name', value_name='Index Value')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Index Name</th>
      <th>Index Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>Nasdaq</td>
      <td>4123.13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>Nasdaq</td>
      <td>4103.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/01/30</td>
      <td>S&amp;P 500</td>
      <td>1794.19</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/01/31</td>
      <td>S&amp;P 500</td>
      <td>1782.59</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/01/30</td>
      <td>Russell 2000</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/01/31</td>
      <td>Russell 2000</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2014/01/30</td>
      <td>DJIA</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2014/01/31</td>
      <td>DJIA</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>



* The pandas.get_dummies() function


```python
melted=melt(USIndexDataDF[:2], id_vars=['TradingDate'], var_name='Index Name', value_name='Index Value')
melted
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TradingDate</th>
      <th>Index Name</th>
      <th>Index Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014/01/30</td>
      <td>Nasdaq</td>
      <td>4123.13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014/01/31</td>
      <td>Nasdaq</td>
      <td>4103.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014/01/30</td>
      <td>S&amp;P 500</td>
      <td>1794.19</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014/01/31</td>
      <td>S&amp;P 500</td>
      <td>1782.59</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014/01/30</td>
      <td>Russell 2000</td>
      <td>1139.36</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2014/01/31</td>
      <td>Russell 2000</td>
      <td>1130.88</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2014/01/30</td>
      <td>DJIA</td>
      <td>15848.61</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2014/01/31</td>
      <td>DJIA</td>
      <td>15698.85</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.get_dummies(melted['Index Name'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DJIA</th>
      <th>Nasdaq</th>
      <th>Russell 2000</th>
      <th>S&amp;P 500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Summary
