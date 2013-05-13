# -*- coding: utf-8 -*-
import unittest

# http://www.geocities.jp/m_hiroi/light/pyalgo07.html から引用
def sort(buf):
    size = len(buf)
    work = [0] * size
    count = [0] * 256

    for i in range(4):
        shift = i * 8
        for x in range(256):
            count[x] = 0
        for x in range(size):
            count[(buf[x] >> shift) & 0xff] += 1
        for x in range(256):
            count[x] += count[x - 1]
        for x in range(size - 1, -1, -1):
            y = (buf[x] >> shift) & 0xff
            count[y] -= 1
            work[count[y]] = buf[x]
        temp = buf
        buf = work
        work = temp
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 3, 6, 1, 3, 2, 5, 7, 5, 4]), [1, 2, 3, 3, 3, 4, 5, 5, 6, 7])
        self.assertEquals(sort([30, 30, 61, 12, 3, 21, 53, 7, 53, 4]), [3, 4, 7, 12, 21, 30, 30, 53, 53, 61])

if __name__ == '__main__':
    unittest.main()

