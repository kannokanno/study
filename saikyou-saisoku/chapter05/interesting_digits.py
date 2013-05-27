# -*- coding: utf-8 -*-
import unittest

def solve(base):
    return s2(base)

# 全探索(力技)
def s1(base):
    return [n for n in xrange(2, base) if check(n, base)]

def check(n, base):
    for i in xrange(base):
        for j in xrange(base):
            for k in xrange(base):
                is_baisuu = (i + j * base + k * base * base) % n == 0
                sum_is_not_baisuu = (i + j + k) % n != 0
                if is_baisuu and sum_is_not_baisuu:
                    return False
    return True

def s2(base):
    return [n for n in range(2, base) if (base - 1) % n == 0]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(10), [3, 9])
        self.assertEqual(solve(3), [2])
        self.assertEqual(solve(9), [2, 4, 8])
        self.assertEqual(solve(26), [5, 25])
        self.assertEqual(solve(30), [29])

if __name__ == '__main__':
    unittest.main()

