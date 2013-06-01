class HashTable:
    def __init__(self, size=5):
        self.__EMPTY__ = None
        self.__DELETED__ = ()

        self.size = size
        self.table = [None] * size

    def add(self, key, value):
        hashcode = self.hash(key)
        count = 0
        while count < self.size:
            data = self.table[hashcode]
            if data is self.__EMPTY__:
                self.table[hashcode] = (key, value)
                return True
            elif data[0] == key:
                return False
            count += 1
            hashcode = self.__rehash(hashcode)
        return False

    def get(self, key):
        hashcode = self.hash(key)
        count = 0
        while count < self.size:
            data = self.table[hashcode]
            if data is self.__EMPTY__:
                return None
            if data is not self.__DELETED__ and data[0] == key:
                return data[1]
            hashcode = self.__rehash(hashcode)
            count += 1
        return None

    def delete(self, key):
        hashcode = self.hash(key)
        count = 0
        while count < self.size:
            data = self.table[hashcode]
            if data is self.__EMPTY__:
                return False
            if data is not self.__DELETED__ and data[0] == key:
                self.table[hashcode] = self.__DELETED__
                return True
            hashcode = self.__rehash(hashcode)
            count += 1
        return False

    # tekitou
    def hash(self, key):
        hashcode = key << 3
        return hashcode % self.size

    def __rehash(self, hashcode):
        return (hashcode + 1) % self.size
