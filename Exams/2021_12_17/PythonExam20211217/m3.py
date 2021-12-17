"""
Solutions to exam tasks for module 3.

"""

"""
Solutions to exam tasks for module 1.
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

import random
import time


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ
      
    def __init__(self, param=None):      
        self.first = None
        if param is None:
            return
        try:
            iter(param)
        except TypeError:
            self.first = self.Node(param)  
            return
        self.first = self.Node(None) # dummy instace
        self.last = self.first
        temp = self.first 
        for x in param:
            temp.succ = self.Node(x)
            temp = temp.succ
            self.last = temp
        self.first = self.first.succ 
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ
    
    def __str__(self):
        if self.first is None:
            return '()'
        res = ''
        for x in self:
            res += str(x) + ', '
        return '(' + res[:-2] + ')'

    
    def append(self, x):                  
        if self.first == None:
            self.first = self.Node(x)
        else:
            node = self.first
            while node.succ:
                node = node.succ
            node.succ = self.Node(x)
    
    def append_better(self, x):                # Task A5
        if self.first == None:
            self.first = self.Node(x)
            self.last =  self.first 
        else:
            self.last.succ = self.Node(x)
            self.last = self.last.succ


def random_tree(n):                            # Task A6 
    t = BST()
    for x in range(n):
        t.insert(random.random())
    return t
"""
Answer to A6 (Complexity of random_tree)
Since it BST, for average case 
The existing binary search tree is a balanced tree. Unlike the worst case, 
we don't need to compare the new node's value with every node in the existing tree
The existing binary search tree is a balanced tree when each level has 2^L nodes, 
where L is the level of the tree. Now we want to insert a node with a value. First, 
we check the root node's value. 
As it is less than the new node's value, we explore the right subtree for the insertion. 
Here the number of comparisons we need to do is (L+1).
For any new node that we want to insert, 
(L+1) would be the maximum number of comparisons required, which is the height of the binary search tree 
(Here, L is the level of the existing binary search tree). 
The height of the binary search tree is also equal to logN, where N is the total number of the node in the binary search tree.
Hence complexity merley halves, complexity O(logN)} behvoior
"""


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, param=None):
        self.root = None
        if param:
            for x in param:
                self.insert(x)

    def __iter__(self):
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

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ', '
        if self.root:
            result = result[:-2]
        return '<' + result + '>'
    
    def size(self):
        result = 0
        for x in self:
            result += 1
        return result

    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return level + self._ipl(r.left, level + 1) + \
                self._ipl(r.right, level + 1)

    def ipl(self):
        return self._ipl(self.root, 1)     

    def epl(self):                          # Task A7
         return self.ipl() + 2*self.size() + 1
    
    def __eq__(self, other):                  # Task A8
        return str(self) == str(other)
    
    def equal(self, other):                   # Task B3
        if(self != other):
            return False
        return self.epl() == other.epl()

            



def main():
    print('Trying append_better')
    print('====================')
    ll = LinkedList()
    print('Empty list:', ll)
    for i in range(5):
        ll.append_better(i)
    print('After some appends   : ', ll)
    ll.append_better('x')
    print('After one more append: ', ll)



    print('\nTrying epl')
    print('============')
    t = BST()
    print(f'{t.epl()} should be 1')
    t = BST([1])
    print(f'{t.epl()} should be 4')
    t = BST([1, 2])
    print(f'{t.epl()} should be 8')
    t = BST([1, 2, 3])
    print(f'{t.epl()} should be 13')
    t = BST([2, 1, 3])
    print(f'{t.epl()} should be 12')
    t = BST([2, 1, 3, 4])
    print(f'{t.epl()} should be 17')
        
    print('\nTrying ==')
    print('=========')
    t1 = BST([1,2,3])
    t2 = BST([2,1,3])
    t3 = BST([3,1,2,4])
    t4 = BST([1,2,3,4])
    t5 = BST([1,2,3])
    print(f'{t1} == {t2} : {t1==t2}')
    print(f'{t1} == {t3} : {t1==t3}')
    print(f'{t3} == {t4} : {t3==t4}')    
    print(f'equal: {t1.equal(t2)}')


    print('\nTrying equal')
    print('============')
    t5 = BST([1,2])
    t6 = BST(['1, 2'])
    print(f't5 : {t5}, t5.size(): {t5.size()}')
    print(f't6 : {t6}, t6.size(): {t6.size()}')
    print(t5 == t6)
    print(f't5.equal(t6): {t5.equal(t6)}')
        
if __name__ == '__main__':
    main()
