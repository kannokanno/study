import unittest
import doubly_cell

class ListQueue:
  def __init__(self):
    self.head = doubly_cell.DoublyCell(None)
    self.head.prev = self.head
    self.head.next = self.head

  def enqueue(self, item):
    cell = doubly_cell.DoublyCell(item)
    cell.prev = self.head
    cell.next = self.head.next
    self.head.next.prev = cell
    self.head.next = cell

  def dequeue(self):
    target = self.head.prev
    target.prev.next = target.next
    target.next.prev = target.prev
    return target.data


class Test(unittest.TestCase):
  def setUp(self):
    self.target = ListQueue()

  def test_enqueue_and_dequeue(self):
    self.assertEqual(self.target.dequeue(), None)
    self.target.enqueue(3)
    self.target.enqueue(4)
    self.target.enqueue(2)
    self.assertEqual(self.target.dequeue(), 3)
    self.assertEqual(self.target.dequeue(), 4)
    self.assertEqual(self.target.dequeue(), 2)
    self.assertEqual(self.target.dequeue(), None)

if __name__ == '__main__':
  unittest.main()

