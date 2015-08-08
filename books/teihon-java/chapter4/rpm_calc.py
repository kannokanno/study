import unittest
import stack

class RPMCalcException(Exception):
  pass

class RPMCalc:
  def __init__(self):
    self.stack = stack.Stack()

  def compute(self, item):
    if type(item) == type(1):
      self.stack.push(item)
      return item
    else:
      b = self.stack.pop()
      a = self.stack.pop()
      result = self.__operate(a, b, item)
      self.stack.push(result)
      return result

  def __operate(self, a, b, operator):
    if operator == '+':
      return a + b
    elif operator == '-':
      return a - b
    elif operator == '*':
      return a * b
    elif operator == '/':
      return a / b
    else:
      raise RPMCalcException()


class Test(unittest.TestCase):
  def setUp(self):
    self.target = RPMCalc()

  def test_add(self):
    self.assertEqual(self.target.compute(1), 1)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("+"), 4)

  def test_subtract(self):
    self.assertEqual(self.target.compute(1), 1)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("-"), -2)

  def test_multiple(self):
    self.assertEqual(self.target.compute(2), 2)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("*"), 6)

  def test_division(self):
    self.assertEqual(self.target.compute(6), 6)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("/"), 2)

  def test_invalid_operation(self):
    self.assertEqual(self.target.compute(6), 6)
    self.assertEqual(self.target.compute(3), 3)
    self.assertRaises(RPMCalcException, self.target.compute, ("="))

  def test_continue(self):
    self.assertEqual(self.target.compute(1), 1)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("+"), 4)
    self.assertEqual(self.target.compute(1), 1)
    self.assertEqual(self.target.compute("+"), 5)
    self.assertEqual(self.target.compute(3), 3)
    self.assertEqual(self.target.compute("-"), 2)

if __name__ == '__main__':
  unittest.main()

