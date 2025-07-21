"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(x, y):
    return x * y
# - id
def id(x):
    return x
# - add
def add(x, y):
    return x + y
# - neg
def neg(x):
    return -x
# - lt
def lt(x, y):
    return x < y
# - eq
def eq(x, y):
    return abs(x - y) < 1e-5
# - max
def max(x, y):
    if x > y:
        return x
    return y
# - is_close
def is_close(x, y, eps=1e-2):
    if abs(x - y) < eps:
        return 1
    return 0
# - sigmoid
def sigmoid(x):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))
# - relu
def relu(x):
    return max(0, x)
# - log
def log(x):
    return math.log(x)
# - exp
def exp(x):
    return math.exp(x)
# - log_back
def log_back(x, y):
    if x ==0:
        return float('inf')
    return y * 1.0 / x
# - inv
def inv(x):
    if x ==0:
        return float('inf')
    return 1.0 / x
# - inv_back
def inv_back(x, y):
    if x ==0:
        return float('inf')
    return -y * 1.0 / (x * x)
# - relu_back
#
def relu_back(x, y):
    if x > 0:
        return y
    return 0
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
