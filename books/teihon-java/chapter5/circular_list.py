import unittest
import cell

# Oh dirty...
class CircularList:
  def __init__(self):
    self.head = cell.Cell(None)
    self.head.next = self.head
    self.tail = self.head

  def add(self, data):
    c = cell.Cell(data)
    c.next = self.head
    self.tail.next = c
    self.tail = c

  def get(self, n):
    return self.__nth(n).data

  def delete(self, n):
    cell = self.__nth(n)
    if cell is not self.head:
      prev = self.__nth(n - 1)
      prev.next = cell.next
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
    self.target = CircularList()

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

