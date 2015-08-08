# -*- coding: utf-8 -*-
import oa_hash
from guppy import hpy


def table(size):
    table = oa_hash.HashTable(size)
    for i in xrange(size):
        table.add(i, 'value' + str(i))
    return table


def search(data, key):
    data.get(key)

if __name__ == '__main__':
    h = hpy()

    print "100万件:最悪時"
    data = table(1000000)
    search(data, -1)
    print h.heap()
