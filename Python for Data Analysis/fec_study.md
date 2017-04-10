
# Example: 2012 Federal Election Commission Database


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
%cd book_scripts/fec
```

    /home/phillip/Documents/code/py/pandas-book/rev_539000/book_scripts/fec
    


```python
fec = read_csv('P00000001-ALL.csv')
```


```python
fec
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cmte_id</th>
      <th>cand_id</th>
      <th>cand_nm</th>
      <th>contbr_nm</th>
      <th>contbr_city</th>
      <th>...</th>
      <th>receipt_desc</th>
      <th>memo_cd</th>
      <th>memo_text</th>
      <th>form_tp</th>
      <th>file_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>             HARVEY, WILLIAM</td>
      <td>             MOBILE</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 736166</td>
    </tr>
    <tr>
      <th>1      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>             HARVEY, WILLIAM</td>
      <td>             MOBILE</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 736166</td>
    </tr>
    <tr>
      <th>2      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>               SMITH, LANIER</td>
      <td>             LANETT</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 749073</td>
    </tr>
    <tr>
      <th>3      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>            BLEVINS, DARONDA</td>
      <td>            PIGGOTT</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 749073</td>
    </tr>
    <tr>
      <th>4      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>          WARDENBURG, HAROLD</td>
      <td> HOT SPRINGS NATION</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 736166</td>
    </tr>
    <tr>
      <th>5      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>              BECKMAN, JAMES</td>
      <td>         SPRINGDALE</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 736166</td>
    </tr>
    <tr>
      <th>6      </th>
      <td> C00410118</td>
      <td> P20002978</td>
      <td> Bachmann, Michelle</td>
      <td>            BLEVINS, DARONDA</td>
      <td>            PIGGOTT</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 736166</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1001724</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td> HEFFERNAN, JILL PRINCE MRS.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001725</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>            ELWOOD, MIKE MR.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001726</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>        GORMAN, CHRIS D. MR.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td> REATTRIBUTION / REDESIGNATION REQUESTED (AUTOM...</td>
      <td> NaN</td>
      <td> REATTRIBUTION / REDESIGNATION REQUESTED (AUTOM...</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001727</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>         DUFFY, DAVID A. MR.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001728</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>         GRANE, BRYAN F. MR.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001729</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>          TOLBERT, DARYL MR.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
    <tr>
      <th>1001730</th>
      <td> C00500587</td>
      <td> P20003281</td>
      <td>        Perry, Rick</td>
      <td>      ANDERSON, MARILEE MRS.</td>
      <td>     INFO REQUESTED</td>
      <td>...</td>
      <td>                                               NaN</td>
      <td> NaN</td>
      <td>                                               NaN</td>
      <td> SA17A</td>
      <td> 751678</td>
    </tr>
  </tbody>
</table>
<p>1001731 rows × 16 columns</p>
</div>




```python
fec.ix[123456]
```




    cmte_id            C00431445
    cand_id            P80003338
    cand_nm        Obama, Barack
    contbr_nm        ELLMAN, IRA
    contbr_city            TEMPE
    ...
    contb_receipt_dt    01-DEC-11
    receipt_desc              NaN
    memo_cd                   NaN
    memo_text                 NaN
    form_tp                 SA17A
    file_num               772372
    Name: 123456, Length: 16, dtype: object




```python
unique_cands = fec.cand_nm.unique()
unique_cands
unique_cands[2]
```




    'Obama, Barack'




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

```python
fec.cand_nm[123456:123461]
fec.cand_nm[123456:123461].map(parties)
# Add it as a column
fec['party'] = fec.cand_nm.map(parties)
fec['party'].value_counts()
```




    Democrat      593746
    Republican    407985
    dtype: int64




```python
(fec.contb_receipt_amt > 0).value_counts()
```




    True     991475
    False     10256
    dtype: int64




```python
fec = fec[fec.contb_receipt_amt > 0]
```


```python
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
```
