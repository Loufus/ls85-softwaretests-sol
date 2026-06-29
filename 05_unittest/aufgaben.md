# Baustein 05 – Python unittest 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> **Voraussetzung:** Baustein 01–04 abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/YKEuBgsNm9" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 05: unittest</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich habe bereits Unit-Tests in Python geschrieben
- [ ] 🟡 Ich weiß was Unit-Tests sind, habe aber noch keinen geschrieben
- [ ] 🔴 Das ist Neuland für mich

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … das `unittest`-Modul importieren und eine Testklasse erstellen
- 🟡 … Testmethoden mit `self.assertEqual`, `self.assertRaises`, `self.assertTrue` schreiben
- 🟡 … `setUp()` und `tearDown()` für Testvorbereitung und -bereinigung nutzen
- 🟡 … Tests mit `python -m unittest` ausführen und das Ergebnis interpretieren
- 🔴 … Tests sinnvoll benennen, strukturieren und nach Äquivalenzklassen organisieren

---

## Hintergrund

Das Modul `unittest` ist Pythons eingebautes Test-Framework – keine Installation notwendig.
Es folgt dem xUnit-Muster, das aus Java (JUnit) stammt und in fast allen Sprachen existiert.

```bash
# Tests ausführen (im Verzeichnis des Projekts):
python -m unittest 05_unittest/code/starter.py -v

# Alle Tests im Projekt finden und ausführen:
python -m unittest discover -v
```

Das `-v` steht für "verbose" – du siehst dann den Namen jedes Tests.

---

## Aufgabe 0 – Grundbegriffe: Unit-Test lesen und verstehen 🟢

**Einstieg: Tests lesen lernen**

Lies den folgenden Unit-Test und beantworte die Fragen – ohne die Implementierung zu kennen:

```python
import unittest

class TestBestellsystem(unittest.TestCase):

    def test_rabatt_wird_korrekt_abgezogen(self):
        bestellung = Bestellsystem()
        bestellung.artikel_hinzufuegen("Stift", 2.00, 5)
        bestellung.rabatt_setzen(10)
        self.assertAlmostEqual(bestellung.gesamtpreis(), 9.00)

    def test_leere_bestellung_hat_preis_null(self):
        bestellung = Bestellsystem()
        self.assertEqual(bestellung.gesamtpreis(), 0.0)

    def test_negativer_rabatt_wirft_fehler(self):
        bestellung = Bestellsystem()
        with self.assertRaises(ValueError):
            bestellung.rabatt_setzen(-5)
```

**a)** Was testet jeder dieser Tests? Beschreibe in je einem Satz.

**b)** Welche Klasse und welche Methoden werden in den Tests verwendet?

**c)** Was bedeutet `assertAlmostEqual` und warum wird es hier statt `assertEqual` verwendet?

**d)** Was passiert, wenn `test_negativer_rabatt_wirft_fehler` fehlschlägt?
Was wäre dann das Problem in der Implementierung?

Trage deine Antworten in `05_antworten.md` ein.

---

## Aufgabe 1 – Erste Unit-Tests schreiben 🟡

In `code/starter.py` findest du die Klasse `Kontorechner` – ein vereinfachter Kontostand-Manager.

**a)** Analysiere die Klasse: Welche Methoden hat sie? Was soll jede Methode tun?

**b)** Schreibe in der vorbereiteten Testklasse `TestKontorechner` mindestens folgende Tests:

| Testmethode | Was wird geprüft |
|-------------|-----------------|
| `test_einzahlen_positiver_betrag` | Einzahlung erhöht den Kontostand korrekt |
| `test_einzahlen_null_wirft_fehler` | Einzahlung von 0 → `ValueError` |
| `test_einzahlen_negativ_wirft_fehler` | Negativer Betrag → `ValueError` |
| `test_abheben_guthaben_vorhanden` | Abhebung reduziert Kontostand korrekt |
| `test_abheben_kein_guthaben` | Abhebung ohne Guthaben → `ValueError` |
| `test_kontostand_anfangswert` | Neues Konto hat Kontostand 0 |

**c)** Führe die Tests aus und interpretiere die Ausgabe.
Was bedeuten `.`, `F` und `E` in der Ausgabe?

---

## Aufgabe 2 – setUp und tearDown 🟡

**Szenario:** Du testest eine Klasse `Einkaufsliste`, die Artikel hinzufügen, entfernen und anzeigen kann.

**a)** Implementiere `Einkaufsliste` in `starter.py` (mindestens: `hinzufuegen`, `entfernen`, `anzeigen`, `ist_leer`).

**b)** Schreibe eine Testklasse `TestEinkaufsliste`, die:
- In `setUp()` eine neue `Einkaufsliste` anlegt
- In `tearDown()` eine Meldung ausgibt (demonstriert die Reihenfolge)
- Mindestens 5 Testmethoden enthält

**c)** Warum ist `setUp()` sinnvoller als das Erstellen des Objekts in jeder einzelnen Testmethode?

---

## Aufgabe 3 – assertRaises richtig nutzen 🟡

Ein häufiger Fehler: `assertRaises` wird falsch verwendet.

```python
# Falsch – Exception wird sofort geworfen, nicht gefangen:
self.assertRaises(ValueError, meine_funktion(-1))

# Richtig – Variante 1 (Callable + Argumente):
self.assertRaises(ValueError, meine_funktion, -1)

# Richtig – Variante 2 (Context Manager):
with self.assertRaises(ValueError):
    meine_funktion(-1)
```

**a)** Zeige anhand deiner Tests aus Aufgabe 1, dass du beide Varianten korrekt anwenden kannst.

**b)** Schreibe einen Test für die Funktion `berechne_note()` aus Baustein 04, der prüft,
dass bei einer Punktzahl von -1 und 101 jeweils ein `ValueError` geworfen wird.

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Betrieb hat eine Funktion `berechne_mehrwertsteuer(netto: float, steuersatz: float) -> float` entwickelt.

**(a)** Nennen Sie vier sinnvolle Testfälle mit konkreten Eingabe- und Erwartungswerten. *(4 Punkte)*

**(b)** Schreiben Sie die vier Testfälle als Python-`unittest`-Methoden in eine Testklasse. *(8 Punkte)*

**(c)** Welcher Assertion-Typ ist bei Kommazahlen problematisch? Nennen Sie die Alternative und warum diese nötig ist. *(3 Punkte)*

---

## Tandem-Aufgabe 👥

**Gegenseitiges Testen:**

Person A: Implementiert eine Klasse `Dateilogger` mit den Methoden:
- `schreiben(nachricht: str)` → fügt Nachricht zur Log-Liste hinzu
- `auslesen()` → gibt alle Nachrichten als Liste zurück
- `loeschen()` → leert den Log
- `anzahl_eintraege()` → gibt Anzahl der Einträge zurück

Person B: Schreibt die Tests für diese Klasse, ohne die Implementierung zu kennen (nur die Schnittstellenbeschreibung).

Dann: Tests zusammenführen, ausführen – was schlägt fehl? Warum?

**Erkläre deinem Tandempartner:** Erkläre den Unterschied zwischen `setUp()`, dem eigentlichen Testcode und `tearDown()`. Warum ist die Trennung dieser drei Teile wichtig? Dein Tandempartner stellt mindestens eine Rückfrage.

---

## Active Recall 🧠

*Unterlagen zu:*

1. Wie heißt die Basisklasse, von der alle Testklassen erben müssen?
2. Mit welchem Befehl führst du alle Tests in einem Verzeichnis aus?
3. Was ist der Unterschied zwischen `assertEqual` und `assertAlmostEqual`?
4. Wann wird `setUp()` aufgerufen – einmal pro Testklasse oder einmal pro Testmethode?
5. Was bedeutet ein `E` (Error) in der unittest-Ausgabe im Unterschied zu `F` (Failure)?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann eigenständig Unit-Tests mit unittest schreiben
- [ ] 🟡 Ich verstehe das Konzept, habe aber noch Probleme mit assertRaises
- [ ] 🔴 Ich brauche mehr Erklärungen oder Beispiele

**Was nimmst du mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*

08:49Claude hat geantwortet: Aufgabe 0Aufgabe 0
a) Was testet jeder Test?
test_rabatt_wird_korrekt_abgezogen → Prüft, ob 10% Rabatt auf 5× 2,00 € = 10,00 € korrekt zu 9,00 € führt.

test_leere_bestellung_hat_preis_null → Prüft, ob ein neues Bestellsystem ohne Artikel den Gesamtpreis 0.0 zurückgibt.

test_negativer_rabatt_wirft_fehler → Prüft, ob ein negativer Rabatt einen ValueError auslöst.
b) Klasse und Methoden
Klasse: Bestellsystem

Methoden: artikel_hinzufuegen(name, preis, menge), rabatt_setzen(prozent), gesamtpreis()
c) assertAlmostEqual
assertAlmostEqual prüft auf 7 Nachkommastellen statt auf exakte Gleichheit. Bei Kommazahlen entstehen durch Floating-Point-Arithmetik minimale Rundungsfehler (z. B. 9.000000000001), die assertEqual scheitern lassen würden.
d) Fehlschlag von test_negativer_rabatt_wirft_fehler
Die Implementierung wirft keinen ValueError bei negativem Rabatt – sie akzeptiert ihn einfach oder verhält sich undefiniert. Der Test meldet dann einen Fehler (F).

Aufgabe 1
pythonimport unittest

class TestKontorechner(unittest.TestCase):

    def setUp(self):
        self.konto = Kontorechner()

    def test_kontostand_anfangswert(self):
        self.assertEqual(self.konto.kontostand, 0)

    def test_einzahlen_positiver_betrag(self):
        self.konto.einzahlen(100)
        self.assertEqual(self.konto.kontostand, 100)

    def test_einzahlen_null_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.konto.einzahlen(0)

    def test_einzahlen_negativ_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.konto.einzahlen(-50)

    def test_abheben_guthaben_vorhanden(self):
        self.konto.einzahlen(200)
        self.konto.abheben(80)
        self.assertEqual(self.konto.kontostand, 120)

    def test_abheben_kein_guthaben(self):
        with self.assertRaises(ValueError):
            self.konto.abheben(50)

if __name__ == '__main__':
    unittest.main()
c) Ausgabe-Bedeutung
. → Test bestanden

F → Test fehlgeschlagen (Assertion nicht erfüllt)

E → Fehler (unerwartete Exception während des Tests)

Aufgabe 2
a) Implementierung
pythonclass Einkaufsliste:
    def __init__(self):
        self._artikel = []

    def hinzufuegen(self, artikel: str):
        self._artikel.append(artikel)

    def entfernen(self, artikel: str):
        if artikel not in self._artikel:
            raise ValueError(f"{artikel} nicht in der Liste")
        self._artikel.remove(artikel)

    def anzeigen(self) -> list:
        return list(self._artikel)

    def ist_leer(self) -> bool:
        return len(self._artikel) == 0
b) Testklasse
pythonclass TestEinkaufsliste(unittest.TestCase):

    def setUp(self):
        self.liste = Einkaufsliste()

    def tearDown(self):
        print("Test abgeschlossen.")

    def test_neue_liste_ist_leer(self):
        self.assertTrue(self.liste.ist_leer())

    def test_artikel_hinzufuegen(self):
        self.liste.hinzufuegen("Milch")
        self.assertIn("Milch", self.liste.anzeigen())

    def test_artikel_entfernen(self):
        self.liste.hinzufuegen("Brot")
        self.liste.entfernen("Brot")
        self.assertNotIn("Brot", self.liste.anzeigen())

    def test_nicht_vorhandener_artikel_wirft_fehler(self):
        with self.assertRaises(ValueError):
            self.liste.entfernen("Butter")

    def test_mehrere_artikel_hinzufuegen(self):
        self.liste.hinzufuegen("Milch")
        self.liste.hinzufuegen("Brot")
        self.assertEqual(len(self.liste.anzeigen()), 2)
c) Warum setUp?
Ohne setUp() müsste man self.liste = Einkaufsliste() in jede Testmethode schreiben – das ist Codeduplikation. setUp() stellt sicher, dass jeder Test mit einem frischen, sauberen Objekt startet, unabhängig davon, was vorherige Tests verändert haben.

Aufgabe 3
a) Beide Varianten
python# Variante 1 – Callable + Argument
def test_einzahlen_negativ_v1(self):
    self.assertRaises(ValueError, self.konto.einzahlen, -50)

# Variante 2 – Context Manager
def test_einzahlen_negativ_v2(self):
    with self.assertRaises(ValueError):
        self.konto.einzahlen(-50)
b) berechne_note() aus Baustein 04
pythonclass TestBerechneNote(unittest.TestCase):

    def test_negative_punktzahl_wirft_fehler(self):
        with self.assertRaises(ValueError):
            berechne_note(-1)

    def test_punktzahl_ueber_100_wirft_fehler(self):
        with self.assertRaises(ValueError):
            berechne_note(101)

Aufgabe 4
a) Vier Testfälle
TCnettosteuersatzErwartungTC1100.0019.0119.00TC2100.007.0107.00TC30.0019.00.00TC4100.000.0100.00
b) Testklasse
pythonimport unittest

class TestMehrwertsteuer(unittest.TestCase):

    def test_normaler_steuersatz_19(self):
        self.assertAlmostEqual(berechne_mehrwertsteuer(100.00, 19.0), 119.00, places=2)

    def test_ermaessigter_steuersatz_7(self):
        self.assertAlmostEqual(berechne_mehrwertsteuer(100.00, 7.0), 107.00, places=2)

    def test_netto_null(self):
        self.assertAlmostEqual(berechne_mehrwertsteuer(0.00, 19.0), 0.00, places=2)

    def test_steuersatz_null(self):
        self.assertAlmostEqual(berechne_mehrwertsteuer(100.00, 0.0), 100.00, places=2)

if __name__ == '__main__':
    unittest.main()
c) Problem mit Kommazahlen
assertEqual ist bei Floats problematisch, weil Floating-Point-Arithmetik minimale Rundungsfehler erzeugt (z. B. 119.00000000001). Alternative: assertAlmostEqual, das standardmäßig auf 7 Nachkommastellen vergleicht – mit places=2 kann man die Genauigkeit anpassen.

Active Recall

unittest.TestCase
python -m unittest discover -v
assertEqual prüft auf exakte Gleichheit; assertAlmostEqual toleriert Rundungsfehler bei Floats (Standard: 7 Stellen)
Einmal pro Testmethode – jede Methode bekommt eine frische Umgebung
F (Failure) = eine Assertion ist fehlgeschlagen (erwartetes ≠ tatsächliches Ergebnis); E (Error) = eine unerwartete Exception ist aufgetreten (z. B. NameError, AttributeError)