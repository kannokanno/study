import unittest

class StackOverflowException(Exception):
  pass

class StackEmptyException(Exception):
  pass

class Stack:
  def __init__(self, size=3):
    self.size = size
    self.pointer = 0
    self.data = []

  def push(self, item):
    if self.pointer >= self.size:
      raise StackOverflowException
    self.data.insert(self.pointer, item)
    self.pointer += 1

  def pop(self):
    if self.pointer < 1:
      raise StackEmptyException
    self.pointer -= 1
    data = self.data[self.pointer]
    return data

  def clear(self):
    self.pointer = 0
    self.data = []

  def is_empty(self):
    return self.pointer == 0


class Test(unittest.TestCase):
  def setUp(self):
    self.target = Stack()

  def test_push_raise_exception_when_overflow(self):
    self.target.push(1)
    self.target.push(1)
    self.target.push(1)
    # size over
    self.assertRaises(StackOverflowException, self.target.push, (1))

  def test_pop(self):
    self.target.push(1)
    self.assertEqual(self.target.pop(), 1)

  def test_pop_raise_exception_when_empty(self):
    self.assertRaises(StackEmptyException, self.target.pop)

  def test_clear(self):
    self.target.push(1)
    self.target.push(1)
    self.target.push(1)

    self.target.clear()

    # not raise exception because clear
    self.target.push(1)
    self.target.push(1)
    self.target.push(1)

  def test_is_empty(self):
    self.assertEqual(self.target.is_empty(), True)
    self.target.push(1)
    self.assertEqual(self.target.is_empty(), False)
    self.target.pop()
    self.assertEqual(self.target.is_empty(), True)

if __name__ == '__main__':
  unittest.main()
