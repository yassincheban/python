#!/usr/bin/python3
"""
Thema: Suchen, Minimum, Maximum und Bereich im RBTree-Kontext.

Enthalten sind:
- Node, nil(), new_node()
- insert_bst()
- find()
- min_key()
- max_key()
- between()

Klausurbezug:
Diese Methoden sind typisch, weil sie einfache Python-Logik pruefen:
while-Schleifen, if-Bedingungen, Listen, Rueckgabewerte und KeyError.
Der Baum nutzt RBTree-NIL-Knoten, aber das Balancing ist hier absichtlich
nicht Thema.
"""


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein kleiner RBTree-Knoten fuer Suchaufgaben.

    Zweck:
    Der Knoten speichert key, value, color, parent, left und right.

    Attribute:
    key bestimmt die Position im Baum.
    value ist der gespeicherte Inhalt.
    color ist fuer RBTree-Kontext da.
    left/right sind Kindknoten, parent ist der Elternknoten.

    Methoden:
    is_nil erkennt schwarze NIL-Knoten.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        """
        Erstellt einen Knoten.

        Parameter:
        key: Schluessel zum Sortieren.
        value: gespeicherter Wert.
        color: RED oder BLACK.
        parent: Elternknoten.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        self speichert die Werte im aktuellen Objekt. left und right werden
        danach als NIL-Knoten gesetzt.
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
        Prueft, ob dieser Knoten ein NIL-Knoten ist.

        Parameter:
        Nur self.

        Rueckgabe:
        True oder False.

        Logik:
        Ein NIL-Knoten hat keinen key, keinen value und ist schwarz.
        """
        return self.key is None and self.value is None and self.color == BLACK


def nil(parent=None):
    """
    Erstellt einen NIL-Knoten.

    Parameter:
    parent: Elternknoten.

    Rueckgabe:
    Einen schwarzen Knoten ohne Daten.

    Logik:
    NIL steht fuer ein fehlendes Kind im RBTree.
    """
    return Node(None, None, BLACK, parent)


def new_node(key, value=None, color=RED, parent=None):
    """
    Erstellt einen echten Datenknoten.

    Parameter:
    key, value, color, parent beschreiben den neuen Knoten.

    Rueckgabe:
    Den neuen Knoten mit zwei NIL-Kindern.

    Logik:
    Jeder echte RBTree-Knoten bekommt links und rechts NIL-Knoten.
    """
    node = Node(key, value, color, parent)
    node.left = nil(node)
    node.right = nil(node)
    return node


def is_empty(node):
    """
    Prueft, ob ein Knoten leer ist.

    Parameter:
    node: ein Knoten, None oder NIL.

    Rueckgabe:
    True, wenn node None oder NIL ist.

    Logik:
    So kann der gleiche Test in Schleifen und Rekursion benutzt werden.
    """
    return node is None or node.is_nil


def insert_bst(root, key, value=None):
    """
    Fuegt einen Knoten nach BST-Regeln ein.

    Parameter:
    root: Wurzel des Baums.
    key: neuer Schluessel.
    value: neuer Wert.

    Rueckgabe:
    Die Wurzel des Baums.

    Logik:
    Es wird nur links/rechts gesucht und eingefuegt. RBTree-Fix wird hier
    nicht gemacht, weil diese Datei nur Suchmethoden vorbereitet.
    """
    if is_empty(root):
        return new_node(key, value, BLACK)

    current = root
    parent = None
    # Die Schleife laeuft bis zur Stelle, an der ein NIL-Knoten steht.
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


def find(root, key):
    """
    Sucht den Wert zu einem Schluessel.

    Parameter:
    root: Wurzel des Baums.
    key: gesuchter Schluessel.

    Rueckgabe:
    Den value des gefundenen Knotens.

    Logik:
    Bei kleinerem key geht man links, sonst rechts. Wenn NIL erreicht wird,
    existiert der key nicht und KeyError wird geworfen.
    """
    node = root
    while not is_empty(node):
        if key == node.key:
            return node.value
        if key < node.key:
            node = node.left
        else:
            node = node.right
    raise KeyError(key)


def min_key(root):
    """
    Findet den kleinsten Schluessel.

    Parameter:
    root: Wurzel des Baums.

    Rueckgabe:
    Kleinster key.

    Logik:
    Der kleinste key liegt ganz links. Deshalb laeuft die Schleife nach links,
    bis das linke Kind NIL ist.
    """
    if is_empty(root):
        raise KeyError("empty tree")
    node = root
    while not is_empty(node.left):
        node = node.left
    return node.key


def max_key(root):
    """
    Findet den groessten Schluessel.

    Parameter:
    root: Wurzel des Baums.

    Rueckgabe:
    Groesster key.

    Logik:
    Der groesste key liegt ganz rechts. Deshalb laeuft die Schleife nach
    rechts, bis das rechte Kind NIL ist.
    """
    if is_empty(root):
        raise KeyError("empty tree")
    node = root
    while not is_empty(node.right):
        node = node.right
    return node.key


def between(root, low, high):
    """
    Sammelt alle keys im geschlossenen Bereich [low, high].

    Parameter:
    root: Wurzel oder Teilbaum.
    low: untere Grenze.
    high: obere Grenze.

    Rueckgabe:
    Liste mit passenden keys.

    Logik:
    Die Funktion ist rekursiv. Links wird nur gesucht, wenn dort noch Werte
    im Bereich liegen koennen. Rechts genauso. Dadurch bleibt die Liste
    sortiert wie bei Inorder.
    """
    if is_empty(root) or low > high:
        return []

    result = []
    if low < root.key:
        result += between(root.left, low, high)
    if low <= root.key <= high:
        result.append(root.key)
    if root.key < high:
        result += between(root.right, low, high)
    return result


if __name__ == "__main__":
    root = nil()
    for key in [20, 10, 5, 15, 30, 25, 40]:
        root = insert_bst(root, key, str(key))

    print("min", min_key(root))
    print("max", max_key(root))
    print("find 25", find(root, 25))
    print("between 10..30", between(root, 10, 30))
    one = new_node(7, "seven", BLACK)
    print("one node", min_key(one), max_key(one))
    print("empty between", between(nil(), 1, 9))
    try:
        find(root, 99)
    except KeyError as exc:
        print("missing", exc)
