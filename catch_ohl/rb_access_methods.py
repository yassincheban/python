#!/usr/bin/python3
"""
Thema: Methoden in einer RBTree-Klasse, wie sie in einer Klausur vorkommen koennen.

Enthalten sind:
- RBTreeNode
- RBTree
- max(), min(), find(), between()
- visit_post_order(), visit_level_order()

Klausurbezug:
Die alte Klausur zeigt moegliche Methodentypen. Hier sind sie in RBTree-Form
mit NIL-Knoten umgesetzt. Es geht vor allem um Python: Klassen, Methoden,
Rekursion, Listen und Bedingungen.
"""


RED = "RED"
BLACK = "BLACK"


class RBTreeNode:
    """
    Ein Knoten fuer die Klasse RBTree.

    Zweck:
    Der Knoten speichert Daten und Verbindungen zu anderen Knoten.

    Attribute:
    key: Sortierschluessel.
    value: gespeicherter Wert.
    color: RED oder BLACK.
    parent: Elternknoten.
    left/right: Kinder.

    Methoden:
    is_nil prueft, ob es ein schwarzer leerer NIL-Knoten ist.
    """

    def __init__(self, key, value=None, color=RED, parent=None):
        """
        Erstellt einen RBTreeNode.

        Parameter:
        key, value, color und parent beschreiben den Knoten.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        self speichert die Daten im aktuellen Objekt. Kinder werden danach
        gesetzt.
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
        True, wenn key/value leer sind und der Knoten schwarz ist.

        Logik:
        NIL-Knoten sind keine Daten, sondern markieren fehlende Kinder.
        """
        return self.key is None and self.value is None and self.color == BLACK


def nil(parent=None):
    """
    Erstellt einen NIL-Knoten.

    Parameter:
    parent: Elternknoten.

    Rueckgabe:
    Schwarzen leeren RBTreeNode.

    Logik:
    Jeder echte Knoten kann solche NIL-Kinder haben.
    """
    return RBTreeNode(None, None, BLACK, parent)


def new_node(key, value=None, color=RED, parent=None):
    """
    Erstellt einen echten Knoten mit NIL-Kindern.

    Parameter:
    key, value, color, parent.

    Rueckgabe:
    Den neuen Knoten.

    Logik:
    left und right werden sofort auf NIL gesetzt, damit Methoden sicher sind.
    """
    node = RBTreeNode(key, value, color, parent)
    node.left = nil(node)
    node.right = nil(node)
    return node


class RBTree:
    """
    Eine kleine RBTree-Klasse fuer typische Zugriffsmethoden.

    Zweck:
    Die Klasse zeigt, wie Methoden auf self._root arbeiten.

    Attribute:
    _root ist die Wurzel des Baums.

    Methoden:
    insert_without_fix baut Beispielbaeume.
    max, min, find, between und Visitor-Methoden sind klausurnahe Aufgaben.
    """

    def __init__(self):
        """
        Erstellt einen leeren Baum.

        Parameter:
        Nur self.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        Ein leerer RBTree startet mit einem NIL-Knoten als Wurzel.
        """
        self._root = nil()

    def insert_without_fix(self, key, value):
        """
        Fuegt fuer Beispiele einen Knoten ein.

        Parameter:
        key: Schluessel.
        value: Wert.

        Rueckgabe:
        None.

        Logik:
        Diese Methode sucht die passende Position wie in einem BST. Sie macht
        keinen RBTree-Fix, weil diese Datei die Zugriffsmethoden zeigt.
        """
        if self._root.is_nil:
            self._root = new_node(key, value, BLACK)
            return

        current = self._root
        parent = None
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

    def max(self):
        """
        Gibt den groessten key zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        Groesster key.

        Logik:
        Im Suchbaum liegt der groesste key ganz rechts. Deshalb wird so lange
        rechts gelaufen, bis rechts ein NIL-Knoten steht.
        """
        if self._root.is_nil:
            raise KeyError("empty tree")
        node = self._root
        while not node.right.is_nil:
            node = node.right
        return node.key

    def min(self):
        """
        Gibt den kleinsten key zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        Kleinster key.

        Logik:
        Im Suchbaum liegt der kleinste key ganz links.
        """
        if self._root.is_nil:
            raise KeyError("empty tree")
        node = self._root
        while not node.left.is_nil:
            node = node.left
        return node.key

    def find(self, key):
        """
        Sucht den value zu einem key.

        Parameter:
        key: gesuchter Schluessel.

        Rueckgabe:
        value des gefundenen Knotens.

        Logik:
        Der Vergleich entscheidet links oder rechts. Wird NIL erreicht, gibt
        es den key nicht und KeyError wird geworfen.
        """
        node = self._root
        while not node.is_nil:
            if key == node.key:
                return node.value
            if key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError(key)

    def _between_rec(self, node, low, high, result):
        """
        Hilfsfunktion fuer between().

        Parameter:
        node: aktueller Teilbaum.
        low/high: Grenzen.
        result: Liste, die gefuellt wird.

        Rueckgabe:
        None.

        Logik:
        Rekursion spart unnoetige Teilbaeume. Links wird nur besucht, wenn
        dort noch Werte >= low liegen koennen.
        """
        if node.is_nil:
            return
        if low < node.key:
            self._between_rec(node.left, low, high, result)
        if low <= node.key <= high:
            result.append(node.key)
        if node.key < high:
            self._between_rec(node.right, low, high, result)

    def between(self, low, high):
        """
        Gibt alle keys im Bereich [low, high] zurueck.

        Parameter:
        low: untere Grenze.
        high: obere Grenze.

        Rueckgabe:
        Liste mit keys.

        Logik:
        Die Methode legt eine Ergebnisliste an und laesst die Rekursion diese
        Liste fuellen.
        """
        result = []
        self._between_rec(self._root, low, high, result)
        return result

    def _visit_post_order_rec(self, node, callback):
        """
        Hilfsfunktion fuer Postorder-Visitor.

        Parameter:
        node: aktueller Knoten.
        callback: Funktion, die einen key bekommt.

        Rueckgabe:
        None.

        Logik:
        Erst links, dann rechts, dann callback fuer den aktuellen Knoten.
        """
        if node.is_nil:
            return
        self._visit_post_order_rec(node.left, callback)
        self._visit_post_order_rec(node.right, callback)
        callback(node.key)

    def visit_post_order(self, callback):
        """
        Besucht alle Knoten in Postorder.

        Parameter:
        callback: Funktion mit einem key als Parameter.

        Rueckgabe:
        None.

        Logik:
        Die eigentliche Rekursion steht in der Hilfsfunktion.
        """
        self._visit_post_order_rec(self._root, callback)

    def visit_level_order(self, callback):
        """
        Besucht alle Knoten Ebene fuer Ebene.

        Parameter:
        callback: Funktion mit einem key als Parameter.

        Rueckgabe:
        None.

        Logik:
        Eine Liste wird als Queue benutzt. So werden erst alle Knoten einer
        Ebene besucht, bevor die naechste Ebene kommt.
        """
        if self._root.is_nil:
            return

        queue = [self._root]
        while queue:
            node = queue.pop(0)
            callback(node.key)
            # Nur echte Kinder kommen in die Queue, keine NIL-Knoten.
            if not node.left.is_nil:
                queue.append(node.left)
            if not node.right.is_nil:
                queue.append(node.right)


if __name__ == "__main__":
    tree = RBTree()
    for key in [20, 10, 5, 15, 30, 25, 40]:
        tree.insert_without_fix(key, str(key))

    print("min", tree.min())
    print("max", tree.max())
    print("find 25", tree.find(25))
    print("between 10..30", tree.between(10, 30))

    seen = []
    tree.visit_post_order(seen.append)
    print("post", seen)

    seen = []
    tree.visit_level_order(seen.append)
    print("level", seen)
