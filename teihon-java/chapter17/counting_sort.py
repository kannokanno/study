# -*- coding: utf-8 -*-
import unittest

# 書籍とは違う実装になった。
# 分布図を使っていないんだけど、ロジック勘違いしている？
def sort(buf):
    # ビンのサイズは10で固定とする
    bin_size = 10
    bin = [0] * bin_size
    for i in range(len(buf)):
        x = buf[i]
        bin[x] += 1

    j = 0
    for i in range(bin_size):
        for n in range(bin[i]):
            buf[j] = i
            j += 1
    return buf

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 3, 6, 1, 3, 2, 5, 7, 5, 4]), [1, 2, 3, 3, 3, 4, 5, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
