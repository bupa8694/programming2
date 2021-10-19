import math
from statistics import mean

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg

def fib(n):
    if not n.is_integer():
        raise EvaluationError('Argument to fib is {}. Must integer >= 0'.format(n))
    if n < 0:
        raise EvaluationError('Argument to fib is {}. Must integer >= 0'.format(n))
    if n <= 1:
       return n
    else:
       return(fib(n-1) + fib(n-2))

def fac(n):
    if not n.is_integer():
        raise EvaluationError('Argument to fib is {}. Must integer >= 0'.format(n))
    if n<=0:
        raise EvaluationError('Argument to fac is {}. Must integer >= 0'.format(n))
    if n == 1:
        return n
    else:
       return n*fac(n-1)

def sum_(*args):
    return sum(args)
def mean_(*args):
    return mean(args)

fn_1 = {'sqrt':math.sqrt,'exp':math.exp,'log':math.log,'sin':math.sin,'cos':math.cos,
'tan':math.tan,'fac':math.factorial,'fib':fib}

fn_n = {'sum':sum_,'mean':mean,'min':min,'max':max}