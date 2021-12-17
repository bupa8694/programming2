"""
Solutions to exam tasks for module 4
"""
"""
Solutions to exam tasks for module 1.
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

# A9
def dice(n,sides):
    from random import choice
    return [choice(range(1,sides+1)) for _ in range(n)]

def throw_dice(ns,n_sides):
    futures = []
    import concurrent.futures as future
    with future.ThreadPoolExecutor() as ex:
        for n in ns:
             futures.append(ex.submit(dice,n,n_sides))
    count = 0
    sz = 0;
    for f in future.as_completed(futures): 
        a = f.result()
        sz += len(a)
        for e in a:
            if e == n_sides:
                count += 1

    return float(count/sz)

# A10
def make_list(lst):
    lst = [x for l in lst for x in l]
    return  lst

# B4
import string 

def letterCount(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
    text = file.read()
    text = text.lower()
    return text.count(letter)
  

def count_letters():
    from string import ascii_lowercase as letters
    import matplotlib.pyplot as plt

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    freq = [letterCount("C:\\Users\\macxf\\Desktop\\Exam_2021_12_17_bups8694\\PythonExam20211217\\a.txt",letter) for letter in alphabet_list]
    dictionary = dict(zip(alphabet_list, freq))
    print(dictionary)

    plt.title("Letter counters")
    plt.ylabel('Counts')
    plt.xlabel('letter')
    plt.plot(alphabet_list, freq)
    plt.legend()
    plt.show()
    
def main():
    print('Test of A9')
    print(throw_dice([8,9,2,10,3,1],6))  # will probably not yield a good 
                                         # approximation of 1/6, since too few throws
    print(throw_dice([100000,100000],20)) # should yield approximately 1/20=0.05

    print('\nTest of A10')
    print(make_list([[1,7,8],[9],[3,3],[1]])) # should print [1, 7, 8, 9, 3, 3, 1]


    print('\nTest of B4')
    count_letters()
    

if __name__ == "__main__":
    main()
    print('Over and out')
