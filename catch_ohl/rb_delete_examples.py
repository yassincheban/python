#!/usr/bin/python3
"""
Thema: Loeschen in einem Red-Black Tree.

Enthalten sind:
- search(), minimum(), transplant()
- delete()
- fix_delete()
- Rotationen und ein kleines insert() fuer Testbaeume

Klausurbezug:
Diese Datei passt zu RBTree2. Wichtig sind nicht perfekte Theorie-Worte,
sondern saubere Python-Schritte: Knoten suchen, Nachfolger finden, Links
ersetzen, Farben pruefen und gespiegelte Faelle schreiben.
"""


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein Knoten fuer RBTree-Delete.

    Zweck:
    Der Knoten speichert Daten, Farbe und Baumverbindungen.

    Attribute:
    key, value, color, parent, left, right.

    Methoden:
    is_nil erkennt schwarze leere Kinder.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        """
        Erstellt einen Knoten.

        Parameter:
        key: Schluessel.
        value: Wert.
        color: RED oder BLACK.
        parent: Elternknoten.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        self speichert alle Attribute fuer genau diesen Knoten.
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
        Prueft auf NIL-Knoten.

        Parameter:
        Nur self.

        Rueckgabe:
        True, wenn der Knoten schwarz und leer ist.

        Logik:
        Beim Loeschen kann ein NIL-Knoten der Ersatzknoten sein.
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
    NIL-Knoten sind im RBTree schwarz und duerfen Parent-Links haben.
    """
    return Node(None, None, BLACK, parent)


def new_node(key, value, color=RED, parent=None):
    """
    Erstellt einen echten Knoten mit NIL-Kindern.

    Parameter:
    key, value, color, parent.

    Rueckgabe:
    Den neuen Knoten.

    Logik:
    left und right werden auf NIL gesetzt, damit spaetere Zugriffe sicher sind.
    """
    result = Node(key, value, color, parent)
    result.left = nil(result)
    result.right = nil(result)
    return result


def is_empty(node):
    """
    Prueft auf None oder NIL.

    Parameter:
    node: Knoten.

    Rueckgabe:
    True bei None oder NIL.

    Logik:
    Delete-Faelle brauchen oft diese kurze Abfrage.
    """
    return node is None or node.is_nil


def is_red(node):
    """
    Prueft, ob node rot ist.

    Parameter:
    node: Knoten.

    Rueckgabe:
    True bei echten roten Knoten.

    Logik:
    NIL ist nie rot.
    """
    return not is_empty(node) and node.color == RED


def is_black(node):
    """
    Prueft, ob node schwarz ist.

    Parameter:
    node: Knoten.

    Rueckgabe:
    True bei schwarz oder NIL.

    Logik:
    NIL wird als schwarz behandelt, wie in den RBTree-Regeln.
    """
    return is_empty(node) or node.color == BLACK


def left_rotate(root, node):
    """
    Fuehrt eine Linksrotation aus.

    Parameter:
    root: Wurzel.
    node: Drehpunkt.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Das rechte Kind wandert nach oben. Parent-Links werden angepasst, weil
    Delete-Fix sonst spaeter falsche Eltern findet.
    """
    y = node.right
    node.right = y.left
    if not is_empty(y.left):
        y.left.parent = node
    y.parent = node.parent
    if node.parent is None:
        root = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.left = node
    node.parent = y
    return root


def right_rotate(root, node):
    """
    Fuehrt eine Rechtsrotation aus.

    Parameter:
    root: Wurzel.
    node: Drehpunkt.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Das linke Kind wandert nach oben. Das ist die gespiegelte Linksrotation.
    """
    y = node.left
    node.left = y.right
    if not is_empty(y.right):
        y.right.parent = node
    y.parent = node.parent
    if node.parent is None:
        root = y
    elif node == node.parent.right:
        node.parent.right = y
    else:
        node.parent.left = y
    y.right = node
    node.parent = y
    return root


def fix_insert(root, node):
    """
    Repariert Insert fuer Testbaeume.

    Parameter:
    root: Wurzel.
    node: neu eingefuegter Knoten.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Diese Funktion ist hier nur da, damit der Delete-Testbaum gueltig startet.
    """
    while node.parent is not None and is_red(node.parent):
        grand = node.parent.parent
        if node.parent == grand.left:
            uncle = grand.right
            if is_red(uncle):
                node.parent.color = BLACK
                uncle.color = BLACK
                grand.color = RED
                node = grand
            else:
                if node == node.parent.right:
                    node = node.parent
                    root = left_rotate(root, node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                root = right_rotate(root, node.parent.parent)
        else:
            uncle = grand.left
            if is_red(uncle):
                node.parent.color = BLACK
                uncle.color = BLACK
                grand.color = RED
                node = grand
            else:
                if node == node.parent.left:
                    node = node.parent
                    root = right_rotate(root, node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                root = left_rotate(root, node.parent.parent)

    root.color = BLACK
    root.parent = None
    return root


def insert(root, key, value=None):
    """
    Fuegt fuer Beispiele einen Knoten ein.

    Parameter:
    root: Wurzel.
    key: neuer Schluessel.
    value: neuer Wert.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Erst wird normal eingefuegt, dann wird fix_insert aufgerufen.
    """
    if is_empty(root):
        return new_node(key, value, BLACK)

    parent = None
    current = root
    while not is_empty(current):
        parent = current
        current = current.left if key < current.key else current.right

    added = new_node(key, value, RED, parent)
    if key < parent.key:
        parent.left = added
    else:
        parent.right = added
    return fix_insert(root, added)


def search(root, key):
    """
    Sucht den Knoten zu einem key.

    Parameter:
    root: Wurzel.
    key: gesuchter Schluessel.

    Rueckgabe:
    Den gefundenen Knoten.

    Logik:
    Wie bei find(): kleiner geht links, groesser geht rechts. Bei NIL wird
    KeyError geworfen.
    """
    current = root
    while not is_empty(current) and current.key != key:
        current = current.left if key < current.key else current.right
    if is_empty(current):
        raise KeyError(key)
    return current


def minimum(node):
    """
    Findet den kleinsten Knoten in einem Teilbaum.

    Parameter:
    node: Wurzel des Teilbaums.

    Rueckgabe:
    Knoten mit kleinstem key.

    Logik:
    Der Nachfolger beim Loeschen liegt oft ganz links im rechten Teilbaum.
    """
    if is_empty(node):
        raise KeyError("empty tree")
    while not is_empty(node.left):
        node = node.left
    return node


def transplant(root, old, replacement):
    """
    Ersetzt old durch replacement im Baum.

    Parameter:
    root: Wurzel.
    old: Knoten, der entfernt wird.
    replacement: Ersatzknoten.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Parent-Links und Kind-Links muessen zusammen passen, sonst ist der Baum
    nach dem Loeschen falsch verbunden.
    """
    if old.parent is None:
        root = replacement
    elif old == old.parent.left:
        old.parent.left = replacement
    else:
        old.parent.right = replacement
    replacement.parent = old.parent
    return root


def fix_delete(root, node):
    """
    Repariert RBTree-Regeln nach dem Loeschen eines schwarzen Knotens.

    Parameter:
    root: Wurzel.
    node: Ersatzknoten, bei dem die Reparatur startet.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Solange node nicht die Wurzel ist und schwarz ist, wird mit dem Bruder
    gearbeitet. Die rechte Seite ist die gespiegelte Version der linken Seite.
    """
    while node != root and is_black(node):
        if node == node.parent.left:
            brother = node.parent.right
            if is_red(brother):
                # Fall 1: roter Bruder. Rotation macht daraus einen schwarzen Bruder.
                brother.color = BLACK
                node.parent.color = RED
                root = left_rotate(root, node.parent)
                brother = node.parent.right

            if is_black(brother.left) and is_black(brother.right):
                # Fall 2: Bruder hat keine roten Kinder. Problem wandert nach oben.
                if not is_empty(brother):
                    brother.color = RED
                node = node.parent
            else:
                if is_black(brother.right):
                    # Fall 3: nahes Kind rot, erst Bruder drehen.
                    brother.left.color = BLACK
                    brother.color = RED
                    root = right_rotate(root, brother)
                    brother = node.parent.right

                # Fall 4: fernes Kind rot, Elternknoten drehen und fertig.
                brother.color = node.parent.color
                node.parent.color = BLACK
                brother.right.color = BLACK
                root = left_rotate(root, node.parent)
                node = root
        else:
            # Gleiche Faelle, aber links und rechts gespiegelt.
            brother = node.parent.left
            if is_red(brother):
                brother.color = BLACK
                node.parent.color = RED
                root = right_rotate(root, node.parent)
                brother = node.parent.left

            if is_black(brother.left) and is_black(brother.right):
                if not is_empty(brother):
                    brother.color = RED
                node = node.parent
            else:
                if is_black(brother.left):
                    brother.right.color = BLACK
                    brother.color = RED
                    root = left_rotate(root, brother)
                    brother = node.parent.left

                brother.color = node.parent.color
                node.parent.color = BLACK
                brother.left.color = BLACK
                root = right_rotate(root, node.parent)
                node = root

    node.color = BLACK
    return root


def delete(root, key):
    """
    Loescht einen Knoten aus dem Baum.

    Parameter:
    root: Wurzel.
    key: zu loeschender Schluessel.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Erst wird der Knoten gesucht. Bei zwei Kindern wird der Nachfolger aus
    dem rechten Teilbaum benutzt. Wenn ein schwarzer Knoten entfernt wurde,
    muss fix_delete aufgerufen werden.
    """
    node = search(root, key)
    moved = node
    moved_original_color = moved.color

    if is_empty(node.left):
        replacement = node.right
        root = transplant(root, node, node.right)
    elif is_empty(node.right):
        replacement = node.left
        root = transplant(root, node, node.left)
    else:
        moved = minimum(node.right)
        moved_original_color = moved.color
        replacement = moved.right

        if moved.parent == node:
            replacement.parent = moved
        else:
            root = transplant(root, moved, moved.right)
            moved.right = node.right
            moved.right.parent = moved

        root = transplant(root, node, moved)
        moved.left = node.left
        moved.left.parent = moved
        moved.color = node.color

    if moved_original_color == BLACK:
        root = fix_delete(root, replacement)
    if not is_empty(root):
        root.color = BLACK
        root.parent = None
    return root


def inorder(root):
    """
    Gibt key und color in Inorder zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von Tupeln.

    Logik:
    Diese Ausgabe hilft beim Testen, ob die keys noch sortiert sind.
    """
    if is_empty(root):
        return []
    return inorder(root.left) + [(root.key, root.color)] + inorder(root.right)


if __name__ == "__main__":
    root = nil()
    for key in [20, 10, 5, 15, 30, 25, 40, 35, 50]:
        root = insert(root, key, str(key))

    print("start", inorder(root))
    for key in [5, 30, 20]:
        root = delete(root, key)
        print("delete", key, inorder(root))

    try:
        delete(root, 99)
    except KeyError as exc:
        print("missing", exc)
