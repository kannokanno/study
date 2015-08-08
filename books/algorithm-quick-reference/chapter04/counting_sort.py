# -*- coding: utf-8 -*-
from benchmarker import Benchmarker
import random


def sort(buf, bin_size):
    bin = [0] * bin_size
    for i in buf:
        bin[i] += 1

    j = 0
    for i in range(bin_size):
        for n in range(bin[i]):
            buf[j] = i
            j += 1
    return buf


def random_data(size):
    ary = range(size)
    random.shuffle(ary)
    return ary

if __name__ == '__main__':
    with Benchmarker(width=35) as bm:
        ary = random_data(1000)
        with bm('random:size=1000'):
            sort(ary, 1000)
        ary = random_data(10000)
        with bm('random:size=10000'):
            sort(ary, 10000)
        ary = random_data(100000)
        with bm('random:size=100000'):
            sort(ary, 100000)

        ex = random_data(100)
        ary = range(900)
        ary.extend(ex)
        with bm('already sort of 90%:size=1000'):
            sort(ary, 1000)
        ex = random_data(1000)
        ary = range(9000)
        ary.extend(ex)
        with bm('already sort of 90%:size=10000'):
            sort(ary, 10000)
        ex = random_data(10000)
        ary = range(90000)
        ary.extend(ex)
        with bm('already sort of 90%:size=100000'):
            sort(ary, 100000)
