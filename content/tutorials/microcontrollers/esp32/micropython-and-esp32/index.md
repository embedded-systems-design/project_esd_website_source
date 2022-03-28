---
title: ESP32 and MicroPython
published: false
---

## What is Python

The #1 Programming language*

::: incremental
* Python: 14.2%  
* Matlab: 0.8%  
* Labview: 0.14%  
:::

:::{style="font-size:12pt"}
\* as of March 2022, [tiobe.com](https://www.tiobe.com/tiobe-index/)
:::

## What is Python, really?

A **really** easy to learn programming language

::: incremental
* simple formatting: 
    * mostly spaces, 
    * few extraneous brackets, braces, or parenthesis
    * No terminating character like ```;```
    * similar basic keywords as other languages.
    * easy access to complex data types
:::

:::{style="font-size:12pt"}
* <https://www.bitdegree.org/tutorials/python-vs-c-plus-plus/>
* <https://realpython.com/python-vs-cpp/>
:::

## What else is Python?

An extensible system of software "packages"

::: incremental
* use pip/pypi to install
* install straight from github!
:::

## But what makes it unique?

An "interpreted" language

::: incremental
* In its simplest form, the Python interpreter simply runs human-readable scripts*.
* Can load and run code compiled in C, C++ FORTRAN, etc.
:::

:::{style="font-size:12pt"}
\* there are many exceptions
:::

## Is there anything else?

::: incremental
* "Dynamically Typed"
    * Variables don't need to be declared as one type or another.  You simply set them equal to something and they become that data type.
* Object-oriented
    * concept of classes and inheritance
* "Public" by definition
    * data is not easily hidden.
    * data is accessible by anything
:::

## So then, why C?

* Lower level language that is easier to map to hardware-specific registers and functionality
* Compilation makes running code faster and more memory efficient

## Python Interpreter

::: incremental
* Simple program that runs scripts or typed commands.
* A lot like ```bash```, ```powershell```, or ```cmd```, only cross-platform and independent of the operating system.
:::

## What is MicroPython?

::: incremental
* A slimmed down, limited version of Python that fits within the program space of a little microcontroller
* The system of software packages written for it
* The same idea of an interpreter... you just access it over UART/USB.
:::

## What is Thonny?

::: incremental
* a Graphical User Interface (GUI)  _written in Python_
* A text editor
* The interface to your device and its interpreter
* A nice way to re-flash your device
:::

## What is Anaconda/Miniconda?

::: incremental
* A way to manage all the "packages" you can install on your PC
* A solution for dealing with conflicting installation requirements.
* A way to share packages that contained OS-specific, compiled libraries.
:::


## Why do I need to use Anaconda?

Many packages include libraries that are compiled specific to one operating system

. . .

this requires a compiler, and understanding the compilation process in case it doesn't work

. . .

or, requires access to compiled packages


:::{.notes style="font-size:12pt"}
\* <https://www.lfd.uci.edu/~gohlke/pythonlibs/>
:::

## Ok, so how do I get started?

::: incremental
1. Install anaconda/miniconda
1. Install Thonny and some other packages
1. Open Thonny
1. Flash the ESP32 with MicroPython over USB
1. Load some micropython libraries
1. Start writing code.
:::

# Python Basics

## Data Types

### Really Basic

int, float, bool, complex

* can convert from one to another using the data type class itself
* identify the type using ```type()```

### Less Basic

string, function

### Advanced

list, dict, set, tuple

### Even More Advanced

class

## Operators

* assignment: =
* math: +, -, *, /, **, %, //
* equality: ==, !=, <, <=, >, >=
* binary opertors: &, | , ^, <<, >>

## Functions

    * def, return, pass keywords
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
    * if, elif, else
    * NO switch ([yet...](https://towardsdatascience.com/switch-case-statements-are-coming-to-python-d0caf7b2bfd3))
* logic
    * and, not, or
    * ==, !=, >, >= <, <=

## iterable data types

* list, tuple, string
* range() keyword
* can use ```else```
* can access one item at a time using square brackets
* can "slice" iterables

## Looping

* for, while
* break, continue
* iterate through iterables

## Strings

* easy to format, easy to search, easy to operate on
* split(), join(), find(), index(), format()...
* ```print()```

## Classes

* containers for functions _and_ data.
* "inheritance"

```python
class MyClass(object):
    def __init__(self,value):
        self.value = value
    def my_method(self):
        return self.value
```

## Modules & Packages

* module is just another name for a python file
* package is a set of modules made for sharing & distribution


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