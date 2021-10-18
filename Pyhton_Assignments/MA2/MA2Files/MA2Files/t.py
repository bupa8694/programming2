import io
import math
from statistics import mean

def sum_(*args):
    return sum(args)
def mean_(*args):
    return mean(args)

fn_table = {'sqrt':math.sqrt , 'log':math.log}
print (fn_table['log'](25))

print(math.exp(34.669))
print(max(34,4,45,67,56,69))
print(min(34,4,45,67,56,69))
print(mean_(34,4,45))
print(sum([34,4,45]))
print(mean([2,4,5]))