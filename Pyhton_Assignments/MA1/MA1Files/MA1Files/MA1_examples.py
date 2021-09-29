"""
Exemple code in module 1

"""
import random   
import time     

def fac(n):
    """ Computes and returns n!""" 
    if n==0:
        return 1
    else:
        return n*fac(n-1)


def power(x,n):
    """ Computes and returns x**n recursively"""
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1./power(x, -n)



def reverse_mid(x):
    """ Returns s reversed """
    if len(x) <= 1:
        return x
    else:
        mid = len(x)//2
        return reverse_mid(x[mid:]) + reverse_mid(x[:mid])
    


def exchange(a, coins):
    """ Count possible way to exchange a with the coins in coins"""
    if a == 0:
        return 1
    elif (a < 0) or (len(coins) == 0):
        return 0
    else:
        return exchange(a, coins[1:]) + exchange(a - coins[0], coins)


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

memory = {0:0, 1:1}
def fib_mem(n, memory):
    if n in memory:
        return memory[n]
    else:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
        return memory[n]     




def insertion_sort_rec(l, n):
    """ Recursive insertion sort. Not suitable for large lists"""
    if n > 1:
        insertion_sort_rec( l, n-1 )    # sort the n-1 first
        x = l[n-1]
        i = n-2              # move elements larger than x to the right
        while i>=0 and l[i]>x :
            l[i+1] = l[i]
            i=i-1
        l[i+1] = x           # put in x


def insertion_sort(l):
    """ Iterative insertion sort """
    for j in range(1, len(l)):
        x = l[j]
        i = j-1
        while i >= 0 and x < l[i]:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = x
             

def merge(l1, l2):
    """ Merges two lists.
    Not suitable for large lists because of the recursion depth
    and because of a lot of list building.
    """
    if len(l1) == 0:
        return l2.copy()
    elif len(l2) == 0:
        return l1.copy()
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])       
  
  
def merge_sort(l):
    """ Merge sort. Just to demonstrate the idea"""
    if len(l) <= 1:
        return l
    else:
        n = len(l)//2
        l1 = l[:n]
        l2 = l[n:]
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        return merge(l1, l2)


def main():
    
    print(f"fac(100) = {fac(100)}\n")
    
    print(f"power(2, 5) = {power(2, 5)}")
    print(f"power(2,-1) = {power(2,-1)}\n")

    coins = (1, 5, 10, 50, 100)
    for a in [1, 4, 5, 9, 10, 100]:
        print(f"exchange({a}, {coins}) : {exchange(a, coins)}")
    print()

    for i in [0, 1, 2, 5, 10]:
        print(f"fib({i}) : {fib(i)}")
    print()
    
    for i in [0, 1, 2, 5, 10]:
        print(f"fib_mem({i}) : {fib_mem(i, {0:0, 1:1})}")
    print()
    
    print('Trying merge sort')
    test_size = 20
    l =[random.randint(1,100) for i in range(test_size)]
    print('Created list:', l)
    r = merge_sort(l)
    print('Sorted list :', r[0:test_size])
   
   
    # Demonstrates how the time complexity can be verified by experiments
    print('\nSorting with non recursive insertion sort')
    for test_size in [1000, 2000, 4000, 8000]:   
        l =[random.random() for i in range(test_size)]
        tstart = time.perf_counter()
        insertion_sort(l)
        tstop = time.perf_counter()
        print(f"Time for sorting {test_size} values: {tstop-tstart:.2f} seconds")
        
if __name__ == "__main__":
    main()
    print('Bye!')



