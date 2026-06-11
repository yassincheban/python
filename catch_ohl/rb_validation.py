#!/usr/bin/python3
"""
Thema: Einfache Pruefungen fuer Red-Black Trees.

Enthalten sind:
- count_color()
- validate_bst_order()
- black_height()
- no_red_red()
- validate_rb_tree()

Klausurbezug:
Solche Funktionen pruefen Rekursion, boolsche Rueckgaben und Bedingungen.
Es geht nicht um tiefe Theorie, sondern um sauber geschriebenen Python-Code.
"""


RED = "RED"
BLACK = "BLACK"


class Node:
    """
    Ein kleiner RBTree-Knoten fuer Validierung.

    Zweck:
    Der Knoten speichert genug Daten, um RB-Regeln zu pruefen.

    Attribute:
    key, value, color, parent, left, right.

    Methoden:
    is_nil erkennt schwarze leere Kinder.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        """
        Erstellt einen Knoten.

        Parameter:
        key, value, color, parent.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        self speichert die Attribute im aktuellen Objekt.
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
        True oder False.

        Logik:
        NIL ist schwarz und hat keine Daten.
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
    NIL zaehlt bei Black-Height als schwarzes Ende.
    """
    return Node(None, None, BLACK, parent)


def node(key, color=RED, parent=None):
    """
    Erstellt einen echten Knoten fuer Tests.

    Parameter:
    key, color, parent.

    Rueckgabe:
    Knoten mit value=str(key) und NIL-Kindern.

    Logik:
    Kleine Testbaeume lassen sich damit schnell bauen.
    """
    result = Node(key, str(key), color, parent)
    result.left = nil(result)
    result.right = nil(result)
    return result


def is_empty(root):
    """
    Prueft, ob root leer ist.

    Parameter:
    root: Knoten, None oder NIL.

    Rueckgabe:
    True bei None oder NIL.

    Logik:
    Viele Pruefungen sollen bei leeren Teilbaeumen stoppen.
    """
    return root is None or root.is_nil


def is_red(root):
    """
    Prueft, ob ein Knoten rot ist.

    Parameter:
    root: Knoten.

    Rueckgabe:
    True nur bei echten roten Knoten.

    Logik:
    Leere Knoten werden nicht als rot betrachtet.
    """
    return not is_empty(root) and root.color == RED


def is_black(root):
    """
    Prueft, ob ein Knoten schwarz ist.

    Parameter:
    root: Knoten.

    Rueckgabe:
    True bei schwarz oder leer.

    Logik:
    NIL-Knoten gelten im RBTree als schwarz.
    """
    return is_empty(root) or root.color == BLACK


def count_color(root, color):
    """
    Zaehlt echte Knoten mit einer bestimmten Farbe.

    Parameter:
    root: Wurzel oder Teilbaum.
    color: RED oder BLACK.

    Rueckgabe:
    Anzahl als int.

    Logik:
    Rekursion zaehlt links, rechts und dann den aktuellen Knoten.
    NIL-Knoten werden nicht als Datenknoten gezaehlt.
    """
    if is_empty(root):
        return 0
    return (
        count_color(root.left, color)
        + count_color(root.right, color)
        + (1 if root.color == color else 0)
    )


def validate_bst_order(root, low=None, high=None):
    """
    Prueft die Suchbaum-Reihenfolge.

    Parameter:
    root: aktueller Knoten.
    low/high: erlaubte Grenzen.

    Rueckgabe:
    True, wenn alle keys richtig liegen.

    Logik:
    Links muss kleiner als root.key sein, rechts groesser. Die Grenzen werden
    in der Rekursion weitergegeben.
    """
    if is_empty(root):
        return True
    if low is not None and root.key <= low:
        return False
    if high is not None and root.key >= high:
        return False
    return validate_bst_order(root.left, low, root.key) and validate_bst_order(
        root.right, root.key, high
    )


def black_height(root):
    """
    Berechnet die Black-Height oder meldet Fehler mit 0.

    Parameter:
    root: aktueller Knoten.

    Rueckgabe:
    Black-Height als int, oder 0 wenn links und rechts nicht gleich sind.

    Logik:
    Beide Teilbaeume muessen gleiche Black-Height haben. NIL zaehlt als 1.
    """
    if is_empty(root):
        return 1

    left = black_height(root.left)
    right = black_height(root.right)
    if left == 0 or right == 0 or left != right:
        return 0
    return left + (1 if root.color == BLACK else 0)


def no_red_red(root):
    """
    Prueft die Regel: Ein roter Knoten hat keine roten Kinder.

    Parameter:
    root: aktueller Knoten.

    Rueckgabe:
    True, wenn keine rot-rot Kante gefunden wird.

    Logik:
    Bei einem roten Knoten werden beide Kinder auf rot geprueft.
    """
    if is_empty(root):
        return True
    if is_red(root) and (is_red(root.left) or is_red(root.right)):
        return False
    return no_red_red(root.left) and no_red_red(root.right)


def validate_rb_tree(root):
    """
    Prueft die wichtigsten RBTree-Regeln.

    Parameter:
    root: Wurzel des Baums.

    Rueckgabe:
    True, wenn die einfachen Regeln passen.

    Logik:
    Die Funktion kombiniert mehrere kleine Pruefungen: Wurzel schwarz,
    Suchbaum-Reihenfolge, keine rot-rot Kante und gleiche Black-Height.
    """
    if is_empty(root):
        return True
    return (
        root.color == BLACK
        and validate_bst_order(root)
        and no_red_red(root)
        and black_height(root) != 0
    )


if __name__ == "__main__":
    root = node(20, BLACK)
    root.left = node(10, RED, root)
    root.right = node(30, RED, root)
    print("valid", validate_rb_tree(root))
    print("red count", count_color(root, RED))
    print("black count", count_color(root, BLACK))

    root.left.left = node(5, RED, root.left)
    print("red-red valid?", validate_rb_tree(root))
    print("empty valid", validate_rb_tree(nil()))
