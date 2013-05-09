# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    # NOTE: len(buf) > 2の場合にgapを大きくすると失敗する(追加制御が必要)
    # NOTE: gapが奇数でも失敗するね
    gap = 2
    h = len(buf) / gap
    while h > 0:
        for i in range(h, len(buf)):
            tmp = buf[i]
            j = i - h
            while 0 <= j and buf[j] > tmp :
                buf[j + h] = buf[j]
                j -= h
            buf[j + h] = tmp
        h /= gap

    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()



