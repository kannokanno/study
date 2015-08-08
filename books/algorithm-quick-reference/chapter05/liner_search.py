# -*- coding: utf-8 -*-
def search(data, key):
    for i, x in enumerate(data):
        if x == key:
            return i
    return None
