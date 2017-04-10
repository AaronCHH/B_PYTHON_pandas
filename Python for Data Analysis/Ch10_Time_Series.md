
# Chapter 10. Time Series


```python
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np
pd.options.display.max_rows = 12
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 4))
```


```python
%matplotlib inline
```

## 10.1 Date and Time Data Types and Tools


```python
from datetime import datetime
now = datetime.now()
now
```


```python
now.year, now.month, now.day
```


```python
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
```


```python
delta.days
```


```python
delta.seconds
```


```python
from datetime import timedelta
start = datetime(2011, 1, 7)
start + timedelta(12)
```


```python
start - 2 * timedelta(12)
```

### 10.1.1 Converting between string and datetime


```python
stamp = datetime(2011, 1, 3)
```


```python
str(stamp)
```


```python
stamp.strftime('%Y-%m-%d')
```


```python
value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')
```


```python
datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]
```


```python
from dateutil.parser import parse
parse('2011-01-03')
```


```python
parse('Jan 31, 1997 10:45 PM')
```


```python
parse('6/12/2011', dayfirst=True)
```


```python
datestrs
```


```python
pd.to_datetime(datestrs)
# note: output changed (no '00:00:00' anymore)
```


```python
idx = pd.to_datetime(datestrs + [None])
idx
```


```python
idx[2]
```


```python
pd.isnull(idx)
```

## 10.2 Time Series Basics


```python
from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = Series(np.random.randn(6), index=dates)
ts
```


```python
type(ts)
# note: output changed to "pandas.core.series.Series"
```


```python
ts.index
```


```python
ts + ts[::2]
```


```python
ts.index.dtype
# note: output changed from dtype('datetime64[ns]') to dtype('<M8[ns]')
```


```python
stamp = ts.index[0]
stamp
# note: output changed from <Timestamp: 2011-01-02 00:00:00> to Timestamp('2011-01-02 00:00:00')
```

### 10.2.1 Indexing, Selection, Subsetting


```python
stamp = ts.index[2]
ts[stamp]
```


```python
ts['1/10/2011']
```


```python
ts['20110110']
```


```python
longer_ts = Series(np.random.randn(1000),
                   index=pd.date_range('1/1/2000', periods=1000))
longer_ts
```


```python
longer_ts['2001']
```


```python
longer_ts['2001-05']
```


```python
ts[datetime(2011, 1, 7):]
```


```python
ts
```


```python
ts['1/6/2011':'1/11/2011']
```


```python
ts.truncate(after='1/9/2011')
```


```python
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = DataFrame(np.random.randn(100, 4),
                    index=dates,
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])
long_df.ix['5-2001']
```

### 10.2.2 Time Series with Duplicate Indices


```python
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000',
                          '1/3/2000'])
dup_ts = Series(np.arange(5), index=dates)
dup_ts
```


```python
dup_ts.index.is_unique
```


```python
dup_ts['1/3/2000']  # not duplicated
```


```python
dup_ts['1/2/2000']  # duplicated
```


```python
grouped = dup_ts.groupby(level=0)
grouped.mean()
```


```python
grouped.count()
```

## 10.3 Date Ranges, Frequencies, and Shifting


```python
ts
```


```python
ts.resample('D')
```

### 10.3.1 Generating Date Ranges


```python
index = pd.date_range('4/1/2012', '6/1/2012')
index
```


```python
pd.date_range(start='4/1/2012', periods=20)
```


```python
pd.date_range(end='6/1/2012', periods=20)
```


```python
pd.date_range('1/1/2000', '12/1/2000', freq='BM')
```


```python
pd.date_range('5/2/2012 12:56:31', periods=5)
```


```python
pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True)
```

### 10.3.2 Frequencies and Date Offsets


```python
from pandas.tseries.offsets import Hour, Minute
hour = Hour()
hour
```


```python
four_hours = Hour(4)
four_hours
```


```python
pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')
```


```python
Hour(2) + Minute(30)
```


```python
pd.date_range('1/1/2000', periods=10, freq='1h30min')
```

* __Week of month dates__


```python
rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
list(rng)
```

### 10.3.3 Shifting (Leading and Lagging) Data


```python
ts = Series(np.random.randn(4),
            index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts
```


```python
ts.shift(2)
```


```python
ts.shift(-2)
```
ts / ts.shift(1) - 1

```python
ts.shift(2, freq='M')
```


```python
ts.shift(3, freq='D')
```


```python
ts.shift(1, freq='3D')
```


```python
ts.shift(1, freq='90T')
```

* __Shifting dates with offsets__


```python
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()
```


```python
now + MonthEnd()
```


```python
now + MonthEnd(2)
```


```python
offset = MonthEnd()
offset.rollforward(now)
```


```python
offset.rollback(now)
```


```python
ts = Series(np.random.randn(20),
            index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()
```


```python
ts.resample('M', how='mean')
```

## 10.4 Time Zone Handling


```python
import pytz
pytz.common_timezones[-5:]
```


```python
tz = pytz.timezone('US/Eastern')
tz
```

### 10.4.1 Localization and Conversion


```python
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = Series(np.random.randn(len(rng)), index=rng)
```


```python
print(ts.index.tz)
```


```python
pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC')
```


```python
ts_utc = ts.tz_localize('UTC')
ts_utc
```


```python
ts_utc.index
```


```python
ts_utc.tz_convert('US/Eastern')
```


```python
ts_eastern = ts.tz_localize('US/Eastern')
ts_eastern.tz_convert('UTC')
```


```python
ts_eastern.tz_convert('Europe/Berlin')
```


```python
ts.index.tz_localize('Asia/Shanghai')
```

### 10.4.2 Operations with Time Zone−aware Timestamp Objects


```python
stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc = stamp.tz_localize('utc')
stamp_utc.tz_convert('US/Eastern')
```


```python
stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
stamp_moscow
```


```python
stamp_utc.value
```


```python
stamp_utc.tz_convert('US/Eastern').value
```


```python
# 30 minutes before DST transition
from pandas.tseries.offsets import Hour
stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
stamp
```


```python
stamp + Hour()
```


```python
# 90 minutes before DST transition
stamp = pd.Timestamp('2012-11-04 00:30', tz='US/Eastern')
stamp
```


```python
stamp + 2 * Hour()
```

### 10.4.3 Operations between Different Time Zones


```python
rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = Series(np.random.randn(len(rng)), index=rng)
ts
```


```python
ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts1[2:].tz_convert('Europe/Moscow')
result = ts1 + ts2
result.index
```

## 10.5 Periods and Period Arithmetic


```python
p = pd.Period(2007, freq='A-DEC')
p
```


```python
p + 5
```


```python
p - 2
```


```python
pd.Period('2014', freq='A-DEC') - p
```


```python
rng = pd.period_range('1/1/2000', '6/30/2000', freq='M')
rng
```


```python
Series(np.random.randn(6), index=rng)
```


```python
values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
index
```

### 10.5.1 Period Frequency Conversion


```python
p = pd.Period('2007', freq='A-DEC')
p.asfreq('M', how='start')
```


```python
p.asfreq('M', how='end')
```


```python
p = pd.Period('2007', freq='A-JUN')
p.asfreq('M', 'start')
```


```python
p.asfreq('M', 'end')
```


```python
p = pd.Period('Aug-2007', 'M')
p.asfreq('A-JUN')
```


```python
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = Series(np.random.randn(len(rng)), index=rng)
ts
```


```python
ts.asfreq('M', how='start')
```


```python
ts.asfreq('B', how='end')
```

### 10.5.2 Quarterly Period Frequencies


```python
p = pd.Period('2012Q4', freq='Q-JAN')
p
```


```python
p.asfreq('D', 'start')
```


```python
p.asfreq('D', 'end')
```


```python
p4pm = (p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
p4pm
```


```python
p4pm.to_timestamp()
```


```python
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = Series(np.arange(len(rng)), index=rng)
ts
```


```python
new_rng = (rng.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
ts.index = new_rng.to_timestamp()
ts
```

### 10.5.3 Converting Timestamps to Periods (and Back)


```python
rng = pd.date_range('1/1/2000', periods=3, freq='M')
ts = Series(randn(3), index=rng)
pts = ts.to_period()
ts
```


```python
pts
```


```python
rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = Series(randn(6), index=rng)
ts2.to_period('M')
```


```python
pts = ts.to_period()
pts
```


```python
pts.to_timestamp(how='end')
```

### 10.5.4 Creating a PeriodIndex from Arrays


```python
data = pd.read_csv('ch08/macrodata.csv')
data.year
```


```python
data.quarter
```


```python
index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
index
```


```python
data.index = index
data.infl
```

## 10.6 Resampling and Frequency Conversion


```python
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(randn(len(rng)), index=rng)
ts.resample('M', how='mean')
```


```python
ts.resample('M', how='mean', kind='period')
```

### 10.6.1 Downsampling


```python
rng = pd.date_range('1/1/2000', periods=12, freq='T')
ts = Series(np.arange(12), index=rng)
ts
```


```python
ts.resample('5min', how='sum')
# note: output changed (as the default changed from closed='right', label='right' to closed='left', label='left'
```


```python
ts.resample('5min', how='sum', closed='left')
```


```python
ts.resample('5min', how='sum', closed='left', label='left')
```


```python
ts.resample('5min', how='sum', loffset='-1s')
```

* __Open-High-Low-Close (OHLC) resampling__


```python
ts.resample('5min', how='ohlc')
# note: output changed because of changed defaults
```

* __Resampling with GroupBy__


```python
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(np.arange(100), index=rng)
ts.groupby(lambda x: x.month).mean()
```


```python
ts.groupby(lambda x: x.weekday).mean()
```

### 10.6.2 Upsampling and Interpolation


```python
frame = DataFrame(np.random.randn(2, 4),
                  index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                  columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame
```


```python
df_daily = frame.resample('D')
df_daily
```


```python
frame.resample('D', fill_method='ffill')
```


```python
frame.resample('D', fill_method='ffill', limit=2)
```


```python
frame.resample('W-THU', fill_method='ffill')
```

### 10.6.3 Resampling with Periods


```python
frame = DataFrame(np.random.randn(24, 4),
                  index=pd.period_range('1-2000', '12-2001', freq='M'),
                  columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame[:5]
```


```python
annual_frame = frame.resample('A-DEC', how='mean')
annual_frame
```


```python
# Q-DEC: Quarterly, year ending in December
annual_frame.resample('Q-DEC', fill_method='ffill')
# note: output changed, default value changed from convention='end' to convention='start' + 'start' changed to span-like
# also the following cells
```


```python
annual_frame.resample('Q-DEC', fill_method='ffill', convention='start')
```


```python
annual_frame.resample('Q-MAR', fill_method='ffill')
```

## 10.7 Time Series Plotting


```python
close_px_all = pd.read_csv('ch09/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B', fill_method='ffill')
close_px.info()
```


```python
close_px['AAPL'].plot()
```


```python
close_px.ix['2009'].plot()
```


```python
close_px['AAPL'].ix['01-2011':'03-2011'].plot()
```


```python
appl_q = close_px['AAPL'].resample('Q-DEC', fill_method='ffill')
appl_q.ix['2009':].plot()
```

## 10.8 Moving Window Functions


```python
close_px = close_px.asfreq('B').fillna(method='ffill')
```


```python
close_px.AAPL.plot()
pd.rolling_mean(close_px.AAPL, 250).plot()
```


```python
plt.figure()
```


```python
appl_std250 = pd.rolling_std(close_px.AAPL, 250, min_periods=10)
appl_std250[5:12]
```


```python
appl_std250.plot()
```


```python
# Define expanding mean in terms of rolling_mean
expanding_mean = lambda x: rolling_mean(x, len(x), min_periods=1)
```


```python
pd.rolling_mean(close_px, 60).plot(logy=True)
```


```python
plt.close('all')
```

### 10.8.1 Exponentially-weighted functions


```python
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True,
                         figsize=(12, 7))

aapl_px = close_px.AAPL['2005':'2009']

ma60 = pd.rolling_mean(aapl_px, 60, min_periods=50)
ewma60 = pd.ewma(aapl_px, span=60)

aapl_px.plot(style='k-', ax=axes[0])
ma60.plot(style='k--', ax=axes[0])
aapl_px.plot(style='k-', ax=axes[1])
ewma60.plot(style='k--', ax=axes[1])
axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially-weighted MA')
```

### 10.8.2 Binary Moving Window Functions


```python
close_px
spx_px = close_px_all['SPX']
```


```python
spx_rets = spx_px / spx_px.shift(1) - 1
returns = close_px.pct_change()
corr = pd.rolling_corr(returns.AAPL, spx_rets, 125, min_periods=100)
corr.plot()
```


```python
corr = pd.rolling_corr(returns, spx_rets, 125, min_periods=100)
corr.plot()
```

### 10.8.3 User-Defined Moving Window Functions


```python
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = pd.rolling_apply(returns.AAPL, 250, score_at_2percent)
result.plot()
```

## 10.9 Performance and Memory Usage Notes 


```python
rng = pd.date_range('1/1/2000', periods=10000000, freq='10ms')
ts = Series(np.random.randn(len(rng)), index=rng)
ts
```


```python
ts.resample('15min', how='ohlc').info()
```


```python
%timeit ts.resample('15min', how='ohlc')
```


```python
rng = pd.date_range('1/1/2000', periods=10000000, freq='1s')
ts = Series(np.random.randn(len(rng)), index=rng)
%timeit ts.resample('15s', how='ohlc')
```
