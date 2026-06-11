# Python-Klausurvorbereitung mit RBTree-Kontext

Dieses Repository enthaelt kleine Python-Aufgaben und Beispiele zur Klausurvorbereitung. Das Hauptziel ist Python zu ueben. Red-Black Trees (`RBTree`) dienen dabei nur als gemeinsamer Kontext fuer die Aufgaben.

Der Fokus liegt auf:

- Python-Grundlagen: Dictionaries, Schleifen, Bedingungen, Listen, Strings, Dateien und JSON
- rekursiven Funktionen
- OOP: Klassen, `__init__`, Attribute, Properties und Methoden
- nur der RBTree-Logik, die fuer Insert, Delete, Traversal, Validation und einfache Zugriffsmethoden noetig ist

Das ist keine tiefe mathematische oder theoretische Untersuchung von Baeumen und Knoten. Die Baumaufgaben sind vor allem ein Rahmen, um sauberen Python-Code im Stil der Uebungen zu schreiben.

## Workspace

- `simpleBinaryTree/`: verschachtelte Dictionary-Baeume und einfache Traversals.
- `classesBinaryTree/`: Klassen fuer Baumknoten, Insert-Logik und Visitor-Callbacks.
- `RBTree1/`: RBTree-Insert, Umfaerben und Rotationen.
- `RBTree2/`: RBTree-Delete, Transplant, Successor und Delete-Fix-Faelle.
- `RBTree3/`: RBTree speichern/laden mit flachem JSON.
- `alte_klausure/`: alte Klausurmaterialien, nur als Hinweis auf moegliche Python-Aufgabentypen.

## Exam-Prep-Dateien

- `notiz.md` ist die schnelle Navigation. Dort steht kurz, welche `catch_ohl/*.py`-Datei welche Methoden enthaelt.
- `catch_ohl/` enthaelt die ausfuehrlichen, direkt ausfuehrbaren Beispiele. Jede Datei behandelt ein Thema und bleibt nah am Stil der originalen Uebungen.

## Testen

Ein einzelnes Beispiel ausfuehren:

```bash
python3 catch_ohl/rb_access_methods.py
```

Alle Beispiele kompilieren:

```bash
python3 -m py_compile catch_ohl/*.py
```
