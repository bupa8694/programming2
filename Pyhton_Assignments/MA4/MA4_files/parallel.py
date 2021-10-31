import concurrent.futures as future
import random as rnd
rnd.seed(10)

def mymul(a_list,multiply_by):
	return [multiply_by*element for element in a_list]

# mymul([1,3,2],3) returns [3,9,6]


def parallel_mymul(no_processes, len_list, multiply_by):
	len_sub_list = len_list // no_processes # length of sub list
	
	# # generate a list with no_process elements each with len_sub_list random integers (0-9)
	print(len_sub_list)
	list_of_lists=[[rnd.randrange(10) for _ in range(len_sub_list)] for i in range(no_processes)]

	print(list_of_lists)
	list_of_multiply_bys=[multiply_by]*no_processes

	print(list_of_multiply_bys)

	with future.ProcessPoolExecutor() as ex:
		result = ex.map(mymul,list_of_lists,list_of_multiply_bys)

	print(list(result))


if __name__ == '__main__':
	parallel_mymul(4,12,3)
	# parallel_mymul(2,12,3)
	# parallel_mymul(3,12,3)
	# parallel_mymul(4,12,2.2) #works also fine with floats instead of integers

