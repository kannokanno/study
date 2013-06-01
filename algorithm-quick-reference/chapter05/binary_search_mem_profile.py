# -*- coding: utf-8 -*-
import binary_search
from guppy import hpy


def search(data, key):
    binary_search.search(data, key)

if __name__ == '__main__':
    h = hpy()

    print "100万件:最悪時"
    search(range(1000000), -1)
    print h.heap()
