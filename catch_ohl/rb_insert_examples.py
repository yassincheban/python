#!/usr/bin/python3
"""
Thema: Einfuegen in einen Red-Black Tree.

Enthalten sind:
- left_rotate(), right_rotate()
- fix_insert()
- insert()
- insert_many()
- insert_or_replace()
- inorder()

Klausurbezug:
Diese Datei passt zu RBTree1. Man uebt Klassen, Bedingungen, Schleifen,
Rotationen und Umfaerben. Die Erklaerung bleibt praktisch: Welche Zeile
haelt die RBTree-Regeln wieder ein?
"""


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein Knoten fuer RBTree-Insert.

    Zweck:
    Der Knoten speichert key/value, Farbe und Baumverbindungen.

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
        Der Knoten speichert seine Daten. left/right werden danach gesetzt.
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
        True bei schwarzem Knoten ohne Daten.

        Logik:
        Insert laeuft bis zu einem NIL-Knoten und ersetzt ihn durch Daten.
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
    NIL-Knoten sind die Blaetter im RBTree.
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
    Neue eingefuegte RBTree-Knoten sind normalerweise rot.
    """
    result = Node(key, value, color, parent)
    result.left = nil(result)
    result.right = nil(result)
    return result


def is_empty(node):
    """
    Prueft auf None oder NIL.

    Parameter:
    node: Knoten oder None.

    Rueckgabe:
    True bei None oder NIL.

    Logik:
    So endet die Suche nach der Einfuegestelle.
    """
    return node is None or node.is_nil


def is_red(node):
    """
    Prueft, ob ein Knoten rot ist.

    Parameter:
    node: Knoten.

    Rueckgabe:
    True bei echten roten Knoten.

    Logik:
    NIL ist nicht rot und wird vorher ausgeschlossen.
    """
    return not is_empty(node) and node.color == RED


def left_rotate(root, node):
    """
    Fuehrt eine Linksrotation aus.

    Parameter:
    root: aktuelle Wurzel.
    node: Knoten, um den rotiert wird.

    Rueckgabe:
    Neue Wurzel des Baums.

    Logik:
    node.right wandert nach oben. Parent-Links muessen mitgepflegt werden,
    sonst ist der Baum danach kaputt.
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
    root: aktuelle Wurzel.
    node: Knoten, um den rotiert wird.

    Rueckgabe:
    Neue Wurzel des Baums.

    Logik:
    node.left wandert nach oben. Das ist die gespiegelte Form der
    Linksrotation.
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
    Repariert den RBTree nach dem Einfuegen.

    Parameter:
    root: Wurzel.
    node: neu eingefuegter roter Knoten.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Solange der Elternknoten rot ist, ist eine RB-Regel verletzt. Dann werden
    Uncle-Faelle, Rotationen und Umfaerbungen angewendet.
    """
    while node.parent is not None and is_red(node.parent):
        grand = node.parent.parent
        if node.parent == grand.left:
            uncle = grand.right
            if is_red(uncle):
                # Fall 1: Parent und Uncle sind rot, also beide schwarz machen.
                node.parent.color = BLACK
                uncle.color = BLACK
                grand.color = RED
                node = grand
            else:
                # Innenfall: erst drehen, damit danach der Aussenfall entsteht.
                if node == node.parent.right:
                    node = node.parent
                    root = left_rotate(root, node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                root = right_rotate(root, node.parent.parent)
        else:
            # Gleiche Logik wie oben, nur links/rechts gespiegelt.
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

    # Die Wurzel muss am Ende immer schwarz sein.
    root.color = BLACK
    root.parent = None
    return root


def insert(root, key, value=None):
    """
    Fuegt einen neuen key/value ein.

    Parameter:
    root: Wurzel.
    key: neuer Schluessel.
    value: neuer Wert.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Erst wird wie im Suchbaum eingefuegt. Der neue Knoten ist rot. Danach
    repariert fix_insert die RBTree-Regeln.
    """
    if is_empty(root):
        return new_node(key, value, BLACK)

    parent = None
    current = root
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

    return fix_insert(root, added)


def find_node(root, key):
    """
    Sucht einen Knoten nach key.

    Parameter:
    root: Wurzel.
    key: gesuchter Schluessel.

    Rueckgabe:
    Knoten oder None.

    Logik:
    Diese kleine Hilfsfunktion wird fuer die Duplikat-Variante benutzt.
    """
    current = root
    while not is_empty(current):
        if key == current.key:
            return current
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return None


def insert_or_replace(root, key, value=None):
    """
    Fuegt einen key ein oder ersetzt den value bei vorhandenem key.

    Parameter:
    root: Wurzel.
    key: neuer oder vorhandener Schluessel.
    value: neuer Wert.

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Manche Klausurvarianten erlauben keine doppelten Keys. Dann wird zuerst
    gesucht. Wenn der key existiert, wird nur der value geaendert.
    """
    found = find_node(root, key)
    if found is not None:
        found.value = value
        return root
    return insert(root, key, value)


def insert_many(root, items):
    """
    Fuegt mehrere Eintraege nacheinander ein.

    Parameter:
    root: Wurzel.
    items: Liste von Tupeln wie [(10, "10")].

    Rueckgabe:
    Neue Wurzel.

    Logik:
    Die Schleife ruft fuer jedes Tupel die normale insert()-Funktion auf.
    Dadurch wird nach jedem Einfuegen wieder repariert.
    """
    for key, value in items:
        root = insert(root, key, value)
    return root


def inorder(root):
    """
    Gibt key und color in Inorder zurueck.

    Parameter:
    root: Wurzel oder Teilbaum.

    Rueckgabe:
    Liste von Tupeln, zum Beispiel (10, "BLACK").

    Logik:
    NIL-Knoten liefern eine leere Liste. Echte Knoten werden links-node-rechts
    gesammelt.
    """
    if is_empty(root):
        return []
    return inorder(root.left) + [(root.key, root.color)] + inorder(root.right)


if __name__ == "__main__":
    root = nil()
    for key in [10, 20, 30, 15, 5, 25, 40]:
        root = insert(root, key, str(key))
        print("after", key, inorder(root))
    root = insert_or_replace(root, 25, "changed")
    print("root", root.key, root.color)
    print("value 25", find_node(root, 25).value)

    other = insert_many(nil(), [(7, "seven"), (3, "three"), (9, "nine")])
    print("many", inorder(other))
