import unittest

def search(data, key):
  print 'key: ' + str(key) + ' => ',
  low = 0
  high = len(data) - 1
  while low <= high:
    middle = (low + high) / 2
    x = data[middle]
    print x,
    if x == key:
      print "<Found>"
      return True
    elif x < key:
      low = middle + 1
    else:
      high = middle - 1

  print "<Not Found>"
  return False


class Test(unittest.TestCase):
  def test_search(self):
    data = [1, 4, 6, 11, 40, 56]
    self.assertEquals(search(data, 4), True)
    self.assertEquals(search(data, 56), True)
    self.assertEquals(search(data, 20), False)

if __name__ == '__main__':
  unittest.main()

