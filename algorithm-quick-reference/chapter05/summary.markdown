## リニアサーチ(線形探索)

### 時間計算量

| 最良 | 平均   | 最悪   |
|------|--------|--------|
| O(1) | O(n) | O(n) |

### 計測

* liner_search_benchmark.py

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

* liner_search_mem_profile.py

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
* 入力データの整列状態に制限がない(整列されている必要がない)
* 探索アルゴリズムの中では遅い部類
* equalsの処理速度にも依存する

### 感想

* あれ、単なる数値/文字列検索程度なら100万件でも十分早い？
* 億になるとアカン

## バイナリサーチ(二分探索)

### 時間計算量

| 最良 | 平均   | 最悪   |
|------|--------|--------|
| O(1) | O(log n) | O(log n) |

### 計測

* binary_search_benchmark.py

    ##                                      user       sys     total      real
    data=range(1000), key=first           0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=middle          0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=not_found       0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=not_found     0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=first        0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=middle       0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=not_found    0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=not_found     0.0000    0.0000    0.0000    0.0000

* binary_search_mem_profile.py

    100万件:最悪時
    Partition of a set of 25369 objects. Total size = 3237104 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0  10963  43   927448  29    927448  29 str
         1   5785  23   466744  14   1394192  43 tuple
         2    314   1   211568   7   1605760  50 dict (no owner)
         3    199   1   210088   6   1815848  56 dict of type
         4     65   0   206360   6   2022208  62 dict of module
         5   1595   6   204160   6   2226368  69 types.CodeType
         6   1558   6   186960   6   2413328  75 function
         7    199   1   177008   5   2590336  80 type
         8    124   0   135328   4   2725664  84 dict of class
         9   1044   4    83520   3   2809184  87 __builtin__.wrapper_descriptor
    <91 more rows. Type e.g. '_.more' to view.>

### 特徴

* 入力データが整列されている必要がある
    * 整列状態を維持するために、挿入や削除に負荷がかかる
        * リストを使えば多少マシ。配列だときつい
* メモリ内で収まらず二次記憶を使うようになると効率悪い
* 二分木(平衡二分木)を使うのが良い

### 感想

* ちゃんと計測できているのかこれ
    * 特性上、早いのは分かるんだけど、数字上は一瞬じゃないか...

## ハッシュ法(チェインハッシュ)

### 時間計算量

| 最良 | 平均   | 最悪   |
|------|--------|--------|
| O(1) | O(1) | O(n) |

### 計測

* chain_hash_search_benchmark.py

    * テーブルサイズ = n/3

    ##                                      user       sys     total      real
    data=range(1000), key=first           0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=middle          0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=not_found       0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=not_found     0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=first        0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=middle       0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=not_found    0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=not_found     0.0000    0.0000    0.0000    0.0000

    * テーブルサイズ = n/100

    ##                                      user       sys     total      real
    data=range(1000), key=first           0.0000    0.0000    0.0000    0.0001
    data=range(1000), key=middle          0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=not_found       0.0000    0.0000    0.0000    0.0001
    data=range(10,000), key=first         0.0000    0.0000    0.0000    0.0002
    data=range(10,000), key=middle        0.0000    0.0000    0.0000    0.0001
    data=range(10,000), key=not_found     0.0000    0.0000    0.0000    0.0002
    data=range(100,000), key=first        0.0000    0.0000    0.0000    0.0005
    data=range(100,000), key=middle       0.0000    0.0000    0.0000    0.0003
    data=range(100,000), key=not_found    0.0000    0.0000    0.0000    0.0005
    data=range(100万), key=first         0.0000    0.0000    0.0000    0.0006
    data=range(100万), key=middle        0.0000    0.0000    0.0000    0.0003
    data=range(100万), key=not_found     0.0000    0.0000    0.0000    0.0006

* chain_hash_search_mem_profile.py

    * テーブルサイズ = n/100

    100万件:最悪時
    Partition of a set of 4025301 objects. Total size = 427322576 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0 1000000  25 280000000  66 280000000  66 dict of chain_hash.Cell
         1 1000000  25 72000000  17 352000000  82 chain_hash.Cell
         2 1010984  25 48929128  11 400929128  94 str
         3 1000548  25 24013152   6 424942280  99 int
         4   5805   0   468328   0 425410608 100 tuple
         5    314   0   211568   0 425622176 100 dict (no owner)
         6    199   0   210088   0 425832264 100 dict of type
         7     65   0   206360   0 426038624 100 dict of module
         8   1601   0   204928   0 426243552 100 types.CodeType
         9   1564   0   187680   0 426431232 100 function
    <95 more rows. Type e.g. '_.more' to view.>

### 特徴

* 入力データに整列条件はない
* ハッシュテーブル構築のためのコストがある
* ハッシュ関数の戦略に依存
    * 最悪すべてのデータが同じハッシュ値になると、O(n)の探索になるし空き容量も無駄になる
* しかし早い

### 感想

* 早いで
* 計測に関しては、ハッシュ関数の衝突率とかも調べないとなんとも言えないな
* 計測結果には表示されないけど、このサンプルコードだとハッシュ表構築にめっちゃ時間かかっている
* セル(連結リスト)がめっちゃメモリ食っている
* 上記計測だと最悪時が試せていないな(ハッシュ値がすべて同じ場合)

## ハッシュ法(オープンアドレス)

### 時間計算量

| 最良 | 平均   | 最悪   |
|------|--------|--------|
| O(1) | O(1) | O(b) |

※b = ハッシュテーブルのサイズ  
  n個のデータを全て入れようと思えば最終的にnサイズ必要か？

### 計測

* oa_hash_search_benchmark.py

    ##                                      user       sys     total      real
    data=range(1000), key=first           0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=middle          0.0000    0.0000    0.0000    0.0000
    data=range(1000), key=not_found       0.0000    0.0000    0.0000    0.0017
    data=range(10,000), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(10,000), key=not_found     0.0100    0.0000    0.0100    0.0116
    data=range(100,000), key=first        0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=middle       0.0000    0.0000    0.0000    0.0000
    data=range(100,000), key=not_found    0.1300    0.0000    0.1300    0.1276
    data=range(100万), key=first         0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=middle        0.0000    0.0000    0.0000    0.0000
    data=range(100万), key=not_found     1.1800    0.0000    1.1800    1.1783

* oa_hash_search_mem_profile.py

    100万件:最悪時
    Partition of a set of 3025298 objects. Total size = 155366832 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0 1005804  33 72468336  47  72468336  47 tuple
         1 1010985  33 48929240  31 121397576  78 str
         2 1000547  33 24013128  15 145410704  94 int
         3    175   0  8151160   5 153561864  99 list
         4    314   0   211568   0 153773432  99 dict (no owner)
         5    199   0   210088   0 153983520  99 dict of type
         6     65   0   206360   0 154189880  99 dict of module
         7   1601   0   204928   0 154394808  99 types.CodeType
         8   1564   0   187680   0 154582488  99 function
         9    199   0   177008   0 154759496 100 type
    <93 more rows. Type e.g. '_.more' to view.>

### 特徴

* 入力データに整列条件はない
* ハッシュテーブル構築のためのコストがある
* ハッシュ関数の戦略に依存
* しかし早い

### 感想

* 早いで
* 計測に関しては、ハッシュ関数の衝突率とかも調べないとなんとも言えないな
* 計測結果には表示されないけど、このサンプルコードだとハッシュ表構築にめっちゃ時間かかっている
* チェインハッシュよりメモリ使用量少ない。tuple使わなければもっと削減できそう
* 最悪時でも100万程度ならそこまで悪く無いか？
