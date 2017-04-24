
# Chapter 3. IPython: An Interactive Computing and Development Environment

## 3.1 IPython Basics

### 3.1.1 Tab Completion
### 3.1.2 Introspection
### 3.1.3 The %run Command
* __Interrupting running code__

### 3.1.4 Executing Code from the Clipboard
* __IPython interaction with editors and IDEs__

### 3.1.5 Keyboard Shortcuts
### 3.1.6 Exceptions and Tracebacks

### 3.1.7 Magic Commands

IPython has many special commands, known as “magic” commands, which are de- signed to faciliate common tasks and enable you to easily control the behavior of the IPython system.  
A magic command is any command prefixed by the the percent symbol %.  
For example, you can check the execution time of any Python statement, such as a matrix multiplication, using the %timeit magic function (which will be discussed in more detail later):   


* __Table 3-2. Frequently-used IPython Magic Commands__

| Command           | Description                                                                                                                         |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| %quickref         | Display the IPython Quick Reference Card                                                                                            |
| %magic            | Display detailed documentation for all of the available magic commands                                                              |
| %debug            | Enter the interactive debugger at the bottom of the last exception traceback                                                        |
| %hist             | Print command input (and optionally output) history                                                                                 |
| %pdb              | Automatically enter debugger after any exception                                                                                    |
| %paste            | Execute pre-formatted Python code from clipboard                                                                                    |
| %cpaste           | Open a special prompt for manually pasting Python code to be executed                                                               |
| %reset            | Delete all variables / names defined in interactive namespace                                                                       |
| %page OBJECT      | Pretty print the object and display it through a pager                                                                              |
| %run script.py    | Run a Python script inside IPython                                                                                                  |
| %prun statement   | Execute statement with cProfile and report the profiler output                                                                      |
| %time statement   | Report the execution time of single statement                                                                                       |
| %timeit statement | Run a statement multiple times to compute an emsemble average execution time. Useful for timing code with very short execution time |
| %who %who_ls %whos| Display variables defined in interactive namespace with, varying levels of information/verbosity                                    |
| %xdel variable    | Delete a variable and attempt to clear any references to the object in the IPython internals                                        |

### 3.1.8 Qt-based Rich GUI Console
### 3.1.9 Matplotlib Integration and Pylab Mode

## 3.2 Using the Command History

### 3.2.1 Searching and Reusing the Command History
### 3.2.2 Input and Output Variables
### 3.2.3 Logging the Input and Output

## 3.3 Interacting with the Operating System

Another important feature of IPython is that it provides very strong integration with the operating system shell.  
This means, among other things, that you can perform most standard command line actions as you would in the Windows or UNIX (Linux, OS X) shell without having to exit IPython.  
This includes executing shell commands, changing directories, and storing the results of a command in a Python object (list or string).  
There are also simple shell command aliasing and directory bookmarking features.

See Table 3-3 for a summary of magic functions and syntax for calling shell commands.  
I’ll briefly visit these features in the next few sections.  


* __Table 3-3. IPython system-related commands__  

| Command               | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| !cmd                  | Execute cmd in the system shell                                 |
| output = !cmd args    | Run cmd and store the stdout in output                          |
| %alias alias_name cmd | Define an alias for a system (shell) command                    |
| %bookmark             | Utilize IPython’s directory bookmarking system                  |
| %cd directory         | Change system working directory to passed directory             |
| %pwd                  | Return the current system working directory                     |
| %pushd directory      | Place current directory on stack and change to target directory |
| %popd                 | Change to directory popped off the top of the stack             |
| %dirs                 | Return a list containing the current directory stack            |
| %dhist                | Print the history of visited directories                        |
| %env                  | Return the system environment variables as a dict               |

### 3.1.1 Shell Commands and Aliases
### 3.1.2 Directory Bookmark System

## 3.4 Software Development Tools

### 3.4.1 Interactive Debugger
* __Other ways to make use of the debugger__

### 3.4.2 Timing Code: %time and %timeit
### 3.4.3 Basic Profiling: %prun and %run -p
### 3.4.4 Profiling a Function Line-by-Line

## 3.5 IPython HTML Notebook

## 3.6 Tips for Productive Code Development Using IPython

### 3.6.1 Reloading Module Dependencies
### 3.6.2 Code Design Tips
* __Keep relevant objects and data alive__
* __Flat is better than nested__
* __Overcome a fear of longer files__

## 3.7 Advanced IPython Features

### 3.7.1 Making Your Own Classes IPython-friendly
### 3.7.2 Profiles and Configuration

## 3.8 Credits 


```python

```
