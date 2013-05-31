# -*- coding: utf-8 -*-
import unittest

def solve(friends):
    return s1(friends)

def s1(friends):
    most = 0
    for i0, elems in enumerate(friends):
        tmp = 0
        for i, s in enumerate(elems):
            if s is 'Y':
                tmp += 1
                tmp += len([i2 for i2, s2 in enumerate(friends[i]) if i0 != i2 and s2 is 'Y'])

        if most < tmp:
            most = tmp
    return most

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(['NNN', 'NNN', 'NNN']), 0)
        self.assertEqual(solve(['NYNNN', 'YNYNN', 'NYNYN', 'NNYNY', 'NNNYN']), 4)
        self.assertEqual(solve([
            'NNNNYNNNNN',
            'NNNNYNYYNN',
            'NNNYYYNNNN',
            'NNYNNNNNNN',
            'YYYNNNNNNY',
            'NNYNNNNNYN',
            'NYNNNNNYNN',
            'NYNNNNYNNN',
            'NNNNNYNNNN',
            'NNNNYNNNNN',
            ]), 8)

if __name__ == '__main__':
    unittest.main()


