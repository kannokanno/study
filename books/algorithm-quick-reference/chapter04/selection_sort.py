# -*- coding: utf-8 -*-
from benchmarker import Benchmarker
import random
import sys

def sort(buf):
    for i in range(len(buf) - 1):
        _min = buf[i]
        p = i
        for j in range(i+1, len(buf)):
            if buf[j] < _min:
                _min = buf[j]
                p = j
        buf[p] = buf[i]
        buf[i] = _min
    return buf


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

