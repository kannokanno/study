# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    n = len(buf)
    if n < 2:
        return buf
    mid = n / 2
    a = sort(buf[0:mid])
    b = sort(buf[mid:n])
    print "a:", a, "b:", b
    m = merge(a, b)
    print "  =>", m
    return m

def merge(a, b):
    c = []
    while a != [] and b != []:
        x = a.pop(0) if a[0] < b[0] else b.pop(0)
        c.append(x)
    c.extend(a)
    c.extend(b)
    return c

class Test(unittest.TestCase):
    def test_sort(self):
        #self.assertEquals(sort([1]), [1])
        #self.assertEquals(sort([1, 2]), [1, 2])
        #self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()


