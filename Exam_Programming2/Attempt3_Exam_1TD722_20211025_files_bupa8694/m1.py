"""
Solutions to exam tasks for module 1.
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

import random
import time
import math


#*********** A1 **************#
def _length_longest(lst):
    if type(lst) == list:
        yield len(lst)
        for ele in lst:
            yield from _length_longest(ele)


def length_longest(lst):
    """Returns the length of the longest (sub-)list in lst"""
    if type(lst) != list:  # checking parameter is a list
        return 0
    return max(_length_longest(lst))  # recursively call subsists yield their respective lengths and take max out of it


#*********** A2 **************#
def bubbelsort(aList):
    for i in range(len(aList) - 1):
        for j in range(len(aList) - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


def foo(n):
    result = 1
    for k in range(3):
        for i in range(n * n):
            result += k * n
    return result


def main():
    print(length_longest(1))  # Should be 0
    print(length_longest([]))  # Should be 0
    print(length_longest([1, 2, 3]))  # Should be 3
    print(length_longest([1, [2, 3]]))  # Should be 2
    print(length_longest([1, [1, 2, 3, 4], 3]))  # Should be 4

    # *********** A2 **************#
    print("*** Analysis of A2 ***")
    aList = [3, 2, 5, 1, 7]
    pwe_lst = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    lst = [random.sample(range(min(pwe_lst), max(pwe_lst) + 1), k) for k in pwe_lst]
    from time import perf_counter
    for ele in lst:
        start_stamp = perf_counter()
        bubbelsort(ele)
        end_stamp = perf_counter()
        time_delta = round((end_stamp - start_stamp)*1000, 4)
        print("Elapsed Time for n = {} : {} milliseconds".format(len(ele), time_delta))

    print(aList)
# *********** A3 **************#
    print("*** Analysis of A3 ***")
    for ele in [10,100,1000,10000]:
        start_stamp = perf_counter()
        foo(ele)
        end_stamp = perf_counter()
        time_delta = round((end_stamp - start_stamp) * 1000, 4)
        print("Elapsed Time for n = {} : {} milliseconds".format(ele, time_delta))

if __name__ == "__main__":
    main()

"""
Solution to A2 (Time complexity for bubbelsort):

Assume aList is quite large n elements , also assume for large n-1 approximately equal to n ,hence 

def bubbelsort ( aList ):                       Consider single operation
    for i in range (len ( aList ) -1):    => if this operation take c time for generate number,then total c.n times
       for j in range (len ( aList ) -1): =>  Same,if this operation take c time for generate numbers,then c.n times
          if aList [j] > aList [j +1]:    =>    this take constant time let us say k1, since list access is constant time
               aList [j], aList [j+1] = aList [j+1] , aList [j] =>    this take constant time let us say k2, since lists 
                                                                        accessing is constant time


now let us sum up all operations , 
            
            within inner for loop if approximately measure the time theoretically it takes t1 = (c.n)(k1+k2) = C1.n = t1 
            hence with outer loop takes to time to complete = cn(t1) => t2 -> C1.n.2 this implies Theta nxn = Θ(n²)

Sample code test results:
Elapsed Time for n = 1 : 0.00209996 milliseconds
Elapsed Time for n = 2 : 0.00160001 milliseconds
Elapsed Time for n = 4 : 0.00260002 milliseconds
Elapsed Time for n = 8 : 0.00659999 milliseconds
Elapsed Time for n = 16 : 0.02390001 milliseconds
Elapsed Time for n = 32 : 0.1758 milliseconds
Elapsed Time for n = 64 : 0.40020002 milliseconds
Elapsed Time for n = 128 : 1.51250005 milliseconds
Elapsed Time for n = 256 : 5.36949997 milliseconds

when n gets squared its clearly show time in milliseconds raising up exponentially approximately closing (n²)

Solution to B1 (Time complexity for function foo):

def foo(n):
    result = 1
    for k in range(3):      -> let us think one one iteration it takes c, then 3c
        for i in range(n * n): -> when n is 0, this function do nothing at all let us say time T ,T approximately => 0
            result += k * n            - but when n grows up range is getting n.n ,even range getting higher it the time 
    return result                      - progression for the operation is heiger linear manner ,where T(n) - T(n-1) = C 
                                        - ,Hence this has Θ(n) it's linear complexity,

Sample set 1 
Elapsed Time for n = 1 : 0.0021 milliseconds
Elapsed Time for n = 2 : 0.0016 milliseconds
Elapsed Time for n = 4 : 0.0033 milliseconds
Elapsed Time for n = 8 : 0.0104 milliseconds
Elapsed Time for n = 16 : 0.0383 milliseconds
Elapsed Time for n = 32 : 0.1519 milliseconds
Elapsed Time for n = 64 : 0.6062 milliseconds
Elapsed Time for n = 128 : 2.4356 milliseconds
Elapsed Time for n = 256 : 8.8419 milliseconds

Sample set 2
Elapsed Time for n = 80 : 1.1118 milliseconds
Elapsed Time for n = 81 : 1.0202 milliseconds
Elapsed Time for n = 82 : 1.1509 milliseconds
Elapsed Time for n = 83 : 1.113 milliseconds
Elapsed Time for n = 84 : 1.0754 milliseconds
Elapsed Time for n = 85 : 1.1755 milliseconds
Elapsed Time for n = 86 : 1.2742 milliseconds
Elapsed Time for n = 87 : 1.2549 milliseconds
Elapsed Time for n = 88 : 1.2108 milliseconds
Elapsed Time for n = 89 : 1.2427 milliseconds
Elapsed Time for n = 90 : 1.2726 milliseconds
Elapsed Time for n = 91 : 1.2896 milliseconds
Elapsed Time for n = 92 : 1.3311 milliseconds
Elapsed Time for n = 93 : 1.6744 milliseconds
Elapsed Time for n = 94 : 1.5624 milliseconds
Elapsed Time for n = 95 : 1.2972 milliseconds
Elapsed Time for n = 96 : 1.2352 milliseconds
Elapsed Time for n = 97 : 1.2793 milliseconds
Elapsed Time for n = 98 : 1.3056 milliseconds
Elapsed Time for n = 99 : 1.6375 milliseconds

foo(1000000) ??
since this is linear let us treat pwrset = [10,100,1000,10000]
Elapsed Time for n = 10 : 0.0176 milliseconds         -> t1
Elapsed Time for n = 100 : 1.1704 milliseconds        -> t2
Elapsed Time for n = 1000 : 131.8791 milliseconds     -> t3
Elapsed Time for n = 10000 : 14646.4394 milliseconds  -> t4
Relation ?
t4/t3 = t3/t2  = approximately 112
hence  -> foo(100000) -> 1640400.16 milliseconds
        ->foo(1000000) -> 183,724,817.92 seconds means  approximately 51 hours
"""
