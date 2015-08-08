# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    for i in range(len(buf) - 1):
        _min = buf[i]
        p = i
        for j in range(i+1, len(buf)):
            if buf[j] < _min:
                _min = buf[j]
                p = j
        buf[p] = buf[i]
        buf[i] = _min
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()

