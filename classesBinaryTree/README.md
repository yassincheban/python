# Binary Tree mit Klassen

**lesen sie diese Datei bis zum Ende!**

## Kontext
Die Datenstruktur der ersten Übung ist als eher unkomfortabel einzustufen. Dies soll nun durch eine komfortable Klassen 
Schnittstelle ersetzt werden. Diese besteht aus den Klassen `BinaryTree` und `BinaryTreeNode`. Erstere bildet den 
gesamten Baum ab während die zweite einen einzelnen Knoten abbildet.

## Aufgabe:
Datei `binaryTree.py`
* Ein Objekt der Klasse `BinaryTreeNode` enthält einen Schlüssel `key` nach dem sortiert wird und einen Wert `value`
  der ein unabhängiges Datum darstellt. Drüberhinaus natürlich potentielle Kindknoten. Der Fehlen eines solchen wird 
  durch den Wert `None` dargestellt. Erstellen sie nun Properties und Setter für all diese Attribute.
* Die Klasse `BinaryTree` stellt das Interface für die Baumstruktur dar. Damit der Baum gefüllt werden kann ist ein
  rekursiver Einfügealgorithmus notwendig. Diesen sollen sie in der Funktion `_insert_rec` umsetzen.
* Damit ihre Baumstruktur visualisierbar wird wird das Visitor-Pattern angewand. Diese läuft in diesem Fall alle
  Knoten der Baumstruktur ab und soll eine Callback Funktion aufrufen. Dabei erfolgt die Abarbeitung nach dem Preorder
  Verfahren. Der Wert für die Position `pos` berechnet sich für den linken Pfad zu `2 * pos - 1`, für den rechten Pfad 
  zu `2 * pos + 1` und den aktuellen Knoten zu `pos`.

## Hinweise:
* **Wechseln sie in das richtige Projekt Verzeichnis** (Drei Striche oben links drücken -> File -> Open Folder
  und dann das Projektverzeichnis auswählen)
* **Arbeiten sie sich schrittweise vor!**
* Sie müssen nichts vollständig neu schreiben. Wenn sie also auf die Idee kommen sollten viel neuen Code zu schreiben: 
  **Denken sie erst nach!**

## Hinweise zur Aufgabe:
* Wenn ihr Bildschirm groß genug ist, starten sie die Terminals im Split Modus
* Wenn sich ihre Software komisch verhält, überprüfen sie ob diese nicht noch 
  irgendwo anders läuft. Schließen sie ggf. alle Terminals!
* Starten sie mit der Klasse `BinaryTreeNode`!
* Das Programm erzeugt einerseits eine Ausgabe des Baums auf der Konsole als auch
  eine graphische Darstellung in `tree.png`.


## Hinweise zur Moodle Einreichung:
Bitte laden sie nur **einen** Versuch in Moodle hoch und **schließen** den am Ende ab. Sie können mehrere Uploads machen innerhalb eines Versuchs durchführen.

Zum Erstellen des Upload-Zips öffnen sie eine Konsole (Drei Striche oben links drücken -> Terminal -> New Terminal). Dort geben sie "./zipUpload.sh" ein.
Anschließend können sie die Upload-Datei im File-Explorer über die rechte Maustaste herunterladen und in Moodle wieder hochladen.


## Links

* Moodle <https://moodle.ostfalia.de/>
* Python 3 <https://docs.python.org/3/>
* Simulator <https://www.cs.usfca.edu/~galles/visualization/BST.html>