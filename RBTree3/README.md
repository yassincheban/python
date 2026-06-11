# RB Tree Save & Load

**lesen sie diese Datei bis zum Ende!**

## Kontext
Ihr RBTree ist inzwischen schon sehr mächtig geworden. In dieser letzten Übung soll das Speichern und Laden eines `RBTree`-Objekts 
umgesetzt werden.

## Aufgabe:
Datei `RBTree.py`
* Setzen sie zunächst die Methode `save_to_file` um. Das Ergebnis soll der Datei `example.json` entsprechen. Speichern sie
  den Inhalt in dem Dateinamen welchen sie als Parameter übergeben bekommen haben.
* Setzen sie nun die Methode `load_from_file` um. Laden sie den Inhalt der Datei welche sie als Parameter übergeben bekommen.
  Der Visualisierte Baum sollte anschließend genauso aussehen wie vorher.

## Hinweise zur Klausur:
* **Wechseln sie in das richtige Projekt Verzeichnis** (Drei Striche oben links drücken -> File -> Open Folder
  und dann das Projektverzeichnis auswählen)
* **Arbeiten sie sich schrittweise vor!**
* Sie müssen nichts vollständig neu schreiben. Wenn sie also auf die Idee kommen sollten viel neuen Code zu schreiben: 
  **Denken sie erst nach!**

## Hinweise zur Aufgabe:
* Wenn ihr Bildschirm groß genug ist, starten sie die Terminals im Split Modus
* Wenn sich ihre Software komisch verhält, überprüfen sie ob diese nicht noch 
  irgendwo anders läuft. Schließen sie ggf. alle Terminals!
* Beginnen sie mit der Umsetzung der `save_to_file`-Methode!
* Ihr Programm speichert zwei Bilder `tree_saved.png` (Inhalt vor dem Speichern) und `tree_loaded.png` (Inhalt
  nach dem Laden). Beide sollten vom Inhalt her gleich aussehen!

## Hinweise zur Moodle Einreichung:
Bitte laden sie nur **einen** Versuch in Moodle hoch und **schließen** den am Ende ab. Sie können mehrere Uploads machen innerhalb eines Versuchs durchführen.

Zum Erstellen des Upload-Zips öffnen sie eine Konsole (Drei Striche oben links drücken -> Terminal -> New Terminal). Dort geben sie "./zipUpload.sh" ein.
Anschließend können sie die Upload-Datei im File-Explorer über die rechte Maustaste herunterladen und in Moodle wieder hochladen.

## Links

* Moodle <https://moodle.ostfalia.de/>
* Python 3 <https://docs.python.org/3/>
* Red Black Simulator https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
