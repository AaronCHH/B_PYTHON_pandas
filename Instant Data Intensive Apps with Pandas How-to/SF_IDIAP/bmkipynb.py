# coding: utf-8

import os, sys
import nbformat
import nbformat as nbf
nb = nbf.v4.new_notebook()

nameList = sys.argv[1]

with open(nameList, 'r') as f:
    for line in f:
        line = line.strip()
#         print(line)
        fname = line
        with open(fname + '.ipynb', 'w') as f:
            nbf.write(nb, f)