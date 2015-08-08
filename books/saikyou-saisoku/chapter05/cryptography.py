# -*- coding: utf-8 -*-
import operator
import unittest

def solve(numbers):
    if len(numbers) == 0:
        return 0
    return s2(numbers)

def s1(numbers):
    candidate = []
    for i in xrange(len(numbers)):
        tmp = numbers[:]
        tmp[i] = numbers[i] + 1
        candidate.append(reduce(operator.mul, tmp))
    return max(candidate)

def s2(numbers):
    min_idx = 0
    min_num = 10000
    for i in xrange(len(numbers)):
        if numbers[i] <= min_num:
            min_idx = i
            min_num = numbers[i]
    tmp = numbers[:]
    tmp[min_idx] = numbers[min_idx] + 1
    return reduce(operator.mul, tmp)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
                solve([]),
                0)
        self.assertEqual(
                solve([2, 3, 1]),
                12)
        self.assertEqual(
                solve([1, 3, 2, 1, 1, 3]),
                36)
        self.assertEqual(
                solve([1000, 999, 998, 997, 996, 995]),
                986074810223904000)
        self.assertEqual(
                solve([1, 1, 1, 1]),
                2)

if __name__ == '__main__':
    unittest.main()

