def __logging(visited, rest=[]):
    if rest:
        print "visited:%s\n   rest:%s\n" % (visited, rest)
    else:
        print "visited:%s" % (visited)

def dfs(graph, start, end):
    stack = [start]
    visited = []
    while stack:
        label = stack.pop(0)
        if label == end:
            visited.append(label)
            __logging(visited, stack)
            return visited
        if label not in visited:
            visited.append(label)
            stack = graph.get(label, []) + stack
        __logging(visited, stack)
    return visited


is_finded = False
def dfs_rec(graph, start, end, visited=[]):
    global is_finded
    if is_finded:
        return visited
    if start == end:
        is_finded = True
        visited.append(start)
        __logging(visited)
        return visited
    visited.append(start)
    __logging(visited)
    for label in graph.get(start, []):
        if not label in visited:
            visited = dfs_rec(graph, label, end, visited)
    return visited

if __name__ == '__main__':
    """
    +-------------1
    |             |
    |     +-------+-----+
    |     |       |     |
    |   +-2-+     6   +-8-+
    |   |   |     |   |   |
    |   3   4     7   9   10
    |       |     |   |   |
    +-------5     +---+   11
    """
    graph = { 1: [2, 6, 8],
              2: [3, 4],
              3: [],
              4: [5],
              5: [1],
              6: [7],
              7: [],
              8: [9, 10],
              9: [7],
             10: [11],
             11: [],
            }
    print dfs_rec(graph, 1, 5)
    print dfs(graph, 1, 5)
