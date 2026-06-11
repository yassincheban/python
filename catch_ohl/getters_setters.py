#!/usr/bin/python3
"""
Thema: Getter und Setter in einer einfachen Knotenklasse.

Enthalten sind:
- die Klasse ExamNode
- die Funktion connect_left()

Klausurbezug:
In den Aufgaben kommen oft Properties wie key, value, left, right und parent
vor. Diese Datei zeigt sehr direkt, wie ein Attribut gelesen und geaendert
wird, ohne viel Zusatzlogik.
"""


class ExamNode:
    """
    Ein Beispielknoten mit privaten Attributen und Properties.

    Zweck:
    Die Klasse zeigt das Muster aus den Aufgaben: _key ist intern,
    key ist der Zugriff von aussen.

    Attribute:
    _key, _value, _color speichern Daten.
    _left, _right, _parent speichern Baumverbindungen.

    Methoden:
    Fuer jedes wichtige Attribut gibt es einen Getter und Setter.
    """

    def __init__(self, key, value=None, color="BLACK"):
        """
        Erstellt einen Knoten.

        Parameter:
        key: Sortierschluessel.
        value: gespeicherter Wert.
        color: Farbe als Text.

        Rueckgabe:
        Keine direkte Rueckgabe.

        Logik:
        Die Unterstrich-Attribute werden direkt im Objekt gespeichert.
        """
        self._key = key
        self._value = value
        self._color = color
        self._left = None
        self._right = None
        self._parent = None

    @property
    def key(self):
        """
        Gibt den Schluessel zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._key.

        Logik:
        Der Getter erlaubt node.key statt node._key.
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Setzt den Schluessel.

        Parameter:
        key: neuer Schluessel.

        Rueckgabe:
        None.

        Logik:
        Der Setter schreibt den neuen Wert in self._key.
        """
        self._key = key

    @property
    def value(self):
        """
        Gibt den gespeicherten Wert zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._value.

        Logik:
        Der Wert ist unabhaengig vom Schluessel.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Setzt den gespeicherten Wert.

        Parameter:
        value: neuer Wert.

        Rueckgabe:
        None.

        Logik:
        Nur der Wert wird geaendert, nicht die Baumposition.
        """
        self._value = value

    @property
    def color(self):
        """
        Gibt die Farbe zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._color.

        Logik:
        In RBTree-Aufgaben ist die Farbe wichtig fuer die Regeln.
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Setzt die Farbe.

        Parameter:
        color: neue Farbe.

        Rueckgabe:
        None.

        Logik:
        Beim Fixen eines RBTrees werden Knoten oft umgefaerbt.
        """
        self._color = color

    @property
    def left(self):
        """
        Gibt das linke Kind zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._left.

        Logik:
        Links liegen kleinere Schluessel.
        """
        return self._left

    @left.setter
    def left(self, node):
        """
        Setzt das linke Kind.

        Parameter:
        node: neuer linker Kindknoten.

        Rueckgabe:
        None.

        Logik:
        Der Link vom Elternknoten zum Kind wird gespeichert.
        """
        self._left = node

    @property
    def right(self):
        """
        Gibt das rechte Kind zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._right.

        Logik:
        Rechts liegen groessere oder gleiche Schluessel.
        """
        return self._right

    @right.setter
    def right(self, node):
        """
        Setzt das rechte Kind.

        Parameter:
        node: neuer rechter Kindknoten.

        Rueckgabe:
        None.

        Logik:
        Der Link vom Elternknoten zum rechten Kind wird gespeichert.
        """
        self._right = node

    @property
    def parent(self):
        """
        Gibt den Elternknoten zurueck.

        Parameter:
        Nur self.

        Rueckgabe:
        self._parent.

        Logik:
        Parent-Links sind bei RBTree-Rotationen wichtig.
        """
        return self._parent

    @parent.setter
    def parent(self, node):
        """
        Setzt den Elternknoten.

        Parameter:
        node: neuer Elternknoten.

        Rueckgabe:
        None.

        Logik:
        Nach Insert, Delete oder Rotation muss parent oft angepasst werden.
        """
        self._parent = node


def connect_left(parent, child):
    """
    Verbindet parent und child als linkes Kind.

    Parameter:
    parent: Elternknoten.
    child: neuer linker Kindknoten.

    Rueckgabe:
    None.

    Logik:
    Es werden beide Richtungen gesetzt: parent.left und child.parent.
    """
    parent.left = child
    child.parent = parent


if __name__ == "__main__":
    root = ExamNode(20, "twenty")
    left = ExamNode(10, "ten", "RED")
    connect_left(root, left)
    root.value = "changed"
    print(root.key, root.value, root.color)
    print(root.left.key, root.left.parent.key)
