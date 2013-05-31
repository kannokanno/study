## 挿入ソート

### 時間計算量

最良 | 平均 | 最悪
------------------
O(n) | O(n^2) | O(n^2)

### 空間計算量

* ポインタ差し替えの場合、要素1つ分のメモリがあればいい

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

## クイックソート
