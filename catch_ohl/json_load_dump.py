#!/usr/bin/python3
"""
Thema: Baumdaten als JSON speichern und laden.

Enthalten sind:
- insert()
- preorder_items()
- dump()
- load()
- inorder_keys()

Klausurbezug:
Das passt zu RBTree3. Man uebt Dateien, Dictionaries, JSON, Schleifen und
das Umwandeln von String-Keys zurueck zu int.
"""

import json


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein kleiner RBTree-Knoten fuer Save/Load.

    Zweck:
    Der Knoten speichert key und value, damit diese nach JSON geschrieben
    und danach wieder geladen werden koennen.

    Attribute:
    key, value, color, parent, left, right.

    Methoden:
    is_nil erkennt leere schwarze Kinder.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        """
        Erstellt einen Knoten.

        Parameter:
        key: Schluessel.
        value: gespeicherter Wert.
        color: RED oder BLACK.
        parent: Elternknoten.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        Die Werte werden am Objekt gespeichert. left/right kommen danach.
        """
        self.key = key
        self.value = value
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

    @property
    def is_nil(self):
        """
        Prueft, ob der Knoten ein NIL-Knoten ist.

        Parameter:
        Nur self.

        Rueckgabe:
        True oder False.

        Logik:
        NIL-Knoten werden nicht gespeichert, weil sie keine echten Daten haben.
        """
        return self.key is None and self.value is None and self.color == BLACK


def nil(parent=None):
    """
    Erstellt einen NIL-Knoten.

    Parameter:
    parent: Elternknoten.

    Rueckgabe:
    Schwarzen leeren Knoten.

    Logik:
    NIL ist nur Strukturhilfe und wird nicht in JSON geschrieben.
    """
    return Node(None, None, BLACK, parent)


def new_node(key, value=None, color=RED, parent=None):
    """
    Erstellt einen Datenknoten mit NIL-Kindern.

    Parameter:
    key, value, color, parent.

    Rueckgabe:
    Den neuen Knoten.

    Logik:
    Direkt nach dem Erstellen werden linkes und rechtes NIL-Kind gesetzt.
    """
    node = Node(key, value, color, parent)
    node.left = nil(node)
    node.right = nil(node)
    return node


def is_empty(node):
    """
    Prueft, ob ein Knoten leer ist.

    Parameter:
    node: Knoten, None oder NIL.

    Rueckgabe:
    True bei None oder NIL.

    Logik:
    So werden beim Speichern keine NIL-Knoten besucht.
    """
    return node is None or node.is_nil


def insert(root, key, value):
    """
    Fuegt einen Knoten einfach nach BST-Regeln ein.

    Parameter:
    root: Wurzel.
    key: Schluessel als int.
    value: gespeicherter Wert.

    Rueckgabe:
    Wurzel des Baums.

    Logik:
    Diese Funktion baut nach dem Laden wieder einen Baum auf. Sie balanciert
    nicht, weil hier nur Datei-Logik geuebt wird.
    """
    if is_empty(root):
        return new_node(key, value, BLACK)

    current = root
    parent = None
    while not is_empty(current):
        parent = current
        if key < current.key:
            current = current.left
        else:
            current = current.right

    added = new_node(key, value, RED, parent)
    if key < parent.key:
        parent.left = added
    else:
        parent.right = added
    return root


def preorder_items(root):
    """
    Sammelt key/value-Paare in Preorder.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von Tupeln, zum Beispiel [(20, "20")].

    Logik:
    Erst aktueller Knoten, dann links, dann rechts. NIL-Knoten liefern [].
    """
    if is_empty(root):
        return []
    return [(root.key, root.value)] + preorder_items(root.left) + preorder_items(
        root.right
    )


def dump(root, filename):
    """
    Speichert den Baum als flaches JSON-Dictionary.

    Parameter:
    root: Wurzel.
    filename: Dateiname.

    Rueckgabe:
    None.

    Logik:
    JSON-Schluessel muessen Strings sein. Deshalb wird key mit str(key)
    gespeichert.
    """
    data = {}
    for key, value in preorder_items(root):
        data[str(key)] = value
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load(filename):
    """
    Laedt einen Baum aus einer JSON-Datei.

    Parameter:
    filename: Dateiname.

    Rueckgabe:
    Wurzel des neu aufgebauten Baums.

    Logik:
    Beim Lesen sind JSON-Keys Strings. Fuer Baumvergleiche muessen sie wieder
    int sein, also int(key).
    """
    root = nil()
    with open(filename, "r") as file:
        for key, value in json.load(file).items():
            root = insert(root, int(key), value)
    return root


def inorder_keys(root):
    """
    Gibt alle keys sortiert zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von keys.

    Logik:
    Inorder zeigt, ob der geladene Baum wieder korrekt nach keys geordnet ist.
    """
    if is_empty(root):
        return []
    return inorder_keys(root.left) + [root.key] + inorder_keys(root.right)


if __name__ == "__main__":
    root = nil()
    for key in [20, 10, 5, 15, 30, 25, 40]:
        root = insert(root, key, str(key))

    filename = "/tmp/catch_ohl_tree.json"
    dump(root, filename)
    loaded = load(filename)
    print("saved to", filename)
    print("loaded keys", inorder_keys(loaded))
