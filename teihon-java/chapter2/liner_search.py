import unittest

def search(data, key):
  print 'key: ' + key + ' => ',
  for i, x in enumerate(data):
    print x,
    if x == key:
      print "<Found>"
      return i

  print "<Not Found>"
  return None


class Test(unittest.TestCase):
  def test_search(self):
    data = ['a', 'b', 'CC', 'E', 'hoge']
    self.assertEquals(search(data, 'b'), 1)
    self.assertEquals(search(data, 'E'), 3)
    self.assertEquals(search(data, 'ZZ'), None)

if __name__ == '__main__':
  unittest.main()
