---
title: Python Basics
tags:
  - programming
  - python
---

# Python Basics

## Data Types

### Really Basic

```int````, ```float```, ```bool```, ```complex```

* can convert from one to another using the data type class itself
* identify the type using ```type()```

### Less Basic

```string```, ```function```

### Advanced

```list```, ```dict```, ```set```, ```tuple```

### Even More Advanced

```class```

## Operators

* assignment: ```=```
* math: ```+```, ```-```, ```*```, ```/```, ```**```, ```%```, ```//```
* equality: ```==```, ```!=```, ```<```, ```<=```, ```>```, ```>=```
* binary opertors: ```&```, ```|``` , ```^```, ```<<```, ```>>```

## Functions

    * ```def```, ```return```, ```pass``` keywords
    * arguments and keyword arguments
    * passing in unknown number of arguments

    ```python
    def my_function(arguments,..., keyword_arguments=3):
        #run your code here
        return_variable=1
        return return_variable
    ```

## Conditionals

* logic
    * ```if```, ```elif```, ```else```
    * NO switch ([yet...](https://towardsdatascience.com/switch-case-statements-are-coming-to-python-d0caf7b2bfd3))
* logic
    * ```and```, ```not```, ```or```
    * ```==```, ```!=```, ```>```, ```>=```, ```<```, ```<=```

## iterable data types

* ```list```, ```tuple```, ```string```
* ```range()``` function
* can access one item at a time using square brackets
* can "slice" iterables

## Looping

* ```for```, ```while```
* ```break```, ```continue```
* can iterate through "iterables"
* can use ```else```

## Strings

* easy to format, easy to search, easy to operate on
* ```split()```, ```join()```, ```find()```, ```index()```, ```format()```...
* ```print()```

## Classes

* containers for functions _and_ data.
* concept of "inheritance"

```python
class MyClass(object):
    def __init__(self,value):
        self.value = value
    def my_method(self):
        return self.value
```

## Modules & Packages

* a "module": is just another name for a python file
* a "package" is a set of modules made for sharing & distribution


```python
import X
from X import Y
import X.Z
import X as A
```

## Common Packages

### Matlab-like powers
numpy, scipy, matplotlib

<https://numpy.org/doc/stable/user/numpy-for-matlab-users.html>

### GUI development
pyQt, tkinter

### Other
sympy,

## Installing Packages

* pip
* conda
* "manually"