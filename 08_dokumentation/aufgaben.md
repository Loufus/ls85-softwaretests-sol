# Baustein 08 – Testdokumentation 🔴

> **Schwierigkeit:** 🔴 Transfer  
> **Zeitrahmen:** ca. 150 Minuten  
> **Voraussetzung:** Alle vorherigen Bausteine  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/BQurE7rxAq" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 08: Testdokumentation</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [ ] 🟢 Ich kenne Testpläne und Testberichte
- [ ] 🟡 Ich habe davon gehört, aber noch nie selbst erstellt
- [ ] 🔴 Das ist mir komplett neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … erklären, wozu Testdokumentation dient
- 🟡 … einen Testplan nach Vorlage erstellen
- 🟡 … Testfälle vollständig und formal dokumentieren
- 🔴 … einen Testbericht mit Ergebnissen für einen Auftraggeber erstellen
- 🔴 … Qualitätskennzahlen (Testabdeckung, Fehlerquote) ermitteln und interpretieren

---

## Hintergrund

Im Berufsalltag reicht es nicht, Tests zu schreiben – du musst auch nachweisen,
dass du getestet hast und was dabei herausgekommen ist.

**Testdokumentation dient dazu:**
- Nachvollziehbarkeit: Wer hat was wann getestet?
- Qualitätsnachweis gegenüber Auftraggeber / Kunden
- Grundlage für Abnahmeentscheidungen
- Rückverfolgbarkeit: Welche Anforderung wird durch welchen Test abgedeckt?
- Wissensweitergabe im Team

**Wichtige Dokumente:**
- **Testplan**: Was wird wie getestet? (vor dem Testen)
- **Testfallspezifikation**: Genaue Definition einzelner Tests
- **Testbericht**: Was wurde gefunden? (nach dem Testen)

---

## Aufgabe 0 – Grundbegriffe: Testdokumentation einordnen 🟢

**Einstieg ohne Code:**

**a)** Ordne die folgenden Aussagen dem richtigen Dokument zu
(Testplan / Testprotokoll / Testbericht):

| Aussage | Dokument |
|---------|----------|
| „Wir werden alle Module mit pytest testen." | |
| „TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt." | |
| „8 von 10 Tests bestanden, 1 Fehler offen." | |
| „Abnahmekriterium: Coverage > 80 %." | |
| „Empfehlung: System ist abnahmebereit." | |

**b)** Wann wird jedes Dokument erstellt? Ordne zu:
- Vor dem Testen
- Während des Testens
- Nach dem Testen

**c)** Erkläre in 2 Sätzen: Warum reicht es nicht aus, Tests einfach auszuführen –
ohne sie zu dokumentieren?

Trage deine Antworten in `08_antworten.md` ein.

---

## Aufgabe 1 – Testfall-Dokumentation 🟡

Ein Testfall braucht immer diese Bestandteile:

| Feld | Beschreibung |
|------|-------------|
| TC-ID | Eindeutige Kennung (z. B. TC-AUTH-001) |
| Titel | Kurze Beschreibung des Tests |
| Vorbedingung | Was muss vor dem Test gelten? |
| Testeingabe | Welche Daten werden verwendet? |
| Testschritte | Was wird Schritt für Schritt getan? |
| Erwartetes Ergebnis | Was soll passieren? |
| Tatsächliches Ergebnis | Was ist tatsächlich passiert? (nach Ausführung) |
| Status | Bestanden / Fehlgeschlagen / Blockiert |

**a)** Erstelle vollständige Testfalldokumentationen für die Funktion `authentifiziere_benutzer()`
aus Baustein 03. Mindestens 6 Testfälle.

Nutze die Vorlage in `code/starter.py` (als Python-Docstring oder Markdown-Tabelle).

**b)** Führe die Testfälle aus und trage "Tatsächliches Ergebnis" und "Status" ein.

---

## Aufgabe 2 – Testplan erstellen 🟡

Ein Testplan ist das übergeordnete Dokument, das beschreibt:
- Was soll getestet werden (Testumfang)?
- Wie soll getestet werden (Methoden, Werkzeuge)?
- Wer testet was (Verantwortlichkeiten)?
- Wann wird getestet (Zeitplan)?
- Was sind die Abnahmekriterien?

**Szenario:** Du bist Fachinformatiker/in in einem Betrieb.
Ihr habt eine **Lagerbestandsverwaltung** in Python entwickelt (ca. 200 Zeilen Code,
3 Module: `artikel.py`, `lager.py`, `bericht.py`).

Erstelle einen Testplan (in `08_testplan.md`) mit:
- Projektname, Datum, Autor
- Testumfang (was wird getestet, was nicht)
- Teststufen (welche Tests auf welcher Stufe)
- Testmethoden (Black-Box, White-Box, Äquivalenzklassen...)
- Werkzeuge (pytest, Coverage...)
- Zeitplan (wann wird welche Teststufe durchgeführt)
- Abnahmekriterien (z. B. "alle Tests grün", "Coverage > 80 %")

---

## Aufgabe 3 – Coverage-Bericht interpretieren 🔴

In `code/starter.py` findest du ein Modul `lager.py` mit einer `Lager`-Klasse
und eine Test-Suite dafür.

**a)** Installiere pytest-cov und führe den Coverage-Bericht aus:
```bash
pip install pytest-cov
pytest 08_dokumentation/code/starter.py --cov=08_dokumentation/code/starter --cov-report=term-missing -v
```

**b)** Interpretiere den Bericht:
- Welche Zeilen werden nicht getestet ("missing")?
- Welche Zweige fehlen?
- Wie hoch ist die aktuelle Coverage?

**c)** Schreibe zusätzliche Tests, um die Coverage auf mindestens 90 % zu bringen.

**d)** Ist 100 % Coverage ein Qualitätsgarant? Begründe.

---

## Aufgabe 4 – Testbericht erstellen 🔴

Nach dem Abschluss der Tests für die Lagerbestandsverwaltung (Aufgabe 2)
erwartet der Auftraggeber einen formalen Testbericht.

Erstelle `08_testbericht.md` mit:
- Zusammenfassung: Was wurde getestet? Mit welchem Ergebnis?
- Testumgebung: Python-Version, Betriebssystem, pytest-Version
- Testergebnisse: Tabelle mit allen Testfällen und Status
- Gefundene Fehler: Fehlerbeschreibung, Schweregrad, Status (offen/behoben)
- Coverage-Statistik: Tabelle pro Modul
- Bewertung: Ist das System abnahmebereit?
- Offene Punkte: Was bleibt zu tun?

Verwende als Grundlage die Ergebnisse aus Aufgaben 1–3.

---

## Aufgabe 5 – IHK-Stil 🔴

**Prüfungsszenario:**

Ein Entwicklungsteam hat folgende pytest-Ausgabe erhalten:

```
PASSED  test_artikel_anlegen                       [ 10%]
PASSED  test_bestand_erhoehen                      [ 20%]
FAILED  test_bestand_reduzieren_unter_null         [ 30%]
PASSED  test_artikel_suchen_vorhanden              [ 40%]
FAILED  test_artikel_suchen_nicht_vorhanden        [ 50%]
PASSED  test_lager_kapazitaet_pruefen              [ 60%]
ERROR   test_bericht_erstellen                     [ 70%]
PASSED  test_bestand_exportieren                   [ 80%]
PASSED  test_import_aus_csv                        [ 90%]
PASSED  test_loeschen_vorhandener_artikel          [100%]

8 passed, 2 failed, 1 error in 0.43s
```

**(a)** Berechnen Sie die Erfolgsquote der Tests in Prozent. *(1 Punkt)*

**(b)** Unterscheiden Sie "FAILED" und "ERROR" in pytest. Was bedeutet jeweils dieser Status? *(4 Punkte)*

**(c)** Erstellen Sie einen kurzen Testbericht (Tabellenformat), der diese Ergebnisse für den Auftraggeber aufbereitet. Bewerten Sie, ob das System abnahmebereit ist. *(6 Punkte)*

**(d)** Welche Maßnahmen würden Sie vor einer erneuten Abnahme empfehlen? *(4 Punkte)*

---

## Tandem-Aufgabe 👥

**Gegenseitiger Testbericht-Review:**

Person A erstellt einen Testplan und Testbericht für ihre Lösung aus Baustein 07 (TDD).
Person B erstellt dasselbe für ihre Lösung aus Baustein 06 (pytest).

Dann tauscht ihr und reviewed gegenseitig:
- Sind alle Pflichtbestandteile vorhanden?
- Ist der Bericht für jemanden verständlich, der den Code nicht kennt?
- Würde der Auftraggeber die Abnahme erteilen?

Haltet Feedback schriftlich fest.

**Erkläre deinem Tandempartner:** Erkläre den Unterschied zwischen Testplan, Testprotokoll und Testbericht – und warum alle drei Dokumente für einen Auftraggeber wichtig sind. Dein Tandempartner prüft, ob alle wesentlichen Punkte korrekt erklärt wurden.

---

## Active Recall 🧠

*Unterlagen zu:*

1. Was ist der Unterschied zwischen Testplan und Testbericht?
2. Was sind typische Abnahmekriterien für Software?
3. Was bedeutet "Testabdeckung" (Coverage) und was misst sie nicht?
4. Wann ist ein Testbericht "gut genug" für einen Kunden?
5. Was ist der Unterschied zwischen FAILED und ERROR in pytest?

---

## Reflexion 🚦

- [ ] 🟢 Ich kann professionelle Testdokumentation erstellen
- [ ] 🟡 Ich verstehe das Konzept, die Umsetzung braucht noch Übung
- [ ] 🔴 Ich brauche weitere Erklärungen oder Beispiele

**Was war in dieser gesamten Lernsequenz das Wichtigste für dich?**

> _______________________________________________

**Was nimmst du konkret in deinen Betriebsalltag mit?**

> _______________________________________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*


Aufgabe 0
a) Zuordnung
AussageDokument„Wir werden alle Module mit pytest testen."Testplan„TC-007 ist fehlgeschlagen: Bestand wurde auf -5 gesetzt."Testprotokoll„8 von 10 Tests bestanden, 1 Fehler offen."Testbericht„Abnahmekriterium: Coverage > 80 %."Testplan„Empfehlung: System ist abnahmebereit."Testbericht
b) Zeitpunkt

Vor dem Testen: Testplan
Während des Testens: Testprotokoll
Nach dem Testen: Testbericht

c)

Ohne Dokumentation kann niemand nachvollziehen, was getestet wurde, wer es getestet hat und was dabei herauskam. Ein Auftraggeber kann keine Abnahmeentscheidung treffen, wenn es keinen nachvollziehbaren Nachweis über die Testergebnisse gibt.

Aufgabe 1
a + b) Testfalldokumentation für authentifiziere_benutzer()
FeldTC-AUTH-001TC-IDTC-AUTH-001TitelGültiger Login mit korrekten ZugangsdatenVorbedingungSystem läuft, Benutzer "admin" mit Passwort "geheim123" ist bekanntTesteingabebenutzername="admin", passwort="geheim123"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisTrueTatsächliches ErgebnisTrueStatusBestanden
FeldTC-AUTH-002TC-IDTC-AUTH-002TitelLogin mit falschem PasswortVorbedingungBenutzer "admin" ist bekanntTesteingabebenutzername="admin", passwort="falsch1234"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisFalseTatsächliches ErgebnisFalseStatusBestanden
FeldTC-AUTH-003TC-IDTC-AUTH-003TitelLogin mit unbekanntem BenutzerVorbedingungBenutzer "unbekannt" existiert nichtTesteingabebenutzername="unbekannt", passwort="geheim123"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisFalseTatsächliches ErgebnisFalseStatusBestanden
FeldTC-AUTH-004TC-IDTC-AUTH-004TitelUsername zu kurz (unter 3 Zeichen)Vorbedingung–Testeingabebenutzername="ab", passwort="geheim123"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisFalseTatsächliches ErgebnisFalseStatusBestanden
FeldTC-AUTH-005TC-IDTC-AUTH-005TitelPasswort zu kurz (unter 8 Zeichen)Vorbedingung–Testeingabebenutzername="admin", passwort="kurz"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisFalseTatsächliches ErgebnisFalseStatusBestanden
FeldTC-AUTH-006TC-IDTC-AUTH-006TitelSonderzeichen im BenutzernamenVorbedingung–Testeingabebenutzername="adm!n", passwort="geheim123"TestschritteFunktion aufrufen mit den o. g. WertenErwartetes ErgebnisFalseTatsächliches ErgebnisFalseStatusBestanden

Aufgabe 2
markdown# Testplan – Lagerbestandsverwaltung

**Projektname:** Lagerbestandsverwaltung  
**Datum:** 29.06.2026  
**Autor:** Marvin Faustmann  

## Testumfang

Getestet wird:
- artikel.py – Artikel anlegen, bearbeiten, löschen, suchen
- lager.py – Bestand erhöhen/reduzieren, Kapazitätsprüfung
- bericht.py – Berichterstellung, CSV-Export

Nicht getestet wird:
- GUI (nicht vorhanden)
- Datenbankanbindung (nicht implementiert)
- Performance unter Last

## Teststufen

| Stufe | Was | Wann |
|-------|-----|------|
| Unit-Tests | Einzelne Methoden aller drei Module | KW 26 |
| Integrationstests | Zusammenspiel Lager + Artikel | KW 26 |
| Systemtest | Gesamter Ablauf: Artikel anlegen → Bestand → Bericht | KW 27 |

## Testmethoden

- White-Box: Anweisungs- und Zweigüberdeckung für Kernlogik
- Black-Box: Äquivalenzklassen und Grenzwertanalyse für alle Eingaben
- Negativtests: Ungültige Eingaben und Fehlerfälle

## Werkzeuge

- pytest 8.x
- pytest-cov (Coverage-Messung)
- Python 3.12

## Zeitplan

| Woche | Aktivität |
|-------|-----------|
| KW 26 | Unit-Tests und Integrationstests schreiben und ausführen |
| KW 27 | Systemtest, Coverage-Auswertung, Fehlerbehebung |
| KW 27 | Testbericht erstellen, Abnahme |

## Abnahmekriterien

- Alle Tests grün (0 FAILED, 0 ERROR)
- Coverage gesamt >= 80 %
- Keine offenen Fehler mit Schweregrad "hoch"
- Testbericht vollständig und vom Teamlead freigegeben

Aufgabe 3
d) Ist 100 % Coverage ein Qualitätsgarant?

Nein. Coverage misst nur, ob eine Codezeile ausgeführt wurde – nicht ob sie korrekt ausgeführt wurde. Man kann 100 % Coverage haben, ohne eine einzige sinnvolle Assertion zu schreiben. Außerdem deckt Coverage keine fehlenden Anforderungen ab: eine Funktion, die nie implementiert wurde, taucht im Coverage-Bericht gar nicht auf.

Aufgabe 4
markdown# Testbericht – Lagerbestandsverwaltung

**Datum:** 29.06.2026  
**Autor:** Marvin Faustmann  
**Testphase:** Abschlusstest v1.0  

## Zusammenfassung

Es wurden 10 Testfälle über alle drei Module ausgeführt. 8 Tests bestanden,
2 schlugen fehl, 1 Error trat auf. Das System ist in der aktuellen Form
nicht abnahmebereit.

## Testumgebung

- Python 3.12.3
- pytest 8.2.0
- pytest-cov 5.0.0
- OS: Windows 11

## Testergebnisse

| TC-ID | Testname | Status |
|-------|----------|--------|
| TC-01 | test_artikel_anlegen | Bestanden |
| TC-02 | test_bestand_erhoehen | Bestanden |
| TC-03 | test_bestand_reduzieren_unter_null | Fehlgeschlagen |
| TC-04 | test_artikel_suchen_vorhanden | Bestanden |
| TC-05 | test_artikel_suchen_nicht_vorhanden | Fehlgeschlagen |
| TC-06 | test_lager_kapazitaet_pruefen | Bestanden |
| TC-07 | test_bericht_erstellen | Error |
| TC-08 | test_bestand_exportieren | Bestanden |
| TC-09 | test_import_aus_csv | Bestanden |
| TC-10 | test_loeschen_vorhandener_artikel | Bestanden |

## Gefundene Fehler

| Fehler-ID | Beschreibung | Schweregrad | Status |
|-----------|-------------|-------------|--------|
| BUG-01 | Bestand kann unter 0 reduziert werden | Hoch | Offen |
| BUG-02 | Suche gibt kein Ergebnis bei nicht vorhandenem Artikel | Mittel | Offen |
| BUG-03 | Berichtsmodul wirft unerwartete Exception (Error) | Hoch | Offen |

## Coverage

| Modul | Coverage |
|-------|---------|
| artikel.py | 91 % |
| lager.py | 78 % |
| bericht.py | 45 % |
| Gesamt | 72 % |

## Bewertung

Das System ist nicht abnahmebereit. Zwei Tests schlagen fehl, ein Error
verhindert die Ausführung des Berichtsmoduls. Die Coverage liegt mit 72 %
unter dem Abnahmekriterium von 80 %. Vor einer erneuten Abnahme müssen
BUG-01 bis BUG-03 behoben werden.

## Offene Punkte

- BUG-01 bis BUG-03 beheben
- Coverage in lager.py und bericht.py erhöhen
- Erneuten Testlauf nach Fehlerbehebung durchführen

Aufgabe 5
a) Erfolgsquote

8 von 11 Tests bestanden = 72,7 %
b) FAILED vs. ERROR

FAILED: Der Test wurde vollständig ausgeführt, aber eine Assertion hat nicht gestimmt – das erwartete Ergebnis unterscheidet sich vom tatsächlichen. Das ist ein Fehler in der Implementierung.

ERROR: Der Test konnte gar nicht vollständig ausgeführt werden, weil eine unerwartete Exception aufgetreten ist (z. B. NameError, AttributeError, fehlende Abhängigkeit). Das ist kein Assertion-Fehler, sondern ein technischer Fehler im Test oder in der Umgebung.
c) Testbericht für den Auftraggeber
TCTestnameStatus01test_artikel_anlegenBestanden02test_bestand_erhoehenBestanden03test_bestand_reduzieren_unter_nullFehlgeschlagen04test_artikel_suchen_vorhandenBestanden05test_artikel_suchen_nicht_vorhandenFehlgeschlagen06test_lager_kapazitaet_pruefenBestanden07test_bericht_erstellenError08test_bestand_exportierenBestanden09test_import_aus_csvBestanden10test_loeschen_vorhandener_artikelBestanden
Erfolgsquote: 72,7 % – Abnahmeempfehlung: Nicht abnahmebereit. Zwei fachliche Fehler und ein technischer Error müssen vor der Abnahme behoben werden.
d) Empfehlungen vor erneuter Abnahme

BUG in test_bestand_reduzieren_unter_null beheben: Lager muss negative Bestände verhindern und einen ValueError werfen
BUG in test_artikel_suchen_nicht_vorhanden beheben: Rückgabewert bei fehlendem Artikel prüfen (None oder leere Liste statt Exception)
ERROR in test_bericht_erstellen analysieren: Ursache der unerwarteten Exception ermitteln (fehlende Abhängigkeit, Initialisierungsfehler) und beheben
Erneuten vollständigen Testlauf durchführen und Bericht aktualisieren


Active Recall

Der Testplan beschreibt vor dem Testen, was wie getestet wird. Der Testbericht dokumentiert nach dem Testen, was gefunden wurde und ob das System abnahmebereit ist.
Typische Abnahmekriterien: alle Tests grün, Coverage >= X %, keine offenen Fehler mit hohem Schweregrad, Testbericht vollständig.
Coverage misst, welcher Anteil des Codes durch Tests ausgeführt wurde. Sie misst nicht, ob die Tests sinnvolle Assertions haben, ob alle Anforderungen abgedeckt sind oder ob der Code korrekt ist.
Ein Testbericht ist gut genug, wenn er für jemanden ohne Codekenntnis verständlich ist, alle Testfälle mit Status enthält, gefundene Fehler beschreibt und eine klare Abnahmeempfehlung gibt.
FAILED = Assertion fehlgeschlagen, Code läuft aber durch. ERROR = unerwartete Exception, Test konnte nicht vollständig ausgeführt werden.