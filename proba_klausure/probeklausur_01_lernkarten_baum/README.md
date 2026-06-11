# II3 Probeklausur 01 - Lernkarten-Baum

**Lesen Sie diese Aufgabenstellung bis zum Ende!**

## Kontext

In den Uebungen haben Sie einfache Baeume mit Dictionaries, Klassen und spaeter auch Red-Black Trees benutzt. In dieser Probeklausur geht es nicht um komplizierte Rotationen. Sie sollen eine kleine Baumklasse fuer Lernkarten erweitern und dabei vor allem Python sicher anwenden.

Ein Knoten speichert einen `key`, ein `topic`, eine Punktzahl `points`, eine Farbe und Links zu anderen Knoten. Die Farbe ist nur RBTree-Kontext. Sie muessen keine Red-Black-Reparatur implementieren.

Die Bearbeitungszeit ist ungefaehr 60 Minuten.

## Aufgabe

Datei: `LearningCardTree.py`

- Ergaenzen Sie in der Klasse `LearningCardNode` die fehlenden Getter und Setter. Setzen Sie dies fuer `topic`, `points`, `left`, `right` und `parent` um.

- Fuegen Sie neue Knoten nach Suchbaum-Regeln ein. Setzen Sie dies in der Methode `_insert_rec()` um. Kleinere `key`-Werte gehen nach links, groessere oder gleiche Werte nach rechts. Achten Sie darauf, den `parent`-Link zu setzen.

- Suchen Sie ein Thema ueber einen bestimmten `key`. Geben Sie den gespeicherten `topic` zurueck. Wenn der `key` nicht existiert, werfen Sie einen `KeyError`. Setzen Sie dies in der Methode `find_topic()` um.

- Bestimmen Sie alle `key`-Werte im geschlossenen Intervall `[low, high]`. Geben Sie diese als sortierte Liste zurueck. Setzen Sie dies in der Methode `keys_between()` um.

- Zaehlen Sie die Punkte aller Lernkarten im Intervall `[low, high]`. Geben Sie die Summe als `int` zurueck. Setzen Sie dies in der Methode `sum_points_between()` um.

- Durchlaufen Sie den Baum in Level-order Reihenfolge. Rufen Sie fuer jeden Knoten den uebergebenen Callback auf und uebergeben Sie `key`, `topic` und `points`. Setzen Sie dies in der Methode `visit_level_order()` um.

- Speichern Sie die Themen des Baums als flaches JSON-Dictionary. Das Format soll so aussehen:

```json
{
    "40": "Rekursion",
    "20": "Listen"
}
```

Setzen Sie dies in der Methode `dump_topics()` um. Es sollen nur echte Knoten gespeichert werden.

## Hinweise zur Klausur

- Wechseln Sie in das richtige Projektverzeichnis.
  Drei Striche oben links druecken -> File -> Open Folder und dann das Projektverzeichnis auswaehlen.

- Arbeiten Sie sich schrittweise vor.

- Sie muessen nichts vollstaendig neu schreiben. Wenn Sie auf die Idee kommen, sehr viel neuen Code zu schreiben: Denken Sie erst nach.

- Code, der nicht durch den Python-Interpreter ausgefuehrt werden kann, kann nicht bewertet werden. Testen Sie Ihren Code regelmaessig.

- Die Tests koennen andere Daten verwenden als die Beispieldaten in der Datei. Ihre Methoden muessen allgemein funktionieren.

## Hinweise zur Aufgabe

- Beginnen Sie mit der Klasse `LearningCardNode`.

- Danach testen Sie das Einfuegen mit wenigen Werten, zum Beispiel `40`, `20`, `60`.

- Fuer `keys_between()` ist Rekursion passend. Sie duerfen unnoetige Teilbaeume ueberspringen.

- Fuer `visit_level_order()` koennen Sie eine normale Liste als Queue benutzen.

- Fuer `dump_topics()` duerfen Sie `json.dump()` verwenden. JSON speichert Dictionary-Keys als Strings.

- NIL-Knoten kommen hier nicht als eigene Knoten vor. Die Farbe ist nur als einfacher Bezug zu den RBTree-Uebungen vorhanden.

## Hinweise zur Einreichung und zum Testen

Der Upload-Test in Moodle waere nur ein kleiner Smoke-Test. Er prueft vor allem, ob die Datei kompiliert. Ein einzelner fehlgeschlagener Smoke-Test bedeutet nicht automatisch, dass alle Punkte verloren sind.

Zum schnellen Testen koennen Sie aus diesem Ordner ausfuehren:

```bash
python3 LearningCardTree.py
```

Zum Kompilieren ohne Ausfuehren:

```bash
python3 -m py_compile LearningCardTree.py
```

## Erlaubte Hilfsmittel

- Das Python-Buch und eigene Notizen
- Vorlesungsfolien und Uebungsdateien im Workspace
- Weisse Blaetter fuer Notizen
- Das statische Internet

## Verbotene Hilfsmittel

- AI-basierte Tools, zum Beispiel ChatGPT oder GitHub Copilot
- Online-Kommunikationsanwendungen
- Mobilgeraete

## Wichtigste Methoden

```text
_insert_rec()
find_topic()
keys_between()
sum_points_between()
visit_level_order()
dump_topics()
```
