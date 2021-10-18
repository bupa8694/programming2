import time
import pdb

def rub_fibs(td_lst):
    def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    prev_time_delta = 1
    for idx,e in enumerate(td_lst):
        #pdb.set_trace()
        tstart = time.time()
        fib(e)
        tstop = time.time()
        delta = (tstop - tstart) * 1000000
        print ("Measured time for {} :{} microseconds ".format(e,delta))
        if 0 != idx :
            print ("Delta Ratio for n = {} is :{}".format(e, delta/prev_time_delta))
        prev_time_delta = delta
        
        
def foo():
    #pdb.run("rub_fibs([1,2,4,8,16])")
    rub_fibs([25])
    
foo()