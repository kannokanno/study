# -*- coding: utf-8 -*-
import unittest

def solve():
    return None

class Test(unittest.TestCase):
    def test(self):
        # 通常のケース
        self.assertEqual(
                solve(),
                None)

if __name__ == '__main__':
    unittest.main()
