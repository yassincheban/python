# RB Tree Insert

**lesen sie diese Datei bis zum Ende!**

## Kontext
Wie besprochen können Binary Trees entarten und letztlich nicht besser funktionieren als eine einfache Liste. 
Der Red Black Tree ist ein ausbalancierter Baum welcher bestimmte Eigenschaften einhält und damit ein besseres
Laufzeitverhalten aufweist. Hierzu wird jedoch das Einfügen von Knoten sehr viel komplizierter, da diese 
Eigenschaften durch Rotationen eingehalten werden müssen.

## Aufgabe:
Datei `RBTree.py`
* Die `_insert_rec`-Methode sucht recursiv in dem Baum die richtige Position für eine neue Node
  und legt diese als Rote Node dort an. Anschließend wird auf dieser neuen Node `_fix_rb_tree` 
  aufgerufen.
  Implementieren sie die Logik der Methode `_insert_rec` entsprechened den Regeln für Red Black Trees
* Die Methode `_fix_rb_tree` stellt nach dem Einfügen die Baum eigenschaften durch neufärben und 
  Rotieren wieder her. Auch diese Methode wird ggf. rekursiv aufgerufen. 
  Implementieren sie die Logik der Methode `_fix_rb_tree` entsprechened der Folien


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
* Beginnen sie mit der Umsetzung der `_insert_rec`-Methode!
* Fügen sie zunächst eine einfache Sequenz von Knoten (z.B. 10, 20, 30) ein und
  permutieren sie diese. 
* Zeichnen sie sich auf !PAPIER! die möglichen Fälle auf und setzen sie diese erst DANN um!
* Die Methode `check_red_black_properties` überprüft ihren aktuellen Baum entsprechend der Regeln.
  Nutzen sie diese immer wieder, um Feedback zu bekommen was noch falsch ist.
  
## Hinweise zur Moodle Einreichung:
Bitte laden sie nur **einen** Versuch in Moodle hoch und **schließen** den am Ende ab. Sie können mehrere Uploads machen innerhalb eines Versuchs durchführen.

Zum Erstellen des Upload-Zips öffnen sie eine Konsole (Drei Striche oben links drücken -> Terminal -> New Terminal). Dort geben sie "./zipUpload.sh" ein.
Anschließend können sie die Upload-Datei im File-Explorer über die rechte Maustaste herunterladen und in Moodle wieder hochladen.

## Links

* Moodle <https://moodle.ostfalia.de/>
* Python 3 <https://docs.python.org/3/>
* Red Black Simulator https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
