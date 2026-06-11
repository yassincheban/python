# II3 Klausur WS 2025

**Lesen Sie diese Aufgabenstellung bis zum Ende!**

## Kontext

In den Übungen haben Sie sich mit AVL-Bäumen beschäftigt. In dieser Klausur sollen Sie den Nutzenden der AVL-Baumklasse mehr Zugriffsmöglichkeiten auf die Daten ermöglichen.

## Aufgabe

Datei: `AVLTree.py`

- Bestimmen Sie den maximalen Key im AVL-Baum. Setzen Sie dies in der Methode `max()` um.

- Bestimmen Sie den minimalen Key im AVL-Baum. Setzen Sie dies in der Methode `min()` um.

- Suchen Sie einen bestimmten Key im AVL-Baum und geben Sie den Value des Knotens zurück. Sollten Sie keinen Knoten mit dem Key finden, werfen Sie einen `KeyError`. Setzen Sie dies in der Methode `find()` um.

- Bestimmen Sie alle Keys zwischen dem geschlossenen Intervall `[low, high]` und geben Sie diese als Liste zurück. Setzen Sie dies in der Methode `between()` um.

- Durchlaufen Sie alle Knoten des AVL-Baums in Post-order Reihenfolge. Dabei rufen Sie einen übergebenen Callback für jeden Knoten auf und übergeben diesem den Key. Setzen Sie dies in der Methode `visit_post_order()` um.

- Durchlaufen Sie alle Knoten des AVL-Baums in Level-order Reihenfolge. Dabei rufen Sie einen übergebenen Callback für jeden Knoten auf und übergeben diesem den Key. Setzen Sie dies in der Methode `visit_level_order()` um.

## Hinweise zur Klausur

- Wechseln Sie in das richtige Projektverzeichnis.  
  Drei Striche oben links drücken -> File -> Open Folder und dann das Projektverzeichnis auswählen.

- Arbeiten Sie sich schrittweise vor!

- Sie müssen nichts vollständig neu schreiben. Wenn Sie also auf die Idee kommen sollten, viel neuen Code zu schreiben: Denken Sie erst nach!

- Code, der nicht interpretierbar ist, also durch den Python-Interpreter ausführbar ist, führt zu einer Bewertung mit 5.0. Testen Sie diesen!

- Code, der anderen Code an der Ausführung hindert, zum Beispiel durch Abstürze oder falsche Bedingungen, führt zum Verlust von Punkten, da diese Codeabschnitte nicht getestet werden können.

## Hinweise zur Aufgabe

- Wenn Ihr Bildschirm groß genug ist, starten Sie die Terminals im Split-Modus.

- Wenn sich Ihre Software komisch verhält, überprüfen Sie, ob diese nicht noch irgendwo anders läuft. Schließen Sie gegebenenfalls alle Terminals!

- Die Datei `example.png` enthält Ihren aktuellen Baum. Die Tests werden aber mit anderen Bäumen durchgeführt. Ihre Umsetzung muss auch mit diesen funktionieren.

## Hinweise zur Moodle-Einreichung

Der Test beim Hochladen nach der Klausur ist ein kleiner Test, also ein Smoke-Test. Er enthält nur wenige Tests, welche überprüfen sollen, ob Ihr Upload erfolgreich war und Ihre Einreichung kompiliert.

Achtung: Sollten nicht alle Smoke-Testfälle erfolgreich sein, ist das kein Grund, das Ergebnis nicht einzureichen! Der große Moodle-Test für die Bestimmung Ihrer Punkte enthält mehr Tests, von denen etliche erfolgreich sein können und Ihnen damit Punkte bringen, obwohl ein einzelner Test des Smoke-Tests nicht erfolgreich ist.

Bitte laden Sie nur einen Versuch in Moodle hoch und schließen Sie diesen am Ende ab. Sie können mehrere Uploads innerhalb eines Versuchs durchführen. Gewertet wird der letzte Upload.

Zum Erstellen des Upload-Zips öffnen Sie eine Konsole:  
Drei Striche oben links drücken -> Terminal -> New Terminal.

Dort geben Sie ein:

```bash
./zipUpload.sh
```

Anschließend können Sie die Upload-Datei im File-Explorer über die rechte Maustaste herunterladen und in Moodle wieder hochladen.

## Erlaubte Hilfsmittel

- Das Buch nach Bedarf, zum Beispiel das Python-Buch im Workspace
- Die Vorlesungsfolien als PDF im Workspace
- Eigene Notizen
- Weiße Blätter für Notizen während der Klausur, werden nicht bewertet
- Das statische Internet

## Verbotene Hilfsmittel

- AI-basierte Tools, zum Beispiel ChatGPT oder GitHub Copilot
- Online-Kommunikationsanwendungen, zum Beispiel WhatsAppWeb oder Signal
- Mobilgeräte

## Links

- Anmeldung am Terminal mit den Klausuraccounts
- Moodle: https://moodle.ostfalia.de/
- Python 3: https://docs.python.org/3/
- Online VSCode: https://ii-e.ostfalia.de/

## Wichtigste Methoden

```text
max()
min()
find()
between()
visit_post_order()
visit_level_order()
```
