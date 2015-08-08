# -*- coding: utf-8 -*-
import unittest

class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def add(self, label):
        return self.__add(Node(label))

    def __add(self, append):
        parent = self
        current = self
        is_left = False
        while current is not None:
            if current.label == append.label:
                # 重複データの場合は何もしない
                return self
            elif append.label < current.label:
                parent = current
                current = current.left
                is_left = True
            else:
                parent = current
                current = current.right
                is_left = False

        self.__reconnect(parent, append, is_left)
        return self

    def get(self, key):
        return self.__get(Node(key))

    def __get(self, search):
        current = self
        while current is not None:
            if current.label == search.label:
                return current
            elif search.label < current.label:
                current = current.left
            else:
                current = current.right

        return Node(None)

    def delete(self, key):
        return self.__delete(Node(key))

    def __delete(self, search):
        """
        該当するノードがない
            False
        該当するノードがある
            ノード == リーフ
                親ノードから自身への参照を消す
            左部分木しかない
                親ノードから自身への参照を消す
                親ノードからの参照を子ノードにつける
            右部分木しかない
                親ノードから自身への参照を消す
                親ノードからの参照を子ノードにつける
            左部分木も右部分木もある
                right = 右部分木の取得
                bottom_left = rightを基点として再帰的に左部分木を取得する
                bottom_left == リーフ
                    親ノードから自身への参照を消す
                bottom_leftの左部分木がある
                    エラー。性質上有り得ない
                bottom_leftの右部分木がある
                    right = bottom_leftの右部分木
                    bottom_left.parent.left = right
                bottom_left.left = 削除ノード.left
                削除ノード.parent.left = bottom_left
        """
        if self.label == search.label and self.is_leaf():
            self.label = None
            return True

        parent = self
        current = self
        is_left = False
        while current is not None:
            if current.label == search.label:
                self.__reconnect(parent, self.__fetch_delete_child(current), is_left)
                return True
            elif search.label < current.label:
                parent = current
                current = current.left
                is_left = True
            else:
                parent = current
                current = current.right
                is_left = False

        return False

    def __fetch_delete_child(self, target):
        if target.is_leaf():
            return None
        elif target.left is not None and target.right is not None:
            left_bottom, left_bottom_parent = self.__min_and_parent(target.right)
            # left_bottomは左部分木の末端なので、リーフじゃなければ必ず右部分木しかない
            # TODO: fetchと言いながらここで参照を書き換えている(副作用)
            left_bottom_parent.left = None if left_bottom.is_leaf() else left_bottom.right
            left_bottom.left = target.left
            left_bottom.right = target.right
            return left_bottom
        else:
            # 左部分木のみ or 右部分木のみ
            return target.left if target.left is not None else target.right

    def __min_and_parent(self, node):
        """ 左部分木の最下部(リーフ)とその親を取得 """
        left_bottom_parent = node
        left_bottom = node
        while left_bottom.left is not None:
            left_bottom_parent = left_bottom
            left_bottom = left_bottom.left
        return (left_bottom, left_bottom_parent)

    def __reconnect(self, parent, child, is_left):
        if is_left:
            parent.left = child
        else:
            parent.right = child

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        if self.is_leaf():
            return "(Leaf %s)" % (self.label)
        return "(Node %s %s %s)" % (self.label, str(self.left), str(self.right))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Node):
            return str(self) == str(other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_eq(self):
        """ ノードの等値性 """
        self.assertEquals(Node(1), Node(1))
        self.assertNotEquals(Node(10), Node(1))

    def test_add(self):
        """ ノード追加 """
        node = Node(5).add(3).add(2).add(10).add(20)
        expected = Node(5,
                        Node(3, Node(2)),
                        Node(10, None, Node(20)))
        self.assertEquals(node, expected)

    def test_get(self):
        """ ノード検索 """
        node = Node(5,
                    Node(3, Node(2)),
                    Node(10, None, Node(20)))
        self.assertEquals(node.get(10), Node(10, None, Node(20)))
        self.assertEquals(node.get(999), Node(None))

    def test_is_leaf(self):
        """ リーフかどうか """
        self.assertEquals(Node(10).is_leaf(), True)
        self.assertEquals(Node(10, Node(5)).is_leaf(), False)
        self.assertEquals(Node(10, None, Node(15)).is_leaf(), False)
        self.assertEquals(Node(10, Node(5), Node(15)).is_leaf(), False)

    def test_delete(self):
        """ ノード削除 """

        """ 存在しないノードは消せない """
        node = Node(10)
        self.assertEquals(node.delete(7), False)
        """ ルート(リーフ)のみ """
        node = Node(10)
        self.assertEquals(node.delete(10), True)
        self.assertEquals(node, Node(None))

        """ 該当ノード == リーフ(左) """
        node = Node(10, Node(5))
        self.assertEquals(node.delete(5), True)
        self.assertEquals(node, Node(10))

        """ 該当ノード == リーフ(右) """
        node = Node(10, None, Node(15))
        self.assertEquals(node.delete(15), True)
        self.assertEquals(node, Node(10))

        """ 子が左部分木のみ """
        node = Node(10, Node(5, Node(3, None, Node(4))))
        self.assertEquals(node.delete(5), True)
        self.assertEquals(node, Node(10, Node(3, None, Node(4))))

        """ 子が右部分木のみ """
        node = Node(10, None, Node(15, None, Node(13, None, Node(14))))
        self.assertEquals(node.delete(15), True)
        self.assertEquals(node, Node(10, None, Node(13, None, Node(14))))

        """ 子が両方ともある """
        """
        Before:
                  ┌ーーー20ーーー┐
                  │              │
             ┌ーー7ーー┐        23ーー┐
             │         │              │
         ┌ー4ー┐  ┌ー18              29
         │     │  │
          2     5   10ー┐
                        15
        """
        node = Node(20,
                    Node(7, Node(4, Node(2), Node(5)), Node(18, Node(10, None, Node(15)))),
                    Node(23, None, Node(29)))

        # 上記ツリーから7を削除
        self.assertEquals(node.delete(7), True)

        """
        After:
                  ┌ーーー20ーーー┐
                  │              │
            ┌ーー10ーー┐        23ーー┐
            │          │              │
         ┌ー4ー┐  ┌ー18              29
         │     │  │
          2     5   15
        """
        expected = Node(20,
                    Node(10, Node(4, Node(2), Node(5)), Node(18, Node(15))),
                    Node(23, None, Node(29)))
        self.assertEquals(node, expected)


if __name__ == '__main__':
    unittest.main()
