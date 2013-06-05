# -*- coding: utf-8 -*-
def __logging(visited, rest=[]):
    print "visited:%s\n   rest:%s\n" % (visited, rest)


def bfs(graph, start, end):
    queue = [start]
    visited = []
    while queue:
        label = queue.pop(0)
        if label == end:
            visited.append(label)
            __logging(visited, queue)
            return visited
        if label not in visited:
            visited.append(label)
            queue += graph.get(label, [])
            #こっちでもいい
            #queue += [x for x in graph.get(label, []) if x not in visited]
        __logging(visited, queue)
    return visited


if __name__ == '__main__':
    """
    +-------------1
    |             |
    |     +-------+-----+
    |     |       |     |
    |   +-2-+     3   +-4-+
    |   |   |     |   |   |
    |   5   6     7   8   9
    |       |     |   |   |
    +-------10    +---+   11
    """
    graph = {1: [2, 3, 4],
             2: [5, 6],
             3: [7],
             4: [8, 9],
             5: [],
             6: [10],
             7: [],
             8: [7],
             9: [11],
             10: [1],
             11: [],
             }
    print bfs(graph, 1, 1)
    print bfs(graph, 1, 3)
    print bfs(graph, 1, 10)
    print bfs(graph, 1, -1)
