#!/usr/bin/python3
"""
Thema: Ein einzelner Knoten fuer einen Red-Black Tree.

Enthalten sind:
- die Klasse Node
- die Hilfsfunktion nil()
- die Hilfsfunktion leaf()

Klausurbezug:
Diese Datei uebt Klassen, __init__, Attribute, einfache Properties und den
schwarzen NIL-Knoten. Das ist wichtig, weil die RBTree-Aufgaben nicht mit
None-Kindern arbeiten, sondern mit schwarzen NIL-Knoten.
"""


class Node:
    """
    Ein einfacher Baumknoten.

    Zweck:
    Der Knoten speichert Daten fuer einen RBTree.

    Attribute:
    key: Sortierschluessel des Knotens.
    value: Wert, der zum Schluessel gehoert.
    color: RED oder BLACK.
    parent: Elternknoten.
    left/right: linkes und rechtes Kind.

    Methoden:
    is_nil, is_red und is_black pruefen den Zustand des Knotens.
    """

    RED = "RED"
    BLACK = "BLACK"

    def __init__(self, key, value=None, color=BLACK, parent=None):
        """
        Erstellt einen neuen Knoten.

        Parameter:
        key: Schluessel des Knotens.
        value: gespeicherter Wert.
        color: Farbe des Knotens.
        parent: Elternknoten oder None.

        Rueckgabe:
        Keine direkte Rueckgabe. __init__ bereitet das neue Objekt vor.

        Logik:
        self bedeutet: Dieses Objekt bekommt eigene Attribute.
        left und right werden spaeter gesetzt.
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
        Nur self, also der aktuelle Knoten.

        Rueckgabe:
        True, wenn key und value leer sind und die Farbe BLACK ist.

        Logik:
        In den RBTree-Aufgaben sind fehlende Kinder schwarze NIL-Knoten.
        """
        return self.key is None and self.value is None and self.color == Node.BLACK

    @property
    def is_red(self):
        """
        Prueft, ob der Knoten rot ist.

        Parameter:
        Nur self.

        Rueckgabe:
        True, wenn color gleich RED ist.

        Logik:
        Der Vergleich ist kurz, damit man ihn in if-Bedingungen nutzen kann.
        """
        return self.color == Node.RED

    @property
    def is_black(self):
        """
        Prueft, ob der Knoten schwarz ist.

        Parameter:
        Nur self.

        Rueckgabe:
        True, wenn color gleich BLACK ist.

        Logik:
        NIL-Knoten sind immer schwarz.
        """
        return self.color == Node.BLACK


def nil(parent=None):
    """
    Erstellt einen schwarzen NIL-Knoten.

    Parameter:
    parent: Elternknoten fuer den NIL-Knoten.

    Rueckgabe:
    Einen Node ohne key und value, aber mit Farbe BLACK.

    Logik:
    Ein NIL-Knoten steht fuer ein fehlendes Kind im RBTree.
    """
    return Node(None, None, Node.BLACK, parent)


def leaf(key, value=None, color=Node.RED, parent=None):
    """
    Erstellt einen normalen Datenknoten mit NIL-Kindern.

    Parameter:
    key, value, color und parent beschreiben den neuen Knoten.

    Rueckgabe:
    Den fertig vorbereiteten Knoten.

    Logik:
    Nach dem Erstellen bekommt der Knoten links und rechts je einen NIL-Knoten.
    """
    node = Node(key, value, color, parent)
    # Jeder echte RBTree-Knoten hat links und rechts einen NIL-Knoten.
    node.left = nil(node)
    node.right = nil(node)
    return node


if __name__ == "__main__":
    root = leaf(20, "twenty", Node.BLACK)
    root.left = leaf(10, "ten", Node.RED, root)
    print(root.key, root.color, root.left.key, root.left.parent.key)
    print("left nil?", root.left.left.is_nil)
