import unittest
import doubly_cell

class DoublyList:
  def __init__(self):
    self.head = doubly_cell.DoublyCell(None)
    self.head.prev = self.head
    self.head.next = self.head

  def add(self, data):
    added = doubly_cell.DoublyCell(data)
    added.prev = self.head.prev
    added.next = self.head
    self.head.prev.next = added
    self.head.prev = added
    if self.head.next == self.head:
      self.head.next = added

  def get(self, n):
    return self.__nth(n).data

  def delete(self, n):
    cell = self.__nth(n)
    if cell is not self.head:
      cell.prev.next = cell.next
      return True

    return False

  def __nth(self, n):
    i = 0
    cell = self.head.next
    while cell is not self.head:
      if i == n:
        return cell
      i += 1
      cell = cell.next
    return self.head


class Test(unittest.TestCase):
  def setUp(self):
    self.target = DoublyList()

  def test_add_and_get(self):
    self.target.add(1)
    self.target.add(3)
    self.target.add(5)
    self.assertEqual(self.target.get(0), 1)
    self.assertEqual(self.target.get(1), 3)
    self.assertEqual(self.target.get(2), 5)

  def test_delete(self):
    self.target.add(1)
    self.target.add(3)
    self.target.add(5)
    self.target.delete(1)
    self.assertEqual(self.target.get(0), 1)
    self.assertEqual(self.target.get(1), 5)
    self.target.delete(0)
    self.assertEqual(self.target.get(0), 5)


if __name__ == '__main__':
  unittest.main()


