#!/usr/bin/python3

from platform import node
from pprint import pprint
import math
from enum import Enum
from typing import Type, TypeVar

T = TypeVar('T', bound='Node')


class RBTreeNode:
    """
    A node in a binary tree.
    """

    class Color(Enum):
        UNKNOWN = None
        RED = 1
        BLACK = 2

    def __init__(self, key: int, parent: 'RBTreeNode', color: Color,
                 value: any):
        """ Initialize the node 
        :param key: Key of the node
        :param parent: Parent of the node
        :param color: color of node
        :param value: Value of the node
        """
        self._key = key
        self._parent = parent
        self._color = color
        self._left = RBTreeNode.nil(self) if key is not None else None
        self._right = RBTreeNode.nil(self) if key is not None else None
        self._value = value

    @property
    def is_leaf(self):
        """ Return True if the node is a leaf """
        return self._left.is_nil and self._right.is_nil

    @property
    def left(self) -> 'RBTreeNode':
        """
        Return the left child of the node
        """
        return self._left

    @property
    def right(self) -> 'RBTreeNode':
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

    @property
    def parent(self) -> 'RBTreeNode':
        """
        Return the parent of the node
        """
        return self._parent

    @parent.setter
    def parent(self, parent: 'RBTreeNode'):
        """
        Set the parent of the node
        """
        self._parent = parent

    @property
    def color(self) -> Color:
        """
        Return the color of the node
        """
        return self._color

    @color.setter
    def color(self, c: Color):
        """
        Set the color of the node
        """
        self._color = c

    @property
    def is_red(self) -> bool:
        """
        Return if node is red
        """
        return self._color == RBTreeNode.Color.RED

    @property
    def is_black(self) -> bool:
        """
        Return if node is black
        """
        return self._color == RBTreeNode.Color.BLACK

    @value.setter
    def value(self, value: any):
        """
        Set the value of the node
        """
        self._value = value

    @left.setter
    def left(self, node: 'RBTreeNode'):
        """
        Set the left child of the node
        """
        self._left = node

    @right.setter
    def right(self, node: 'RBTreeNode'):
        """
        Set the right child of the node
        """
        self._right = node

    @property
    def is_nil(self) -> bool:
        """
        Return True if the node is a nil node (a leaf node that is not None)
        """
        return self._key is None and self._value is None and self.is_black

    def count_colored_nodes(self,
                            color: 'RBTreeNode.Color',
                            node: 'RBTreeNode' = None) -> int:
        """
        Count the number of nodes of a specific color in the subtree rooted at the given node
        :param color: Color to count
        :param node: Node to start from
        :return: Number of nodes of the specified color in the subtree
        """

        left_count = self.left.count_colored_nodes(
            color) if self.left is not None else 0
        right_count = self.right.count_colored_nodes(
            color) if self.right is not None else 0

        return max([left_count, right_count
                    ]) + (1 if self.color == color else 0)

    @classmethod
    def nil(cls: Type[T], parent: 'RBTreeNode' = None) -> T:
        return cls(None, parent, cls.Color.BLACK, None)


class RBTree:
    """
    A red black tree.
    """

    def __init__(self):
        """
        Initialize the tree
        """
        self._root = RBTreeNode.nil()

    def _left_rotate(self, node: RBTreeNode) -> None:
        """
        Perform a left rotation on the given node
        :param node: Node to rotate
        """

        # print('Rotate left on node', node.key)

        y = node.right
        node.right = y.left
        if not y.left.is_nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self._root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def _right_rotate(self, node: RBTreeNode) -> None:
        """
        Perform a right rotation on the given node
        :param node: Node to rotate
        """
        # print('Rotate right on node', node.key)
        y = node.left
        node.left = y.right
        if not y.right.is_nil:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self._root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def _insert_rec(self, node: RBTreeNode, key: int,
                    value: any) -> RBTreeNode:
        """
        Insert a new node with the given key and value
        :param node: Current node
        :param key: Key of the new node
        :param value: Value of the new node
        :return: New root of the subtree
        """
        # print(f"Inserting {key} at node {node.key}")
        if key < node.key:
            if node.left.is_nil:
                # print(f"Inserting {key} as left child of {node.key}")
                node.left = RBTreeNode(key, node, RBTreeNode.Color.RED, value)
                self._fix_rb_tree(node.left)
            else:
                # print(f"Going left from {node.key} to insert {key}")
                self._insert_rec(node.left, key, value)
        else:
            if node.right.is_nil:
                # print(f"Inserting {key} as right child of {node.key}")
                node.right = RBTreeNode(key, node, RBTreeNode.Color.RED, value)
                self._fix_rb_tree(node.right)
            else:
                # print(f"Going right from {node.key} to insert {key}")
                self._insert_rec(node.right, key, value)

    def _fix_rb_tree(self, node: RBTreeNode):
        # print(f"Fixing tree at node {node.key}")
        if node.parent is None:
            node.color = RBTreeNode.Color.BLACK
            return

        if node.parent.is_black:
            # print("Parent is black, no need to fix")
            return

        if node.parent.parent is not None:
            # print("Parent parent is not None, checking cases")
            if node.parent == node.parent.parent.left:
                # print("Parent is left child of grandparent")
                uncle = node.parent.parent.right
                if uncle.is_red:
                    # print("Case 1: Uncle is red")
                    # Case 1: Uncle is red
                    node.parent.color = RBTreeNode.Color.BLACK
                    uncle.color = RBTreeNode.Color.BLACK
                    node.parent.parent.color = RBTreeNode.Color.RED
                    self._fix_rb_tree(node.parent.parent)
                else:
                    # Case 2: Uncle is black and node is right child
                    if node == node.parent.right:
                        # print("Case 2: Uncle is black and node is right child")
                        self._left_rotate(node.parent)
                        node = node.left
                    # print("Case 3: Uncle is black and node is left child")
                    # Case 3: Uncle is black and node is left child
                    node.parent.color = RBTreeNode.Color.BLACK
                    node.parent.parent.color = RBTreeNode.Color.RED
                    self._right_rotate(node.parent.parent)
                    self._fix_rb_tree(node.parent)
            else:
                # print("Parent is right child of grandparent")
                uncle = node.parent.parent.left
                if uncle.is_red:
                    # print("Case 1: Uncle is red")
                    # Case 1: Uncle is red
                    node.parent.color = RBTreeNode.Color.BLACK
                    uncle.color = RBTreeNode.Color.BLACK
                    node.parent.parent.color = RBTreeNode.Color.RED
                    self._fix_rb_tree(node.parent.parent)
                else:
                    # Case 2: Uncle is black and node is left child
                    if node == node.parent.left:
                        # print("Case 2: Uncle is black and node is left child")

                        self._right_rotate(node.parent)
                        node = node.right
                    # print("Case 3: Uncle is black and node is right child")
                    # Case 3: Uncle is black and node is right child
                    node.parent.color = RBTreeNode.Color.BLACK
                    node.parent.parent.color = RBTreeNode.Color.RED
                    self._left_rotate(node.parent.parent)
                    self._fix_rb_tree(node.parent)

    def insert(self, key: int, value: any):
        """
        Insert a new node with the given key and value
        :param key: Key of the new node
        :param value: Value of the new node
        """
        print(f"Inserting {key} into the tree")
        if self._root.is_nil:
            # root always need to be black
            self._root = RBTreeNode(key, None, RBTreeNode.Color.BLACK, value)
            return

        # find correct not to insert
        self._insert_rec(self._root, key, value)

    def check_red_black_properties(self, node: RBTreeNode = None) -> bool:
        """
        Check if the tree satisfies the red-black properties
        :param node: Node to start from, if None, start from root
        :return: True if the tree satisfies the red-black properties, False otherwise
        """
        if node is None:
            node = self._root

        if node is None:
            return True

        # Check if the root is black
        if node.parent is None and not node.is_black:
            print("Root is not black")
            return False

        # Check if red nodes have black children
        if node.is_red:
            if node.left.is_red or node.right.is_red:
                print(f"Red node {node.key} has red child")
                return False

        # special case for empty tree, we consider it as a valid red-black tree
        if node.left is None and node.right is None:
            return True

        # Check if all paths from a node to its descendant leaves contain the same number of black nodes
        left_black_count = node.left.count_colored_nodes(
            RBTreeNode.Color.BLACK)
        right_black_count = node.right.count_colored_nodes(
            RBTreeNode.Color.BLACK)
        if left_black_count != right_black_count:
            print(
                f"Node {node.key} has different number of black nodes in left and right subtrees ({left_black_count} vs {right_black_count})"
            )
            return False

        # Recursively check the left and right subtrees
        return (True if node.left.is_nil else self.check_red_black_properties(
            node.left)) and (True if node.right.is_nil else
                             self.check_red_black_properties(node.right))

    def _binary_tree_delete(self, node: RBTreeNode) -> RBTreeNode:
        """
        Delete a node with the given key using binary tree deletion
        :param node: Node to delete
        :return: Node that replaces the deleted node (if any)
        """

        if not node.is_leaf:
            # delete node with two children: find the successor of the node to delete and replace the node with the successor
            successor = node.right
            # Find the successor of the node to delete
            while not successor.left.is_nil:
                successor = successor.left

            node.key = successor.key
            node.value = successor.value

            return successor
        else:
            # delete node with zero children: simply remove the node from the tree
            return node

    def _binary_tree_transplant(self, node: RBTreeNode,
                                replacement: RBTreeNode) -> None:
        """
        Replace a node with another node in the tree
        :param node: Node to be replaced
        :param replacement: Node to replace with
        """

        if node.parent is None:
            self._root = replacement
        elif node == node.parent.left:
            node.parent.left = replacement
        else:
            node.parent.right = replacement
        replacement.parent = node.parent

    def delete(self, key: int):
        """
        Delete a node with the given key
        :param key: Key of the node to delete
        """
        print(f"Deleting {key} from the tree")

        node = self._root
        # Find the node to delete
        while not node.is_nil and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        # If the node to delete is not found, return
        if node.is_nil:
            raise KeyError(f"Key {key} not found in the tree")

        # print(f"Found node with key {node.key} to delete")
        orginal_node = node
        orginal_color = node.color
        if node.left.is_nil:
            # print("Node has no left child, replacing with right child")
            replacement = node.right
            self._binary_tree_transplant(node, replacement)
        elif node.right.is_nil:
            # print("Node has no right child, replacing with left child")
            replacement = node.left
            self._binary_tree_transplant(node, replacement)
        else:
            # print("Node has two children, finding successor to replace")
            successor = node.right
            while not successor.left.is_nil:
                successor = successor.left

            # print(f"Successor of node {node.key} is {successor.key}")
            orginal_color = successor.color
            replacement = successor.right

            if successor.parent == node:
                # print(f"Successor is right child of node to delete, transplanting successor with its right child {replacement.key}")
                replacement.parent = successor
            else:
                # print("Successor is not right child of node to delete, transplanting successor with its right child and replacing successor with node to delete")
                self._binary_tree_transplant(successor, successor.right)
                successor.right = node.right
                node.right.parent = successor

            self._binary_tree_transplant(node, successor)
            successor.left = node.left
            node.left.parent = successor
            successor.color = orginal_node.color

        if orginal_color == RBTreeNode.Color.BLACK:
            # print("Deleted node was black, fixing tree")
            self._fix_delete(replacement)

    def _fix_delete(self, node: RBTreeNode):
        """
        Fix the tree after deletion to maintain the red-black properties
        :param node: Node to start fixing from
        """

        # print(f"Fixing tree after deletion at node {node.key}")
        while node != self._root and node.is_black:
            print(
                f"Node {node.key} has red parent {node.parent.key}, checking cases"
            )
            if node == node.parent.left:
                print("Node is left child of parent")
                brother = node.parent.right
                print(f"brother of node {node.key} is {brother.key}")
                if brother.is_red:
                    print("Case 1: brother is red")
                    brother.color = RBTreeNode.Color.BLACK
                    node.parent.color = RBTreeNode.Color.RED
                    self._left_rotate(node.parent)
                    brother = node.parent.right

                if brother.left.is_black and brother.right.is_black:
                    print("Case 2: brother is black and node is right child")
                    brother.color = RBTreeNode.Color.RED
                    node = node.parent
                else:
                    if brother.right.is_black:
                        print(
                            "Case 3: brother is black and node is left child")
                        brother.left.color = RBTreeNode.Color.BLACK
                        brother.color = RBTreeNode.Color.RED
                        self._right_rotate(brother)
                        brother = node.parent.right

                    print("Case 4: brother is black and node is right child")
                    brother.color = node.parent.color
                    node.parent.color = RBTreeNode.Color.BLACK
                    brother.right.color = RBTreeNode.Color.BLACK
                    self._left_rotate(node.parent)
                    break
            else:
                print("Node is right child of parent")
                brother = node.parent.left
                print(f"brother of node {node.key} is {brother.key}")
                if brother.is_red:
                    print("Case 1: brother is red")
                    brother.color = RBTreeNode.Color.BLACK
                    node.parent.color = RBTreeNode.Color.RED
                    self._right_rotate(node.parent)
                    brother = node.parent.left

                if brother.left.is_black and brother.right.is_black:
                    print("Case 2: brother is black and node is right child")
                    brother.color = RBTreeNode.Color.RED
                    node = node.parent
                else:
                    if brother.left.is_black:
                        print(
                            "Case 3: brother is black and node is left child")
                        brother.right.color = RBTreeNode.Color.BLACK
                        brother.color = RBTreeNode.Color.RED
                        self._left_rotate(brother)
                        brother = node.parent.left

                    print("Case 4: brother is black and node is right child")
                    brother.color = node.parent.color
                    node.parent.color = RBTreeNode.Color.BLACK
                    brother.left.color = RBTreeNode.Color.BLACK
                    self._right_rotate(node.parent)
                    break

        node.color = RBTreeNode.Color.BLACK

    def _depth(self, node: RBTreeNode = None) -> int:
        """
        Return the depth of the tree
        :param node: Node to start from, if None, start from root
        :return: Depth of the tree
        """
        if self._root.is_nil:
            return 0

        if node.is_nil:
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
               node: RBTreeNode,
               parent: RBTreeNode = None,
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

        if node.is_nil:
            return

        #if not node.left is None:
        if not node.left.is_nil:
            self._visit(callback,
                        level + 1,
                        2 * pos - 1,
                        node.left,
                        node,
                        left=True,
                        right=False)
        #if not node.right is None:
        if not node.right.is_nil:
            self._visit(callback,
                        level + 1,
                        2 * pos + 1,
                        node.right,
                        node,
                        right=True,
                        left=False)

    def visualize(self) -> None:
        """
        Visualize the tree by printing it to the console
        """

        def callback(parent, node, level, pos, left, right):
            print(
                " " * (level * 4) +
                ("L-- " if left else "R-- " if right else "") +
                f"{node.key} ({'B' if node.is_black else 'R'}) -> {node.value}"
            )

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
        colors = []

        def callback(parent, node, level, pos, left, right):
            nonlocal nodes_x
            nonlocal nodes_y

            x = pos
            y = -level
            nodes_x.append(x)
            nodes_y.append(y)
            #print(
            #    f"Node ({level}): {node.key} -> {node.value} at position ({x}, {y}), color: {'black' if node.is_black else 'red'}"
            #)
            colors.append([0.0, 0.0, 0.0, 1.0] if node.
                          is_black else [1.0, 0.0, 0.0, 1.0])
            plt.text(x + 0.2, y, f"  {str(node.key)}")
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

        plt.scatter(nodes_x, nodes_y, c=colors, s=100, edgecolors='black')
        plt.savefig(filename)
        plt.clf()


def main():
    print("hello tree")
    bt = RBTree()
    for i in [10, 5, 20, 15, 30, 25, 40, 35, 50]:
        bt.insert(i, str(i))
        check = bt.check_red_black_properties()
        print("Checking red-black properties:", check)
        if not check:
            bt.create_figure("final_tree.png")
            print("Tree does not satisfy red-black properties after inserting",
                  i)
            return

    bt.visualize()
    print("Depth:", bt.depth())
    bt.create_figure("final_tree.png")
    for i in [10, 5, 20, 15, 30, 25, 40, 35, 50]:
        bt.delete(i)
        check = bt.check_red_black_properties()
        print("Checking red-black properties:", check)
        if not check:
            bt.create_figure("deleted_tree.png")
            print("Tree does not satisfy red-black properties after deleting",
                  i)
            return

    bt.create_figure("deleted_tree.png")


if __name__ == "__main__":
    main()
