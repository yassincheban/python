#!/usr/bin/python3
"""
Thema: Traversals, also verschiedene Reihenfolgen zum Durchlaufen eines Baums.

Enthalten sind:
- inorder(), preorder(), postorder(), levelorder()
- levelorder_with_level()
- visit_in_order(), visit_post_order(), visit_level_order()
- einfache RBTree-Knoten mit NIL-Kindern

Klausurbezug:
Traversal-Aufgaben pruefen Rekursion, Listen, Schleifen und Callback-Funktionen.
Das passt direkt zu den bisherigen Baum-Aufgaben.
"""


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein kleiner Knoten fuer Traversal-Uebungen.

    Zweck:
    Der Knoten speichert nur das, was fuer die Reihenfolgen gebraucht wird.

    Attribute:
    key ist der Wert, der ausgegeben wird.
    color ist fuer RBTree-Kontext da.
    parent, left und right bilden die Baumstruktur.

    Methoden:
    is_nil prueft, ob ein Kind nur ein NIL-Knoten ist.
    """

    def __init__(self, key, color=RED, parent=None):
        """
        Erstellt einen Knoten.

        Parameter:
        key: Schluessel.
        color: RED oder BLACK.
        parent: Elternknoten.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        self bedeutet: Diese Werte gehoeren zu genau diesem Objekt.
        """
        self.key = key
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
        True, wenn key leer ist und color BLACK ist.

        Logik:
        Traversals sollen NIL-Knoten nicht als Daten besuchen.
        """
        return self.key is None and self.color == BLACK


def nil(parent=None):
    """
    Erstellt einen NIL-Knoten.

    Parameter:
    parent: Elternknoten.

    Rueckgabe:
    Schwarzen leeren Knoten.

    Logik:
    Der NIL-Knoten beendet Rekursion und Schleifen.
    """
    return Node(None, BLACK, parent)


def new_node(key, color=RED, parent=None):
    """
    Erstellt einen normalen Knoten mit NIL-Kindern.

    Parameter:
    key, color, parent fuer den neuen Knoten.

    Rueckgabe:
    Den neuen Knoten.

    Logik:
    left und right werden sofort gesetzt, damit Traversals sicher zugreifen.
    """
    node = Node(key, color, parent)
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
    So stoppen Rekursion und Levelorder-Schleife an leeren Stellen.
    """
    return node is None or node.is_nil


def inorder(root):
    """
    Gibt die keys in Inorder zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von keys.

    Logik:
    Links, aktueller Knoten, rechts. Bei Suchbaeumen ist das sortiert.
    """
    if is_empty(root):
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


def preorder(root):
    """
    Gibt die keys in Preorder zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von keys.

    Logik:
    Aktueller Knoten zuerst, dann links, dann rechts.
    """
    if is_empty(root):
        return []
    return [root.key] + preorder(root.left) + preorder(root.right)


def postorder(root):
    """
    Gibt die keys in Postorder zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von keys.

    Logik:
    Erst Kinder, dann aktueller Knoten. Das kann in Klausuren als Visitor
    gefragt werden.
    """
    if is_empty(root):
        return []
    return postorder(root.left) + postorder(root.right) + [root.key]


def levelorder(root):
    """
    Gibt die keys Ebene fuer Ebene zurueck.

    Parameter:
    root: Wurzel des Baums.

    Rueckgabe:
    Liste von keys.

    Logik:
    Eine normale Liste wird als Queue genutzt. pop(0) nimmt den aeltesten
    Knoten. Danach werden seine Kinder angehaengt.
    """
    if is_empty(root):
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.key)
        # NIL-Kinder werden nicht in die Queue gelegt, weil sie keine Daten haben.
        if not is_empty(node.left):
            queue.append(node.left)
        if not is_empty(node.right):
            queue.append(node.right)
    return result


def levelorder_with_level(root):
    """
    Gibt keys zusammen mit ihrer Ebene zurueck.

    Parameter:
    root: Wurzel des Baums.

    Rueckgabe:
    Liste von Tupeln, zum Beispiel (20, 0).

    Logik:
    In der Queue liegt nicht nur der Knoten, sondern auch seine Ebene.
    Kinder bekommen immer level + 1.
    """
    if is_empty(root):
        return []

    result = []
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        result.append((node.key, level))
        if not is_empty(node.left):
            queue.append((node.left, level + 1))
        if not is_empty(node.right):
            queue.append((node.right, level + 1))
    return result


def visit_in_order(root, callback):
    """
    Ruft callback fuer jeden key in Inorder auf.

    Parameter:
    root: Wurzel oder Teilbaum.
    callback: Funktion, die einen key bekommt.

    Rueckgabe:
    None.

    Logik:
    Die Reihenfolge ist links, aktueller Knoten, rechts. Gesammelt wird nicht
    in der Funktion, sondern im callback.
    """
    if is_empty(root):
        return
    visit_in_order(root.left, callback)
    callback(root.key)
    visit_in_order(root.right, callback)


def visit_post_order(root, callback):
    """
    Ruft callback fuer jeden key in Postorder auf.

    Parameter:
    root: Wurzel oder Teilbaum.
    callback: Funktion, die einen key bekommt.

    Rueckgabe:
    None.

    Logik:
    Die Funktion sammelt nichts selbst, sondern uebergibt jeden key an callback.
    """
    if is_empty(root):
        return
    visit_post_order(root.left, callback)
    visit_post_order(root.right, callback)
    callback(root.key)


def visit_level_order(root, callback):
    """
    Ruft callback fuer jeden key in Levelorder auf.

    Parameter:
    root: Wurzel des Baums.
    callback: Funktion, die einen key bekommt.

    Rueckgabe:
    None.

    Logik:
    Die vorhandene Funktion levelorder() liefert die Reihenfolge, danach wird
    jeder key einzeln an callback gegeben.
    """
    for key in levelorder(root):
        callback(key)


if __name__ == "__main__":
    root = new_node(20, BLACK)
    root.left = new_node(10, RED, root)
    root.right = new_node(30, RED, root)
    root.left.left = new_node(5, BLACK, root.left)
    root.left.right = new_node(15, BLACK, root.left)
    root.right.left = new_node(25, BLACK, root.right)
    root.right.right = new_node(40, BLACK, root.right)

    print("in", inorder(root))
    print("pre", preorder(root))
    print("post", postorder(root))
    print("level", levelorder(root))
    print("level with level", levelorder_with_level(root))

    seen = []
    visit_in_order(root, seen.append)
    print("callback in", seen)

    seen = []
    visit_post_order(root, seen.append)
    print("callback post", seen)

    seen = []
    visit_level_order(root, seen.append)
    print("callback level", seen)
