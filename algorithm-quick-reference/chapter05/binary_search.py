def search(data, key):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) / 2
        x = data[middle]
        if x == key:
            return True
        elif x < key:
            low = middle + 1
        else:
            high = middle - 1
    return False
