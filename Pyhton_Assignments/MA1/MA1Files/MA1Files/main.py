
def merge(l1, l2):
    """ Merges two lists.
    Not suitable for large lists because of the recursion depth
    and because of a lot of list building.
    """
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
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
        print(l1,l2)
        return merge(l1, l2)

def duplicate_removal(p,l):
    if len(l) <= 1: 
        return l
    set = [p]
    if p == l[0]:
        return
def zippa(l1, l2):
    sorted_list =  merge(merge_sort(l1),merge_sort(l2))
    return 

def power(x, n):         # Optional
    """ Computes and returns x**n recursively"""
    if 0 == n:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1.00/power(x, -n)
    
def bricklek(f, t, h, n): 
	if n == 1:
		return [f+'->'+t]
	return bricklek(f,h,t,n-1) + [f+'->'+t] + bricklek(h,t,f,n-1)

def multiply(m, n):      # Compulsory
  if 1 == n:
      return m
  return m + multiply(m-1, n-1)

import time
def rub_fibs(td_lst):
    def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    for e in td_lst:
        tstart = time.perf_counter()
        fib(1)
        tstop = time.perf_counter()
        print ("Measured time :{}seconds ".format(tstop - tstart))
    
def foo(n):
    rub_fibs([1,2,4,8,16,32])
    
   
    
if __name__ == '__main__':
    foo(4)

