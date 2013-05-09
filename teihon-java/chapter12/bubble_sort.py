# -*- coding: utf-8 -*-
import timeit
import unittest

def sort(buf):
    size = len(buf) - 1
    for i in range(size):
        for j in range(size, i, -1):
            if buf[i] > buf[j]:
                tmp = buf[i]
                buf[i] = buf[j]
                buf[j] = tmp
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
    #print timeit.timeit('bubble_sort.sort(range(10000))', 'import bubble_sort', number=1)
