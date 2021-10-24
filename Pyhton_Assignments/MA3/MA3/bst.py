""" bst.py

Student: P.K Buddhika Chaturanga
Mail: bupa8694@student.uu.se
Reviewed by:
Date reviewed:
"""
from math import log2

from linked_list import LinkedList


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def insertX(self, key):
        new_node = self.Node(key)
        x = self.root
        y = None
        while x is not None:
            # monitoring root
            y = x
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                break

        if y is None:  # -> means tree is empty and new_node will be the root
            y = new_node
            self.root = y
        elif key < y.key:  # -> means new_Node will be connected to to left side to current leaf node
            y.left = new_node
        else:
            y.right = new_node
        return y

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def _containsX(self, n, k):
        if n and n.key == k:
            return True
        elif n is None:
            return False
        if k < n.key:
            n = n.left
        else:
            n = n.right
        return self._containsX(n, k)

    def containsX(self, k):
        n = self.root
        return self._containsX(n, k)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    # experimental
    # def sizeX(self):
    #   size = 0
    #  size += (1 for ele in self.root if ele.left or ele.right)
    # return size

    #
    #   Methods to be completed
    #
    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))

    def height(self):  # Compulsory
        if self.root is None:
            return 0
        r = self.root
        if r.left is None and r.right is None:
            return 1
        return self._height(r)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):  # Compulsory
        def smalleKeyNode(node):
            current = node
            while (current.left is not None):
                current = current.left
            return current

        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                small_node = smalleKeyNode(r.right)
                # Put that key in this node
                r.key = small_node.key
                # Remove that key from the right subtree
                r.right = self._remove(r.right, small_node.key)
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):  # Compulsory
        if self.root is None:
            return '<>'
        return '<' + ', '.join(str(ele) for ele in self) + '>'

    def to_list(self):  # Compulsory
        if self.root is None:
            return []
        lst = [ele for ele in self]
        return lst

    # complexity of the function below - Theta(n.log(n))
    def to_LinkedList(self):  # Compulsory
        lst = LinkedList()
        if self.root is None:
            return lst
        [lst.insert(ele) for ele in self]
        return lst

    def _ipl(self, r, lvl):
        r_cnt = 0
        l_cnt = 0
        if not (r.right or r.left):
            return 0
        if r.left is not None:
            l_cnt += 1
            l_cnt *= lvl
            l_cnt += self._ipl(r.left, lvl + 1)
        if r.right is not None:
            r_cnt += 1
            r_cnt *= lvl
            r_cnt += self._ipl(r.right, lvl + 1)
        return r_cnt + l_cnt

    def ipl(self):  # Compulsory
        if self.root is None:
            return 0
        if not (self.root.right or self.root.left):
            return 1
        return 1 + self._ipl(self.root, 2)


def random_tree(n):  # Useful
    import random
    bst = BST()
    for x in range(n):
        bst.insert(random.random())
    return bst


def fib(n):
    if n <= 1:
        return n, n
    else:
        return fib(n - 1)[0] + fib(n - 2)[0], n


def multi_fib(fr=1, to=18):
    from concurrent import futures as f

    l = [i for i in range(fr, to + 1)]

    with f.ProcessPoolExecutor() as ex:
        results = ex.map(fib, l)

    d = dict()
    for value, key in results:
        d[key] = value
    print(d)
    return d


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insertX(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.containsX(k)}")
    n_nodes = [1, 2, 4, 8, 16, 32, 64, 128]
    cum_ipl = 0
    for n in n_nodes:
        bst = random_tree(n)
        ipl = bst.ipl()
        est_ipl = round(1.39 * n * log2(n), 2)
        cum_ipl += ipl
        print("BST size : ", bst.size(), " BST height : ", bst.height(), " BST IPL : ", ipl, \
                " BST [IPL/n] Avg : ", round(ipl / n, 2), " EST IPL : ", est_ipl, "    IPL Δ: ", \
                abs(round(ipl - est_ipl, 2)), " Cumulative IPL : ", cum_ipl)
    multi_fib()

if __name__ == "__main__":
    main()

"""
What is the generator good for?
==============================

1. computing size?
2. computing height?
3. contains?
4. insert?
5. remove?

generator good for replacing iterator protocol ,hence its so efficient suitable for iterate through current BST 
Hence we can use it for Contains , computing height , computing Size,

some cautions :- https://www.python.org/dev/peps/pep-0380/#optimisations

Results for ipl of random trees
===============================                                 

# without O(n) operation - 1:39nlog2(n)

Sample one - number of nodes -  [1, 2, 4, 8, 16, 32, 64 , 128]
BST size :  1  BST height :  1  BST IPL :  1  BST [IPL/n] Avg :  1.0  EST IPL :  0.0     IPL Δ:  1.0  Cumulative IPL :  1
BST size :  2  BST height :  2  BST IPL :  3  BST [IPL/n] Avg :  1.5  EST IPL :  2.78     IPL Δ:  0.22  Cumulative IPL :  4
BST size :  4  BST height :  3  BST IPL :  8  BST [IPL/n] Avg :  2.0  EST IPL :  11.12     IPL Δ:  3.12  Cumulative IPL :  12
BST size :  8  BST height :  4  BST IPL :  22  BST [IPL/n] Avg :  2.75  EST IPL :  33.36     IPL Δ:  11.36  Cumulative IPL :  34
BST size :  16  BST height :  8  BST IPL :  70  BST [IPL/n] Avg :  4.38  EST IPL :  88.96     IPL Δ:  18.96  Cumulative IPL :  104
BST size :  32  BST height :  8  BST IPL :  155  BST [IPL/n] Avg :  4.84  EST IPL :  222.4     IPL Δ:  67.4  Cumulative IPL :  259
BST size :  64  BST height :  11  BST IPL :  380  BST [IPL/n] Avg :  5.94  EST IPL :  533.76     IPL Δ:  153.76  Cumulative IPL :  639
BST size :  128  BST height :  16  BST IPL :  1132  BST [IPL/n] Avg :  8.84  EST IPL :  1245.44     IPL Δ:  113.44  Cumulative IPL :  1771

Sample Two number of nodes -  [1, 2, 5, 7, 11, 13, 29, 47, 123] Prime nodes
BST size :  1  BST height :  1  BST IPL :  1  BST [IPL/n] Avg :  1.0  EST IPL :  0.0     IPL Δ:  1.0  Cumulative IPL :  1
BST size :  2  BST height :  2  BST IPL :  3  BST [IPL/n] Avg :  1.5  EST IPL :  2.78     IPL Δ:  0.22  Cumulative IPL :  4
BST size :  5  BST height :  3  BST IPL :  11  BST [IPL/n] Avg :  2.2  EST IPL :  16.14     IPL Δ:  5.14  Cumulative IPL :  15
BST size :  7  BST height :  5  BST IPL :  20  BST [IPL/n] Avg :  2.86  EST IPL :  27.32     IPL Δ:  7.32  Cumulative IPL :  35
BST size :  11  BST height :  6  BST IPL :  43  BST [IPL/n] Avg :  3.91  EST IPL :  52.89     IPL Δ:  9.89  Cumulative IPL :  78
BST size :  13  BST height :  7  BST IPL :  61  BST [IPL/n] Avg :  4.69  EST IPL :  66.87     IPL Δ:  5.87  Cumulative IPL :  139
BST size :  29  BST height :  8  BST IPL :  137  BST [IPL/n] Avg :  4.72  EST IPL :  195.83     IPL Δ:  58.83  Cumulative IPL :  276
BST size :  47  BST height :  10  BST IPL :  280  BST [IPL/n] Avg :  5.96  EST IPL :  362.88     IPL Δ:  82.88  Cumulative IPL :  556
BST size :  123  BST height :  14  BST IPL :  890  BST [IPL/n] Avg :  7.24  EST IPL :  1186.96     IPL Δ:  296.96  Cumulative IPL :  1446

Machine - (Intel Corei7 Gen 11 Windows 11 x64)
i > As experimentally shown above when number of numbers exponentially grows up the deviation between theoretical IPL - 
calculated IPL getting much deviated even without adding O(n) operation
Bit of disagreement happens when the number of nodes goes too high.

ii > height approximately twice of the value of (Average IPL/n )  h ≈ ipl/n


"""
