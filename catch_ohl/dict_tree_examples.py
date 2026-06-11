#!/usr/bin/python3
"""
Thema: Traversieren eines Baums aus verschachtelten Dictionaries.

Enthalten sind:
- inorder()
- preorder()
- postorder()
- levelorder()

Klausurbezug:
Das passt zur Aufgabe simpleBinaryTree. Man uebt Dictionaries, Rekursion,
Listen als Queue und String-Aufbau mit Zeilenumbruechen.
"""


def inorder(tree):
    """
    Erstellt eine Inorder-Ausgabe.

    Parameter:
    tree: Dictionary-Knoten oder None.

    Rueckgabe:
    Ein String mit einem Wert pro Zeile.

    Logik:
    Erst links, dann aktueller Wert, dann rechts.
    Bei None ist der Teilbaum leer und gibt "" zurueck.
    """
    if tree is None:
        return ""
    # Rekursion: Die Funktion ruft sich fuer den linken Teilbaum selbst auf.
    return inorder(tree["left"]) + f"{tree['value']}\n" + inorder(tree["right"])


def preorder(tree):
    """
    Erstellt eine Preorder-Ausgabe.

    Parameter:
    tree: Dictionary-Knoten oder None.

    Rueckgabe:
    Ein String mit einem Wert pro Zeile.

    Logik:
    Erst aktueller Wert, dann links, dann rechts.
    """
    if tree is None:
        return ""
    return f"{tree['value']}\n" + preorder(tree["left"]) + preorder(tree["right"])


def postorder(tree):
    """
    Erstellt eine Postorder-Ausgabe.

    Parameter:
    tree: Dictionary-Knoten oder None.

    Rueckgabe:
    Ein String mit einem Wert pro Zeile.

    Logik:
    Erst links, dann rechts, dann aktueller Wert.
    """
    if tree is None:
        return ""
    return postorder(tree["left"]) + postorder(tree["right"]) + f"{tree['value']}\n"


def levelorder(tree):
    """
    Erstellt eine Levelorder-Ausgabe.

    Parameter:
    tree: Dictionary-Knoten oder None.

    Rueckgabe:
    Ein String mit einem Wert pro Zeile.

    Logik:
    Eine Liste wird als Queue benutzt. pop(0) nimmt immer den vordersten
    Knoten. Danach werden linkes und rechtes Kind hinten angehaengt.
    """
    if tree is None:
        return ""

    result = ""
    queue = [tree]
    while queue:
        node = queue.pop(0)
        result += f"{node['value']}\n"
        # Kinder werden nur angehaengt, wenn sie wirklich existieren.
        if node["left"] is not None:
            queue.append(node["left"])
        if node["right"] is not None:
            queue.append(node["right"])
    return result


if __name__ == "__main__":
    tree = {
        "value": 20,
        "left": {"value": 10, "left": None, "right": None},
        "right": {"value": 30, "left": None, "right": None},
    }
    print("inorder:\n" + inorder(tree), end="")
    print("preorder:\n" + preorder(tree), end="")
    print("postorder:\n" + postorder(tree), end="")
    print("levelorder:\n" + levelorder(tree), end="")
