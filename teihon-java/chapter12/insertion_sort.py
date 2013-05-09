# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    for i in range(1, len(buf)):
        j = i
        while 0 < j and buf[j - 1] > buf[j] :
            tmp = buf[j]
            buf[j] = buf[j - 1]
            buf[j - 1] = tmp
            j -= 1
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()


