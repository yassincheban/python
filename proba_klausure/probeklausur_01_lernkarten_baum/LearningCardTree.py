#!/usr/bin/python3

import json


class LearningCardNode:
    """
    Ein Knoten fuer eine Lernkarten-Baumstruktur.

    key sortiert die Knoten.
    topic ist das Thema der Lernkarte.
    points ist eine kleine Punktzahl fuer die Schwierigkeit.
    color ist nur Kontext aus den RBTree-Uebungen.
    """

    RED = "RED"
    BLACK = "BLACK"

    def __init__(self, key: int, topic: str, points: int, color: str = BLACK):
        self._key = key
        self._topic = topic
        self._points = points
        self._color = color
        self._left = None
        self._right = None
        self._parent = None

    @property
    def key(self) -> int:
        return self._key

    @key.setter
    def key(self, key: int) -> None:
        self._key = key

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        self._color = color

    @property
    def topic(self) -> str:
        # TODO: Geben Sie self._topic zurueck.
        pass

    @topic.setter
    def topic(self, topic: str) -> None:
        # TODO: Speichern Sie topic in self._topic.
        pass

    @property
    def points(self) -> int:
        # TODO: Geben Sie self._points zurueck.
        pass

    @points.setter
    def points(self, points: int) -> None:
        # TODO: Speichern Sie points in self._points.
        pass

    @property
    def left(self):
        # TODO: Geben Sie self._left zurueck.
        pass

    @left.setter
    def left(self, node) -> None:
        # TODO: Speichern Sie node in self._left.
        pass

    @property
    def right(self):
        # TODO: Geben Sie self._right zurueck.
        pass

    @right.setter
    def right(self, node) -> None:
        # TODO: Speichern Sie node in self._right.
        pass

    @property
    def parent(self):
        # TODO: Geben Sie self._parent zurueck.
        pass

    @parent.setter
    def parent(self, node) -> None:
        # TODO: Speichern Sie node in self._parent.
        pass

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


class LearningCardTree:
    """
    Ein einfacher Suchbaum fuer Lernkarten.

    Der Baum ist kein vollstaendiger RBTree. Die Farbe bleibt nur als
    Zusatzinformation an den Knoten erhalten.
    """

    def __init__(self):
        self._root = None

    def _insert_rec(
        self,
        node: LearningCardNode,
        key: int,
        topic: str,
        points: int,
        parent: LearningCardNode = None,
    ) -> LearningCardNode:
        """
        Fuegt rekursiv einen neuen Knoten ein.

        TODO:
        - Wenn node None ist, erstellen Sie einen neuen LearningCardNode.
        - Setzen Sie bei diesem neuen Knoten den parent.
        - Gehen Sie bei kleinerem key nach links.
        - Gehen Sie sonst nach rechts.
        - Geben Sie am Ende node zurueck.
        """
        pass

    def insert(self, key: int, topic: str, points: int) -> None:
        self._root = self._insert_rec(self._root, key, topic, points)
        if self._root is not None:
            self._root.color = LearningCardNode.BLACK

    def find_topic(self, key: int) -> str:
        """
        Sucht den topic-Wert zu einem key.

        TODO:
        - Laufen Sie mit einer while-Schleife ab self._root durch den Baum.
        - Vergleichen Sie key mit dem key des aktuellen Knotens.
        - Geben Sie topic zurueck, wenn der Knoten gefunden wurde.
        - Werfen Sie KeyError, wenn der key fehlt.
        """
        pass

    def _keys_between_rec(self, node, low: int, high: int, result: list) -> None:
        """
        Hilfsfunktion fuer keys_between().

        TODO:
        - Brechen Sie bei None ab.
        - Besuchen Sie links nur, wenn dort noch passende keys liegen koennen.
        - Fuegen Sie node.key hinzu, wenn er im Intervall liegt.
        - Besuchen Sie rechts nur, wenn dort noch passende keys liegen koennen.
        """
        pass

    def keys_between(self, low: int, high: int) -> list:
        result = []
        if low > high:
            return result
        self._keys_between_rec(self._root, low, high, result)
        return result

    def _sum_points_between_rec(self, node, low: int, high: int) -> int:
        """
        Hilfsfunktion fuer sum_points_between().

        TODO:
        - Geben Sie bei None den Wert 0 zurueck.
        - Zaehlen Sie nur Punkte von Knoten im Intervall.
        - Nutzen Sie Rekursion fuer linke und rechte Teilbaeume.
        """
        pass

    def sum_points_between(self, low: int, high: int) -> int:
        if low > high:
            return 0
        return self._sum_points_between_rec(self._root, low, high)

    def visit_level_order(self, callback) -> None:
        """
        Besucht alle Knoten Ebene fuer Ebene.

        callback hat die Form callback(key, topic, points).

        TODO:
        - Nutzen Sie eine Liste als Queue.
        - Starten Sie mit self._root, wenn der Baum nicht leer ist.
        - Rufen Sie callback fuer jeden echten Knoten auf.
        - Haengen Sie vorhandene Kinder hinten an die Queue an.
        """
        pass

    def _collect_topics_rec(self, node, result: dict) -> None:
        """
        Hilfsfunktion fuer dump_topics().

        TODO:
        - Brechen Sie bei None ab.
        - Speichern Sie result[str(node.key)] = node.topic.
        - Besuchen Sie danach den linken und rechten Teilbaum.
        """
        pass

    def dump_topics(self, filename: str) -> None:
        data = {}
        self._collect_topics_rec(self._root, data)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


EXAMPLE_CARDS = [
    (40, "Rekursion", 5),
    (20, "Listen", 3),
    (60, "Dictionaries", 4),
    (10, "if und Schleifen", 2),
    (30, "Klassen", 4),
    (50, "JSON", 3),
    (70, "Callbacks", 5),
]


def build_example_tree() -> LearningCardTree:
    tree = LearningCardTree()
    for key, topic, points in EXAMPLE_CARDS:
        tree.insert(key, topic, points)
    return tree


def main() -> None:
    print("Probeklausur 01: LearningCardTree")
    print("Beispieldaten:", EXAMPLE_CARDS)
    print("Fuellen Sie die TODO-Stellen, bevor Sie die Methoden testen.")


if __name__ == "__main__":
    main()
