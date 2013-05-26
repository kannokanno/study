# -*- coding: utf-8 -*-
import unittest

def solve(first, second):
    num = len(first)
    if num < 1:
        return 0
    elif num == 1 and first[0] == '':
        return 0
    return s2(num, first, second)

def s1(num, first, second):
    talks = {}
    for i in xrange(num):
        talks[first[i]] = 0
        talks[second[i]] = 0
    for k, v in talks.items():
        for i in xrange(num):
            if first[i] == k or second[i] == k:
                v += 1
        talks[k] = v
    return max(talks.values())

def s2(num, first, second):
    ans = 0
    for i in xrange(num):
        f = 0
        s = 0
        for j in xrange(num):
            if first[i] == first[j]:   f += 1
            if first[i] == second[j]:  f += 1
            if second[i] == first[j]:  s += 1
            if second[i] == second[j]: s += 1
        ans = max([f, ans])
        ans = max([s, ans])
    return ans

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
                solve([], []),
                0)
        self.assertEqual(
                solve([''], ['']),
                0)
        self.assertEqual(
                solve(['aa', 'bb', 'cc', 'aa'],
                      ['ee', 'aa', 'aa', 'ff']),
                4)
        self.assertEqual(
                solve(['aa', 'bb', 'cc', 'ee'],
                      ['ff', 'gg', 'hh', 'ii']),
                1)
        self.assertEqual(
                solve(['aa', 'bb', 'cc', 'ee'],
                      ['ff', 'gg', 'hh', 'gg']),
                2)

if __name__ == '__main__':
    unittest.main()

