"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Der Entwickler hat Falsch gerechnet anstadt 80 würde bei den Error 20000 raus kommen.

# Defect (fehlerhafte Stelle im Code):
# TODO: mit (prozent / 100) kann man das richtig kriegen egal mit welchen rabatt.

# Failure (was der Benutzer bemerken würde):
# TODO: Der User würde mitbekommen das er viel mehr bezahlen müsste.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent / 100)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))
    print(berechne_rabatt_korrigiert(100.0, 30))
    print(berechne_rabatt_korrigiert(500.0, 10))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | TODO     | TODO      |
# | Programm mit Testdaten ausführen    | TODO     | TODO      |
# | Syntaxprüfung durch den Editor      | TODO     | TODO      |
# | Walkthroughs im Team                | TODO     | TODO      |
# | Unit-Tests laufen lassen            | TODO     | TODO      |
# | Checklisten für Codestruktur        | TODO     | TODO      |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Wenn man nur sich den Code anschaut kann man Sachen vergessen, übersehen. Man muss den code auf richtig laufen lassen damit man sehen kann was man nicht bedacht hat.



# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag: Windows..
# TODO: Ein Programm vollständig zu testen ist beihnahe unmöglich wegen der Dauer um "Alles" zu testen.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag: Wenn ein Prozess auf Fehler laüft laufen mehrer auf Fehler bis man den Fehler behebt.
# TODO: ja häufigen sich halt.

# Welches Prinzip überrascht dich? Warum?
# TODO: garkeins sind doch alle logisch.
