# Baustein 03 – Testmethoden 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/zeNGxav483" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 03: Testmethoden</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne Black-Box und White-Box-Tests
- [ ] 🟡 Ich habe von diesen Begriffen gehört, bin aber unsicher
- [ ] 🔴 Diese Methoden sind mir unbekannt

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … Black-Box-Tests von White-Box-Tests unterscheiden
- 🟡 … Testfälle nach der Black-Box-Methode ohne Codekenntnis ableiten
- 🟡 … Anweisungsüberdeckung (Statement Coverage) und Zweigüberdeckung (Branch Coverage) erklären
- 🟡 … einen einfachen Kontrollflussgraphen aus Code erstellen
- 🔴 … begründen, welche Testmethode für welches Testziel am besten geeignet ist

---

## Hintergrund

Bei **Black-Box-Tests** (funktionaler Test) kennst du den Quellcode nicht – du testest nur über
Ein- und Ausgaben. Das entspricht der Perspektive des Kunden oder des Testers ohne Codekenntnis.

Bei **White-Box-Tests** (struktureller Test) kennst du den Quellcode und prüfst gezielt,
ob bestimmte Codeabschnitte durchlaufen werden. Ziel ist eine möglichst hohe **Testabdeckung** (Coverage).

**Grey-Box**: Kombination beider Ansätze – du kennst die Architektur, aber nicht alle Details.

---

## Aufgabe 0 – Grundbegriffe: Black-Box vs. White-Box 🟢

**Wiederholen und verorten:**

**a)** Erkläre in eigenen Worten (ohne Nachschauen):
- Was ist der grundlegende Unterschied zwischen Black-Box- und White-Box-Test?
- Welche Frage stellt der Tester beim Black-Box-Test?
- Welche Frage stellt der Tester beim White-Box-Test?

**b)** Ordne die folgenden Situationen zu (Black-Box oder White-Box):

| Situation | Methode |
|-----------|---------|
| Ein Kunde testet, ob er sich einloggen kann | |
| Ein Entwickler prüft, ob alle if-Zweige durchlaufen werden | |
| Ein Tester gibt verschiedene Passwörter ein und schaut, was passiert | |
| Ein Entwickler misst die Testabdeckung (Coverage) | |
| Ein externes Testteam prüft das System gegen die Spezifikation | |

**c)** Erkläre in einem Satz, warum es sinnvoll ist, beide Methoden zu kombinieren.

Trage deine Antworten in `03_antworten.md` ein.

---

## Aufgabe 1 – Black-Box-Test: Benutzerauthentifizierung 🟡

In `code/starter.py` ist eine Funktion `authentifiziere_benutzer()` implementiert.
Du darfst den Implementierungstext **nicht** lesen (falte ihn mental weg) –
arbeite nur mit der Schnittstellenbeschreibung:

**Spezifikation:**
- Eingabe: `benutzername` (str), `passwort` (str)
- Ausgabe: `True` wenn gültig, `False` wenn ungültig
- Regeln:
  - Benutzername: 3–20 Zeichen, keine Sonderzeichen außer `_`
  - Passwort: mindestens 8 Zeichen
  - Bekannte gültige Zugangsdaten: `admin` / `geheim123`

**a)** Erstelle eine Testtabelle mit mindestens 6 Black-Box-Testfällen:

| TC-Nr | Eingabe (User/PW) | Erwartete Ausgabe | Kategorie |
|-------|-------------------|------------------|-----------|
| TC01 | admin / geheim123 | True | Gültiger Login |
| TC02 | | | |
| TC03 | | | |
| ... | | | |

**b)** Führe deine Testfälle aus, indem du die Funktion in `starter.py` aufrufst.
Welche Testfälle schlagen fehl? Dokumentiere die Ergebnisse.

---

## Aufgabe 2 – White-Box-Test: Coverage 🟡

In `code/starter.py` findest du die Funktion `kategorisiere_bestellung()`.

**a)** Zeichne den **Kontrollflussgraphen** dieser Funktion auf Papier (oder als ASCII-Art in `03_antworten.md`).
Nummeriere alle Knoten (Anweisungen) und alle Kanten (Bedingungszweige).

**b)** **Anweisungsüberdeckung (Statement Coverage):**
Wie viele Testfälle brauchst du mindestens, um jede Anweisung einmal auszuführen?
Erstelle diese Testfälle.

**c)** **Zweigüberdeckung (Branch Coverage):**
Wie viele Testfälle brauchst du, um jeden Zweig (jedes if/else) mindestens einmal zu durchlaufen?
Warum sind das mehr als bei Statement Coverage?

---

## Aufgabe 3 – Methoden vergleichen 🟡

Fülle die Tabelle aus:

| Merkmal | Black-Box | White-Box |
|---------|-----------|-----------|
| Codekenntnis notwendig? | | |
| Aus wessen Perspektive? | | |
| Was wird geprüft? | | |
| Typische Werkzeuge | | |
| Vorteil | | |
| Nachteil | | |

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwickler hat folgende Python-Funktion geschrieben:

```python
def versandkosten(gewicht_kg: float, express: bool) -> float:
    if gewicht_kg <= 0:
        raise ValueError("Gewicht muss positiv sein")
    if express:
        if gewicht_kg <= 5:
            return 8.90
        else:
            return 14.90
    else:
        if gewicht_kg <= 5:
            return 3.90
        else:
            return 6.90
```

**(a)** Erstellen Sie einen Kontrollflussgraphen für diese Funktion. Benennen Sie alle Knoten und Kanten. *(4 Punkte)*

**(b)** Wie viele Testfälle sind für eine vollständige **Zweigüberdeckung** erforderlich? Listen Sie diese auf. *(4 Punkte)*

**(c)** Welche Testfälle würden Sie zusätzlich aus **Black-Box-Sicht** (Grenzwertanalyse) ergänzen? *(2 Punkte)*

---

## Tandem-Aufgabe 👥

**Code Review mit Testbrille:**

Person A: Schreibt eine kurze Python-Funktion (10–15 Zeilen, mindestens 2 if-Zweige)
Person B: Kennt den Code **nicht** (Black-Box) und erstellt Testfälle nur aus der Beschreibung

Dann tauscht ihr:
Person B liest den Code und prüft mit White-Box-Methode, welche Testfälle fehlen.

Diskutiert: Was hat die Black-Box-Perspektive übersehen? Was hat die White-Box-Analyse ergänzt?

**Erkläre deinem Tandempartner:** Wähle einen konkreten Fall aus deinem Berufsalltag und erkläre, wann du Black-Box- und wann White-Box-Testing einsetzen würdest – und warum. Dein Tandempartner nennt anschließend eine Ergänzung oder ein Gegenbeispiel.

---

## Active Recall 🧠

*Unterlagen zu – beantworte aus dem Gedächtnis:*

1. Was ist der fundamentale Unterschied zwischen Black-Box und White-Box?
2. Was bedeutet 100 % Statement Coverage? Garantiert das fehlerfreie Software?
3. Warum ist Branch Coverage strenger als Statement Coverage?
4. In welcher Teststufe (aus Baustein 02) wird meistens White-Box-Testing eingesetzt?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann beide Methoden anwenden und den Unterschied erklären
- [ ] 🟡 Ich verstehe die Theorie, brauche aber mehr Übung
- [ ] 🔴 Ich brauche Unterstützung bei Coverage-Konzepten

**Was nimmst du mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*



a) Unterschiede:

Black-Box: Tester kennt den Code nicht – er testet nur über Ein- und Ausgaben. Frage: „Liefert die Funktion bei dieser Eingabe die richtige Ausgabe?"
White-Box: Tester kennt den Code und prüft, ob alle Pfade/Zweige durchlaufen werden. Frage: „Wird jede Codezeile/jeder Zweig tatsächlich ausgeführt?"

b) Zuordnung:
SituationMethodeEin Kunde testet, ob er sich einloggen kannBlack-BoxEin Entwickler prüft, ob alle if-Zweige durchlaufen werdenWhite-BoxEin Tester gibt verschiedene Passwörter ein und schaut, was passiertBlack-BoxEin Entwickler misst die Testabdeckung (Coverage)White-BoxEin externes Testteam prüft das System gegen die SpezifikationBlack-Box
c) Beide Methoden kombiniert decken sowohl funktionale Fehler (falsche Ausgaben) als auch strukturelle Lücken (nicht getestete Codepfade) ab.

Aufgabe 1 – Black-Box: Benutzerauthentifizierung
TC-NrEingabe (User/PW)Erwartete AusgabeKategorieTC01admin / geheim123TrueGültiger LoginTC02admin / falsch1234FalseFalsches PasswortTC03unbekannt / geheim123FalseUnbekannter BenutzerTC04ab / geheim123FalseUsername zu kurz (< 3 Zeichen)TC05admin / kurzFalsePasswort zu kurz (< 8 Zeichen)TC06adm!n / geheim123FalseSonderzeichen im UsernameTC07(leer) / geheim123FalseLeerer UsernameTC08admin / (leer)FalseLeeres Passwort

Aufgabe 2 – White-Box: Coverage (versandkosten-ähnliche Logik)
Für kategorisiere_bestellung() gilt analog – hier am Beispiel der Aufgabe 4-Funktion erklärt, da kein starter.py vorliegt.
Kontrollflussgraph (ASCII) für versandkosten:
        [Start]
           |
    [gewicht <= 0?]
      /          \
   Ja             Nein
[raise ValueError] [express?]
                  /        \
               Ja            Nein
        [gewicht<=5?]    [gewicht<=5?]
         /      \          /      \
       Ja       Nein     Ja       Nein
   [8.90]     [14.90] [3.90]    [6.90]
Knoten: 8 | Kanten: 9

Aufgabe 3 – Methoden vergleichen
MerkmalBlack-BoxWhite-BoxCodekenntnis notwendig?NeinJaAus wessen Perspektive?Benutzer / Kunde / externer TesterEntwicklerWas wird geprüft?Funktionalität (Ein-/Ausgabe)Codestruktur, Pfade, ZweigeTypische WerkzeugeTestfallkataloge, Äquivalenzklassen, GrenzwertanalyseCoverage-Tools (z. B. pytest-cov), DebuggerVorteilUnabhängig vom Code, NutzerperspektiveFindet ungetestete Codepfade, hohe PräzisionNachteilKann interne Fehler übersehenAufwendig, kein Blick auf Gesamtverhalten

Aufgabe 4 – IHK-Stil (versandkosten)
(a) Kontrollflussgraph:
N1: Funktionsstart
N2: if gewicht_kg <= 0  →  Ja → N3: raise ValueError / Ende
                         →  Nein → N4
N4: if express           →  Ja → N5
                         →  Nein → N7
N5: if gewicht_kg <= 5  →  Ja → N6: return 8.90
                         →  Nein → N6b: return 14.90
N7: if gewicht_kg <= 5  →  Ja → N8: return 3.90
                         →  Nein → N8b: return 6.90
(b) Zweigüberdeckung – 5 Testfälle:
TCgewicht_kgexpressErwartungAbgedeckter ZweigTC1-1FalseValueErrorN2 → JaTC23.0True8.90N2→Nein, N4→Ja, N5→JaTC37.0True14.90N4→Ja, N5→NeinTC43.0False3.90N4→Nein, N7→JaTC57.0False6.90N7→Nein
→ Alle 9 Kanten abgedeckt ✅
(c) Grenzwertanalyse (Black-Box):
TCgewicht_kgexpressBegründungTC65.0TrueGrenzwert genau 5 kg → 8.90?TC75.01TrueKnapp über Grenze → 14.90?TC85.0FalseGrenzwert genau 5 kg → 3.90?TC90.01FalseKleinstes gültiges Gewicht

Active Recall

Black-Box = nur Ein-/Ausgabe bekannt; White-Box = Code bekannt, interne Pfade werden geprüft
Jede Anweisung wurde mindestens einmal ausgeführt – garantiert keine fehlerfreie Software, da Zweige evtl. nicht alle getestet wurden
Branch Coverage fordert, dass jeder if/else-Zweig (auch der else-Fall) durchlaufen wird – Statement Coverage reicht schon, wenn die Zeile einmal erreicht wurde, egal über welchen Pfad
Unit-Tests (Modultest) – hier hat der Entwickler direkten Codezugriff