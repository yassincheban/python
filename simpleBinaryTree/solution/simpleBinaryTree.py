#!/usr/bin/python3

from pprint import pprint


def get_tree() -> dict:
    """
    Create a binary tree as a nested dictionary.

    returns A binary tree represented as a nested dictionary.
    """

    # follow the !extact! structure:
    # {
    #     'value': int,
    #     'left': {...} or None,
    #     'right': {...} or None
    # }

    # example data!
    tree = {
        'value': 100,
        'right': {
            'value': 125,
            'left': {
                'value': 115,
                'left': None,
                'right': None
            },
            'right': {
                'value': 150,
                'left': {
                    'value': 135,
                    'left': None,
                    'right': None
                },
                'right': {
                    'value': 175,
                    'left': None,
                    'right': None
                }
            }
        },
        'left': {
            'value': 75,
            'left': {
                'value': 65,
                'left': {
                    'value': 60,
                    'left': None,
                    'right': None
                },
                'right': {
                    'value': 70,
                    'left': None,
                    'right': None
                }
            },
            'right': {
                'value': 85,
                'left': {
                    'value': 80,
                    'left': None,
                    'right': None
                },
                'right': {
                    'value': 95,
                    'left': None,
                    'right': None
                }
            }
        },
    }
    return tree


def generate_tree_inorder(tree: dict) -> str:
    """
    Print the binary tree in inorder traversal.
    
    tree (dict): The binary tree represented as a nested dictionary.
    returns A string representation of the tree in inorder traversal. seperated by newlines.
    """
    value = ""
    if tree is not None:
        value += generate_tree_inorder(tree['left'])
        value += f"{tree['value']}\n"
        value += generate_tree_inorder(tree['right'])
    return value


def generate_tree_preorder(tree: dict) -> str:
    """
    Print the binary tree in inorder traversal.
    
    tree (dict): The binary tree represented as a nested dictionary.
    returns A string representation of the tree in preorder traversal. seperated by newlines.
    """
    value = ""
    if tree is not None:
        # add subtree values in preorder
        value += f"{tree['value']}\n"
        value += generate_tree_preorder(tree['left'])
        value += generate_tree_preorder(tree['right'])

    return value


def generate_tree_postorder(tree: dict) -> str:
    """
    Print the binary tree in inorder traversal.
    
    tree (dict): The binary tree represented as a nested dictionary.
    returns A string representation of the tree in postorder traversal. seperated by newlines.
    """
    value = ""
    if tree is not None:
        # add subtree values in postorder
        value += generate_tree_postorder(tree['left'])
        value += generate_tree_postorder(tree['right'])
        value += f"{tree['value']}\n"

    return value


def generate_tree_levelorder(tree: dict) -> str:
    """
    Print the binary tree in inorder traversal.
    
    tree (dict): The binary tree represented as a nested dictionary.
    returns A string representation of the tree in levelorder traversal. seperated by newlines.
    """
    value = ""
    if tree is not None:
        # add subtree values in levelorder
        queue = [tree]
        while queue:
            current = queue.pop(0)
            value += f"{current['value']}\n"
            if current['left'] is not None:
                queue.append(current['left'])
            if current['right'] is not None:
                queue.append(current['right'])

        value += "\n".join(list(map(lambda x: f"{x['value']}", queue)))

        pass

    return value


def main():
    print("inorder:\n" + generate_tree_inorder(get_tree()), end='')
    print("preorder:\n" + generate_tree_preorder(get_tree()), end='')
    print("postorder:\n" + generate_tree_postorder(get_tree()), end='')
    print("levelorder:\n" + generate_tree_levelorder(get_tree()), end='')


if __name__ == "__main__":
    main()
