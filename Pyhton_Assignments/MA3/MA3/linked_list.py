""" linked_list.py

Student: Pallimulla Kapugamage Buddhika Chaturanga
Mail: bupa8694@student.uu.se
Reviewed by:
Date reviewed:
"""
import numbers


class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        len = 0
        f = self.first
        while f:
            f = f.succ
            len += 1
        return len
  
  
    def mean(self):               # Optional
        len = self.length()
        if not len:
            return 0
        mean = 0.0
        f = self.first
        while f:
            if isinstance(f.data, numbers.Number):
                mean += f.data
            f = f.succ
        return mean/len

    
    
    def remove_last(self):        # Optional
        f = self.first
        if f == None:
            return None
        if f.succ == None:
            data = f.data
            self.first = None
            return data
        len = self.length()
        cnt = len - 1
        data = 0
        while f.succ.succ:
            f = f.succ
        data = f.succ.data
        f.succ = None
        return data
    
    
    def remove(self, x):          # Compulsory
        if not self.first:
            return
        f = self.first
        if f.data == x:
            self.first = f.succ
            return True
        found = False
        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                f = f.succ
                found = True
                break
            f = f.succ
        return found

    def _count(self, x, f, cnt):
        if f is None:
            return cnt
        if f.data == x:
            cnt += 1
        return self._count(x, f.succ, cnt)

    def count(self, x):           # Optional
        cnt = 0
        return self._count(x, self.first, cnt)

    def _to_list(self, f):
        if f.succ is None:
            return [f.data]
        return [f.data] + self._to_list(f.succ)

    def to_list(self):            # Compulsory
        if self.length() == 0:
            return []
        return self._to_list(self.first)

    def _remove_all(self, x):
        if not self.remove(x):
            return
        self._remove_all(x)

    def remove_all(self, x):      # Compulsory
        if self.length() == 0:
            return
        self._remove_all(x)

    

    def __str__(self):            # Compulsary
        if self.length() == 0:
            return '()'
        return '('+', '.join(str(ele) for ele in self) + ')'

    
    # complexity of this function is Θ(n²)
    def merge(self, lst):         # Compulsory
        if self.length() == 0:
            return lst
        elif lst.length() == 0:
            return self
        # linear complexity Θ(n) , time vary linearly with size of the elements
        for ele in lst:
            # linear Θ(n) assume element is biggest worst case  Ω(n)
            self.insert(ele) 
        return self
    
    def __getitem__(self, ind):   # Compulsory
        ind = ind if ind >= 0 else self.length()+ind
        for idx, val in enumerate(self):
            if idx == ind:
                return val
        raise IndexError


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return "{}:{}:".format(self.name,self.pnr)

    def __lt__(self, other):
        return self.pnr < other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr

    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    # Test code:

    


if __name__ == '__main__':
    main()
    


    

