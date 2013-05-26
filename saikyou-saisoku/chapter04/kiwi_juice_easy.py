# -*- coding: utf-8 -*-
import unittest

# 実装メモ
    # 注ぎ先の空き容量を取得
    # 注ぎ元の量を取得
    # 実際にどのくらい入るか計算
        # もし容量が足りなければ、残りの容量だけ移す
    # 入る量を注ぎ先に追加
    # 注ぎ元から出てった量を引く

def solve(capacities, bottles, from_id, to_id):
    for i, _from in enumerate(from_id):
        _to = to_id[i]
        sum = bottles[_from] + bottles[_to]
        bottles[_to]   = min(sum, capacities[_to])
        bottles[_from] = sum - bottles[_to]
    return bottles

class Test(unittest.TestCase):
    def test(self):
        # 通常
        self.assertEqual(
                solve([20, 20], [5, 8], [0], [1]),
                [0, 13])

        # 注ぐ量が溢れる
        self.assertEqual(
                solve([10, 10], [5, 8], [0], [1]),
                [3, 10])

        # 連続して注ぐ
        self.assertEqual(
                solve([30, 20, 10], [10, 5, 5], [0, 1, 2], [1, 2, 0]),
                [10, 10, 0])

        # 注ぎ元が空になる
        self.assertEqual(
                solve([14, 35, 86, 58, 25, 62],
                      [6, 34, 27, 38, 9, 60],
                      [1, 2, 4, 5, 3, 3, 1, 0],
                      [0, 1, 2, 4, 2, 5, 3, 1]),
                [0, 14, 65, 35, 25, 35])

        # 注ぎ先がすでに満杯。かな？
        self.assertEqual(
                solve([700000, 800000, 900000, 1000000],
                      [478478, 478478, 478478, 478478],
                      [2, 3, 2, 0, 1],
                      [0, 1, 1, 3, 2]),
                [0, 156956, 900000, 856956])

if __name__ == '__main__':
    unittest.main()
