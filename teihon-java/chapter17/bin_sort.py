# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    # ビンのサイズは10で固定とする
    bin_size = 10
    bin = [None] * bin_size
    for i in range(len(buf)):
        x = buf[i]
        bin[x] = x

    j = 0
    for i in range(bin_size):
        if bin[i] is not None:
            buf[j] = bin[i]
            j += 1
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
