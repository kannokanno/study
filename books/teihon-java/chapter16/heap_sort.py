# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    n = len(buf)
    start = n / 2
    while start >= 0:
        down_heap(buf, start, n - 1)
        start -= 1

    for i in range(n - 1, 0, -1):
        tmp = buf[0]
        buf[0] = buf[i]
        buf[i] = tmp
        down_heap(buf, 0, i - 1)

    # 他のテストと合わせるために昇順に並び替え
    buf.reverse()
    return buf

def down_heap(a, start, end):
    v = a[start]
    i = start
    while i <= end / 2:
        j = i * 2
        if j + 1 <= end and a[j] > a[j + 1]:
            j += 1
        if v <= a[j]:
            break
        a[i] = a[j]
        i = j
    a[i] = v

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 3, 6, 1, 3, 2, 5, 7, 5, 4]), [1, 2, 3, 3, 3, 4, 5, 5, 6, 7])
        self.assertEquals(sort([30, 30, 61, 12, 3, 21, 53, 7, 53, 4]), [3, 4, 7, 12, 21, 30, 30, 53, 53, 61])

if __name__ == '__main__':
    unittest.main()

