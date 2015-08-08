class HashTable:
    class Cell:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, size=3):
        self.size = size
        self.table = [None] * size

    def add(self, key, value):
        if self.get(key) is not None:
            return False
        hash_key = self.hash(key)
        cell = HashTable.Cell(key, value, self.table[hash_key])
        self.table[hash_key] = cell
        return True

    def get(self, key):
        cell = self.table[self.hash(key)]
        while cell is not None:
            if cell.key == key:
                return cell.value
            cell = cell.next
        return None

    def delete(self, key):
        head = self.table[self.hash(key)]
        if head is None:
            return False

        if head.key == key:
            self.table[self.hash(key)] = head.next
            return True

        prev = head
        next = head.next
        while next is not None:
            if next.key == key:
                prev.next = next.next
                return True
            next = next.next

        return False

    # tekitou
    def hash(self, key):
        hashcode = key << 3
        return hashcode % self.size
