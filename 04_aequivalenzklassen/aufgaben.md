# Baustein 04 – Äquivalenzklassen & Grenzwertanalyse 🟡

> **Schwierigkeit:** 🟡 Anwendung  
> **Zeitrahmen:** ca. 120 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=AVtDSgxpSk2SjJ-w6Dswu9p-7diy21FJmEKm_woHizhURTVaWUNOQjA1WERLUDRMTVdVTElEUkMwTS4u" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 04: Äquivalenzklassen</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich weiß, was Äquivalenzklassen sind
- [ ] 🟡 Ich habe den Begriff schon gehört
- [ ] 🔴 Das ist mir komplett neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … erklären, was eine Äquivalenzklasse ist
- 🟢 … gültige und ungültige Äquivalenzklassen eines Eingabebereichs ermitteln
- 🟡 … Grenzwerte identifizieren und daraus Testfälle ableiten
- 🟡 … eine vollständige Äquivalenzklassentabelle erstellen
- 🔴 … begründen, warum diese Methoden die Anzahl notwendiger Testfälle sinnvoll reduzieren

---

## Hintergrund

Vollständiges Testen ist unmöglich (Prinzip 2 aus Baustein 01).
Äquivalenzklassen helfen, die unendlich vielen Eingabemöglichkeiten auf
eine handhabbare Anzahl sinnvoller Vertreter zu reduzieren.

**Grundidee:** Alle Eingaben innerhalb einer Klasse verhalten sich gleich –
es reicht, einen repräsentativen Wert je Klasse zu testen.

**Grenzwertanalyse** ergänzt dies: Fehler entstehen besonders häufig an den Grenzen
(z. B. bei `>= 18` werden oft 17, 18 und 19 verwechselt).

---

## Aufgabe 0 – Grundbegriffe: Äquivalenzklassen erkennen 🟢

**Einstieg ohne Code:**

**a)** Eine Ampel-Steuerung akzeptiert nur Ganzzahlen von 1 bis 5 als Prioritätsstufe.
Benenne ohne viel Nachdenken: Was sind gültige, was ungültige Eingaben?

**b)** Erkläre in einem Satz, was eine Äquivalenzklasse ist –
so als würdest du es einem Mitschüler ohne IT-Kenntnis erklären.

**c)** Nenne je ein Beispiel aus dem Berufsalltag für:
- Eine gültige Äquivalenzklasse
- Eine ungültige Äquivalenzklasse
- Einen Grenzwert, der besonders kritisch sein könnte

**d)** Warum reicht es aus, nur **einen** repräsentativen Wert pro Klasse zu testen?
Erkläre die Grundannahme dahinter.

Trage deine Antworten in `04_antworten.md` ein.

---

## Aufgabe 1 – Äquivalenzklassen für ein Bestellformular 🟡

Eine E-Commerce-Anwendung hat folgende Validierungsregeln für das Bestellfeld "Menge":
- Typ: ganzzahlig
- Minimum: 1
- Maximum: 999
- Sonderfall: 0 ist explizit verboten ("Mindestbestellmenge")

**a)** Ermittle alle Äquivalenzklassen und trage sie in die Tabelle ein:

| AK-Nr | Klasse | Repräsentativer Wert | Gültig / Ungültig |
|-------|--------|---------------------|-------------------|
| AK1 | | | |
| AK2 | | | |
| AK3 | | | |
| AK4 | | | |

**b)** Ergänze die Tabelle um Grenzwerttestfälle:

| GW-Nr | Grenzwert | Erwartetes Ergebnis |
|-------|-----------|---------------------|
| GW1 | 0 | Ungültig |
| GW2 | 1 | Gültig |
| GW3 | | |
| GW4 | | |
| GW5 | | |

**c)** Implementiere in `code/starter.py` die Funktion `validiere_menge()` und schreibe manuelle Tests für alle Äquivalenzklassen und Grenzwerte.

---

## Aufgabe 2 – Äquivalenzklassen für Passwortstärke 🟡

Eine Anwendung prüft Passwörter nach folgenden Regeln:
- Länge: 8–64 Zeichen
- Muss mindestens einen Großbuchstaben enthalten
- Muss mindestens eine Ziffer enthalten
- Darf keine Leerzeichen enthalten

**a)** Erstelle die Äquivalenzklassentabelle für alle vier Regeln kombiniert.
Hinweis: Jede Regel erzeugt eigene gültige/ungültige Klassen!

**b)** Wähle repräsentative Testwerte aus und begründe deine Wahl.

**c)** Implementiere `pruefe_passwort()` in `starter.py` und teste alle Klassen.

---

## Aufgabe 3 – Grenzwertanalyse: Altersverifikation 🟡

Eine Plattform hat drei Kategorien:
- Unter 12: Kinder-Modus (eingeschränkt)
- 12–17: Jugend-Modus (teils eingeschränkt)
- Ab 18: Vollzugang

**a)** Bestimme alle Grenzwerte und erstelle eine Grenzwerttabelle mit:
- Unterer Grenzwert der Klasse
- Wert genau an der Grenze
- Oberer Grenzwert der Klasse

**b)** Welche Fälle würden erfahrene Tester zusätzlich einbeziehen?
(Denke an ungültige Werte wie negative Zahlen, 0, 150, Kommazahlen)

---

## Aufgabe 4 – IHK-Stil 🔴

**Prüfungsszenario:**

Eine Prüfungssoftware berechnet das Prüfungsergebnis:

- Eingabe: Punktzahl (ganzzahlig, 0–100)
- Ausgabe: Note (1–6) nach folgendem Schema:
  - 92–100: Note 1
  - 81–91:  Note 2
  - 67–80:  Note 3
  - 50–66:  Note 4
  - 30–49:  Note 5
  - 0–29:   Note 6

**(a)** Ermitteln Sie alle Äquivalenzklassen (gültige und ungültige). *(4 Punkte)*

**(b)** Erstellen Sie eine vollständige Grenzwerttabelle für alle Notengrenzen. *(6 Punkte)*

**(c)** Welche Eingabewerte würden Sie als Tester wählen, um mit möglichst wenigen Testfällen alle Klassen und Grenzwerte abzudecken? Begründen Sie Ihre Wahl. *(4 Punkte)*

Implementiere die Funktion `berechne_note()` und teste alle Fälle aus (a)–(c) in `starter.py`.

---

## Tandem-Aufgabe 👥

**Spiegeltest – Gegenseitiges Überprüfen:**

Jede Person wählt eine Funktion aus dem Berufsalltag (Beispiele: Telefonnummernvalidierung, PLZ-Prüfung, Datumseingabe, Kreditkartennummer).

Erstellt unabhängig voneinander Äquivalenzklassen und Grenzwerttabellen.
Dann vergleicht: Was hat die andere Person gefunden, was du übersehen hast?

Diskutiert: Würden eure Testfälle denselben Fehler finden?

**Erkläre deinem Tandempartner:** Erkläre das Prinzip der Äquivalenzklassenbildung so, als würdest du es einem Nicht-IT-Kollegen erklären müssen – ohne Fachbegriffe, nur mit einem Alltagsbeispiel. Dein Tandempartner gibt Feedback: War es verständlich?

---

## Active Recall 🧠

*Unterlagen zu:*

1. Was ist der Kerngedanke hinter Äquivalenzklassen?
2. Warum testet man immer auch ungültige Klassen?
3. An welchen Stellen entstehen besonders häufig Programmfehler? (Stichwort: Grenzwerte)
4. Wie viele Testfälle braucht man mindestens für vollständige Äquivalenzklassenabdeckung?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann eigenständig Äquivalenzklassen und Grenzwerte ermitteln
- [ ] 🟡 Das Konzept ist klar, aber ich brauche noch Übung
- [ ] 🔴 Ich brauche weitere Erklärungen oder Beispiele

**Was nimmst du mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*


Aufgabe 0
a)

Gültig: 1, 2, 3, 4, 5

Ungültig: 0, –1, 6, 100, 2.5, "hoch"
b)

Eine Äquivalenzklasse ist eine Gruppe von Eingaben, bei denen das Programm immer gleich reagiert – testet man einen Wert, weiß man wie es bei allen anderen in der Gruppe auch läuft.
c)

Gültig: Eine Bestellmenge zwischen 1 und 999 wird akzeptiert.

Ungültig: Eine Bestellmenge von 0 oder –5 wird abgelehnt.

Grenzwert: Genau 999 – hier entstehen oft Off-by-One-Fehler.
d)

Die Grundannahme ist: Alle Werte innerhalb einer Klasse lösen dieselbe Programmlogik aus. Wenn 50 korrekt verarbeitet wird, wird auch 200 korrekt verarbeitet – beide nehmen denselben Codepfad.

Aufgabe 1
a) Äquivalenzklassentabelle
AK-NrKlasseRepräsentativer WertGültig / UngültigAK11–999 (gültiger Bereich)500GültigAK2= 0 (explizit verboten)0UngültigAK3< 0 (negativ)–5UngültigAK4> 999 (zu groß)1000Ungültig
b) Grenzwerttabelle
GW-NrGrenzwertErwartetes ErgebnisGW10UngültigGW21GültigGW32GültigGW4998GültigGW5999GültigGW61000Ungültig
c)
pythondef validiere_menge(menge: int) -> bool:
    return isinstance(menge, int) and 1 <= menge <= 999

assert validiere_menge(500)  == True
assert validiere_menge(1)    == True
assert validiere_menge(999)  == True
assert validiere_menge(0)    == False
assert validiere_menge(-5)   == False
assert validiere_menge(1000) == False

Aufgabe 2
a) Äquivalenzklassentabelle
AK-NrRegelKlasseRepräsentantG/UAK1Länge8–64 ZeichenAbcd1234GültigAK2Länge< 8 ZeichenAb1!UngültigAK3Länge> 64 Zeichen65× 'a'UngültigAK4Großbuchstabemind. einer vorhandenAbcd1234GültigAK5Großbuchstabekeiner vorhandenabcd1234UngültigAK6Ziffermind. eine vorhandenAbcd1234GültigAK7Zifferkeine vorhandenAbcdefghUngültigAK8Leerzeichenkeines vorhandenAbcd1234GültigAK9Leerzeichenenthält LeerzeichenAbc d123Ungültig
b)

Abcd1234 → deckt AK1/4/6/8 ab (alle Regeln erfüllt, Minimalfall 8 Zeichen)

Ab1! → AK2 (zu kurz)

abcd1234 → AK5 (kein Großbuchstabe)

Abcdefgh → AK7 (keine Ziffer)

Abc d123 → AK9 (Leerzeichen)

'A1' + 'x'×63 → AK3 (65 Zeichen, zu lang)
c)
pythonimport re

def pruefe_passwort(pw: str) -> bool:
    if not (8 <= len(pw) <= 64): return False
    if not re.search(r'[A-Z]', pw): return False
    if not re.search(r'\d', pw): return False
    if ' ' in pw: return False
    return True

Aufgabe 3
a) Grenzwerttabelle
AlterKategorieKommentar11Kinder-Modusobere Grenze Kinder12Jugend-Modusuntere Grenze Jugend (Grenzwert!)13Jugend-Modusknapp über unterer Grenze17Jugend-Modusknapp unter oberer Grenze18Vollzuganguntere Grenze Vollzugang (Grenzwert!)19Vollzugangknapp über unterer Grenze
b)

0 → Ungültige Eingabe

–1 → Negatives Alter muss abgefangen werden

150 → Unrealistisch hoch

12.5 → Kommazahl – akzeptiert das System nur Ganzzahlen?

"abc" → Falscher Typ

Aufgabe 4
a) Äquivalenzklassen
AK-NrKlasseRepräsentantNoteG/UAK192–100951GültigAK281–91852GültigAK367–80743GültigAK450–66584GültigAK530–49405GültigAK60–29156GültigAK7< 0–1FehlerUngültigAK8> 100101FehlerUngültig
b) Grenzwerttabelle
WertErwartete Note–1Fehler062963054955046646738038129129211001101Fehler
c)

Minimale Testfälle: –1, 0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100, 101

Diese 14 Werte decken alle 8 Äquivalenzklassen ab und testen jeden Notenübergang beidseitig – Off-by-One-Fehler werden sicher erkannt.
pythondef berechne_note(punkte: int) -> int:
    if not (0 <= punkte <= 100):
        raise ValueError(f"Ungültige Punktzahl: {punkte}")
    if punkte >= 92: return 1
    if punkte >= 81: return 2
    if punkte >= 67: return 3
    if punkte >= 50: return 4
    if punkte >= 30: return 5
    return 6

Active Recall

Alle Eingaben einer Klasse lösen dieselbe Programmlogik aus – ein Repräsentant genügt.
Ungültige Klassen prüfen, ob das System Fehleingaben korrekt abfängt und nicht abstürzt.
Besonders häufig an Grenzwerten – Off-by-One-Fehler sind klassische Bugs.
Mindestens ein Testfall pro Klasse – so viele wie es Klassen gibt.