
# Ch13 Reporting with pandas objects (Medium)


```python
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route('/report/<month>')
def report(month):
    from pandas.io.data import DataReader
    ibm = DataReader('ibm', 'yahoo', '2010-01-01', '2010-12-31')
    df = ibm[ibm.index.month == month]
    return render_template('report.html',
                           df=df.to_html(classes='table'))
if __name__ == '__main__':
    app.run()
```


```python
<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href={{
            url_for('static', filename='css/bootstrap.css') }}>
            <link rel="stylesheet" type="text/css" href={{
            url_for('static', filename='css/style.css') }}>
        </head>
        <body>
            <h1>Month Performance of IBM</h1>
            {{ df|safe }}
        </body>
    </html>
```


```python
body {
    margin: auto;
    width: 960px;
    padding-top: 50px;
}
```
