def strong_strategy():
    return [2, 3, 3, 4, 5]

def weak_strategy():
    return [1, 2, 3, 3, 4]

def game(first, second):
    result = []
    for (f, s) in zip(first(), second()):
        if f < s:
            result.append('S')
        elif f > s:
            result.append('F')
        else:
            result.append('DRAW')
    return result

if __name__ == '__main__':
    print game(strong_strategy, strong_strategy)
    print game(weak_strategy, strong_strategy)
    print game(weak_strategy, weak_strategy)
