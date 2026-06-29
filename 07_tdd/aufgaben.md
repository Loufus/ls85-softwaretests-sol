# Baustein 07 – Test-Driven Development (TDD) 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Baustein 05 und 06 abgeschlossen  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/DA4KdSKMba" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 07: TDD</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich habe bereits nach TDD entwickelt
- [ ] 🟡 Ich habe von TDD gehört und verstehe das Konzept
- [ ] 🔴 TDD ist mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … den Red-Green-Refactor-Zyklus erklären und visuell darstellen
- 🟡 … einen fehlschlagenden Test schreiben, bevor der Code existiert
- 🟡 … minimalen Code schreiben, der genau diesen Test grün macht
- 🔴 … Refactoring durchführen ohne bestehende Tests zu brechen
- 🔴 … Vor- und Nachteile von TDD für echte Berufsszenarien bewerten

---

## Hintergrund: Der TDD-Zyklus

```
         🔴 RED
      Test schreiben
    (schlägt fehl – ok!)
          │
          ▼
       🟢 GREEN
  Minimalen Code schreiben
  (nur so viel, dass Test grünt)
          │
          ▼
      🔵 REFACTOR
   Code verbessern ohne
   Funktionalität zu ändern
          │
          └──────► zurück zu RED
```

**Goldene TDD-Regel:** Kein Produktionscode ohne vorher einen fehlschlagenden Test!

**Baby Steps:** Immer nur einen Test auf einmal. Kein "ich implementiere schon mal alles durch".

---

## Aufgabe 0 – Grundbegriffe: TDD-Zyklus einordnen 🟢

**Einstieg: Den Zyklus verstehen**

**a)** Bringe die folgenden Schritte in die richtige TDD-Reihenfolge:

| Schritt | Aktion |
|---------|--------|
| A | Code refactorn: Namen verbessern, Dopplungen beseitigen |
| B | Test ausführen → er schlägt fehl (🔴 Red) |
| C | Test für eine neue Funktion schreiben |
| D | Minimalen Code schreiben, bis der Test grün wird (🟢 Green) |
| E | Alle Tests erneut ausführen → sie bleiben grün |

Richtige Reihenfolge: ___

**b)** Was bedeutet die „Goldene TDD-Regel"? Formuliere sie mit eigenen Worten.

**c)** Warum schreibt man beim Green-Schritt bewusst „hässlichen" (minimalen) Code?
Was passiert damit im nächsten Schritt?

**d)** Was ist ein „Baby Step" im TDD-Kontext?
Warum ist diese Vorgehensweise sinnvoll?

Trage deine Antworten in `07_tdd_protokoll.md` ein.

---

## Aufgabe 1 – TDD-Zyklus verstehen 🟡

**Szenario:** Du sollst eine Funktion `runden_auf_naechste_fuenf(zahl)` entwickeln,
die eine Zahl auf das nächste Vielfache von 5 aufrundet.

Beispiele:
- `runden_auf_naechste_fuenf(3)` → `5`
- `runden_auf_naechste_fuenf(7)` → `10`
- `runden_auf_naechste_fuenf(10)` → `10`
- `runden_auf_naechste_fuenf(0)` → `0`

**Gehe exakt nach dem TDD-Zyklus vor – Schritt für Schritt:**

**Zyklus 1:**
1. 🔴 Schreibe `test_runden_3_ergibt_5` – führe aus – er **muss** rot sein (Funktion existiert nicht)
2. 🟢 Implementiere genau so viel Code, dass dieser Test grünt
3. 🔵 Gibt es schon etwas zu verbessern? (wahrscheinlich noch nicht)

**Zyklus 2:**
1. 🔴 Schreibe `test_runden_7_ergibt_10`
2. 🟢 Passe Code an (minimal!)
3. 🔵 Refactoring?

**Zyklus 3–5:** Wiederhole für 10, 0, und negative Zahlen.

**Dokumentiere in `07_tdd_protokoll.md`:** Was war nach jedem Schritt der Zustand der Tests?

---

## Aufgabe 2 – TDD Praxisprojekt: Passwort-Generator 🔴

Entwickle nach TDD einen `PasswortGenerator` mit folgenden Anforderungen
(aber NUR die, für die du vorher einen Test geschrieben hast!):

**Anforderungen (als User Stories):**

1. Als Benutzer möchte ich ein Passwort mit konfigurierbarer Länge generieren können.
2. Als Benutzer möchte ich wählen, ob Großbuchstaben enthalten sein sollen.
3. Als Benutzer möchte ich wählen, ob Ziffern enthalten sein sollen.
4. Als Benutzer möchte ich wählen, ob Sonderzeichen enthalten sein sollen.
5. Als Benutzer möchte ich, dass eine Mindestlänge von 8 Zeichen erzwungen wird.
6. Als Benutzer möchte ich, dass bei ungültigen Parametern eine klare Fehlermeldung erscheint.

**Vorgehensweise:**
- Schreibe für jede User Story **zuerst** den Test
- Implementiere dann den Code
- Refactore wenn nötig
- Commit nach jedem Green-Zustand: `[LS85] 07 TDD: User Story 1 – Passwortlänge`

Starte mit `code/starter.py` – die Testklasse ist bereits vorbereitet.

---

## Aufgabe 3 – Refactoring unter Tests 🔴

In `starter.py` findest du eine funktionierende (aber schlecht strukturierte) Funktion `verarbeite_bestellung()`.
Alle Tests dafür sind bereits grün.

**a)** Führe die vorhandenen Tests aus – sie müssen alle grün sein.

**b)** Refactore den Code: Extrahiere sinnvolle Hilfsfunktionen, verbessere Namen, beseitige Duplikation.

**c)** Führe die Tests nach jedem Refactoring-Schritt erneut aus.
**Ziel: Alle Tests bleiben grün während du den Code verbesserst.**

**d)** Protokolliere in `07_tdd_protokoll.md`:
- Welche Änderungen hast du gemacht?
- Welche Tests haben dabei geholfen, Regressionen zu verhindern?

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler soll eine Funktion `berechne_zinsen(kapital, zinssatz, jahre)` entwickeln.
Er entscheidet sich für TDD.

**(a)** Beschreiben Sie die drei Phasen des TDD-Zyklus und was in jeder Phase konkret zu tun ist. *(3 Punkte)*

**(b)** Schreiben Sie für `berechne_zinsen()` mindestens vier Tests **bevor** Sie die Funktion implementieren.
Die Tests sollen verschiedene Äquivalenzklassen und Fehlerfälle abdecken. *(6 Punkte)*

**(c)** Implementieren Sie `berechne_zinsen()` so, dass alle Tests in (b) grün werden. *(4 Punkte)*

**(d)** Nennen Sie zwei Vorteile und einen Nachteil von TDD im Berufsalltag. *(3 Punkte)*

---

## Tandem-Aufgabe 👥

**Ping-Pong TDD:**

Person A schreibt einen Test → Person B implementiert minimalen Code, der grünt, und schreibt den nächsten Test → Person A implementiert → ...

**Aufgabe:** Entwickelt gemeinsam nach diesem Muster einen einfachen `Taschenrechner` mit:
`addieren`, `subtrahieren`, `multiplizieren`, `dividieren`

Wechselt nach jedem Test die Rollen.

Am Ende: Wieviele Tests habt ihr? Ist der Code gut strukturiert?

**Erkläre deinem Tandempartner:** Erkläre, was die „Goldene TDD-Regel" bedeutet und warum es in der Praxis schwer ist, sie konsequent einzuhalten. Teile deine eigene Erfahrung aus dieser Übung.

---

## Active Recall 🧠

*Unterlagen zu:*

1. Was ist die "Goldene TDD-Regel"?
2. Was bedeutet "Baby Steps" im TDD-Kontext?
3. Warum darf man beim Green-Step "hässlichen" Code schreiben?
4. Was ist das Ziel der Refactor-Phase?
5. Wie hilft TDD dabei, über den Code nachzudenken, bevor man ihn schreibt?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann TDD anwenden und habe den Zyklus verinnerlicht
- [ ] 🟡 Ich verstehe TDD, fällt mir aber noch schwer "zuerst den Test zu schreiben"
- [ ] 🔴 Ich brauche mehr Übung oder Erklärungen

**Was war für dich die größte Herausforderung bei TDD?**

> _______________________________________________

**Würdest du TDD im Betrieb einsetzen? Warum / Warum nicht?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*

a) Richtige Reihenfolge: C → B → D → A → E
b) Goldene TDD-Regel:

Kein Produktionscode wird geschrieben, ohne dass vorher ein fehlschlagender Test existiert. Man beweist erst, dass etwas fehlt, bevor man es baut.
c) Warum minimaler/hässlicher Code beim Green-Schritt?

Weil das Ziel in dieser Phase nur ist, den Test zum Laufen zu bringen – nicht mehr. Sauberkeit kommt im Refactor-Schritt. Würde man sofort alles perfekt schreiben, verliert man den Fokus und riskiert, mehr zu implementieren als nötig.
d) Baby Steps:

Man schreibt immer nur einen einzigen Test für einen einzigen Aspekt und implementiert genau so viel, dass dieser eine Test grün wird. Das hält die Schritte klein und kontrollierbar – Fehler sind sofort lokalisierbar und man verliert nie den Überblick.

Aufgabe 1
pythonimport pytest

# Zyklus 1
def test_runden_3_ergibt_5():
    assert runden_auf_naechste_fuenf(3) == 5

# Minimale Implementierung nach Zyklus 1:
def runden_auf_naechste_fuenf(zahl):
    return 5  # hardcoded – reicht für genau diesen Test

# Zyklus 2
def test_runden_7_ergibt_10():
    assert runden_auf_naechste_fuenf(7) == 10

# Implementierung nach Zyklus 2:
def runden_auf_naechste_fuenf(zahl):
    import math
    return math.ceil(zahl / 5) * 5

# Zyklus 3
def test_runden_10_ergibt_10():
    assert runden_auf_naechste_fuenf(10) == 10

# Zyklus 4
def test_runden_0_ergibt_0():
    assert runden_auf_naechste_fuenf(0) == 0

# Zyklus 5
def test_runden_negativ():
    assert runden_auf_naechste_fuenf(-3) == 0

# Finale Implementierung nach Refactoring:
import math

def runden_auf_naechste_fuenf(zahl: int | float) -> int:
    if zahl <= 0:
        return 0
    return math.ceil(zahl / 5) * 5
Protokoll:

Nach Zyklus 1: 1 grün (hardcoded), 0 rot
Nach Zyklus 2: 2 grün, echte Logik vorhanden
Nach Zyklus 3–4: 4 grün, kein Refactoring nötig
Nach Zyklus 5: 5 grün, Sonderfall für ≤ 0 ergänzt


Aufgabe 2
pythonimport pytest
import string
import random

class TestPasswortGenerator:

    # User Story 1 – Länge
    def test_passwort_hat_korrekte_laenge(self):
        gen = PasswortGenerator(laenge=12)
        assert len(gen.generieren()) == 12

    # User Story 2 – Großbuchstaben
    def test_passwort_enthaelt_grossbuchstaben(self):
        gen = PasswortGenerator(laenge=12, grossbuchstaben=True)
        pw = gen.generieren()
        assert any(c.isupper() for c in pw)

    def test_passwort_ohne_grossbuchstaben(self):
        gen = PasswortGenerator(laenge=12, grossbuchstaben=False)
        pw = gen.generieren()
        assert not any(c.isupper() for c in pw)

    # User Story 3 – Ziffern
    def test_passwort_enthaelt_ziffern(self):
        gen = PasswortGenerator(laenge=12, ziffern=True)
        pw = gen.generieren()
        assert any(c.isdigit() for c in pw)

    # User Story 4 – Sonderzeichen
    def test_passwort_enthaelt_sonderzeichen(self):
        gen = PasswortGenerator(laenge=12, sonderzeichen=True)
        pw = gen.generieren()
        assert any(c in string.punctuation for c in pw)

    # User Story 5 – Mindestlänge
    def test_mindestlaenge_wird_erzwungen(self):
        with pytest.raises(ValueError, match="Mindestlänge"):
            PasswortGenerator(laenge=4)

    # User Story 6 – Ungültige Parameter
    def test_keine_zeichenklasse_ausgewaehlt(self):
        with pytest.raises(ValueError, match="Zeichenklasse"):
            PasswortGenerator(laenge=8, grossbuchstaben=False,
                              kleinbuchstaben=False, ziffern=False,
                              sonderzeichen=False)


class PasswortGenerator:
    def __init__(self, laenge=12, grossbuchstaben=True,
                 kleinbuchstaben=True, ziffern=True, sonderzeichen=False):
        if laenge < 8:
            raise ValueError("Mindestlänge ist 8 Zeichen")
        if not any([grossbuchstaben, kleinbuchstaben, ziffern, sonderzeichen]):
            raise ValueError("Mindestens eine Zeichenklasse muss ausgewählt sein")
        self.laenge = laenge
        self.zeichen = ""
        if grossbuchstaben:
            self.zeichen += string.ascii_uppercase
        if kleinbuchstaben:
            self.zeichen += string.ascii_lowercase
        if ziffern:
            self.zeichen += string.digits
        if sonderzeichen:
            self.zeichen += string.punctuation

    def generieren(self) -> str:
        return ''.join(random.choice(self.zeichen) for _ in range(self.laenge))

Aufgabe 4
a) Die drei TDD-Phasen:
Red: Einen Test für eine noch nicht existierende Funktionalität schreiben und ausführen – er muss fehlschlagen, um zu beweisen, dass der Code noch fehlt.
Green: Minimalen Produktionscode schreiben, der genau diesen Test grün macht – nicht mehr, nicht weniger. Qualität ist hier zweitrangig.
Refactor: Den Code sauber machen (Namen verbessern, Duplikation beseitigen, Struktur verbessern), ohne die Funktionalität zu ändern. Alle Tests müssen danach weiterhin grün sein.
b) Tests vor der Implementierung:
pythonimport pytest

def test_zinsen_normaler_fall():
    assert berechne_zinsen(1000, 5, 1) == pytest.approx(50.0)

def test_zinsen_mehrere_jahre():
    assert berechne_zinsen(1000, 10, 3) == pytest.approx(300.0)

def test_zinsen_nullprozent():
    assert berechne_zinsen(1000, 0, 5) == pytest.approx(0.0)

def test_negatives_kapital_wirft_fehler():
    with pytest.raises(ValueError, match="Kapital"):
        berechne_zinsen(-100, 5, 1)

def test_negativer_zinssatz_wirft_fehler():
    with pytest.raises(ValueError, match="Zinssatz"):
        berechne_zinsen(1000, -5, 1)

def test_negative_jahre_wirft_fehler():
    with pytest.raises(ValueError, match="Jahre"):
        berechne_zinsen(1000, 5, -1)
c) Implementierung:
pythondef berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
    if kapital < 0:
        raise ValueError("Kapital darf nicht negativ sein")
    if zinssatz < 0:
        raise ValueError("Zinssatz darf nicht negativ sein")
    if jahre < 0:
        raise ValueError("Jahre darf nicht negativ sein")
    return kapital * (zinssatz / 100) * jahre
d) Vor- und Nachteile:
Vorteile:

Tests entstehen automatisch als Nebenprodukt der Entwicklung – keine nachträgliche Testarbeit
Man denkt gezwungenermaßen über die Schnittstelle nach, bevor man implementiert – führt zu besserem Design

Nachteil:

Anfangs deutlich langsamer, vor allem bei wenig TDD-Erfahrung – das kostet in Projekten mit Zeitdruck Überzeugungsarbeit


Active Recall

Kein Produktionscode ohne vorher einen fehlschlagenden Test.
Immer nur einen Test auf einmal schreiben und genau so viel Code, dass dieser eine Test grün wird.
Weil der Refactor-Schritt direkt danach kommt – sauberer Code ist das Ziel der Refactor-Phase, nicht der Green-Phase.
Den Code lesbarer, wartbarer und strukturierter machen, ohne Funktionalität zu verändern – alle Tests müssen grün bleiben.
Man ist gezwungen, die Schnittstelle (Eingaben, Ausgaben, Fehlerfälle) zu durchdenken, bevor man irgendetwas implementiert – das führt zu durchdachterem Design.