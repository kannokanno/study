import unittest

class HashTable:
  class Cell:
    # key is string only
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
    hashcode = 0
    for x in key:
      hashcode = ord(x) + hashcode
    return hashcode % self.size

class Test(unittest.TestCase):
  def setUp(self):
    self.target = HashTable()

  def test_hashcode(self):
    table = self.target
    self.assertEqual(table.hash('a'), table.hash('a'))
    self.assertEqual(table.hash('aA'), table.hash('Aa'))
    self.assertNotEqual(table.hash('a'), table.hash('b'))

  def test_search(self):
    table = self.target
    table.add('a', 'Hoge')
    table.add('bX', 'Piyo1')
    table.add('Xb', 'Piyo2')
    table.add('c', 'Fuga')
    table.add('d', 'Fugaa')
    table.add('e', 'Fugah')

    self.assertEqual(table.get('XX'), None)
    self.assertEqual(table.get('bX'), 'Piyo1')

  def test_add_once(self):
    table = self.target
    self.assertEqual(table.add('a', 'Hoge1'), True)
    self.assertEqual(table.add('a', 'Hoge2'), False)

  def test_delete(self):
    table = self.target
    table.add('a', 'Hoge')
    table.add('bA', 'Piyo1')
    table.add('Ab', 'Piyo2')
    table.add('c', 'Fuga')

    self.assertEqual(table.get('bA'), 'Piyo1')
    self.assertEqual(table.delete('bA'), True)
    self.assertEqual(table.delete('bA'), False)
    self.assertEqual(table.get('bA'), None)


if __name__ == '__main__':
  unittest.main()
