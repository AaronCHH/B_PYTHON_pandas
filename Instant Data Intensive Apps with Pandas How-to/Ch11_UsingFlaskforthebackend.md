
# Ch11 Using Flask for the backend (Advanced)


```python
#app.py
from flask import Flask, render_template
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route('/report')

def report():
    df = pd.DataFrame(np.random.randn(10,10))
    return render_template('report.html', df=df.to_html())

if __name__ == '__main__':
app.run()
```


```python
#templates/report.html
<!DOCTYPE html>
    <html>
        <body>
        <h1>My Great Report</h1>
        #This is the only fancy part… we're clearing the html
        #from the to_html() method
        {{ df|safe }}
    </body>
</html>
```


```python
<link rel="stylesheet" type="text/css" href={{
url_for('static', filename='css/bootstrap.css') }}>
```
