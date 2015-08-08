# -*- coding: utf-8 -*-
import unittest


def solve(answer):
    # 最初のマッピングindexを1にするためのダミー空文字
    answer_mapping = ['',
                      'YYYY', 'YYYN', 'YYNY', 'YYNN',
                      'YNYY', 'YNYN', 'YNNY', 'YNNN',
                      'NYYY', 'NYYN', 'NYNY', 'NYNN',
                      'NNYY', 'NNYN', 'NNNY', 'NNNN',
                      ]
    return answer_mapping.index(answer)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve('YNNN'), 8)
        self.assertEqual(solve('NNNN'), 16)
        self.assertEqual(solve('YYYY'), 1)
        self.assertEqual(solve('NYNY'), 11)

if __name__ == '__main__':
    unittest.main()
