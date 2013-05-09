import unittest
import cell

class LinkedList:
  def __init__(self):
    # head
    self.head = cell.Cell(None)
    # head - tail
    self.tail = self.head

  def add(self, data):
    c = cell.Cell(data)
    # head - tail(old) - c
    self.tail.next = c
    # head - old - tail(c)
    self.tail = c

  def get(self, n):
    cell = self.__nth(n)
    return cell is None and None or cell.data

  def delete(self, n):
    cell = self.__nth(n)
    if cell is not None:
      prev = self.__nth(n - 1)
      prev.next = cell.next
      return True

    return False

  def __nth(self, n):
    i = -1
    cell = self.head
    while cell is not None:
      if i == n:
        return cell
      i += 1
      cell = cell.next
    return None


class Test(unittest.TestCase):
  def setUp(self):
    self.target = LinkedList()

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
