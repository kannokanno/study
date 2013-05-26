# -*- coding: utf-8 -*-
import unittest

def solve(first, second):
    return s1(first, second)

def s1(first, second):
    num = len(first)
    if num < 1:
        return 0
    elif num == 1 and first[0] == '':
        return 0

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

