import unittest
import doubly_cell

class ListStack:
  def __init__(self):
    self.head = doubly_cell.DoublyCell(None)
    self.head.prev = self.head
    self.head.next = self.head

  def push(self, item):
    cell = doubly_cell.DoublyCell(item)
    cell.prev = self.head
    cell.next = self.head.next
    self.head.next.prev = cell
    self.head.next = cell

  def pop(self):
    target = self.head.next
    target.prev.next = target.next
    target.next.prev = target.prev
    return target.data

  def clear(self):
    self.head.prev = self.head
    self.head.next = self.head

  def is_empty(self):
    return self.head.prev == self.head


class Test(unittest.TestCase):
  def setUp(self):
    self.target = ListStack()

  def test_pop(self):
    self.assertEqual(self.target.pop(), None)
    self.target.push(1)
    self.assertEqual(self.target.pop(), 1)
    self.target.push(2)
    self.target.push(3)
    self.assertEqual(self.target.pop(), 3)
    self.assertEqual(self.target.pop(), 2)
    self.assertEqual(self.target.pop(), None)

  def test_clear(self):
    self.assertEqual(self.target.pop(), None)
    self.target.push(1)
    self.target.push(2)
    self.target.push(3)
    self.target.clear()
    self.assertEqual(self.target.pop(), None)

  def test_is_empty(self):
    self.assertEqual(self.target.is_empty(), True)
    self.target.push(1)
    self.assertEqual(self.target.is_empty(), False)
    self.target.pop()
    self.assertEqual(self.target.is_empty(), True)

if __name__ == '__main__':
  unittest.main()
