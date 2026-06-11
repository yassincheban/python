#!/usr/bin/python3

import json


RED = "RED"
BLACK = "BLACK"


class RBNode:
    """
    Ein kleiner Knoten fuer RBTree-nahe Aufgaben.

    Ein echter Knoten hat key und value.
    Ein NIL-Knoten hat key=None, value=None und color=BLACK.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        self.key = key
        self._value = value
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

    @property
    def value(self):
        # TODO Mini-Aufgabe: Geben Sie self._value zurueck.
        pass

    @value.setter
    def value(self, value):
        # TODO Mini-Aufgabe: Speichern Sie value in self._value.
        pass

    @property
    def is_nil(self):
        return self.key is None and self._value is None and self.color == BLACK

    @property
    def is_red(self):
        return not self.is_nil and self.color == RED

    @property
    def is_black(self):
        return self.is_nil or self.color == BLACK


def nil(parent=None):
    return RBNode(None, None, BLACK, parent)


def new_node(key, value=None, color=RED, parent=None):
    node = RBNode(key, value, color, parent)
    node.left = nil(node)
    node.right = nil(node)
    return node


class RBTreeExam:
    """
    Ein RBTree-Scaffold fuer Zugriffsmethoden und JSON.

    insert_without_fix() ist nur eine Hilfsmethode fuer Beispieldaten und load.
    Die RBTree-Fix-Faelle sind nicht Teil dieser Probeklausur.
    """

    def __init__(self):
        self._root = nil()

    def is_empty(self, node) -> bool:
        return node is None or node.is_nil

    def insert_without_fix(self, key, value=None) -> None:
        if self._root.is_nil:
            self._root = new_node(key, value, BLACK)
            return

        parent = None
        current = self._root
        while not current.is_nil:
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

    def min_key(self):
        """
        TODO:
        - Werfen Sie KeyError, wenn der Baum leer ist.
        - Starten Sie bei self._root.
        - Laufen Sie nach links, solange das linke Kind kein NIL-Knoten ist.
        - Geben Sie den key des gefundenen Knotens zurueck.
        """
        pass

    def max_key(self):
        """
        TODO:
        - Werfen Sie KeyError, wenn der Baum leer ist.
        - Starten Sie bei self._root.
        - Laufen Sie nach rechts, solange das rechte Kind kein NIL-Knoten ist.
        - Geben Sie den key des gefundenen Knotens zurueck.
        """
        pass

    def find(self, key):
        """
        TODO:
        - Suchen Sie iterativ ab self._root.
        - Bei gleichem key geben Sie value zurueck.
        - Bei kleinerem key gehen Sie links, sonst rechts.
        - Wenn NIL erreicht wird, werfen Sie KeyError.
        """
        pass

    def _between_rec(self, node, low, high, result):
        """
        TODO:
        - Brechen Sie bei NIL ab.
        - Besuchen Sie links nur, wenn dort Werte im Bereich liegen koennen.
        - Fuegen Sie node.key hinzu, wenn low <= node.key <= high gilt.
        - Besuchen Sie rechts nur, wenn dort Werte im Bereich liegen koennen.
        """
        pass

    def between(self, low, high):
        result = []
        if low > high:
            return result
        self._between_rec(self._root, low, high, result)
        return result

    def count_color(self, color):
        """
        TODO:
        - Zaehlen Sie alle echten Knoten mit der Farbe color.
        - NIL-Knoten sollen 0 zaehlen.
        - Nutzen Sie eine rekursive Hilfsfunktion oder eine innere Funktion.
        - Geben Sie die Anzahl als int zurueck.
        """
        pass

    def _to_dict_rec(self, node, data):
        """
        TODO:
        - Brechen Sie bei NIL ab.
        - Speichern Sie data[str(node.key)] = node.value.
        - Besuchen Sie danach links und rechts.
        """
        pass

    def to_dict(self):
        data = {}
        self._to_dict_rec(self._root, data)
        return data

    def dump(self, filename):
        """
        TODO:
        - Nutzen Sie to_dict(), um die Baumdaten vorzubereiten.
        - Oeffnen Sie filename zum Schreiben.
        - Speichern Sie die Daten mit json.dump(..., indent=4).
        """
        pass

    def load_from_dict(self, data):
        """
        TODO:
        - Setzen Sie self._root wieder auf nil().
        - Iterieren Sie ueber data.items().
        - Wandeln Sie den key mit int(key) zurueck in eine Zahl.
        - Fuegen Sie key und value mit insert_without_fix() ein.
        """
        pass


EXAMPLE_ITEMS = [
    (40, "root"),
    (20, "left"),
    (60, "right"),
    (10, "left-left"),
    (30, "left-right"),
    (50, "right-left"),
    (70, "right-right"),
]


def build_example_tree():
    tree = RBTreeExam()
    for key, value in EXAMPLE_ITEMS:
        tree.insert_without_fix(key, value)
    return tree


def main():
    print("Probeklausur 02: RBTree Zugriff und JSON")
    print("Beispieldaten:", EXAMPLE_ITEMS)
    print("Fuellen Sie die TODO-Stellen, bevor Sie die Methoden testen.")


if __name__ == "__main__":
    main()
