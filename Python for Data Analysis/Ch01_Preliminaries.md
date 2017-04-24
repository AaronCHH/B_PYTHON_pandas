
# Chapter 1. Preliminaries
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 1. Preliminaries](#chapter-1-preliminaries)
  * [1.1 What Is This Book About](#11-what-is-this-book-about)
  * [1.2 Why Python for Data Analysis?](#12-why-python-for-data-analysis)
    * [1.2.1 Python as Glue](#121-python-as-glue)
    * [1.2.2 Solving the "Two-Language" Problem](#122-solving-the-two-language-problem)
    * [1.2.3 Why Not Python](#123-why-not-python)
  * [1.3 Essential Python Libraries](#13-essential-python-libraries)
    * [1.3.1 NumPy](#131-numpy)
    * [1.3.2 pandas](#132-pandas)
    * [1.3.3 matplotlib](#133-matplotlib)
    * [1.3.4 IPython](#134-ipython)
    * [1.3.5 SciPy](#135-scipy)
  * [1.4 Installation and Setup](#14-installation-and-setup)
    * [1.4.1 Windows](#141-windows)
    * [1.4.2 Apple OS X](#142-apple-os-x)
    * [1.4.3 GNU/Linux](#143-gnulinux)
    * [1.4.4 Python 2 and Python 3](#144-python-2-and-python-3)
    * [1.4.5 Integrated Development Environments (IDEs)](#145-integrated-development-environments-ides)
  * [1.5 Community and Conferences](#15-community-and-conferences)
  * [1.6 Navigating This Book](#16-navigating-this-book)
    * [1.6.1 Code Examples](#161-code-examples)
    * [1.6.2 Data for Examples](#162-data-for-examples)
    * [1.6.3 Import Conventions](#163-import-conventions)
    * [1.6.4 Jargon](#164-jargon)
  * [1.7 Acknowledgements](#17-acknowledgements)

<!-- tocstop -->


## 1.1 What Is This Book About
## 1.2 Why Python for Data Analysis?
### 1.2.1 Python as Glue

Part of Python’s success as a scientific computing platform is the ease of integrating C, C++, and FORTRAN code.
Most modern computing environments share a similar set of legacy FORTRAN and C libraries for doing linear algebra, optimization, integration, fast fourier transforms, and other such algorithms.
The same story has held true for many companies and national labs that have used Python to glue together 30 years’ worth of legacy software.

Most programs consist of small portions of code where most of the time is spent, with large amounts of “glue code” that doesn’t run often.
In many cases, the execution time of the glue code is insignificant; effort is most fruitfully invested in optimizing the computational bottlenecks, sometimes by moving the code to a lower-level language like C.

In the last few years, the Cython project (http://cython.org) has become one of the preferred ways of both creating fast compiled extensions for Python and also interfacing with C and C++ code.


### 1.2.2 Solving the "Two-Language" Problem
### 1.2.3 Why Not Python
## 1.3 Essential Python Libraries
### 1.3.1 NumPy
### 1.3.2 pandas
### 1.3.3 matplotlib
### 1.3.4 IPython
### 1.3.5 SciPy

## 1.4 Installation and Setup

Since everyone uses Python for different applications, there is no single solution for setting up Python and required add-on packages.
Many readers will not have a complete scientific Python environment suitable for following along with this book, so here I will give detailed instructions to get set up on each operating system.
I recommend using one of the following base Python distributions:

* Enthought Python Distribution: a scientific-oriented Python distribution from En thought (http://www.enthought.com).
This includes EPDFree, a free base scientific distribution (with NumPy, SciPy, matplotlib, Chaco, and IPython) and EPD Full, a comprehensive suite of more than 100 scientific packages across many domains.
EPD Full is free for academic use but has an annual subscription for non-academic users.
* Python(x,y) (http://python-xy.github.io/): A free scientific-oriented Python distribution for Windows.
I will be using EPDFree for the installation guides, though you are welcome to take another approach depending on your needs.
At the time of this writing, EPD includes Python 2.7, though this might change at some point in the future.
After installing, you will have the following packages installed and importable:
* Scientific Python base: NumPy, SciPy, matplotlib, and IPython.
These are all in cluded in EPDFree.
* IPython Notebook dependencies: tornado and pyzmq.
These are included in EPD Free.
* pandas (version 0.8.2 or higher).

At some point while reading you may wish to install one or more of the following packages: statsmodels, PyTables, PyQt (or equivalently, PySide), xlrd, lxml, basemap, pymongo, and requests.
These are used in various examples.
Installing these optional libraries is not necessary, and I would would suggest waiting until you need them.
For example, installing PyQt or PyTables from source on OS X or Linux can be rather arduous.
For now, it’s most important to get up and running with the bare minimum: EPDFree and pandas.

For information on each Python package and links to binary installers or other help, see the Python Package Index (PyPI, http://pypi.python.org).
This is also an excellent resource for finding new Python packages.


### 1.4.1 Windows

To get started on Windows, download the EPDFree installer from http://www.enthought.com, which should be an MSI installer named like epd_free-7.3-1-win- x86.msi.
Run the installer and accept the default installation location C:\Python27.
If you had previously installed Python in this location, you may want to delete it manually first (or using Add/Remove Programs).

Next, you need to verify that Python has been successfully added to the system path and that there are no conflicts with any prior-installed Python versions.
First, open a command prompt by going to the Start Menu and starting the Command Prompt ap- plication, also known as cmd.exe.
Try starting the Python interpreter by typing python.
You should see a message that matches the version of EPDFree you installed:
```py
C:\Users\Wes>python
Python 2.7.3 |EPD_free 7.3-1 (32-bit)| (default, Apr 12 2012, 14:30:37) on win32 Type "credits", "demo" or "enthought" for more information.
>>>
```

If you see a message for a different version of EPD or it doesn’t work at all, you will need to clean up your Windows environment variables.
On Windows 7 you can start typing “environment variables” in the programs search field and select Edit environ ment variables for your account.
On Windows XP, you will have to go to Control Panel > System > Advanced > Environment Variables.
On the window that pops up, you are looking for the Path variable.
It needs to contain the following two directory paths, separated by semicolons:
```py
C:\Python27;C:\Python27\Scripts
```

If you installed other versions of Python, be sure to delete any other Python-related directories from both the system and user Path variables.
After making a path alterna- tion, you have to restart the command prompt for the changes to take effect.

Once you can launch Python successfully from the command prompt, you need to install pandas.
The easiest way is to download the appropriate binary installer from http://pypi.python.org/pypi/pandas.
For EPDFree, this should be pandas-0.9.0.win32- py2.7.exe.
After you run this, let’s launch IPython and check that things are installed correctly by importing pandas and making a simple matplotlib plot:
```py
C:\Users\Wes>ipython --pylab
Python 2.7.3 |EPD_free 7.3-1 (32-bit)|
Type "copyright", "credits" or "license" for more information.

IPython 0.12.1 -- An enhanced Interactive Python.
? -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help  -> Python's own help system.
object? -> Details about 'object', use 'object??' for extra details.

Welcome to pylab, a matplotlib-based Python environment [backend: WXAgg]. For more information, type 'help(pylab)'.

In [1]: import pandas

In [2]: plot(arange(10))
```

If successful, there should be no error messages and a plot window will appear.
You can also check that the IPython HTML notebook can be successfully run by typing:
```
$ ipython notebook --pylab=inline
```

If you use the IPython notebook application on Windows and normally use Internet Explorer, you will likely need to install and run Mozilla Firefox or Google Chrome instead.

EPDFree on Windows contains only 32-bit executables.
If you want or need a 64-bit setup on Windows, using EPD Full is the most painless way to accomplish that.
If you would rather install from scratch and not pay for an EPD subscription, Christoph Gohlke at the University of California, Irvine, publishes unofficial binary installers for all of the book’s necessary packages (http://www.lfd.uci.edu/~gohlke/pythonlibs/) for 32- and 64-bit Windows.


### 1.4.2 Apple OS X
### 1.4.3 GNU/Linux
### 1.4.4 Python 2 and Python 3
### 1.4.5 Integrated Development Environments (IDEs)

## 1.5 Community and Conferences

## 1.6 Navigating This Book

### 1.6.1 Code Examples
### 1.6.2 Data for Examples

Data sets for the examples in each chapter are hosted in a repository on GitHub: http://github.com/pydata/pydata-book.
You can download this data either by using the git revision control command-line program or by downloading a zip file of the repository from the website.

I have made every effort to ensure that it contains everything necessary to reproduce the examples, but I may have made some mistakes or omissions.
If so, please send me an e-mail: wesmckinn@gmail.com.


### 1.6.3 Import Conventions

The Python community has adopted a number of naming conventions for commonly- used modules:
```py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
This means that when you see np.arange, this is a reference to the arange function in NumPy.
This is done as it’s considered bad practice in Python software development to import everything (from numpy import *) from a large package like NumPy.


### 1.6.4 Jargon
## 1.7 Acknowledgements


```python

```
