class BinaryTreeNode:
  def __init__(self, label, left = None, right = None):
    self.label = label
    self.left = left
    self.right = right

class Traverser:
  def preorder(self, node):
    if node == None:
      return None
    print "  Passed: " + node.label
    self.preorder(node.left)
    self.preorder(node.right)

  def inorder(self, node):
    if node == None:
      return None
    self.inorder(node.left)
    print "  Passed: " + node.label
    self.inorder(node.right)

  def postorder(self, node):
    if node == None:
      return None
    self.postorder(node.left)
    self.postorder(node.right)
    print "  Passed: " + node.label


if __name__ == '__main__':
  """
    Tree:
          a
      b       f
    c  d
         e
  """
  tree = BinaryTreeNode("a",
              BinaryTreeNode("b",
                  BinaryTreeNode("c"),
                  BinaryTreeNode("d",
                      None,
                      BinaryTreeNode("e"))),
              BinaryTreeNode("f"))

  traverse = Traverser()
  print "Preorder ==>"
  traverse.preorder(tree)
  print "<== Preorder"

  print "Inorder ==>"
  traverse.inorder(tree)
  print "<== Inorder"

  print "Postorder ==>"
  traverse.postorder(tree)
  print "<== Postorder"
