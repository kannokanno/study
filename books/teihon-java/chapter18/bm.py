# -*- coding: utf-8 -*-
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

    table = skip_table(pattern)
    # テキストの探索位置。パターン文字列の末尾(pattern_len - 1)にて初期化
    i = pattern_len - 1
    while i < text_len:
        j = pattern_len - 1 # パターンの探索位置(末尾から)
        while j >= 0: # 照合
            if text[i] != pattern[j]:
                break
            i -= 1
            j -= 1
        if j < 0:
            # 発見
            return i + 1 # whileの最後で1つ余計に左へずれているので戻す
        else:
            i += max(table[ord(text[i])], pattern_len - j)
    return -1

# charごと(256)のskip table
# 文字とインデックスを対応させるためにord()している
def skip_table(pattern):
    size = len(pattern)
    table = [size] * 256
    size -= 1
    for i in range(size):
        table[ord(pattern[i])] = size - i

    return table


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
