# -*- coding: utf-8 -*-
import liner_search
from benchmarker import Benchmarker


def search(data, key):
    liner_search.search(data, key)

if __name__ == '__main__':
    with Benchmarker(width=35) as bm:
        data = range(1000)
        middle = len(data) / 2
        with bm('data=range(1000), key=first'):
            search(data, 0)
        with bm('data=range(1000), key=middle'):
            search(data, middle)
        with bm('data=range(1000), key=not_found'):
            search(data, -1)

        data = range(10000)
        middle = len(data) / 2
        with bm('data=range(10,000), key=first'):
            search(data, 0)
        with bm('data=range(10,000), key=middle'):
            search(data, middle)
        with bm('data=range(10,000), key=not_found'):
            search(data, -1)

        data = range(100000)
        middle = len(data) / 2
        with bm('data=range(100,000), key=first'):
            search(data, 0)
        with bm('data=range(100,000), key=middle'):
            search(data, middle)
        with bm('data=range(100,000), key=not_found'):
            search(data, -1)

        data = range(1000000)
        middle = len(data) / 2
        with bm('data=range(100万), key=first'):
            search(data, 0)
        with bm('data=range(100万), key=middle'):
            search(data, middle)
        with bm('data=range(100万), key=not_found'):
            search(data, -1)

        data = range(100000000)
        middle = 100000000 / 2
        with bm('data=range(1億), key=first'):
            search(data, 0)
        with bm('data=range(1億), key=middle'):
            search(data, middle)
        with bm('data=range(1億), key=not_found'):
            search(data, -1)

        data = ['key']
        data.extend(['notkey'] * 999999)
        with bm('data=文字列100万件, key=first'):
            search(data, 'key')

        data = ['notkey'] * 499999
        data.append('key')
        data.extend(['notkey'] * 500000)
        with bm('data=文字列100万件, key=middle'):
            search(data, 'key')

        data = ['notkey'] * 1000000
        with bm('data=文字列100万件, key=not_found'):
            search(data, 'key')
