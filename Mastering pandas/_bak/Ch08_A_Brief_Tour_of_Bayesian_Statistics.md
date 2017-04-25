
# Chapter 8: A Brief Tour of Bayesian Statistics

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Chapter 8: A Brief Tour of Bayesian Statistics](#chapter-8-a-brief-tour-of-bayesian-statistics)
	- [Introduction to Bayesian statistic](#introduction-to-bayesian-statistic)
	- [Mathematical framework for Bayesian statitics](#mathematical-framework-for-bayesian-statitics)
		- [Bayes theory and odds](#bayes-theory-and-odds)
		- [Applications of Bayesian statistics](#applications-of-bayesian-statistics)
	- [Probability distributions](#probability-distributions)
		- [Fitting a distribution](#fitting-a-distribution)
			- [Discrete uniform distribution](#discrete-uniform-distribution)
			- [Continuous probability distributions](#continuous-probability-distributions)
	- [Bayesian statistics versus Frequentist statistics](#bayesian-statistics-versus-frequentist-statistics)
		- [What is probability](#what-is-probability)
		- [How the model is defined](#how-the-model-is-defined)
		- [Confidence (Frequentist) versus Credible (Bayesian) intervals](#confidence-frequentist-versus-credible-bayesian-intervals)
	- [Conducting Bayesian statistical analysis](#conducting-bayesian-statistical-analysis)
	- [Monte Carlo estimation of the likelihood function and PyMC](#monte-carlo-estimation-of-the-likelihood-function-and-pymc)
		- [Bayesian analysis example – Switchpoint detection](#bayesian-analysis-example-switchpoint-detection)
	- [References](#references)
	- [Summary](#summary)

<!-- tocstop -->

## Introduction to Bayesian statistic

> The fild of Bayesian statistics is built on the work of Reverend Thomas Bayes, an 18th century statistician, philosopher, and Presbyterian minister. His famous Bayes'theorem, which forms the theoretical underpinnings for Bayesian statistics, was published posthumously in 1763 as a solution to the problem of inverse probability. For more details on this topic, refer to http://en.wikipedia.org/wiki/Thomas_Bayes.

## Mathematical framework for Bayesian statitics

> This is somewhat intuitive—that the probability of A given B is obtained by dividing the probability of both A and B occurring by the probability that B occurred. The idea is that B is given, so we divide by its probability. A more rigorous treatment of this equation can be found at http://bit.ly/1bCYXRd, which is titled Probability: Joint, Marginal and Conditional Probabilities.

> Then, (H)  is the probability of our hypothesis before we observe the data. This is known as the prior probability. The use of prior probability is often touted as an advantage by Bayesian statisticians since prior knowledge or previous results can be used as input for the current model, resulting in increased accuracy. For more information on this, refer to http://www.bayesian-inference.com/advantagesbayesian.

### Bayes theory and odds
### Applications of Bayesian statistics

> There are many compelling reasons for studying Bayesian statistics; some of them being the use of prior information to better inform the current model. The Bayesian approach works with probability distributions rather than point estimates, thus producing more realistic predictions. Bayesian inference bases a hypothesis on the available data— P(hypothesis|data).  
The Frequentist approach tries to fi the data based on a hypothesis. It can be argued that the Bayesian approach is the more logical and empirical one as it tries to base its belief on the facts rather than the other way round. For more information on this, refer to http://www.bayesian-inference.com/advantagesbayesian.

## Probability distributions


```python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
```

### Fitting a distribution

#### Discrete uniform distribution

* **Discrete probability distributions**  


```python
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
X = range(0,11)
Y = [1/6.0 if x in range(1,7) else 0.0 for x in X]
plt.plot(X,Y,'go-', linewidth = 0, drawstyle = 'steps-pre',
         label = "p(x) = 1/6")
plt.legend(loc = "upper left")
plt.vlines(range(1,7),0,max(Y), linestyle = '-')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.ylim(0,0.5)
plt.xlim(0,10)
plt.title('Discrete uniform probability distribution with p=1/6')
plt.show()    
```


![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_12_0.png)


* **The Bernoulli distribution**


```python
import matplotlib
from scipy.stats import bernoulli

a = np.arange(2)
colors = matplotlib.rcParams['axes.color_cycle']
plt.figure(figsize=(12,8))

for i, p in enumerate([0.0, 0.2, 0.5, 0.75, 1.0]):
    ax = plt.subplot(1, 5, i+1)

    plt.bar(a, bernoulli.pmf(a, p), label=p, color=colors[i],
            alpha=0.5)
    ax.xaxis.set_ticks(a)
    plt.legend(loc=0)

    if i == 0:
        plt.ylabel("PDF at $k$")
        plt.suptitle("Bernoulli probability for various values of $p$")
```

    C:\Anaconda3\lib\site-packages\matplotlib\__init__.py:898: UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle; please use the latter.
      warnings.warn(self.msg_depr % (key, alt_key))



![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_14_1.png)


* **The binomial distribution**


```python
from scipy.stats import binom
clrs = ['blue','green','red','cyan','magenta']
plt.figure(figsize=(12,6))
k = np.arange(0, 22)

for p, color in zip([0.001, 0.1, 0.3, 0.6, 0.999], clrs):
    rv = binom(20, p)

plt.plot(k, rv.pmf(k), lw=2, color=color, label="$p$=" + str(round(p,1)))
plt.legend()
plt.title("Binomial distribution PMF")
plt.tight_layout()
plt.ylabel("PDF at $k$")
plt.xlabel("$k$")
```




    <matplotlib.text.Text at 0xadfb201b00>




![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_16_1.png)


* **The Poisson distribution**


```python
%matplotlib inline

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from scipy.stats import poisson
colors = matplotlib.rcParams['axes.color_cycle']
k=np.arange(15)
plt.figure(figsize=(12,8))

for i, lambda_ in enumerate([1,2,4,6]):
    plt.plot(k, poisson.pmf(k, lambda_), '-o',
    label="$\lambda$=" + str(lambda_), color=colors[i])

plt.legend()
plt.title("Possion distribution PMF for various $\lambda$")
plt.ylabel("PMF at $k$")
plt.xlabel("$k$")
plt.show()
```

    C:\Anaconda3\lib\site-packages\matplotlib\__init__.py:898: UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle; please use the latter.
      warnings.warn(self.msg_depr % (key, alt_key))



![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_18_1.png)


* **The Geometric distribution**

* **The negative binomial distribution**

#### Continuous probability distributions

* **The continuous uniform distribution**

> A memoryless random variable exhibits the property whereby its future state depends only on relevant information about the current time and not the information from further in the past. An example of modeling a Markovian/memoryless random variable is modeling short-term stock price behavior and the idea that it follows a random walk. This leads to what is called the Effiient Market hypothesis in Finance. For more information, refer to http://en.wikipedia.org/wiki/Random_walk_hypothesis.


```python
np.random.seed(100) # seed the random number generator
# so plots are reproducible
subplots = [111,211,311]
ctr = 0
fig, ax = plt.subplots(len(subplots), figsize=(10,12))
nsteps=10

for i in range(0,3):
    cud = np.random.uniform(0,1,nsteps) # generate distrib
    count, bins, ignored = ax[ctr].hist(cud,15,normed=True)
    ax[ctr].plot(bins,np.ones_like(bins),linewidth=2, color='r')
    ax[ctr].set_title('sample size=%s' % nsteps)
    ctr += 1
    nsteps *= 100

fig.subplots_adjust(hspace=0.4)
plt.suptitle("Continuous Uniform probability distributions for various sample sizes" , fontsize=14)
```




    <matplotlib.text.Text at 0xadfb3584e0>




![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_24_1.png)


* **The exponential distribution**


```python
import scipy.stats
# clrs = colors.cnames
clrs = colors
x = np.linspace(0,4, 100)
expo = scipy.stats.expon
lambda_ = [0.5, 1, 2, 5]
plt.figure(figsize=(12,4))
for l,c in zip(lambda_,clrs):
    plt.plot(x, expo.pdf(x, scale=1./l), lw=2,
             color=c, label = "$\lambda = %.1f$"%l)
    plt.legend()
    plt.ylabel("PDF at $x$")
    plt.xlabel("$x$")
    plt.title("Pdf of an Exponential random variable for various $lambda$");
```


![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_26_0.png)


* **The normal distribution**


```python
import matplotlib
from scipy.stats import norm
X = 2.5
dx = 0.1
R = np.arange(-X,X+dx,dx)
L = list()
sdL = (0.5,1,2,3)

for sd in sdL:
    f = norm.pdf
    L.append([f(x,loc=0,scale=sd) for x in R])

colors = matplotlib.rcParams['axes.color_cycle']

for sd,c,P in zip(sdL,colors,L):
    plt.plot(R,P,zorder=1,lw=1.5,color=c,            
             label="$\sigma$=" + str(sd))
    plt.legend()
    ax = plt.axes()
    ax.set_xlim(-2.1,2.1)
    ax.set_ylim(0,1.0)
    plt.title("Normal distribution Pdf")
    plt.ylabel("PDF at $\mu$=0, $\sigma$")
```

    C:\Anaconda3\lib\site-packages\matplotlib\__init__.py:898: UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle; please use the latter.
      warnings.warn(self.msg_depr % (key, alt_key))



![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_28_1.png)


> Reference for the Python code for the plotting of the distributions can be found at:
http://bit.ly/1E17nYx.


```python
# colors.cnames
```


```python
from scipy.stats import binom
from matplotlib import colors
cols = colors.cnames
n_values = [1, 5,10, 30, 100]
subplots = [111+100*x for x in range(0,len(n_values))]
ctr = 0

fig, ax = plt.subplots(len(subplots), figsize=(6,12))
k = np.arange(0, 200)
p = 0.5

for n, color in zip(n_values, cols):
    k=np.arange(0,n+1)
    rv = binom(n, p)
    ax[ctr].plot(k, rv.pmf(k), lw=2, color=color)
    ax[ctr].set_title("$n$=" + str(n))
    ctr += 1
    fig.subplots_adjust(hspace=0.5)
    plt.suptitle("Binomial distribution PMF (p=0.5) for various values of n", fontsize=14)
```


![png](Ch08_A_Brief_Tour_of_Bayesian_Statistics_files/Ch08_A_Brief_Tour_of_Bayesian_Statistics_31_0.png)


## Bayesian statistics versus Frequentist statistics
### What is probability
### How the model is defined
### Confidence (Frequentist) versus Credible (Bayesian) intervals

> For more information, refer to Frequentism and Bayesianism: What's the Big Deal? | SciPy 2014 | Jake VanderPlas at https://www.youtube.com/watch?v=KhAUfqhLakw.

## Conducting Bayesian statistical analysis
## Monte Carlo estimation of the likelihood function and PyMC

> In conducting Bayesian analysis in Python, we will need a module that will enable us to calculate the likelihood function using the Monte Carlo method that was described earlier. The PyMC library fulfils that need. It provides a Monte Carlo method known commonly as **Markov Chain Monte Carlo (MCMC)**. I will not delve further into the technical details of MCMC, but the interested reader can fid out more about MCMC implementation in PyMC at the following references:  

> • Monte Carlo Integration in Bayesian Estimation at http://bit.ly/1bMALeu  
• Markov Chain Monte Carlo Maximum Likelihood at http://bit.ly/1KBP8hH  
• Bayesian Statistical Analysis Using Python-Part 1| SciPy 2014, Chris Fonnesbeck at http://www.youtube.com/watch?v=vOBB_ycQ0RA  

> MCMC is not a universal panacea; there are some drawbacks to the approach, and one of them is the slow convergence of the algorithm.

### Bayesian analysis example – Switchpoint detection


```python
import pandas as pd
filePath = "./DATA/chapter 8/fb_post_dates.txt"

fbdata_df = pd.read_csv(filePath, sep='|',
                        parse_dates=[0],
                        header=None,
                        names=['Date','Time'])
```


```python
fbdata_df.head() #inspect the data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-09-30</td>
      <td>2:43am EDT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-09-30</td>
      <td>2:22am EDT</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-09-30</td>
      <td>2:06am EDT</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014-09-30</td>
      <td>1:07am EDT</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-09-28</td>
      <td>9:16pm EDT</td>
    </tr>
  </tbody>
</table>
</div>




```python
fbdata_df_ind=fbdata_df.set_index('Date')
fbdata_df_ind.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-09-30</th>
      <td>2:43am EDT</td>
    </tr>
    <tr>
      <th>2014-09-30</th>
      <td>2:22am EDT</td>
    </tr>
    <tr>
      <th>2014-09-30</th>
      <td>2:06am EDT</td>
    </tr>
    <tr>
      <th>2014-09-30</th>
      <td>1:07am EDT</td>
    </tr>
    <tr>
      <th>2014-09-28</th>
      <td>9:16pm EDT</td>
    </tr>
  </tbody>
</table>
</div>




```python
fbdata_df_ind.index
```




    DatetimeIndex(['2014-09-30', '2014-09-30', '2014-09-30', '2014-09-30',
                   '2014-09-28', '2014-09-28', '2014-09-28', '2014-09-28',
                   '2014-09-28', '2014-09-28',
                   ...
                   '2007-07-17', '2007-07-17', '2007-07-16', '2007-07-16',
                   '2007-06-26', '2007-06-22', '2007-06-22', '2007-06-22',
                   '2007-06-22', '2007-04-16'],
                  dtype='datetime64[ns]', name='Date', length=7713, freq=None)




```python
fb_mth_count_=fbdata_df_ind.resample('M', how='count')
fb_mth_count_.rename(columns={'Time':'Count'},
                     inplace=True) # Rename
fb_mth_count_.head()
```

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: how in .resample() is deprecated
    the new syntax is .resample(...).count()
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2007-04-30</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2007-05-31</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2007-06-30</th>
      <td>5</td>
    </tr>
    <tr>
      <th>2007-07-31</th>
      <td>50</td>
    </tr>
    <tr>
      <th>2007-08-31</th>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
fb_mth_count_
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2007-04-30</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2007-05-31</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2007-06-30</th>
      <td>5</td>
    </tr>
    <tr>
      <th>2007-07-31</th>
      <td>50</td>
    </tr>
    <tr>
      <th>2007-08-31</th>
      <td>24</td>
    </tr>
    <tr>
      <th>2007-09-30</th>
      <td>115</td>
    </tr>
    <tr>
      <th>2007-10-31</th>
      <td>39</td>
    </tr>
    <tr>
      <th>2007-11-30</th>
      <td>45</td>
    </tr>
    <tr>
      <th>2007-12-31</th>
      <td>91</td>
    </tr>
    <tr>
      <th>2008-01-31</th>
      <td>58</td>
    </tr>
    <tr>
      <th>2008-02-29</th>
      <td>21</td>
    </tr>
    <tr>
      <th>2008-03-31</th>
      <td>20</td>
    </tr>
    <tr>
      <th>2008-04-30</th>
      <td>30</td>
    </tr>
    <tr>
      <th>2008-05-31</th>
      <td>36</td>
    </tr>
    <tr>
      <th>2008-06-30</th>
      <td>67</td>
    </tr>
    <tr>
      <th>2008-07-31</th>
      <td>52</td>
    </tr>
    <tr>
      <th>2008-08-31</th>
      <td>31</td>
    </tr>
    <tr>
      <th>2008-09-30</th>
      <td>40</td>
    </tr>
    <tr>
      <th>2008-10-31</th>
      <td>38</td>
    </tr>
    <tr>
      <th>2008-11-30</th>
      <td>33</td>
    </tr>
    <tr>
      <th>2008-12-31</th>
      <td>54</td>
    </tr>
    <tr>
      <th>2009-01-31</th>
      <td>142</td>
    </tr>
    <tr>
      <th>2009-02-28</th>
      <td>72</td>
    </tr>
    <tr>
      <th>2009-03-31</th>
      <td>51</td>
    </tr>
    <tr>
      <th>2009-04-30</th>
      <td>52</td>
    </tr>
    <tr>
      <th>2009-05-31</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2009-06-30</th>
      <td>115</td>
    </tr>
    <tr>
      <th>2009-07-31</th>
      <td>72</td>
    </tr>
    <tr>
      <th>2009-08-31</th>
      <td>65</td>
    </tr>
    <tr>
      <th>2009-09-30</th>
      <td>77</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2012-04-30</th>
      <td>46</td>
    </tr>
    <tr>
      <th>2012-05-31</th>
      <td>136</td>
    </tr>
    <tr>
      <th>2012-06-30</th>
      <td>256</td>
    </tr>
    <tr>
      <th>2012-07-31</th>
      <td>99</td>
    </tr>
    <tr>
      <th>2012-08-31</th>
      <td>110</td>
    </tr>
    <tr>
      <th>2012-09-30</th>
      <td>141</td>
    </tr>
    <tr>
      <th>2012-10-31</th>
      <td>48</td>
    </tr>
    <tr>
      <th>2012-11-30</th>
      <td>138</td>
    </tr>
    <tr>
      <th>2012-12-31</th>
      <td>78</td>
    </tr>
    <tr>
      <th>2013-01-31</th>
      <td>190</td>
    </tr>
    <tr>
      <th>2013-02-28</th>
      <td>84</td>
    </tr>
    <tr>
      <th>2013-03-31</th>
      <td>118</td>
    </tr>
    <tr>
      <th>2013-04-30</th>
      <td>88</td>
    </tr>
    <tr>
      <th>2013-05-31</th>
      <td>95</td>
    </tr>
    <tr>
      <th>2013-06-30</th>
      <td>184</td>
    </tr>
    <tr>
      <th>2013-07-31</th>
      <td>87</td>
    </tr>
    <tr>
      <th>2013-08-31</th>
      <td>82</td>
    </tr>
    <tr>
      <th>2013-09-30</th>
      <td>101</td>
    </tr>
    <tr>
      <th>2013-10-31</th>
      <td>87</td>
    </tr>
    <tr>
      <th>2013-11-30</th>
      <td>50</td>
    </tr>
    <tr>
      <th>2013-12-31</th>
      <td>68</td>
    </tr>
    <tr>
      <th>2014-01-31</th>
      <td>62</td>
    </tr>
    <tr>
      <th>2014-02-28</th>
      <td>36</td>
    </tr>
    <tr>
      <th>2014-03-31</th>
      <td>41</td>
    </tr>
    <tr>
      <th>2014-04-30</th>
      <td>40</td>
    </tr>
    <tr>
      <th>2014-05-31</th>
      <td>79</td>
    </tr>
    <tr>
      <th>2014-06-30</th>
      <td>242</td>
    </tr>
    <tr>
      <th>2014-07-31</th>
      <td>165</td>
    </tr>
    <tr>
      <th>2014-08-31</th>
      <td>54</td>
    </tr>
    <tr>
      <th>2014-09-30</th>
      <td>72</td>
    </tr>
  </tbody>
</table>
<p>90 rows × 1 columns</p>
</div>




```python
%matplotlib inline
import datetime as dt
#Obtain the count data from the DataFrame as a dictionary

year_month_count = fb_bymth_count.to_dict()['Count']
size = len(year_month_count.keys())

#get dates as list of strings
xdates = [dt.datetime.strptime(str(yyyymm),'%Y%m') for yyyymm in year_month_count.keys()]
counts=year_month_count.values()
plt.scatter(xdates,counts,s=counts)
plt.xlabel('Year')
plt.ylabel('Number of Facebook posts')
plt.show()
```

> We can make use of the Poisson distribution to model this. You might recall that the Poisson distribution can be used to model time series count data. (Refer to http://bit.ly/1JniIqy for more about this.)


```python
fb_activity_data = [year_month_count[k] for k in
                    sorted(year_month_count.keys())]
fb_activity_data[:5]
```


```python
fb_post_count=len(fb_activity_data)
```


```python
from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt
figsize(8, 5)
plt.bar(np.arange(fb_post_count),
        fb_activity_data, color="#49a178")
plt.xlabel("Time (months)")
plt.ylabel("Number of FB posts")
plt.title("Monthly Facebook posts over time")
plt.xlim(0,fb_post_count);
```


```python
# Define data and stochastics
import pymc as pm
switchpoint = pm.DiscreteUniform('switchpoint',
                                 lower=0,
                                 upper=len(fb_activity_data)-1,
                                 doc='Switchpoint[month]')

avg = np.mean(fb_activity_data)
early_mean = pm.Exponential('early_mean', beta=1./avg)
late_mean = pm.Exponential('late_mean', beta=1./avg)
late_mean
```


```python
@pm.deterministic(plot=False)

def rate(s=switchpoint, e=early_mean, l=late_mean):
    ''' Concatenate Poisson means '''
    out = np.zeros(len(fb_activity_data))
    out[:s] = e
    out[s:] = l
    return out

fb_activity = pm.Poisson('fb_activity', mu=rate,
                         value=fb_activity_data, observed=True)
fb_activity
```

> For more information, refer to the following web pages:  
• http://en.wikipedia.org/wiki/Poisson_process  
• http://pymc-devs.github.io/pymc/tutorial.html  
• https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers  


```python
fb_activity_model=pm.Model([fb_activity,early_mean,
                            late_mean,rate])
```


```python
from pymc import MCMC
fbM = MCMC(fb_activity_model)
fbM.sample(iter=40000, burn=1000, thin=20)
```


```python
from pylab import hist,show
%matplotlib inline
hist(fbM.trace('late_mean')[:])
```


```python
plt.hist(fbM.trace('early_mean')[:])
```


```python
fbM.trace('switchpoint')[:]
```


```python
plt.hist(fbM.trace('switchpoint')[:])
```

> We can see that the Switchpoint is in the neighborhood of the months numbering 35-38. Here, we use matplotlib to display the marginal posterior distributions of e, s, and l in a single fiure:


```python
early_mean_samples=fbM.trace('early_mean')[:]
late_mean_samples=fbM.trace('late_mean')[:]
switchpoint_samples=fbM.trace('switchpoint')[:]
```


```python
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
figsize(12.5, 10)
# histogram of the samples:
fig = plt.figure()
fig.subplots_adjust(bottom=-0.05)
n_mths=len(fb_activity_data)
ax = plt.subplot(311)
ax.set_autoscaley_on(False)

plt.hist(early_mean_samples, histtype='stepfilled',
         bins=30, alpha=0.85, label="posterior of $e$",
         color="turquoise", normed=True)

plt.legend(loc="upper left")
plt.title(r"""Posterior distributions of the variables$e, l, s$""",fontsize=16)
plt.xlim([40, 120])
plt.ylim([0, 0.6])
plt.xlabel("$e$ value",fontsize=14)

ax = plt.subplot(312)
ax.set_autoscaley_on(False)

plt.hist(late_mean_samples, histtype='stepfilled',
         bins=30, alpha=0.85, label="posterior of $l$",
         color="purple", normed=True)

plt.legend(loc="upper left")
plt.xlim([40, 120])
plt.ylim([0, 0.6])
plt.xlabel("$l$ value",fontsize=14)
plt.subplot(313)

w = 1.0 / switchpoint_samples.shape[0] * np.ones_like(switchpoint_samples)

plt.hist(switchpoint_samples, bins=range(0,n_mths), alpha=1,
         label=r"posterior of $s$", color="green",
         weights=w, rwidth=2.)

plt.xlim([20, n_mths - 20])
plt.xlabel(r"$s$ (in days)",fontsize=14)
plt.ylabel("probability")
plt.legend(loc="upper left")
plt.show()
```


```python
from pymc.Matplot import plot
plot(fbM)
Plotting late_mean
Plotting switchpoint
Plotting early_mean
```

## References

> For a more in-depth look at Bayesian statistics topics that we touched upon, please take a look at the following references:   

> • Probabilistic Programming and Bayesian Methods for Hackers at https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers  
• Bayesian Data Analysis, Third Edition, Andrew Gelman at http://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954  
• The Bayesian Choice, Christian P Robert (this is more theoretical) at http://www.springer.com/us/book/9780387952314  
• PyMC documentation at http://pymc-devs.github.io/pymc/index.html  

## Summary


```python

```
