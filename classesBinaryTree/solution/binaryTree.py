#!/usr/bin/python3

from pprint import pprint
import math


class BinaryTreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, key: int, value: any):
        """ Initialize the node 
        :param key: Key of the node
        :param value: Value of the node
        """
        self._key = key
        self._left = None
        self._right = None
        self._value = value

    @property
    def is_leaf(self):
        """ Return True if the node is a leaf """
        return self._left is None and self._right is None

    @property
    def left(self) -> 'BinaryTreeNode':
        """
        Return the left child of the node
        """
        return self._left

    @property
    def right(self) -> 'BinaryTreeNode':
        """
        Return the right child of the node
        """
        return self._right

    @property
    def value(self) -> any:
        """
        Return the value of the node
        """
        return self._value

    @property
    def key(self) -> int:
        """
        Return the key of the node
        """
        return self._key

    @key.setter
    def key(self, key: int):
        """
        Set the key of the node
        """
        self._key = key

    @value.setter
    def value(self, value: any):
        """
        Set the value of the node
        """
        self._value = value

    @left.setter
    def left(self, node: 'BinaryTreeNode'):
        """
        Set the left child of the node
        """
        self._left = node

    @right.setter
    def right(self, node: 'BinaryTreeNode'):
        """
        Set the right child of the node
        """
        self._right = node


class BinaryTree:
    """
    A binary tree.
    """

    def __init__(self):
        """
        Initialize the tree
        """
        self._root = None

    def _insert_rec(self, node: BinaryTreeNode, key: int,
                    value: any) -> BinaryTreeNode:
        """
        Insert a new node with the given key and value
        :param node: Current node
        :param key: Key of the new node
        :param value: Value of the new node
        :return: New root of the subtree
        """
        if node is None:
            return BinaryTreeNode(key, value)
        if key < node.key:
            node._left = self._insert_rec(node.left, key, value)
        else:
            node._right = self._insert_rec(node.right, key, value)

        return node

    def insert(self, key: int, value: any):
        """
        Insert a new node with the given key and value
        :param key: Key of the new node
        :param value: Value of the new node
        """
        self._root = self._insert_rec(self._root, key, value)

    def _depth(self, node: BinaryTreeNode = None) -> int:
        """
        Return the depth of the tree
        :param node: Node to start from, if None, start from root
        :return: Depth of the tree
        """
        if self._root is None:
            return 0

        if node is None:
            return 0

        return max(self._depth(node.left), self._depth(node.right)) + 1

    def depth(self) -> int:
        """
        Return the depth of the tree
        :return: Depth of the tree
        """
        return self._depth(self._root)

    def _visit(self,
               callback,
               level: int,
               pos: int,
               node: BinaryTreeNode,
               parent: BinaryTreeNode = None,
               left=False,
               right=False):
        """
        Visit all nodes in the tree and call the callback function
        :param callback: Callback function to call for each node
        :param level: Current level in the tree
        :param pos: Position of the node in the tree
        :param node: Current node
        :param parent: Parent of the current node
        :param left: True if the current node is a left child
        :param right: True if the current node is a right child
        """

        #print(f"Visiting node {node.key} at level {level} and pos {pos}")
        callback(parent, node, level, pos, left=left, right=right)

        if node.left is not None:
            self._visit(callback,
                        level + 1,
                        2 * pos - 1,
                        node.left,
                        node,
                        left=True,
                        right=False)
        if node.right is not None:
            self._visit(callback,
                        level + 1,
                        2 * pos + 1,
                        node.right,
                        node,
                        right=True,
                        left=False)

    def visualize(self, node: BinaryTreeNode = None, level=None) -> None:
        """
        Visualize the tree by printing it to the console
        :param node: Node to start from, if None, start from root
        :param level: Current level in the tree
        """

        def callback(parent, node, level, pos, left, right):
            print(f"Node ({level}): {node.key} -> {node.value}")

        self._visit(callback, 0, 0, self._root)

    def create_figure(self, filename: str = "tree.png"):
        """
        Create a figure of the tree and save it to a file
        :param filename: Name of the file to save the figure to
        """
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
