#!/usr/bin/python3

from pprint import pprint
import math


class AVLTreeNode:
    """
    AVL Tree Node
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
    def depth(self) -> int:
        """ Return the depth of the node """
        left_depth = 0 if self.left is None else self.left.depth
        right_depth = 0 if self.right is None else self.right.depth
        return max(left_depth, right_depth) + 1

    @property
    def balance_factor(self) -> int:
        """ Return the balance factor of the node """
        left_depth = 0 if self.left is None else self.left.depth
        right_depth = 0 if self.right is None else self.right.depth
        return left_depth - right_depth

    @property
    def is_leaf(self) -> bool:
        """ Return True if the node is a leaf """
        return self._left is None and self._right is None

    @property
    def left(self) -> 'AVLTreeNode':
        """
        Return the left child of the node
        """
        return self._left

    @property
    def right(self) -> 'AVLTreeNode':
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
    def left(self, node: 'AVLTreeNode'):
        """
        Set the left child of the node
        """
        self._left = node

    @right.setter
    def right(self, node: 'AVLTreeNode'):
        """
        Set the right child of the node
        """
        self._right = node


class AVLTree:
    """
    AVL Tree
    """

    def __init__(self):
        """
        Initialize the tree
        """
        self._root = None

    def max(self) -> int:
        """
        Return the maximum key in the tree
        :return: Maximum key
        """

        #search for maximum key logic here
        max = 0 
        for node in self._root:
            if node.key > max:
                max = node.key  

        return max  # example value, replace with actual implementation

    def find(self, key: int) -> any:
        """
        Find the value associated with the given key
        :param key: Key to find
        :return: Value associated with the key
        :raise KeyError, if the key is not found
        """

        # implement search logic here

        pass

    def min(self) -> int:
        """
        Return the minimum key in the tree
        :return: Minimum key
        """
    
        #search for minimum key logic here

        return -999  # example value, replace with actual implementation

    def between(self, low: int, high: int) -> list:
        """
        Return a list of keys between low and high
        :param low: Low key
        :param high: High key
        :return: List of keys between low and high
        """
        result = [1, 2, 3]  # example value, replace with actual implementation

        # implement between logic here and add keys to result

        return result

    def visit_post_order(self, callback) -> None:
        """
        Visit all nodes in post-order and call the callback function
        :param callback: Callback function to call for each node

        callback has the signature func(key: int) -> None
        """

        # implement post-order traversal logic here

        pass

    def visit_level_order(self, callback) -> None:
        """
        Visit all nodes in level-order and call the callback function
        :param callback: Callback function to call for each node

        callback has the signature func(key: int) -> None
        """

        # implement level-order traversal logic here

        pass

    def _left_rotate(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Perform a left rotation on the given node
        :param node: Node to rotate
        :return: New root of the subtree
        """
        #print("rotate left on node", node.key)
        new_node = node.right
        tmp = new_node.left
        new_node.left = node
        node.right = tmp
        return new_node

    def _right_rotate(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Perform a right rotation on the given node
        :param node: Node to rotate
        :return: New root of the subtree
        """
        #print("rotate right on node", node.key)
        new_node = node.left
        tmp = new_node.right
        new_node.right = node
        node.left = tmp
        return new_node

    def _balance(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Balance the given node
        :param node: Node to balance
        :return: New root of the subtree
        """
        if node.balance_factor > 1 and node.left.balance_factor >= 0:
            # print(f"Node {node.key} is left heavy")
            return self._right_rotate(node)
        elif node.balance_factor > 1 and node.left.balance_factor < 0:
            # print(f"Node {node.key} is right left heavy")
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        elif node.balance_factor < -1 and node.right.balance_factor <= 0:
            # print(f"Node {node.key} is right heavy")
            return self._left_rotate(node)
        elif node.balance_factor < -1 and node.right.balance_factor > 0:
            # print(f"Node {node.key} is left right heavy")
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _insert_rec(self, node: AVLTreeNode, key: int,
                    value: any) -> AVLTreeNode:
        """
        Insert a new node with the given key and value
        :param node: Current node
        :param key: Key of the new node
        :param value: Value of the new node
        :return: New root of the subtree
        """
        if node is None:
            return AVLTreeNode(key, value)
        if key < node.key:
            node.left = self._insert_rec(node.left, key, value)
        else:
            node.right = self._insert_rec(node.right, key, value)

        return self._balance(node)

    def insert(self, key: int, value: any):
        """
        Insert a new node with the given key and value
        :param key: Key of the new node
        :param value: Value of the new node
        """
        # print(f"Inserting key {key} with value {value}")
        self._root = self._insert_rec(self._root, key, value)

    def _delete_leaf(self, parent: AVLTreeNode, node: AVLTreeNode):
        """
        Delete a leaf node
        :param parent: Parent of the node to delete
        :param node: Node to delete
        """
        # print(f"Deleting leaf node {node.key} of parent {parent.key}")
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    def _delete_one_child(self, parent: AVLTreeNode, node: AVLTreeNode):
        """
        Delete a node with one child
        :param parent: Parent of the node to delete
        :param node: Node to delete
        """
        # print(f"Deleting node {node.key} with one child")
        if parent.left == node:
            if node.left is not None:
                parent.left = node.left
            else:
                parent.left = node.right
        elif parent.right == node:
            if node.left is not None:
                parent.right = node.left
            else:
                parent.right = node.right

    def _delete_two_children(self, parent: AVLTreeNode, node: AVLTreeNode):
        """
        Delete a node with two children
        :param parent: Parent of the node to delete
        :param node: Node to delete
        """
        # print(f"Deleting node {node.key} with two children")
        # find the inorder successor (smallest in the right subtree)
        successor_parent = node
        successor = node.right
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        # copy the inorder successor's content to this node
        node.key = successor.key
        node.value = successor.value

        # delete the inorder successor
        if successor.is_leaf:
            self._delete_leaf(successor_parent, successor)
        else:
            self._delete_one_child(successor_parent, successor)

    def delete(self, key: int) -> None:
        """
        Delete a node with the given key
        :param key: Key of the node to delete
        """

        p, n = None, None

        def callback(parent, node, level, pos, left, right):
            nonlocal p, n, key
            if node.key == key:
                p, n = parent, node

        self._visit(callback, 0, 0, self._root)

        if n is not None:
            if n.is_leaf:
                self._delete_leaf(p, n)
            if (n.left is None
                    and n.right is not None) or (n.left is not None
                                            and n.right is None):
                self._delete_one_child(p, n)
            if n.left is not None and n.right is not None:
                self._delete_two_children(p, n)
            return
        else:
            raise KeyError(f"Key {key} not found")

    def _depth(self, node: AVLTreeNode = None) -> int:
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
               node: AVLTreeNode,
               parent: AVLTreeNode = None,
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
        # UNKLAR / FOTO FEHLT AB HIER
