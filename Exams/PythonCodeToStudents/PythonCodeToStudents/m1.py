"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count all occurencies of d recursively """
    pass


def c(n):
    if n <= 2:
        return 1
    else:
        return c(n-1) - c(n-3)


def c_mem(n):
    """ A2:
        Compute c(n) recursively as above but use
        memorization to keep the runtime down.
    """
    pass


def main():
    print('Test count_all')
    print(count_all([], 1))
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))

    print('\nTest of c')
    print('c(3):', c(3))
    print('c(4):', c(4))
    print('c(5):', c(5))
    print('c(9):', c(9))

    print('\nTest of c_mem')
    print('c_mem(3):', c_mem(3))
    print('c_mem(4):', c_mem(4))
    print('c_mem(5):', c_mem(5))
    print('c_mem(9):', c_mem(9))

    print('c_mem(100):', c_mem(100))

    print('\nCode for task B1')


if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:




"""
