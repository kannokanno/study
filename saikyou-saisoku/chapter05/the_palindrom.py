# -*- coding: utf-8 -*-
import unittest

def solve(s):
    return s1(s)

# これよく分からんかった
def s1(s):
    size = len(s)
    i = size
    while True:
        flag = True
        for j in xrange(size):
            pos = (i - j - 1)
            if pos < size and s[j] != s[pos]:
                flag = False
                break;
        if flag:
            return i
        i += 1

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve('abab'), 5)
        self.assertEqual(solve('abacaba'), 7)

if __name__ == '__main__':
    unittest.main()

