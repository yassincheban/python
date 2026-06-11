#!/usr/bin/python3

from pprint import pprint
import math


class BinaryTreeNode:

    def __init__(self, key: int, value: any):
        self._key = key
        self._left = None
        self._right = None
        self._value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def is_leaf(self):
        return self._left is None and self._right is None


class BinaryTree:
    """
    A binary tree.
    """

    def __init__(self):
        self._root = None

    
    def _insert_rec(self, node: BinaryTreeNode, key: int,
                    value: any) -> BinaryTreeNode:

        if node is None:
            return BinaryTreeNode(key, value)

        if key < node.key:
            node.left = self._insert_rec(node.left, key, value)
        else:
            node.right = self._insert_rec(node.right, key, value)

        return node

    def insert(self, key: int, value: any):
        self._root = self._insert_rec(self._root, key, value)

    def _depth(self, node: BinaryTreeNode = None) -> int:
        if self._root is None:
            return 0

        if node is None:
            return 0

        return max(self._depth(node.left), self._depth(node.right)) + 1

    def depth(self) -> int:
        return self._depth(self._root)

    # (unverändert gelassen wie bei dir)
    def _visit(self,
               callback,
               level: int,
               pos: int,
               node: BinaryTreeNode,
               parent: BinaryTreeNode = None,
               left=False,
               right=False):

        print(f"Visiting node {node.key} at level {level} and pos {pos}")

        # Call the callback function

        # Visit left child

        # Visit right child

    def visualize(self, node: BinaryTreeNode = None, level=None) -> None:

        def callback(parent, node, level, pos, left, right):
            print(f"Node ({level}): {node.key} -> {node.value}")

        self._visit(callback, 0, 0, self._root)

    def create_figure(self, filename: str = "tree.png"):

        height = self.depth()

        import matplotlib.pyplot as plt

        nodes_x = []
        nodes_y = []

        def callback(parent, node, level, pos, left, right):
            nonlocal nodes_x
            nonlocal nodes_y

            x = pos
            y = -level
            nodes_x.append(x)
            nodes_y.append(y)
            plt.text(x, y, f"  {str(node.key)}")
            if parent is not None:
                px = (pos + (1 if left else 0) + (-1 if right else 0)) / 2
                py = -(level - 1)
                plt.arrow(px,
                          py,
                          x - px,
                          y - py,
                          head_width=0.1,
                          head_length=0.1,
                          length_includes_head=True)

        self._visit(callback, 0, 0, self._root)

        plt.scatter(nodes_x, nodes_y)
        plt.savefig(filename)


def main():
    print("hello tree")
    bt = BinaryTree()
    bt.insert(100, "hundred")
    bt.insert(75, "seventy five")
    bt.insert(65, "sixty five")
    bt.insert(60, "sixty")
    bt.insert(70, "seventy")
    bt.insert(85, "eighty five")
    bt.insert(80, "eighty")
    bt.insert(95, "ninety five")
    bt.insert(125, "one twenty five")
    bt.insert(115, "one fifteen")
    bt.insert(150, "one fifty")
    bt.insert(135, "one thirty five")
    bt.insert(175, "one seventy five")

    bt.visualize()
    print("Depth:", bt.depth())
    bt.create_figure()


if __name__ == "__main__":
    main()
