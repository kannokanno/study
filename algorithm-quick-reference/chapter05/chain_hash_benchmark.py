# -*- coding: utf-8 -*-
import chain_hash
from benchmarker import Benchmarker


def search(data, key):
    data.get(key)


def table(size):
    table = chain_hash.HashTable(size / 100)
    for i in xrange(size):
        table.add(i, 'value' + str(i))
    return table

if __name__ == '__main__':
    with Benchmarker(width=35) as bm:
        data = table(1000)
        middle = 1000 / 2
        with bm('data=range(1000), key=first'):
            search(data, 0)
        with bm('data=range(1000), key=middle'):
            search(data, middle)
        with bm('data=range(1000), key=not_found'):
            search(data, -1)

        data = table(10000)
        middle = 10000 / 2
        with bm('data=range(10,000), key=first'):
            search(data, 0)
        with bm('data=range(10,000), key=middle'):
            search(data, middle)
        with bm('data=range(10,000), key=not_found'):
            search(data, -1)

        data = table(100000)
        middle = 100000 / 2
        with bm('data=range(100,000), key=first'):
            search(data, 0)
        with bm('data=range(100,000), key=middle'):
            search(data, middle)
        with bm('data=range(100,000), key=not_found'):
            search(data, -1)

        data = table(1000000)
        middle = 1000000 / 2
        with bm('data=range(100万), key=first'):
            search(data, 0)
        with bm('data=range(100万), key=middle'):
            search(data, middle)
        with bm('data=range(100万), key=not_found'):
            search(data, -1)
