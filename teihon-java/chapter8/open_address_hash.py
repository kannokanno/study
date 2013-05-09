import unittest

class BucketOverflowException(Exception):
    pass

# ()           => delete mark
# None         => empty
# (key, value) => entry
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

        raise BucketOverflowException()

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
        hashcode = 0
        for x in key:
            hashcode = ord(x) + hashcode
        return hashcode % self.size

    def __rehash(self, hashcode):
        return (hashcode + 1) % self.size

class Test(unittest.TestCase):
    def setUp(self):
        self.target = HashTable()

    def test_search(self):
        table = self.target
        table.add('a', 'Hoge')
        table.add('b', 'Piyo')
        table.add('c', 'Fuga')
        table.add('d', 'Fugaa')

        self.assertEqual(table.get('XX'), None)
        self.assertEqual(table.get('b'), 'Piyo')

    def test_hashcode(self):
        table = self.target
        self.assertEqual(table.hash('a'), table.hash('a'))
        self.assertEqual(table.hash('aA'), table.hash('Aa'))
        self.assertNotEqual(table.hash('a'), table.hash('b'))

    def test_add_once(self):
        table = self.target
        self.assertEqual(table.add('a', 'Hoge1'), True)
        self.assertEqual(table.add('a', 'Hoge2'), False)

    def test_add_overflow(self):
        table = self.target
        table.add('1', 'Hoge')
        table.add('2', 'Hoge')
        table.add('3', 'Hoge')
        table.add('4', 'Hoge')
        table.add('5', 'Hoge')
        with self.assertRaises(BucketOverflowException):
            table.add('6', 'Hoge')

    def test_delete(self):
        table = self.target
        table.add('a', 'Hoge')
        table.add('b', 'Piyo')
        table.add('c', 'Fuga')

        self.assertEqual(table.get('b'), 'Piyo')
        self.assertEqual(table.delete('b'), True)
        self.assertEqual(table.delete('b'), False)
        self.assertEqual(table.get('b'), None)

if __name__ == '__main__':
    unittest.main()
