"""
Solutions to module 1
Student:    Pallimulla Kapugamage Buddhika Chaturanga
Mail:       pkbchaturanga@gmail.com
Reviewed by:
Reviewed date:
"""

import random
import time


def power(x, n):         # Optional
    """ Computes and returns x**n recursively"""
    if 0 == n:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1.00/power(x, -n)


def multiply(m, n):      # Compulsory
    
    if 0 == n:
        return 0
    elif 0 > n:
        return -(m + multiply(m, -n-1))
    return m + multiply(m, n-1)

def divide(t, n):        # Optional
    if t < n:
            return 0
    remainder = t  - n
    quotient  = 1
    if remainder  == 0:
        return 1
    return quotient + divide(remainder, n)


def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    return  1.00 / n + harmonic(n-1)


def digit_sum(x):        # Optional
    if x == 0:
        return 0
    return x % 10 + digit_sum(x // 10)


def get_binary(n):       # Optional
    if n == 0:
        return ""
    scale = "" 
    if n < 0:
        n = -n
        scale = "-" 
    quotient = n // 2
    base_string = "1" if n % 2  else "0"
    return  scale + get_binary(quotient) + base_string


def reverse(s):          # Optional
    if len(s) <= 1:
        return s
    else:
        mid = len(s)// 2
        return  reverse(s[mid:]) + reverse(s[:mid])

def largest(a):          # Compulsory
    if 1  == len(a):
        return a[0] 
    mid = len(a) // 2
    max_set1 = largest(a[:mid])
    max_set2 = largest(a[mid:]) 
    return max_set1 if (max_set1 > max_set2) else max_set2


def count(x, n):         # Compulsory
    sum = 0
    if type(n) is list:
        m = n[0]
        if m == x:
            sum+=1
        if type(m) is list:
            sum+=count(x, m)      
        if len(n) > 1:
            sum += count(x, n[1:])
    return sum
    

def zippa(l1, l2):       # Compulsory
    
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + zippa(l1[1:], l2)
    else:
        return [l2[0]] + zippa(l1, l2[1:])  


def bricklek(f, t, h, n): # Compulsory
	if n == 1:
		return [f+'->'+t]
	return bricklek(f,h,t,n-1) + [f+'->'+t] + bricklek(h,t,f,n-1)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 15: Time for bricklek with 50 bricks:
  
   T  = 2(50) - 1 = 1125899906842624 s
  
  
  
  
  Exercise 16: Time for Fibonacci:
Data set 1:  
Def => Delta Ratio = delta(T(n))/delta(T(n-1)) when n != 1

Measured time for 1 :0.953674316406 microseconds 
Measured time for 2 :1.90734863281 microseconds 
Delta Ratio for n = 2 is :2.0
Measured time for 3 :1.90734863281 microseconds 
Delta Ratio for n = 3 is :1.0
Measured time for 4 :3.09944152832 microseconds 
Delta Ratio for n = 4 is :1.625
Measured time for 5 :4.05311584473 microseconds 
Delta Ratio for n = 5 is :1.30769230769
Measured time for 6 :5.96046447754 microseconds 
Delta Ratio for n = 6 is :1.47058823529
Measured time for 7 :9.05990600586 microseconds 
Delta Ratio for n = 7 is :1.52
Measured time for 8 :15.0203704834 microseconds 
Delta Ratio for n = 8 is :1.65789473684
Measured time for 9 :23.8418579102 microseconds 
Delta Ratio for n = 9 is :1.5873015873
Measured time for 10 :38.1469726562 microseconds 
Delta Ratio for n = 10 is :1.6

Data set 2:
Measured time for 1 :2.14576721191 microseconds 
Measured time for 2 :0.953674316406 microseconds 
Delta Ratio for n = 2 is :0.444444444444
Measured time for 4 :2.86102294922 microseconds 
Delta Ratio for n = 4 is :3.0
Measured time for 8 :13.1130218506 microseconds 
Delta Ratio for n = 8 is :4.58333333333
Measured time for 16 :627.040863037 microseconds 
Delta Ratio for n = 16 is :47.8181818182
Measured time for 32 :1380496.02509 microseconds 
Delta Ratio for n = 32 is :2201.60456274
   
    
fib(50) -> 4436.6253 seconds
fib(100) :( 
  
  Exercise 19: Comparison sorting methods:
  
  disregard base 2 to base 10 for the comparion purpose 
  
  Insert sort : avg
    T(n) -> Theta(n*n) 
    T(n) = C.(n.n)  say C > 0
    with initial valutes , n = 1000, T(1000) = 1s
    Hence C = 0.000001 s  = 1 micro seconds
    Then, say n = 10 to 6 , T(10 to 6) = 10 to 6 seconds
    Then, say n = 10 to 9 , T(10 to 9) = 10 to 12 seconds 
    Every time n scaling 1000 times excution time approximately scaling 10 raise to 6 times,
    thus expotential growing n power 2
  
  Merge sort : avg
    T(n) -> Theta(nlogn) 
    T(n) = C.(nlogn)  say C > 0
    with initial valutes , n = 1000, T(1000) = 1s
    Hence C = 1/3000 s  = 1/3 milli seconds
    Then, say n = 10 to 6 , T(10 to 6) = 2 x 1000 s =  2000 s
    Then, say n = 10 to 9 , T(10 to 9) = 3 x 10to6 s = 3000000 s
    Every time n scaling 1000 times excution time approximately scaling 10 raise to 3 times,
    

 Hence it states  that , when elment raise 1000 times each merge sort takes  
 approximately n.n lesser time than inseration sort
 
  Exercise 20: Comparison Theta(n) and Theta(n log n)
  
  say algo' A time TA(n) = (1).n  ...linear
  algo'     B Time TB(n) = (c)nlogn  where c > 0 and c = 0.1s with intial conditions
                   TB(n) = (0.1)nlogn
  say when n = m , where TA(m) = TB(m) where we state m exist and positive integer > 0
  0.1 m.logm = m , logm = 10 , assume base 10 logrithmic , then m = 10 to power 10, 
  but argument  satisfies , TA < TB thus,
    m < (0.1)mlogm  =>  10 < logm
    log(10 to power 10) < log(m), since llogrithmic is increasing funtion lies under positive integers 
    - greater than 1 , it's trivial  m = 1 never satisified
    hence  when  n at least at  10 to 10 seconds  A can beat the A 
    
  
  
  
  
  
  





"""