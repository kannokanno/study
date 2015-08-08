# -*- coding: utf-8 -*-
from benchmarker import Benchmarker
import random
import sys

def sort(buf):
    n = len(buf)
    start = n / 2
    while start >= 0:
        down_heap(buf, start, n - 1)
        start -= 1

    for i in range(n - 1, 0, -1):
        tmp = buf[0]
        buf[0] = buf[i]
        buf[i] = tmp
        down_heap(buf, 0, i - 1)

    return buf


def down_heap(a, start, end):
    v = a[start]
    i = start
    while i <= end / 2:
        j = i * 2
        if j + 1 <= end and a[j] > a[j + 1]:
            j += 1
        if v <= a[j]:
            break
        a[i] = a[j]
        i = j
    a[i] = v


def random_data(size):
    ary = range(size)
    random.shuffle(ary)
    return ary

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    with Benchmarker(width=35) as bm:
        ary = random_data(1000)
        with bm('random:size=1000'):
            sort(ary)
        ary = random_data(10000)
        with bm('random:size=10000'):
            sort(ary)
        ary = random_data(100000)
        with bm('random:size=100000'):
            sort(ary)

        ex = random_data(100)
        ary = range(900)
        ary.extend(ex)
        with bm('already sort of 90%:size=1000'):
            sort(ary)
        ex = random_data(1000)
        ary = range(9000)
        ary.extend(ex)
        with bm('already sort of 90%:size=10000'):
            sort(ary)
        ex = random_data(10000)
        ary = range(90000)
        ary.extend(ex)
        with bm('already sort of 90%:size=100000'):
            sort(ary)


