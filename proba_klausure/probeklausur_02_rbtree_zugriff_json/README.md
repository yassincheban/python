# II3 Probeklausur 02 - RBTree Zugriff und JSON

**Lesen Sie diese Aufgabenstellung bis zum Ende!**

## Kontext

In diesem Semester haben Sie sich in Vorlesung und Aufgaben mit Red-Black Trees beschaeftigt. Die alte Klausur nutzte AVL-Baeume, weil der alte Stoff AVL-lastig war. Fuer diese Probeklausur ist der Kontext deshalb ein `RBTree`.

Es geht in dieser Aufgabe nicht darum, einen vollstaendigen Red-Black Tree neu zu balancieren. Die Einfuege-Hilfsmethode ist vorbereitet. Sie sollen vor allem typische Python-Methoden auf einer vorhandenen Baumstruktur ergaenzen: Zugriff, Suche, Zaehlen und Speichern.

Die Bearbeitungszeit ist ungefaehr 60 Minuten.

## Aufgabe

Datei: `RBTreeExam.py`

- Ergaenzen Sie als kleine Einstiegsaufgabe den Getter und Setter fuer `value` in der Klasse `RBNode`.

- Bestimmen Sie den kleinsten `key` im Baum. Setzen Sie dies in der Methode `min_key()` um. Wenn der Baum leer ist, werfen Sie einen `KeyError`.

- Bestimmen Sie den groessten `key` im Baum. Setzen Sie dies in der Methode `max_key()` um. Wenn der Baum leer ist, werfen Sie einen `KeyError`.

- Suchen Sie einen bestimmten `key` und geben Sie den gespeicherten `value` zurueck. Wenn der `key` nicht existiert, werfen Sie einen `KeyError`. Setzen Sie dies in der Methode `find()` um.

- Bestimmen Sie alle `key`-Werte im geschlossenen Intervall `[low, high]`. Geben Sie die Werte als sortierte Liste zurueck. Setzen Sie dies in der Methode `between()` um.

- Zaehlen Sie alle echten Knoten mit einer bestimmten Farbe. NIL-Knoten sollen nicht mitgezaehlt werden. Setzen Sie dies in der Methode `count_color()` um.

- Speichern Sie den Baum als flaches Dictionary. Die JSON-Datei soll spaeter so aussehen:

```json
{
    "40": "root",
    "20": "left"
}
```

Setzen Sie dies in der Methode `to_dict()` und danach in der Methode `dump()` um. Speichern Sie keine NIL-Knoten.

- Laden Sie einen Baum aus einem solchen Dictionary wieder in den aktuellen Baum. Die Keys des Dictionary sind Texte und muessen mit `int(key)` wieder in Zahlen umgewandelt werden. Setzen Sie dies in der Methode `load_from_dict()` um.

## Hinweise zur Klausur

- Wechseln Sie in das richtige Projektverzeichnis.  
  Drei Striche oben links druecken -> File -> Open Folder und dann das Projektverzeichnis auswaehlen.

- Arbeiten Sie sich schrittweise vor.

- Sie muessen nichts vollstaendig neu schreiben. Wenn Sie auf die Idee kommen, sehr viel neuen Code zu schreiben: Denken Sie erst nach.

- Code, der nicht durch den Python-Interpreter ausgefuehrt werden kann, kann nicht bewertet werden. Testen Sie diesen.

- Die Tests nutzen wahrscheinlich andere Baeume als die Beispieldaten. Ihre Methoden muessen allgemein funktionieren.

## Hinweise zur Aufgabe

- Beginnen Sie mit dem Getter und Setter fuer `value`.

- Bei `min_key()` gehen Sie immer nach links, bis links ein NIL-Knoten steht.

- Bei `max_key()` gehen Sie immer nach rechts, bis rechts ein NIL-Knoten steht.

- Bei `find()` ist eine `while`-Schleife passend.

- Bei `between()` und `count_color()` ist Rekursion passend.

- Bei `dump()` duerfen Sie `json.dump()` verwenden.

- Bei `load_from_dict()` duerfen Sie die vorhandene Methode `insert_without_fix()` benutzen. Sie muessen keine Rotationen oder RBTree-Fix-Faelle schreiben.

- Ein NIL-Knoten ist schwarz und hat keinen `key` und keinen `value`.

## Hinweise zur Einreichung und zum Testen

Der Upload-Test in Moodle waere nur ein kleiner Smoke-Test. Er prueft vor allem, ob die Datei kompiliert.

Zum schnellen Testen koennen Sie aus diesem Ordner ausfuehren:

```bash
python3 RBTreeExam.py
```

Zum Kompilieren ohne Ausfuehren:

```bash
python3 -m py_compile RBTreeExam.py
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
min_key()
max_key()
find()
between()
count_color()
to_dict()
dump()
load_from_dict()
```
