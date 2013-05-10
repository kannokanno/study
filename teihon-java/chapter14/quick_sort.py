# -*- coding: utf-8 -*-
import unittest

def sort(buf):
    """クイックソート

    引数
        元配列:buf

    戻り値
        ソートされた配列

    処理
        buf.size <= 2 => return buf
        else =>
            int l = 0
            int r = buf.size - 1
            int p = ピボットを選ぶ(buf, l, r)
            再帰で左の部分配列を整列(a, l, p - 1)
            再帰で右の部分配列を整列(a, p + 1, r)
    """
    print "====SORT===="
    print buf
    return quick_sort(buf, 0, len(buf) - 1)

def quick_sort(a, l, r):
    if l >= r:
        return a
    i = partition(a, l, r)
    quick_sort(a, l, i - 1)
    quick_sort(a, i + 1, r)
    return a

def partition(a, l, r):
    """ 配列を分割(整列)

    引数
        元配列      :a
        左端ポインタ:l
        右端ポインタ:r

    戻り値
        配置されたピボットの位置

    処理
        以下を繰り返す
            l = a[l]がpivotよりも大きくなるまでポインタを右に移動
            r = l < r が成り立ち、かつa[r]がpivotよりも小さくなるまでポインタを左に移動
            if lとrがぶつかったら
                return

            a[l]とa[r]を入れかえる

        a[l]とpivotを入れかえる
        ポインタlを返す
    """
    i = l - 1
    j = r
    p = pivot(a, l, r)
    while True:
        # ポインタ(i)を右に移動
        i += 1
        while a[i] < p:
            i += 1
        # ポインタ(j)を左に移動
        j -= 1
        while i < j and p < a[j]:
            j -= 1
        if i >= j:
            break
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    tmp = a[i]
    a[i] = a[r]
    a[r] = tmp
    print "  ", a
    return i

def pivot(a, l, r):
    return a[r]

class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEquals(sort([1]), [1])
        self.assertEquals(sort([1, 2]), [1, 2])
        self.assertEquals(sort([2, 1]), [1, 2])
        self.assertEquals(sort([3, 6, 1, 2, 5, 7, 4]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()

