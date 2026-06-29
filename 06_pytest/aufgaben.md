# Baustein 06 – pytest 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Baustein 05 (unittest) abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/kZUchAUVA9" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 06: pytest</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne pytest und habe damit gearbeitet
- [ ] 🟡 Ich habe von pytest gehört
- [ ] 🔴 Das ist Neuland für mich

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … pytest installieren und einfache Testfunktionen schreiben
- 🟡 … Fixtures mit `@pytest.fixture` definieren und in Testfunktionen nutzen
- 🟡 … mit `@pytest.mark.parametrize` einen Test für viele Eingaben wiederverwenden
- 🟡 … erwartete Ausnahmen mit `pytest.raises` testen
- 🔴 … einen sinnvollen pytest-Testlauf konfigurieren und das Ergebnis auswerten

---

## Setup – pytest installieren

```bash
# Installation (einmalig):
pip install pytest

# Version prüfen:
pytest --version

# Tests ausführen (im Projektverzeichnis):
pytest 06_pytest/code/ -v

# Mit Coverage (optional):
pip install pytest-cov
pytest 06_pytest/code/ --cov=06_pytest/code/ --cov-report=term-missing
```

---

## Hintergrund

pytest ist der de-facto Standard für Python-Tests im Berufsalltag.
Im Vergleich zu unittest hat pytest:
- Kein Boilerplate – Testfunktionen statt Testklassen
- Bessere Fehlerausgaben (zeigt Variablenwerte bei Fehlern)
- Mächtiges Fixture-System für Testvorbereitung
- Parametrisierung für Datentabellen-Tests
- Große Plugin-Bibliothek (pytest-cov, pytest-mock, ...)

---

## Aufgabe 0 – Grundbegriffe: pytest-Ausgabe lesen 🟢

**Einstieg: Ergebnisse interpretieren**

Lies folgende pytest-Ausgabe und beantworte die Fragen:

```
==================== test session starts ====================
collected 5 items

test_rechner.py::test_addieren_positiv   PASSED          [ 20%]
test_rechner.py::test_addieren_negativ   PASSED          [ 40%]
test_rechner.py::test_dividieren         FAILED          [ 60%]
test_rechner.py::test_division_durch_null PASSED         [ 80%]
test_rechner.py::test_falscher_typ       ERROR           [100%]

==================== 3 passed, 1 failed, 1 error in 0.04s ====================
```

**a)** Wie viele Tests wurden ausgeführt? Wie viele waren erfolgreich?

**b)** Was ist der Unterschied zwischen `FAILED` und `ERROR`?

**c)** Welcher Test schlägt fehl? Was könnte der Grund sein?

**d)** In welcher Datei befinden sich die Tests? Wie erkennst du das?

**e)** Wie lautet der Befehl, mit dem diese Ausgabe erzeugt wurde?
(Tipp: Was bedeutet das `-v`-Flag?)

Trage deine Antworten in `06_antworten.md` ein.

---

## Aufgabe 1 – Von unittest zu pytest migrieren 🟡

**a)** Konvertiere zwei Testmethoden aus Baustein 05 in pytest-Testfunktionen.
Vergleiche: Was vereinfacht sich? Was fehlt?

```python
# unittest-Stil (Baustein 05):
class TestKontorechner(unittest.TestCase):
    def test_einzahlen_positiver_betrag(self):
        konto = Kontorechner()
        konto.einzahlen(100)
        self.assertEqual(konto.kontostand, 100)

# pytest-Stil (deine Aufgabe):
def test_einzahlen_positiver_betrag():
    # TODO: Deine Implementierung
    pass
```

**b)** Führe die Tests mit `pytest 06_pytest/code/starter.py -v` aus.
Was bedeutet die Ausgabe `PASSED` / `FAILED` / `ERROR`?

---

## Aufgabe 2 – Fixtures 🟡

**Szenario:** Du testest eine Klasse `Benutzerkontoservice` aus `starter.py`.
Das Anlegen eines Test-Kontos ist aufwändig – du willst es nicht in jedem Test wiederholen.

**a)** Schreibe ein Fixture `kontoservice()`, das einen fertig eingerichteten `BenutzerkontoService` zurückgibt.

```python
@pytest.fixture
def kontoservice():
    # TODO: Service anlegen, Testbenutzer eintragen
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service
```

**b)** Verwende das Fixture in mindestens 4 Testfunktionen.
Beachte: Das Fixture wird für jeden Test neu erzeugt – warum ist das wichtig?

**c)** Erweitere das Fixture um `scope="module"` und erkläre, wann das sinnvoll ist.

---

## Aufgabe 3 – Parametrisierung 🟡

Ohne Parametrisierung:
```python
def test_note_bei_100():
    assert berechne_note(100) == 1

def test_note_bei_90():
    assert berechne_note(90) == 2
# ... (sehr viel Wiederholung)
```

Mit Parametrisierung:
```python
@pytest.mark.parametrize("punkte, erwartete_note", [
    (100, 1),
    (92, 1),
    (91, 2),
    # ...
])
def test_berechne_note(punkte, erwartete_note):
    assert berechne_note(punkte) == erwartete_note
```

**a)** Schreibe einen parametrisierten Test für `berechne_note()` aus Baustein 04,
der alle Notengrenzen und mindestens 2 Vertreter je Äquivalenzklasse prüft (mind. 14 Testfälle).

**b)** Schreibe einen parametrisierten Test für `validiere_menge()` aus Baustein 04,
der alle gültigen und ungültigen Klassen plus alle Grenzwerte abdeckt.

**c)** Führe aus und interpretiere: Wie viele Tests wurden erzeugt? Wie lange hat das gedauert?

---

## Aufgabe 4 – pytest.raises 🟡

```python
# Einfache Variante:
def test_negative_einzahlung():
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.einzahlen(-50)

# Mit Prüfung der Fehlermeldung:
def test_negative_einzahlung_fehlermeldung():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(-50)
```

**a)** Schreibe mindestens 3 Tests mit `pytest.raises`, die auch die Fehlermeldung prüfen (`match=`).

**b)** Was ist der Unterschied zwischen `pytest.raises` und `unittest.assertRaises`?
Welche Variante bevorzugst du und warum?

---

## Aufgabe 5 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwicklungsteam hat folgende Testanforderung dokumentiert:

> "Die Funktion `berechne_versandkosten(gewicht, express)` soll für alle
> Kombination aus Gewichtsklassen (≤5 kg, >5 kg) und Express-Option
> korrekte Preise zurückgeben. Zusätzlich sollen ungültige Eingaben
> (negatives Gewicht, falscher Typ) korrekt abgelehnt werden."

**(a)** Implementieren Sie `berechne_versandkosten()` in `starter.py`. *(4 Punkte)*

**(b)** Schreiben Sie einen vollständigen parametrisierten pytest-Test für alle gültigen Fälle. *(6 Punkte)*

**(c)** Schreiben Sie je einen Test für die beiden ungültigen Eingaben. *(4 Punkte)*

**(d)** Erläutern Sie den Vorteil der Parametrisierung gegenüber einzelnen Testfunktionen. *(2 Punkte)*

---

## Tandem-Aufgabe 👥

**Code Review der Tests:**

Jede Person schreibt für eine selbst gewählte Funktion:
- Mindestens 2 normale Testfunktionen
- Mindestens 1 Fixture
- Mindestens 1 parametrisierten Test

Dann Code-Review im Tandem:
- Sind die Testnamen aussagekräftig?
- Werden alle Äquivalenzklassen aus Baustein 04 abgedeckt?
- Wird `pytest.raises` für alle Fehlerfälle genutzt?
- Gibt es unnötige Wiederholungen, die durch Parametrisierung beseitigt werden könnten?

**Erkläre deinem Tandempartner:** Erkläre, warum `@pytest.fixture` mächtiger ist als das Anlegen eines Objekts direkt im Test. Nutze ein Beispiel aus deiner eigenen Lösung. Dein Tandempartner stellt mindestens eine Rückfrage.

---

## Active Recall 🧠

*Unterlagen zu:*

1. Wie unterscheidet sich eine pytest-Testfunktion von einer unittest-Testmethode?
2. Wozu dient ein Fixture?
3. Was passiert, wenn ein Fixture mit `scope="module"` definiert ist?
4. Wie prüfst du in pytest, dass eine bestimmte Exception geworfen wird?
5. Warum ist Parametrisierung besser als viele separate Testfunktionen?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann pytest eigenständig einsetzen und Fixtures + Parametrisierung nutzen
- [ ] 🟡 Ich verstehe die Konzepte, habe aber noch Probleme bei Fixtures
- [ ] 🔴 Ich brauche mehr Erklärungen oder Übung

**Was nimmst du mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*

Aufgabe 0
a) 5 Tests wurden ausgeführt, 3 waren erfolgreich.
b) FAILED = der Test lief durch, aber eine Assertion war falsch (erwartetes ≠ tatsächliches Ergebnis). ERROR = der Test ist gar nicht erst vollständig gelaufen, weil eine unerwartete Exception aufgetreten ist (z. B. NameError, TypeError).
c) test_dividieren schlägt fehl. Möglicher Grund: Die Funktion liefert ein falsches Ergebnis, z. B. durch einen Rundungsfehler bei Floats oder einen Logikfehler.
d) Die Tests befinden sich in test_rechner.py – erkennbar am Präfix test_rechner.py:: vor jedem Testnamen.
e) pytest test_rechner.py -v – das -v steht für "verbose" und zeigt jeden einzelnen Testnamen mit Ergebnis an.

Aufgabe 1
a)
python# unittest-Stil:
class TestKontorechner(unittest.TestCase):
    def test_einzahlen_positiver_betrag(self):
        konto = Kontorechner()
        konto.einzahlen(100)
        self.assertEqual(konto.kontostand, 100)

    def test_abheben_kein_guthaben(self):
        konto = Kontorechner()
        with self.assertRaises(ValueError):
            konto.abheben(50)

# pytest-Stil:
def test_einzahlen_positiver_betrag():
    konto = Kontorechner()
    konto.einzahlen(100)
    assert konto.kontostand == 100

def test_abheben_kein_guthaben():
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.abheben(50)
Vereinfacht: kein Erben von unittest.TestCase, kein self, keine self.assert...-Methoden – nur normales assert. Fehlt: automatisches setUp/tearDown (wird durch Fixtures ersetzt).
b) PASSED = Assertion erfüllt. FAILED = Assertion fehlgeschlagen. ERROR = unerwartete Exception während des Tests.

Aufgabe 2
a + b)
pythonimport pytest

@pytest.fixture
def kontoservice():
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service

def test_benutzer_existiert(kontoservice):
    assert kontoservice.benutzer_existiert("testuser") == True

def test_login_korrekt(kontoservice):
    assert kontoservice.login("testuser", "Test1234!") == True

def test_login_falsches_passwort(kontoservice):
    assert kontoservice.login("testuser", "falsch") == False

def test_benutzer_loeschen(kontoservice):
    kontoservice.benutzer_loeschen("testuser")
    assert kontoservice.benutzer_existiert("testuser") == False
Das Fixture wird für jeden Test neu erzeugt, damit Tests sich nicht gegenseitig beeinflussen. Wenn test_benutzer_loeschen den Benutzer löscht, hat das keinen Einfluss auf den nächsten Test.
c)
python@pytest.fixture(scope="module")
def kontoservice():
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service
scope="module" ist sinnvoll, wenn das Anlegen des Objekts teuer ist (z. B. Datenbankverbindung) und alle Tests im Modul dasselbe Objekt nutzen können, ohne es zu verändern. Achtung: Tests dürfen dann den Zustand nicht gegenseitig beeinflussen.

Aufgabe 3
a)
pythonimport pytest

@pytest.mark.parametrize("punkte, erwartete_note", [
    (100, 1),
    (95, 1),
    (92, 1),
    (91, 2),
    (85, 2),
    (81, 2),
    (80, 3),
    (74, 3),
    (67, 3),
    (66, 4),
    (58, 4),
    (50, 4),
    (49, 5),
    (40, 5),
    (30, 5),
    (29, 6),
    (15, 6),
    (0, 6),
])
def test_berechne_note(punkte, erwartete_note):
    assert berechne_note(punkte) == erwartete_note
b)
python@pytest.mark.parametrize("menge, erwartet", [
    (1, True),
    (2, True),
    (500, True),
    (998, True),
    (999, True),
    (0, False),
    (-5, False),
    (1000, False),
])
def test_validiere_menge(menge, erwartet):
    assert validiere_menge(menge) == erwartet
c) pytest erzeugt aus den parametrisierten Listen automatisch einzelne Testfälle – 18 für berechne_note, 8 für validiere_menge. Laufzeit liegt im Millisekunden-Bereich, da kein I/O beteiligt ist.

Aufgabe 4
a)
pythondef test_negative_einzahlung():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(-50)

def test_einzahlung_null():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(0)

def test_abheben_ohne_guthaben():
    konto = Kontorechner()
    with pytest.raises(ValueError, match="Guthaben"):
        konto.abheben(100)
b) Beide nutzen denselben Context-Manager-Stil und sind funktional gleichwertig. pytest.raises zeigt bei Fehlern mehr Kontext und unterstützt match= direkt als Parameter. unittest.assertRaises erfordert eine Testklasse. Im Berufsalltag ist pytest.raises üblicher, weil es weniger Boilerplate hat und besser lesbar ist.

Aufgabe 5
a)
pythondef berechne_versandkosten(gewicht: float, express: bool) -> float:
    if not isinstance(gewicht, (int, float)):
        raise TypeError("Gewicht muss eine Zahl sein")
    if gewicht <= 0:
        raise ValueError("Gewicht muss positiv sein")
    if express:
        return 8.90 if gewicht <= 5 else 14.90
    else:
        return 3.90 if gewicht <= 5 else 6.90
b)
python@pytest.mark.parametrize("gewicht, express, erwartet", [
    (3.0, True,  8.90),
    (5.0, True,  8.90),
    (5.1, True,  14.90),
    (10.0, True, 14.90),
    (3.0, False, 3.90),
    (5.0, False, 3.90),
    (5.1, False, 6.90),
    (10.0, False, 6.90),
])
def test_versandkosten_gueltig(gewicht, express, erwartet):
    assert berechne_versandkosten(gewicht, express) == pytest.approx(erwartet)
c)
pythondef test_negatives_gewicht_wirft_fehler():
    with pytest.raises(ValueError, match="positiv"):
        berechne_versandkosten(-1, False)

def test_falscher_typ_wirft_fehler():
    with pytest.raises(TypeError, match="Zahl"):
        berechne_versandkosten("schwer", False)
d) Parametrisierung vermeidet Codeduplikation: statt 8 einzelner Funktionen mit identischer Struktur gibt es eine einzige Funktion mit einer Datentabelle. Neue Testfälle lassen sich durch eine Zeile in der Liste ergänzen, ohne neuen Code zu schreiben. Außerdem zeigt pytest bei Fehlern genau welcher Parametersatz gescheitert ist.

Active Recall

Eine pytest-Testfunktion ist eine normale Funktion (kein self, kein Erben von TestCase), die mit test_ beginnt und normales assert verwendet.
Ein Fixture bereitet Testobjekte oder Ressourcen vor, die mehrere Tests brauchen – ähnlich wie setUp(), aber flexibler und wiederverwendbar per Parameter.
Das Fixture wird nur einmal pro Modul erstellt und von allen Tests im Modul geteilt – statt für jeden Test neu.
Mit pytest.raises(ExceptionType) als Context Manager: with pytest.raises(ValueError): ...
Parametrisierung hält den Code DRY: ein Test, viele Datensätze. Neue Fälle kosten nur eine Zeile, Fehler zeigen genau welcher Datensatz scheitert.