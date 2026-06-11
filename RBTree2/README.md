# RB Tree Delete

**lesen sie diese Datei bis zum Ende!**

## Kontext
Nach dem Einfügen in einen Red Black Tree ist das Löschen von Elementen zu implementieren. Hierzu
wurde bereits die `delete`-Methode umgesetzt. Leider ist der Baum anschließend nicht mehr Konform
zu den RB Eigenschaften. Ihre Aufgabe ist es dies sicherzustellen.

## Aufgabe:
Datei `RBTree.py`
* Die `_fix_delete`-Methode arbeitet sich iterativ durch den RB Baum. Dabei beginnt sie bei dem 
  Knoten welcher als Ersatz für den gelöschten eingesetzt wurde.
  Setzen sie die vier Fix-Fälle entsprechend der Vorlesungsfolien um. Beachten sie das die beiden
  Blöcke jeweils gespiegelt umzusetzen sind. 

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
* Arbeiten sie zunächst mit einer einfachen Sequenz von Knoten (z.B. 10, 20, 30)! 
* Zeichnen sie sich auf !PAPIER! die möglichen Fälle auf und setzen sie diese erst DANN um!
* Die Methode `check_red_black_properties` überprüft ihren aktuellen Baum entsprechend der Regeln.
  Nutzen sie diese immer wieder, um Feedback zu bekommen was noch falsch ist.
* Bitte beachten sie das der RB Simulator eine leicht andere Umsetzung des löschalgorithmus 
  umsetzt. Ihr Ziel ist das der Knoten aus dem Baum entfernt ist und die RB Eigenschaften noch
  gültig sind!
* Bitte beachten sie das es hinsichtlich des Löschens verschiedene Verfahren gibt. Sollten sie
  auf Quellen aus dem Internet oder auch über KI zurückgreifen ist, ist zu erwarten das sie andere
  Lösungen angezeigt bekommen. Diese erfordern z.T. mehr Umbauarbeiten als für diese Aufgabe 
  vorgesehen sind. I.d.R. führen sie aber auch zum Ziel.

## Hinweise zur Moodle Einreichung:
Bitte laden sie nur **einen** Versuch in Moodle hoch und **schließen** den am Ende ab. Sie können mehrere Uploads machen innerhalb eines Versuchs durchführen.

Zum Erstellen des Upload-Zips öffnen sie eine Konsole (Drei Striche oben links drücken -> Terminal -> New Terminal). Dort geben sie "./zipUpload.sh" ein.
Anschließend können sie die Upload-Datei im File-Explorer über die rechte Maustaste herunterladen und in Moodle wieder hochladen.

## Links

* Moodle <https://moodle.ostfalia.de/>
* Python 3 <https://docs.python.org/3/>
* Red Black Simulator https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
