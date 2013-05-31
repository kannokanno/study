# -*- coding: utf-8 -*-
from benchmarker import Benchmarker
import random
import sys

def sort(buf):
    return quick_sort(buf, 0, len(buf) - 1)


def quick_sort(a, l, r):
    if l >= r:
        return a
    i = partition(a, l, r)
    quick_sort(a, l, i - 1)
    quick_sort(a, i + 1, r)
    return a


def partition(a, l, r):
    i = l - 1
    j = r
    p = pivot(a, l, r)
    while True:
        i += 1
        while a[i] < p:
            i += 1
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
    return i


def pivot(a, l, r):
    return a[r]


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
