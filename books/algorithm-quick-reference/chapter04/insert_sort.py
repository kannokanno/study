# -*- coding: utf-8 -*-
from benchmarker import Benchmarker
import random


def sort(buf):
    for i in range(1, len(buf)):
        j = i
        while 0 < j and buf[j - 1] > buf[j]:
            tmp = buf[j]
            buf[j] = buf[j - 1]
            buf[j - 1] = tmp
            j -= 1
    return buf


def random_data(size):
    ary = range(size)
    random.shuffle(ary)
    return ary

if __name__ == '__main__':
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
