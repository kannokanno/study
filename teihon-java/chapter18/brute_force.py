# -*- coding: utf-8 -*-
import timeit
import unittest

def search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    if text_len == pattern_len == 0:
        return 0
    elif text_len == 0:
        return -1
    elif pattern_len == 0:
        return -1

    i = 0
    j = 0
    while i < text_len and j < pattern_len:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            # 途中まで比較したポインタ分戻る
            i = i - (j - 1)
            # パターンはポインタをリセット
            j = 0
    return i - j if j == pattern_len else -1

class Test(unittest.TestCase):
    def test_search(self):
        self.assertEquals(search("", ""), 0)
        self.assertEquals(search("", "a"), -1)
        self.assertEquals(search("a", ""), -1)
        self.assertEquals(search("japanese", "hoge"), -1)
        self.assertEquals(search("japanese", "an"), 3)
        self.assertEquals(search("ananman", "anm"), 2)

if __name__ == '__main__':
    unittest.main()
