
# Chapter 11: Brief Tour of Machine Learning

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

- [Chapter 11: Brief Tour of Machine Learning](#chapter-11-brief-tour-of-machine-learning)
	- [Role of pandas in machine learning](#role-of-pandas-in-machine-learning)
	- [Installation of scikit-learn](#installation-of-scikit-learn)
		- [Installing via Anaconda](#installing-via-anaconda)
		- [Installing on Unix (Linux/Mac OSX](#installing-on-unix-linuxmac-osx)
		- [Installing on Windows](#installing-on-windows)
	- [Introduction to machine learning](#introduction-to-machine-learning)
		- [Supervised versus unsupervised learning](#supervised-versus-unsupervised-learning)
		- [Illustration using document classification](#illustration-using-document-classification)
			- [Supervised learning](#supervised-learning)
			- [Unsupervised learning](#unsupervised-learning)
		- [How machine learning systems learn](#how-machine-learning-systems-learn)
	- [Application of machine learning – Kaggle Titanic competition](#application-of-machine-learning-kaggle-titanic-competition)
		- [The Titanic: Machine Learning from Disaster problem](#the-titanic-machine-learning-from-disaster-problem)
		- [The problem of overfitting](#the-problem-of-overfitting)
	- [Data analysis and preprocessing using pandas](#data-analysis-and-preprocessing-using-pandas)
		- [Examining the data](#examining-the-data)
		- [Handling missing values](#handling-missing-values)
	- [A naïve approach to Titanic problem](#a-naïve-approach-to-titanic-problem)
	- [The scikit-learn ML/classifier interface](#the-scikit-learn-mlclassifier-interface)
	- [Supervised learning algorithms](#supervised-learning-algorithms)
		- [Constructing a model using Patsy scikit-learn](#constructing-a-model-using-patsy-scikit-learn)
		- [General boilerplate code explanation](#general-boilerplate-code-explanation)
		- [Logistic regression](#logistic-regression)
		- [Support vector machine](#support-vector-machine)
		- [Decision trees](#decision-trees)
		- [Random forest](#random-forest)
	- [Unsupervised learning algorithms](#unsupervised-learning-algorithms)
		- [Dimensionality reduction](#dimensionality-reduction)
		- [K-means clustering](#k-means-clustering)
	- [Summary](#summary)

<!-- tocstop -->

## Role of pandas in machine learning
## Installation of scikit-learn
### Installing via Anaconda
### Installing on Unix (Linux/Mac OSX
### Installing on Windows

```py
pip install –U scikit-learn
```

> For more in-depth information on installation, you can take a look at the offiial scikit-learn docs at: http://scikit-learn.org/stable/install.html.  

> You can also take a look at the README fie for the scikit-learn Git repository at: https://github.com/scikit-learn/scikit-learn/blob/master/README.rst.

## Introduction to machine learning

> A Few Useful Things to Know about Machine Learning at http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf

### Supervised versus unsupervised learning
### Illustration using document classification
#### Supervised learning
#### Unsupervised learning
### How machine learning systems learn
## Application of machine learning – Kaggle Titanic competition

> In order to illustrate how we can use pandas to assist us at the start of our machine learning journey, we will apply it to a classic problem, which is hosted on the Kaggle website (http://www.kaggle.com).   

> Kaggle is a competition platform for machine learning problems. The idea behind Kaggle is to enable companies that are interested in solving predictive analytics problems with their data to post their data on Kaggle and invite data scientists to come up with the proposed solutions to their problems. The competition can be ongoing over a period of time, and the rankings of the competitors are posted on a leader board. At the end of the competition, the top-ranked competitors receive cash prizes.

### The Titanic: Machine Learning from Disaster problem
### The problem of overfitting
## Data analysis and preprocessing using pandas
### Examining the data


```python
import pandas as pd
import numpy as np
# For .read_csv, always use header=0 when you know row 0 is the header row
train_df = pd.read_csv('csv/train.csv', header=0)
```


```python
train_df.head(3)
```

### Handling missing values


```python
missing_perc = train_df.apply(lambda x: 100*(1-x.count().sum()/(1.0*len(x))))
sorted_missing_perc=missing_perc.order(ascending=False)
sorted_missing_perc
```


```python
import matplotlib.pyplot as plt
import random
bar_width=0.1
categories_map={'Pclass':{'First':1,'Second':2,
                          'Third':3},
                'Sex':{'Female':'female','Male':'male'},
                'Survived':{'Perished':0,'Survived':1},
                'Embarked':{'Cherbourg':'C','Queenstown':'Q','Southampton':'S'},
                'SibSp': { str(x):x for x in [0,1,2,3,4,5,8]},
                'Parch': {str(x):x for x in range(7)}
               }

colors=['red','green','blue','yellow','magenta','orange']

subplots=[111,211,311,411,511,611,711,811]

cIdx=0

fig,ax=plt.subplots(len(subplots),figsize=(10,12))

keyorder = ['Survived','Sex','Pclass','Embarked','SibSp','Parch']

for category_key,category_items in sorted(categories_map.iteritems(),key=lambda i:keyorder.index(i[0])):
    num_bars=len(category_items)
    index=np.arange(num_bars)
    idx=0

    for cat_name,cat_val in sorted(category_items.iteritems()):
        ax[cIdx].bar(idx,len(train_df[train_df[category_key]==cat_val]),
                     label=cat_name,
                     color=np.random.rand(3,1))
        idx+=1

    ax[cIdx].set_title('%s Breakdown' % category_key)
    xlabels=sorted(category_items.keys())
    ax[cIdx].set_xticks(index+bar_width)
    ax[cIdx].set_xticklabels(xlabels)
    ax[cIdx].set_ylabel('Count')
    cIdx +=1
    fig.subplots_adjust(hspace=0.8)

for hcat in ['Age','Fare']:
    ax[cIdx].hist(train_df[hcat].dropna(),color=np.random.rand(3,1))
    ax[cIdx].set_title('%s Breakdown' % hcat)
    #ax[cIdx].set_xlabel(hcat)
    ax[cIdx].set_ylabel('Frequency')
    cIdx +=1

    fig.subplots_adjust(hspace=0.8)
plt.show()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-2-86cf1a5b5e6f> in <module>()
         21 keyorder = ['Survived','Sex','Pclass','Embarked','SibSp','Parch']
         22
    ---> 23 for category_key,category_items in sorted(categories_map.iteritems(),key=lambda i:keyorder.index(i[0])):
         24     num_bars=len(category_items)
         25     index=np.arange(num_bars)


    AttributeError: 'dict' object has no attribute 'iteritems'


> These observations might lead us to dig deeper and investigate whether there is some correlation between chances of survival and gender and also fare class, particularly if we take into account the fact that the Titanic had a women-and-children-fist policy (http://en.wikipedia.org/wiki/Women_and_children_first) and the fact that the Titanic was carrying fewer lifeboats (20) than it was designed to (32).


```python
from collections import OrderedDict
num_passengers=len(train_df)
num_men=len(train_df[train_df['Sex']=='male'])
men_survived=train_df[(train_df['Survived']==1 ) & (train_df['Sex']=='male')]
num_men_survived=len(men_survived)
num_men_perished=num_men-num_men_survived
num_women=num_passengers-num_men
women_survived=train_df[(train_df['Survived']==1) & (train_df['Sex']=='female')]
num_women_survived=len(women_survived)
num_women_perished=num_women-num_women_survived
gender_survival_dict=OrderedDict()
gender_survival_dict['Survived']={'Men':num_men_survived,'Women':num_women_survived}
gender_survival_dict['Perished']={'Men':num_men_perished,'Women':num_women_perished}
gender_survival_dict['Survival Rate'] = {'Men' : round(100.0*num_men_survived/num_men,2),
                                         'Women':round(100.0*num_women_survived/num_women,2)}
pd.DataFrame(gender_survival_dict)
```


```python

```


```python
#code to display survival by gender
fig = plt.figure()
ax = fig.add_subplot(111)
perished_data=[num_men_perished, num_women_perished]
survived_data=[num_men_survived, num_women_survived]
N=2
ind = np.arange(N) # the x locations for the groups
width = 0.35
survived_rects = ax.barh(ind, survived_data,
                         width,color='green')
perished_rects = ax.barh(ind+width, perished_data,
                         width,color='red')
ax.set_xlabel('Count')
ax.set_title('Count of Survival by Gender')
yTickMarks = ['Men','Women']
ax.set_yticks(ind+width)
ytickNames = ax.set_yticklabels(yTickMarks)

plt.setp(ytickNames, rotation=45, fontsize=10)

## add a legend
ax.legend((survived_rects[0], perished_rects[0]), ('Survived', 'Perished'))
plt.show()
```

* In[86]


```python
from collections import OrderedDict
num_passengers=len(train_df)
num_class1=len(train_df[train_df['Pclass']==1])
class1_survived=train_df[(train_df['Survived']==1 ) & (train_df['Pclass']==1)]
num_class1_survived=len(class1_survived)
num_class1_perished=num_class1-num_class1_survived
num_class2=len(train_df[train_df['Pclass']==2])
class2_survived=train_df[(train_df['Survived']==1) & (train_df['Pclass']==2)]
num_class2_survived=len(class2_survived)
num_class2_perished=num_class2-num_class2_survived
num_class3=num_passengers-num_class1-num_class2
class3_survived=train_df[(train_df['Survived']==1 ) & (train_df['Pclass']==3)]
num_class3_survived=len(class3_survived)
num_class3_perished=num_class3-num_class3_survived
pclass_survival_dict=OrderedDict()

pclass_survival_dict['Survived']={'1st Class':num_class1_survived,
                                  '2nd Class':num_class2_survived,
                                  '3rd Class':num_class3_survived}

pclass_survival_dict['Perished']={'1st Class':num_class1_perished,
                                  '2nd Class':num_class2_perished,
                                  '3rd Class':num_class3_perished}

pclass_survival_dict['Survival Rate']= {'1st Class' : round(100.0*num_class1_survived/num_class1,2),
                                        '2nd Class':round(100.0*num_class2_survived/num_class2,2),
                                        '3rd Class':round(100.0*num_class3_survived/num_class3,2),}

pd.DataFrame(pclass_survival_dict)
```

## A naïve approach to Titanic problem


```python
fig = plt.figure()
ax = fig.add_subplot(111)
perished_data=[num_class1_perished, num_class2_perished, num_class3_perished]
survived_data=[num_class1_survived, num_class2_survived, num_class3_survived]
N=3
ind = np.arange(N) # the x locations for the groups
width = 0.35
survived_rects = ax.barh(ind, survived_data, width,color='blue')
perished_rects = ax.barh(ind+width, perished_data, width,color='red')
ax.set_xlabel('Count')
ax.set_title('Survivor Count by Passenger class')
yTickMarks = ['1st Class','2nd Class', '3rd Class']
ax.set_yticks(ind+width)
ytickNames = ax.set_yticklabels(yTickMarks)
plt.setp(ytickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (survived_rects[0], perished_rects[0]), ('Survived','Perished'), loc=10 )
plt.show()
```

 * **In[173]**


```python
survival_counts=pd.crosstab([train_df.Pclass,train_df.Sex],train_df.Survived.astype(bool))
survival_counts
```

 * **In[183]**


```python
survival_counts.index=survival_counts.index.set_levels([['1st','2nd', '3rd'], ['Women', 'Men']])
survival_counts.columns=['Perished','Survived']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Count')
ax.set_title('Survivor Count by Passenger class, Gender')
survival_counts.plot(kind='barh',ax=ax,width=0.75, color=['red','black'], xlim=(0,400))
```

* **In [192]**


```python
test_df.head(3)[['PassengerId','Pclass','Sex','Fare']]
```

## The scikit-learn ML/classifier interface


```python
from sklearn.linear_model import LinearRegression
model = LinearRegression(normalize=True)
print(model)
LinearRegression(copy_X=True, fit_intercept=True, normalize=True)
```


```python
sample_size=500
x = []
y = []
for i in range(sample_size):
    newVal = random.normalvariate(100,10)   
    x.append(newVal)
    y.append(newVal / 2.0 + random.normalvariate(50,5))
```


```python
X = np.array(x)[:,np.newaxis]
X.shape
```


```python
model.fit(X,y)
print "coeff=%s, intercept=%s" % (model.coef_,model.intercept_)
coeff=[ 0.47071289], intercept=52.7456611783

plt.title("Plot of linear regression line and training data")
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(X,y,marker='o', color='green', label='training data');
plt.plot(X,model.predict(X), color='red', label='regression line')
plt.legend(loc=2)
```

> For extra reference, please see the following: http://bit.ly/1FU7mXj and http://bit.ly/1QqFN2V.

## Supervised learning algorithms


```python

```

### Constructing a model using Patsy scikit-learn


```python
import patsy as pts
pts.dmatrices("y ~ x + a + b + a:b", data)
```

> For further reference, look at: http://patsy.readthedocs.org/en/latest/overview.html

### General boilerplate code explanation


```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import patsy as pt
```


```python
train_df = pd.read_csv('csv/train.csv', header=0)
test_df = pd.read_csv('csv/test.csv', header=0)
```


```python
formula1 = 'C(Pclass) + C(Sex) + Fare'
formula2 = 'C(Pclass) + C(Sex)'
formula3 = 'C(Sex)'
formula4 = 'C(Pclass) + C(Sex) + Age + SibSp + Parch'
formula5 = 'C(Pclass) + C(Sex) + Age + SibSp + Parch + C(Embarked)'
formula6 = 'C(Pclass) + C(Sex) + Age + SibSp + C(Embarked)'
formula7 = 'C(Pclass) + C(Sex) + SibSp + Parch + C(Embarked)'
formula8 = 'C(Pclass) + C(Sex) + SibSp + Parch + C(Embarked)'
```


```python
formula_map = {'PClass_Sex_Fare' : formula1,
               'PClass_Sex' : formula2,
               'Sex' : formula3,
               'PClass_Sex_Age_Sibsp_Parch' : formula4,
               'PClass_Sex_Age_Sibsp_Parch_Embarked' : formula5,
               'PClass_Sex_Embarked' : formula6,
               'PClass_Sex_Age_Parch_Embarked' : formula7,
               'PClass_Sex_SibSp_Parch_Embarked' : formula8
              }
```


```python
def fill_null_vals(df,col_name):
    null_passengers=df[df[col_name].isnull()]
    passenger_id_list = null_passengers['PassengerId'].tolist()
    df_filled=df.copy()

    for pass_id in passenger_id_list:
        idx=df[df['PassengerId'] == pass_id].index[0]
        similar_passengers = df[(df['Sex'] == null_passengers['Sex'][idx]) &
                                (df['Pclass'] == null_passengers['Pclass'][idx])]
        mean_val = np.mean(similar_passengers[col_name].dropna())
        df_filled.loc[idx,col_name]=mean_val

    return df_filled
```


```python
train_df_filled=fill_null_vals(train_df,'Fare')
train_df_filled=fill_null_vals(train_df_filled,'Age')
assert len(train_df_filled) == len(train_df)
test_df_filled=fill_null_vals(test_df,'Fare')
test_df_filled=fill_null_vals(test_df_filled,'Age')
assert len(test_df_filled) == len(test_df)
```


```python
from sklearn import metrics,svm, tree
for formula_name, formula in formula_map.iteritems():
    print "name=%s formula=%s" % (formula_name,formula)
    y_train,X_train = pt.dmatrices('Survived ~ ' + formula,
                                   train_df_filled,return_type='dataframe')
    y_train = np.ravel(y_train)
    model = tree.DecisionTreeClassifier(criterion='entropy',
                                        max_depth=3,min_samples_leaf=5)
    print "About to fit..."

    dt_model = model.fit(X_train, y_train)

    print "Training score:%s" % dt_model.score(X_train,y_train)

    X_test=pt.dmatrix(formula,test_df_filled)
    predicted=dt_model.predict(X_test)

    print "predicted:%s" % predicted[:5]

    assert len(predicted)==len(test_df)
    pred_results = pd.Series(predicted,name='Survived')

    dt_results = pd.concat([test_df['PassengerId'],
                            pred_results],axis=1)
    dt_results.Survived = dt_results.Survived.astype(int)

    results_file = 'csv/dt_%s_1.csv' % (formula_name)

    print "output file: %s\n" % results_file

    dt_results.to_csv(results_file,index=False)
```

### Logistic regression

> A more detailed examination of the logistic regression may be found here at: http://en.wikipedia.org/wiki/Logit and http://logisticregressionanalysis.com/86-what-is-logistic-regression.

### Support vector machine

> For more information on this, refer to http://winfwiki.wi-fom.de/images/c/cf/Support_vector_2.png.

```py
from sklearn import svm
# We then instantiate an SVM classifir, fi the model, and predict the following:
model = svm.SVC(kernel=kernel)
svm_model = model.fit(X_train, y_train)
X_test = pt.dmatrix(formula, test_df_filled)
...
```


```python

```

### Decision trees

> Refer to the following link for more information:
http://bit.ly/1C0cM2e.

```py
from sklearn import tree
model = tree.DecisionTreeClassifier(criterion='entropy',
                                    max_depth=3,min_samples_leaf=5)
dt_model = model.fit(X_train, y_train)
X_test = dt.dmatrix(formula, test_df_filled)
#. . .
```

### Random forest

```py
from sklearn import RandomForestClassifier
model = RandomForestClassifier(n_estimators=num_estimators,
                               random_state=0)
rf_model = model.fit(X_train, y_train)
X_test = dt.dmatrix(formula, test_df_filled)
. . .
```

## Unsupervised learning algorithms


```python

```

### Dimensionality reduction


```python
from sklearn.datasets import load_iris
iris = load_iris()
```


```python
iris_data = iris
```


```python
iris_data.keys()
```




    dict_keys(['feature_names', 'target', 'data', 'target_names', 'DESCR'])




```python
iris_data.data.shape
```




    (150, 4)




```python
print(iris_data.feature_names)
```

    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']



```python
print(iris_data.data[:2])
```

    [[ 5.1  3.5  1.4  0.2]
     [ 4.9  3.   1.4  0.2]]



```python
print(iris_data.target_names)
```


```python
X, y = iris_data.data, iris_data.target
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
X_red=pca.transform(X)
print("Shape of reduced dataset:%s" % str(X_red.shape))
```


```python
figsize(8,6)
fig=plt.figure()
fig.suptitle("Dimensionality reduction on iris data")
ax=fig.add_subplot(1,1,1)
colors=['red','yellow','magenta']
cols=[colors[i] for i in iris_data.target]
ax.scatter(X_red[:,0],X[:,1],c=cols)
```


```python
print("Dimension Composition:")
idx=1
for comp in pca.components_:
    print("Dim %s" % idx)
    print(" + ".join("%.2f x %s" % (value, name)
                     for value, name in zip(comp, iris_data.feature_names)))
    idx += 1
```

### K-means clustering


```python
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(X_red)
y_pred = k_means.predict(X_red)
```


```python
figsize(8,6)
fig=plt.figure()
fig.suptitle("K-Means clustering on PCA-reduced iris data,K=3")
ax=fig.add_subplot(1,1,1)
ax.scatter(X_red[:, 0], X_red[:, 1], c=y_pred);
```

> Note that our K-means algorithm clusters do not exactly correspond to the dimensions obtained via PCA. The source code is available at https://github.com/jakevdp/sklearn_pycon2014.

> More information on K-means clustering in scikit-learn and, in general, can be found here at: http://scikit-learn.org/stable/auto_examples/cluster/ plot_cluster_iris.html and http://en.wikipedia.org/wiki/K-means_clustering.

## Summary


```python

```
