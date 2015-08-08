# -*- coding: utf-8 -*-
import unittest

class QueueOverflowException(Exception):
  pass

class QueueEmptyException(Exception):
  pass

class Queue:
  """ Ring Buffer"""

  def __init__(self, size=4):
    self.size = size
    self.data = []
    self.front = 0
    self.rear = 0

  def enqueue(self, item):
    if self.__next(self.rear) == self.front:
      raise QueueOverflowException()
    self.data.insert(self.rear, item)
    self.rear = self.__next(self.rear)

  def dequeue(self):
    if self.front == self.rear:
      raise QueueEmptyException()
    data = self.data[self.front]
    self.data[self.front] = None
    self.front = self.__next(self.front)
    return data

  def __next(self, n):
    # 必ず最後の一つは空要素として扱う。
    # front == rearの際に「空」なのか「満杯」なのかを判別するため
    return (n + 1) % self.size


class Test(unittest.TestCase):
  def setUp(self):
    self.target = Queue()

  def test_enqueue_and_dequeue(self):
    self.target.enqueue(3)
    self.target.enqueue(4)
    self.target.enqueue(2)
    self.assertEqual(self.target.dequeue(), 3)
    self.assertEqual(self.target.dequeue(), 4)
    self.assertEqual(self.target.dequeue(), 2)

  def test_enqueue_exception_when_be_filled(self):
    self.target.enqueue(3)
    self.target.enqueue(4)
    self.target.enqueue(2)
    self.assertRaises(QueueOverflowException, self.target.enqueue, 3)

  def test_deque_exception_when_be_empty(self):
    self.assertRaises(QueueEmptyException, self.target.dequeue)

if __name__ == '__main__':
  unittest.main()
