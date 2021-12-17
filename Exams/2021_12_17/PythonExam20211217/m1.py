"""
Solutions to exam tasks for modul 1 for exam 2021-12-17
"""
"""
Solutions to exam tasks for module 1.
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

import random
import time
import math

#####                                     Task A1

def number_of_negative(lst):
    if type(lst) != list:
        if lst < 0: return 1
        return 0
    result = 0    
    for x in lst:
        result = result + number_of_negative(x)
    return result


#####                                     Task A2
def s_sort(aList):
    for i in range(len(aList)-1):
        m = i
        for j in range(i+1,len(aList)):
            if aList[j] < aList[m]:
                m = j
        aList[i], aList[m] = aList[m], aList[i]


def random_list(n):
    res = []
    for i in range(n):
        res.append(random.random())
    return res

"""
Answer A2:
Let us take average case scenario means , 
Complexity Theta(n^2).
For each of the n rounds in the outer loop the inner loop will also goes n rounds.



"""



#####                                      Task B1

def foo(n):
    result = 1
    for i in range(n, n*n*n):
        result += 10*n + (n+2)*n
    return result

"""
Answer B1:
Complexity:Complexity Theta(n^2)
Estimated time for foo(5000): foo(70^2) = foo(1000*5) = 50mins
Estimated time for foo(10000): foo(100^2) =  foo(1000*10) = 3.3hrs



"""



def main():
    print('Testing number_of_negative')
    print(number_of_negative(1), '\t Should be 0')
    print(number_of_negative(-1), '\t Should be 1')
    l1 = [1,2,[[1,-2,3,[1,2,-3],5],2,3,-4,5]]
    print(number_of_negative(l1), '\t Should be 3')
    l1 = [1,2,[[1,2,[-2],5,6],2], -1]
    print(number_of_negative(l1), '\t Should be 2')
    l1 = [-1,2,[[1,-2,[-2],5,6],2], -1]
    print(number_of_negative(l1), '\t Should be 4')
  
    #                                       Code for task A2
    print('\nTiming of s_sort')
    measured = []
    for n in [1000, 2000, 4000, 8000]:
        rl = random_list(n)
        tstart = time.perf_counter()
        s_sort(rl)
        print(n,  end =' \t')
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f"{dt:5.1f}")
    print('\nTime growth when doubling input' )  
    for i in range(1,len(measured)):
        print(f'{measured[i]/measured[i-1]:5.1f}')


    #                                       Code for task B1
    print('\nTiming of foo')
    measured = []
    for n in [100, 200, 400,500, 800,1000]:
        tstart = time.perf_counter()
        print(n, end ='\t')
        foo(n)
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f" {dt:5.1f}")
    print('\nTime growth when doubling input' )  
    for i in range(1,len(measured)):
        print(f'{measured[i]/measured[i-1]:5.1f}')  

    print('\nEstimation of time for foo(5000)')
    n = 70
    tstart = time.perf_counter()
    foo(n)
    dt= time.perf_counter()-tstart
    print(f"Time for {n}: {dt:5.1f}")
    print('\nEstimation of time for foo(10000)')
    n = 100
    tstart = time.perf_counter()
    foo(n)
    dt= time.perf_counter()-tstart
    print(f"Time for {n}: {dt:5.1f}")
 
if __name__ == "__main__":
    main()


    