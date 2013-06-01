## リニアサーチ(線形探索)

### 時間計算量

| 最良 | 平均   | 最悪   |
|------|--------|--------|
| O(1) | O(n) | O(n) |

### 計測

liner_search_benchmark.py

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                      user       sys     total      real
    data=range(1000), key=first           0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=middle          0.0000    0.0000    0.0000    0.0001
    data=range(1000), key=not_found       0.0000    0.0000    0.0000    0.0002
    data=range(10,000), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=middle        0.0000    0.0000    0.0000    0.0007
    data=range(10,000), key=not_found     0.0000    0.0000    0.0000    0.0018
    data=range(100,000), key=first        0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=middle       0.0100    0.0000    0.0100    0.0069
    data=range(100,000), key=not_found    0.0200    0.0000    0.0200    0.0159
    data=range(100万), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=middle        0.0600    0.0000    0.0600    0.0640
    data=range(100万), key=not_found     0.1400    0.0000    0.1400    0.1339
    data=range(1億), key=first           0.0000    0.0100    0.0100    0.0078
    data=range(1億), key=middle          6.7600    0.4900    7.2500    8.5581
    data=range(1億), key=not_found      13.8100    1.5400   15.3500   22.3503
    data=文字列100万件, key=first    0.0000    0.0000    0.0000    0.0000
    data=文字列100万件, key=middle   0.0700    0.0000    0.0700    0.0652
    data=文字列100万件, key=not...   0.1300    0.0000    0.1300    0.1303

liner_search_mem_profile.py

    100万件:最悪時
    Partition of a set of 25366 objects. Total size = 3236792 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0  10960  43   927184  29    927184  29 str
         1   5785  23   466696  14   1393880  43 tuple
         2    314   1   211568   7   1605448  50 dict (no owner)
         3    199   1   210088   6   1815536  56 dict of type
         4     65   0   206360   6   2021896  62 dict of module
         5   1595   6   204160   6   2226056  69 types.CodeType
         6   1558   6   186960   6   2413016  75 function
         7    199   1   177008   5   2590024  80 type
         8    124   0   135328   4   2725352  84 dict of class
         9   1044   4    83520   3   2808872  87 __builtin__.wrapper_descriptor
    <91 more rows. Type e.g. '_.more' to view.>

### 特徴

* 実装が簡単
* 探索アルゴリズムの中では遅い部類
* equalsの処理速度にも依存する

### 感想

* あれ、単なる数値/文字列検索程度なら100万件でも十分早い？
* 億になるとアカン
