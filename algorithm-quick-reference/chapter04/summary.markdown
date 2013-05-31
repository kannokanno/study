## 挿入ソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n) | O(n^2) | O(n^2)

### 空間計算量

* O(1)

### 計測

insert_sort.py

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                    user       sys     total      real
    random:size=1000                    0.2300    0.0000    0.2300    0.2260
    random:size=10000                  22.8500    0.0700   22.9200   23.6168
    random:size=100000               1780.5400    2.1500 1782.6900 1786.0807
    already sort of 90%:size=1000       0.0600    0.0000    0.0600    0.0610
    already sort of 90%:size=10000      6.0200    0.0100    6.0300    6.0341
    already sort of 90%:size=100000   604.9200    0.6000  605.5200  605.9159

    ## Ranking                         real
    already sort of 90%:size=1000    0.0610 (100.0%) *************************
    random:size=1000                 0.2260 ( 27.0%) *******
    already sort of 90%:size=10000   6.0341 (  1.0%)
    random:size=10000               23.6168 (  0.3%)
    already sort of 90%:size=100000 605.9159 (  0.0%)
    random:size=100000            1786.0807 (  0.0%)

    ## Ratio Matrix                    real       [01]       [02]       [03]       [04]       [05]       [06]
    [01] already sort of 90%:size=1000   0.0610     100.0%     370.6%    9894.2%   38724.9%  993532.1% 2928671.3%
    [02] random:size=1000            0.2260      27.0%     100.0%    2669.8%   10449.3%  268090.2%  790259.3%
    [03] already sort of 90%:size=10000   6.0341       1.0%       3.7%     100.0%     391.4%   10041.5%   29599.7%
    [04] random:size=10000          23.6168       0.3%       1.0%      25.6%     100.0%    2565.6%    7562.8%
    [05] already sort of 90%:size=100000 605.9159       0.0%       0.0%       1.0%       3.9%     100.0%     294.8%
    [06] random:size=100000       1786.0807       0.0%       0.0%       0.3%       1.3%      33.9%     100.0%


### 特徴

* 特定条件では全ソートアルゴリズム中、最速の部類
* 特定条件とは
    * 要素数が少ない
    * 入力配列のほとんどの要素が整列ずみ

### 感想

* 平均/最悪がO(n^2)ってのは伊達じゃない
    * 要素10倍で計算量100倍だもんなー

## クイックソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n log n) | O(n log n) | O(n^2)

### 空間計算量

* O(n)

### 計測

quick_sort.py

* 再帰版
* pivot(軸)は常にrightにする
    * つまり、ほとんどが整列ずみの場合には著しく計算量が増す

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                      user       sys     total      real
    random:size=1000                      0.0000    0.0000    0.0000    0.0051
    random:size=10000                     0.0700    0.0000    0.0700    0.0655
    random:size=100000                    0.7700    0.0000    0.7700    0.7695
    already sort of 90%:size=1000         0.0100    0.0000    0.0100    0.0106
    already sort of 90%:size=10000        0.6900    0.0000    0.6900    0.6927
    already sort of 90%:size=100000      70.7300    0.0900   70.8200   70.8824

    ## Ranking                              real
    random:size=1000                      0.0051 (100.0%) *************************
    already sort of 90%:size=1000         0.0106 ( 48.3%) ************
    random:size=10000                     0.0655 (  7.8%) **
    already sort of 90%:size=10000        0.6927 (  0.7%)
    random:size=100000                    0.7695 (  0.7%)
    already sort of 90%:size=100000      70.8824 (  0.0%)

    ## Ratio Matrix                         real       [01]       [02]       [03]       [04]       [05]       [06]
    [01] random:size=1000                 0.0051     100.0%     207.1%    1277.8%   13505.4%   15002.6% 1381966.4%
    [02] already sort of 90%:size=1000    0.0106      48.3%     100.0%     617.0%    6521.4%    7244.4%  667315.6%
    [03] random:size=10000                0.0655       7.8%      16.2%     100.0%    1056.9%    1174.1%  108149.7%
    [04] already sort of 90%:size=10000   0.6927       0.7%       1.5%       9.5%     100.0%     111.1%   10232.7%
    [05] random:size=100000               0.7695       0.7%       1.4%       8.5%      90.0%     100.0%    9211.5%
    [06] already sort of 90%:size=100000  70.8824       0.0%       0.0%       0.1%       1.0%       1.1%     100.0%


### 特徴

* 速い！
* 分割する際の一方の配列が偏るほどにO(n^2)に近づく
* 再帰版だとスタックを食う
* 非再帰版を使ってスタックを節約したり、小さい配列には挿入ソートを使うなど改良可能
    * それでも最悪時のO(n^2)は免れないらしい
* pivotの決め方に戦略がいくつかある

### 感想

* 挿入ソートやったあとだから余計早く感じた
* 10万件でも1秒以内とか速い
* 90%ソート済みのデータでも挿入ソートより断然速いので、なんか間違っているかも

## 選択ソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n^2) | O(n^2) | O(n^2)

### 空間計算量

* O(1)かな？

### 計測

selection_sort.py

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                      user       sys     total      real
    random:size=1000                      0.0700    0.0000    0.0700    0.0695
    random:size=10000                     6.6500    0.0100    6.6600    6.6657
    random:size=100000                  955.2500    1.6200  956.8700  957.8695
    already sort of 90%:size=1000         0.0800    0.0000    0.0800    0.0726
    already sort of 90%:size=10000        6.5700    0.0100    6.5800    6.6002
    already sort of 90%:size=100000     700.4900    1.3300  701.8200  703.0027

    ## Ranking                              real
    random:size=1000                      0.0695 (100.0%) *************************
    already sort of 90%:size=1000         0.0726 ( 95.7%) ************************
    already sort of 90%:size=10000        6.6002 (  1.1%)
    random:size=10000                     6.6657 (  1.0%)
    already sort of 90%:size=100000     703.0027 (  0.0%)
    random:size=100000                  957.8695 (  0.0%)

    ## Ratio Matrix                         real       [01]       [02]       [03]       [04]       [05]       [06]
    [01] random:size=1000                 0.0695     100.0%     104.5%    9502.9%    9597.2% 1012171.3% 1379124.3%
    [02] already sort of 90%:size=1000    0.0726      95.7%     100.0%    9090.6%    9180.8%  968258.0% 1319290.5%
    [03] already sort of 90%:size=10000   6.6002       1.1%       1.1%     100.0%     101.0%   10651.2%   14512.6%
    [04] random:size=10000                6.6657       1.0%       1.1%      99.0%     100.0%   10546.6%   14370.1%
    [05] already sort of 90%:size=100000 703.0027       0.0%       0.0%       0.9%       0.9%     100.0%     136.3%
    [06] random:size=100000             957.8695       0.0%       0.0%       0.7%       0.7%      73.4%     100.0%

あれ、挿入ソートより速いことがある...。実装間違っているか？

### 特徴

* つねにO(n^2)。遅すぎる
* 実装は簡単

### 感想

* 遅い。
* 気づかずにこのアルゴリズムで実装してしまわないように気をつけよう

## ヒープソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n log n) | O(n log n) | O(n log n)

### 空間計算量

* O(1) 〜 O(n)
    * ヒープを対象配列自体として扱えばO(1)
    * ヒープを対象配列自体ではなく別実装にしているとO(n)

### 計測

heap_sort.py

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                      user       sys     total      real
    random:size=1000                      0.0100    0.0000    0.0100    0.0115
    random:size=10000                     0.1300    0.0000    0.1300    0.1382
    random:size=100000                    1.6700    0.0000    1.6700    1.6766
    already sort of 90%:size=1000         0.0100    0.0000    0.0100    0.0092
    already sort of 90%:size=10000        0.1200    0.0000    0.1200    0.1248
    already sort of 90%:size=100000       1.5700    0.0000    1.5700    1.5659

    ## Ranking                              real
    already sort of 90%:size=1000         0.0092 (100.0%) *************************
    random:size=1000                      0.0115 ( 79.9%) ********************
    already sort of 90%:size=10000        0.1248 (  7.4%) **
    random:size=10000                     0.1382 (  6.7%) **
    already sort of 90%:size=100000       1.5659 (  0.6%)
    random:size=100000                    1.6766 (  0.5%)

    ## Ratio Matrix                         real     [01]     [02]     [03]     [04]     [05]     [06]
    [01] already sort of 90%:size=1000    0.0092   100.0%   125.2%  1353.2%  1498.8% 16985.4% 18185.7%
    [02] random:size=1000                 0.0115    79.9%   100.0%  1080.8%  1197.1% 13565.9% 14524.5%
    [03] already sort of 90%:size=10000   0.1248     7.4%     9.3%   100.0%   110.8%  1255.2%  1343.9%
    [04] random:size=10000                0.1382     6.7%     8.4%    90.3%   100.0%  1133.3%  1213.3%
    [05] already sort of 90%:size=100000   1.5659     0.6%     0.7%     8.0%     8.8%   100.0%   107.1%

### 特徴

* 常にO(n log n)と速い
* クイックソートで性能が出ない場合の救世主になり得る
    * しかし平均時の性能ではクイックソートに劣るらしい
    * 結果を見ると、クイックソートの最悪時ケースでも安定して速い
    * クイックソートの最良時ケースならクイックソートの方が速い
* 実装に再帰版を使うか非再帰版を使うかでスタックの使用量が変わる
* 実装が少し複雑

### 感想

* 速い...
* サクッと書けない
* 概念や実装面でまだ細かいところが分かっていない

## 数え上げソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n) | O(n) | O(n)

### 空間計算量

* O(k)
    * 数え上げ用の配列サイズkによる

### 計測

counting_sort.py

    ## benchmarker:       release 3.0.1 (for python)
    ## python platform:   darwin [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)]
    ## python version:    2.7.1
    ## python executable: /Users/kanno/.virtualenvs/work/bin/python

    ##                                      user       sys     total      real
    random:size=1000                      0.0000    0.0000    0.0000    0.0010
    random:size=10000                     0.0100    0.0000    0.0100    0.0104
    random:size=100000                    0.1200    0.0000    0.1200    0.1231
    already sort of 90%:size=1000         0.0000    0.0000    0.0000    0.0010
    already sort of 90%:size=10000        0.0100    0.0000    0.0100    0.0105
    already sort of 90%:size=100000       0.1000    0.0000    0.1000    0.1040

    ## Ranking                              real
    already sort of 90%:size=1000         0.0010 (100.0%) *************************
    random:size=1000                      0.0010 ( 99.1%) *************************
    random:size=10000                     0.0104 (  9.9%) **
    already sort of 90%:size=10000        0.0105 (  9.8%) **
    already sort of 90%:size=100000       0.1040 (  1.0%)
    random:size=100000                    0.1231 (  0.8%)

    ## Ratio Matrix                         real     [01]     [02]     [03]     [04]     [05]     [06]
    [01] already sort of 90%:size=1000    0.0010   100.0%   100.9%  1007.4%  1018.4% 10065.8% 11914.0%
    [02] random:size=1000                 0.0010    99.1%   100.0%   998.6%  1009.6%  9978.2% 11810.5%
    [03] random:size=10000                0.0104     9.9%    10.0%   100.0%   101.1%   999.2%  1182.7%
    [04] already sort of 90%:size=10000   0.0105     9.8%     9.9%    98.9%   100.0%   988.4%  1169.8%
    [05] already sort of 90%:size=100000   0.1040     1.0%     1.0%    10.0%    10.1%   100.0%   118.4%
    [06] random:size=100000               0.1231     0.8%     0.8%     8.5%     8.5%    84.5%   100.0%

### 特徴

* 特定条件でしか使えないが、O(n)と最速の部類
* 数え上げ用の配列の大きさと相談
* 実装も楽

### 感想

* 速すぎる
