# -*- coding: utf-8 -*-
def reverse(data):
    for i in range(len(data) -1, -1, -1):
        yield data[i]

g = reverse
print g
for c in g('python'):
    print c,
print

# ジェネレータ式
# 丸括弧で書く(角括弧だと内包表記になるので間違えないように)

# 平方根
g = (i * i for i in range(10))
f = [i * i for i in range(10)]
print g
print f
print sum(g)
print sum(f)
