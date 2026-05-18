# Baustein 02 – Testarten 🟢

> **Schwierigkeit:** 🟢 Grundlagen  
> **Zeitrahmen:** ca. 90 Minuten  
> [Nicht weitergekommen? → Stuck Protocol](../stuck_protocol.md)

---

## 📖 Vorbereitung

> **Lies zuerst [`theorie.md`](theorie.md) vollständig durch.**

Teste dein Vorwissen mit dem Forms-Quiz:  
👉 <a href="https://forms.office.com/e/buC7L4PjPh" target="_blank" rel="noopener noreferrer">
📋 Forms-Quiz Baustein 02: Testarten</a>

> ⚠️ **Hinweis:** Bearbeite die Aufgaben erst NACH dem Theorieteil.

---

## Selbsteinschätzung – Vorher

- [X] 🟢 Ich kenne die verschiedenen Testarten bereits
- [ ] 🟡 Ich kenne manche Begriffe, aber nicht alle
- [ ] 🔴 Das Thema ist mir neu

---

## Lernziele

Nach diesem Baustein kannst du …

- 🟢 … die vier Teststufen (Unit, Integration, System, Abnahmetest) benennen und erklären
- 🟢 … das V-Modell skizzieren und die Testebenen korrekt einordnen
- 🟢 … den Unterschied zwischen funktionalen und nicht-funktionalen Tests beschreiben
- 🟡 … erklären, was Regressionstests sind und wann sie eingesetzt werden
- 🟡 … Testarten einem Praxisszenario korrekt zuordnen

---

## Hintergrund

Software wird selten als Ganzes entwickelt und dann einmal getestet.
In der Praxis gibt es mehrere Teststufen, die aufeinander aufbauen – ähnlich wie bei der
Qualitätskontrolle in der Fertigung: Erst werden Einzelteile geprüft, dann Baugruppen,
dann das Gesamtprodukt, und schließlich der Kunde nimmt ab.

Das **V-Modell** visualisiert diesen Zusammenhang zwischen Entwicklungs- und Teststufen.

---

## Aufgabe 1 – Die vier Teststufen 🟢

Lies die Beschreibungen und ordne sie den Teststufen zu.

| Beschreibung | Teststufe |
|-------------|-----------|
| Testet einzelne Funktionen oder Methoden isoliert | Unit|
| Prüft das Zusammenspiel mehrerer Module |Integrationstest |
| Testet das gesamte System gegen die Anforderungen |Systemtest |
| Der Auftraggeber prüft, ob seine Anforderungen erfüllt sind | Akzeptanztest|

**Teststufen:** Unit-Test · Integrationstest · Systemtest · Abnahmetest (User Acceptance Test)

Trage die Tabelle ausgefüllt in `starter.py` als Kommentar ein.

---

## Aufgabe 2 – Praxisszenario Webshop 🟢

Ein Team entwickelt einen einfachen Online-Webshop mit folgenden Komponenten:
- `preisberechnung.py` – berechnet Gesamtpreis mit Rabatt
- `warenkorb.py` – verwaltet Artikel im Warenkorb
- `bestellprozess.py` – verarbeitet eine Bestellung (Warenkorb + Zahlung + Lager)
- Gesamtsystem: Benutzer legt Artikel in Warenkorb und bestellt

**a)** Nenne je ein Testbeispiel für jede Teststufe in diesem Webshop.

| Teststufe | Konkretes Testbeispiel |
|-----------|----------------------|
| Unit-Test | Preisberechnung Testen = Währung schreibweise|
| Integrationstest | Zussamenarbeit zwischen preisberechnung und Warenkorb testen|
| Systemtest | Ein Test machen wo man eine Person nutzt die nix von system weiß und sagt Bestell einfach was. |
| Abnahmetest | Den Kunden die chance geben zu Testen das alles Funktioniert.|

**b)** In `code/starter.py` findest du die Funktion `berechne_gesamtpreis()`.
Schreibe einen einfachen manuellen Test (mit `print()`), der folgende Fälle prüft:
- Normaler Einkauf ohne Rabatt
- Einkauf mit 10 % Rabatt
- Leerer Warenkorb (Sonderfall!)

---

## Aufgabe 3 – Funktional vs. nicht-funktional 🟢

Ordne die folgenden Testszenarien zu:

| Testszenario | Funktional | Nicht-funktional |
|-------------|-----------|-----------------|
| Login mit korrekten Zugangsdaten klappt | | Funkt |
| Seite lädt in unter 2 Sekunden | |Funkt |
| Bestellung wird korrekt in der Datenbank gespeichert | |Funkt |
| System ist bei 1000 gleichzeitigen Nutzern stabil | | Funkt|
| Passwort-Reset-Mail wird verschickt | | Funk|
| Alle Texte sind auf Deutsch (Lokalisierung) | |Funk |

---

## Aufgabe 4 – Regressionstests 🟡

**Szenario:**  
Dein Team hat den Rabattrechner aus Baustein 01 korrigiert.
Jetzt soll eine neue Funktion "Mengenrabatt" (ab 10 Stück = 5 % extra Rabatt) hinzugefügt werden.

**a)** Was ist ein Regressionstest? Erkläre mit eigenen Worten.

nach geänderten Code sollte nochmal der gleiche Test  durgelaufen werden damit man sehen kann ob noch alles klappt.

**b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? Liste mindestens 3 auf.

Seite neuladen und messen. Bestellung wir richtig gespeichert. System ist stabil bei 1000 Nutzern.

**c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll?

weil wir schon ein erwartes ergebniss haben kann man das darduch vergelciehn wenn es abweicht muss man nur da nachschauen.

---

## Aufgabe 5 – IHK-Stil 🟡

**Prüfungsszenario:**

Ein Ausbildungsbetrieb entwickelt eine Zeiterfassungssoftware.
Das Entwicklungsteam hat folgende Testmaßnahmen geplant:

- Entwickler testen ihre eigenen Funktionen mit isolierten Tests (Unit)
- Anschließend werden die Module Zeiterfassung, Benutzerverwaltung und Auswertung gemeinsam getestet (Integrationtest)
- Das HR-Team führt abschließend einen formalen Abnahmetest durch (Systemtest)

**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu. *(3 Punkte)*

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte. *(3 Punkte)*
Akzeptanztest den Kunden das Produkt zum testen geben. 

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie. *(4 Punkte)*
Integrationstest hätte es aufallen müssen weil es wahrscheinlich nicht eine Einzige Funktion ist sonder mindesten 2 die miteinander arbeiten.
---

## Aufgabe 6 – Transfer: Teststrategie analysieren 🔴

**Transferaufgabe:**

Ein Betrieb hat folgendes Testkonzept für seine neue Zeiterfassungssoftware:

> „Unsere Entwickler testen ihre Funktionen kurz durch Ausführen des Programms.
> Sobald das System läuft, lassen wir das HR-Team damit arbeiten und
> schauen, ob Beschwerden kommen."

**a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.
Integrationstest fehlen und Systemtest

**b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?
Es könnten zu Falschen Urlaubs tagen kommen und zeitplan mässig zu fehlern führen. Und ohne test sagt man einfach hier habt spaß und schaut für euch selber.

**c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.
Unit für jeden. dann Integrationstest für jede mögliche kombination der Funktionen. Dann Systemtest schauen ob alles klappt. und dann Kundenakzeptanztest.

**d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?
Der würde nicht reichen weil ja mehrer sachen beteiligt sind wenn man code ändert auch wenn man jetzt was erwartet sollte man noch riochtig testen.
Schreibe deine Analyse in `02_antworten.md`.

---

## Tandem-Aufgabe 👥

**Szenario für zwei Personen:**

Ihr seid das Testteam für eine Schulverwaltungssoftware.
Eure Aufgabe: Erstellt gemeinsam einen Überblick über alle Testmaßnahmen.

- Person A: Entwirft die Unit-Tests und Integrationstests (welche Module, welche Schnittstellen?)
- Person B: Plant den Systemtest und Abnahmetest (welche Szenarien, wer testet?)
- Zusammen: Prüft, ob alle kritischen Funktionen abgedeckt sind

Haltet euer Ergebnis als Tabelle in `02_antworten.md` fest.

**Erkläre deinem Tandempartner:** Warum bauen Teststufen aufeinander auf und warum kann man nicht direkt mit dem Systemtest oder Abnahmetest starten? Dein Tandempartner hält dagegen und ihr diskutiert 2–3 Minuten.

TeststufeZuständigBeispieleUnit-Test (A)EntwicklerNotenverwaltung: Note wird korrekt gespeichert; Benutzerverwaltung: Login gibt richtigen Nutzer zurück; Stundenplan: Fach wird korrekt eingetragenIntegrationstest (A)EntwicklerNotenverwaltung + Benutzerverwaltung: Nur eingeloggte Lehrer können Noten eintragen; Stundenplan + Benutzerverwaltung: Schüler sieht nur seinen eigenen PlanSystemtest (B)QA/TestteamKompletter Ablauf: Lehrer loggt ein, trägt Noten ein, Schüler sieht Ergebnis; Fehlerfälle: Falsches Passwort, fehlende PflichtfelderAbnahmetest (B)Schulleitung/LehrerSchule testet reale Szenarien aus dem Alltag; Prüfung ob alle Anforderungen erfüllt sind

---

## Active Recall – Mini-Quiz 🧠

*Beantworte diese Fragen aus dem Gedächtnis (Unterlagen geschlossen):*

1. Auf welcher Teststufe werden Schnittstellen zwischen Modulen getestet? Integrationstest
2. Wer führt typischerweise den Abnahmetest durch? Der Kunde
3. Was ist der Unterschied zwischen einem Systemtest und einem Abnahmetest? System das machen wir nochmal und abnahme macht der Kunde
4. Nenne ein Beispiel für einen nicht-funktionalen Test. ob ne seite schneller lädt als lichtgeschwindigkeit
5. Wann werden Regressionstests eingesetzt? wenn sich code verändert
---

## Reflexion 🚦

- [ X] 🟢 Ich kann alle Teststufen erklären und anwenden
- [ ] 🟡 Ich verstehe das Konzept, aber die Abgrenzung ist noch nicht ganz klar
- [ ] 🔴 Ich brauche noch Unterstützung

**Was nimmst du mit?**

> ________________________KI_______________________

---

*Bei Problemen → [Stuck Protocol](../stuck_protocol.md)*
