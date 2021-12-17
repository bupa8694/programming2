import unittest
from m1 import *

class MyTestCase(unittest.TestCase):
    def test_longest_list(self):
        self.assertEqual(length_longest(1), 0)
        self.assertEqual(length_longest([]), 0)
        self.assertEqual(length_longest([1, 2, 3]), 3)
        self.assertEqual(length_longest([1, [2, 3]]), 2)
        self.assertEqual(length_longest([1, [1, 2, 3, 4], 3]), 4)



if __name__ == '__main__':
    unittest.main()
