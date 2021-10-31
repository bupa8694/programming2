#!/usr/bin/env python3

import concurrent.futures as future
from time import perf_counter
from integer import Integer
import random
import math
from numba import njit


def points_within_the_circle(point_set):
    return set(ele for ele in point_set if ele[0] * ele[0] + ele[1] * ele[1] <= 1.0)


def generate_images(n, epsilon):
    upper_boudary = 1.0 + epsilon
    lower_boudary = -1.0 - epsilon
    point_set = set(
        [(random.uniform(lower_boudary, upper_boudary), random.uniform(lower_boudary, upper_boudary)) for _ in
         range(n)])
    point_set_within_circle = points_within_the_circle(point_set)
    point_set_outside_circle = point_set.difference(
        point_set_within_circle)  # we can do render using original set and points within the circle  trick but set approach is more cleaner

    # approximationg pi
    import math
    print("Theoritical Pi- ", round(math.pi, 4))
    approx_pi = round(4 * (len(point_set_within_circle)) / len(point_set), 4)
    print("Appoximated Pi for {}- ".format(n), approx_pi)
    # now we draw unit circle green color
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((0.0, 0.0), 1.0, fill=False, color="green")
    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.scatter(*zip(*point_set_within_circle), color="red")
    plt.scatter(*zip(*point_set_outside_circle), color="blue")
    plt.savefig("Monte_Carlo_pi_for_" + str(n) + ".png")


def gen_point(dimension, epsilon):
    upper_boudary = 1.0 + epsilon
    lower_boudary = -1.0 - epsilon
    return tuple([random.uniform(lower_boudary, upper_boudary) for _ in range(dimension)])


def scalar_of_point(point):
    import functools
    sum = functools.reduce(lambda x, y: x + y, (ele * ele for ele in point))
    return sum


def calc_len_of_inpoints_parallel(n, d, epsilon=0.0001):
    #print("Executing our Task on Process {}".format(os.getpid()))
    points_set = set(gen_point(d, epsilon) for _ in range(n))
    oulier_set = set(e for e in points_set if scalar_of_point(e) <= 1)
    inlier_set = points_set - oulier_set
    return len(inlier_set)


def hyperspace_volume_parallel(n, d, n_process=10, epsilon=0.0001):
    import functools
    import concurrent.futures
    N = n//n_process
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_process) as ex:
        result_futures = list(map(lambda x: ex.submit(
            calc_len_of_inpoints_parallel, N, d, epsilon), range(1, n_process+1)))
        approx_pi = 4*(functools.reduce(lambda x, y: x+y,
                       [e.result() for e in result_futures]))/n
        hyp_vol_1 = (math.pi ** d / 2) / (math.gamma(d / 2 + 1))
        print("Exact value for Vd(1)- ", hyp_vol_1)
        print("Appoximated Pi for {}- ".format(n), approx_pi)
        return (hyp_vol_1, approx_pi)


def hyperspace_volume(n, d, epsilon=0.0001):
    points_set = set(gen_point(d, epsilon) for _ in range(n))
    oulier_set = set(e for e in points_set if scalar_of_point(e) <= 1)
    inlier_set = points_set - oulier_set

    hyp_vol_1 = (math.pi ** d / 2) / (math.gamma(d / 2 + 1))
    print("Exact value for Vd(1)- ", hyp_vol_1)
    approx_pi = round(4 * (len(inlier_set)) / len(points_set), 4)
    print("Appoximated Pi for {}- ".format(n), approx_pi)
    return (hyp_vol_1, approx_pi)


def fib_pure_python(n):
    if n <= 1:
        return n
    return (fib_pure_python(n - 1) + fib_pure_python(n - 2))


@njit
def fib_numba_python(n):
    if n <= 1:
        return n
    return (fib_numba_python(n - 1) + fib_numba_python(n - 2))


def fib(n):
    f = Integer(n)
    if f is None:
        return 0
    return f.fib()


def fn_timing_on_fib(fn_fib, n, ranging=True):
    time_stamps = []
    k = 1
    if not ranging:
        k = n
    for e in range(k, n + 1):
        t1_start = perf_counter()
        fn_fib(e)
        t1_stop = perf_counter()
        delta = (t1_stop - t1_start)
        print("Elapsed time for {}  seconds: {}".format(e, delta))
        time_stamps.append((e, delta))
    return time_stamps


def plot_timings(time_stamps, fn_name):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.xlabel("Number of iterations - n")
    plt.ylabel("Execution time in seconds")
    # plt.xticks([ele[0] for ele in time_stamps])
    # plt.yticks([ele[1] for ele in time_stamps])
    plt.scatter(*zip(*time_stamps), color="blue")
    plt.savefig("Facto_reuslts_for_" + fn_name + ".png")


def parallel_hyperVol(no_processes, n, d):
    with future.ProcessPoolExecutor(max_workers=no_processes) as ex:
        future_res = ex.submit(hyperspace_volume, n, d)
    #print(future_res.result())
    return future_res.result()


def main():
    '''
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	'''
    '''
    epsilon = 0.0001
    for n in [50,100,200,400,1000,10000,100000]:
        generate_images(n, epsilon)
    hyperspace_volume(100000, 2)
    '''

    t1_start = perf_counter()
    hyperspace_volume(1000000, 11)
    t1_stop = perf_counter()
    delta = (t1_stop - t1_start)
    print("Elapsed time for hyperspace volumen(1) ST seconds: {}".format(delta))

    t1_start = perf_counter()
    hyperspace_volume_parallel(1000000, 11)
    t1_stop = perf_counter()
    delta = (t1_stop - t1_start)
    print("Elapsed time for hyperspace volumen(1) MT seconds: {}".format(delta))

    # for the sake of clarity first c++ integration
    '''
    print("\n **** Numba Py timings ****")
    plot_timings(fn_timing_on_fib(fib_numba_python, 47), "numbPyFib")
    print("\n **** C++ Integratiopn timinings ****")
    plot_timings(fn_timing_on_fib(fib, 47), "cppFib")
    print("\n **** Pure Python timinings ****")
    plot_timings(fn_timing_on_fib(fib_pure_python, 47), "purePyFib")
    '''


if __name__ == '__main__':
    main()
