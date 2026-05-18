"""
Baustein 02 – Testarten
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""

from typing import List, Dict


# ============================================================
# Webshop-Komponenten (vereinfacht)
# ============================================================

def berechne_gesamtpreis(artikel: List[Dict], rabatt_prozent: float = 0) -> float:
    """
    Berechnet den Gesamtpreis eines Warenkorbs.

    Args:
        artikel: Liste von Dicts mit 'name', 'preis', 'menge'
        rabatt_prozent: Rabatt in Prozent (0–100)

    Returns:
        Gesamtpreis nach Rabatt, gerundet auf 2 Dezimalstellen.

    Raises:
        ValueError: Wenn rabatt_prozent außerhalb [0, 100] liegt.
    """
    if not 0 <= rabatt_prozent <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt_prozent}")

    summe = sum(a["preis"] * a["menge"] for a in artikel)
    rabatt = summe * (rabatt_prozent / 100)
    return round(summe - rabatt, 2)

warenkorb = [
    {"name": "Apfel", "preis": 0.50, "menge": 4},
    {"name": "Brot",  "preis": 2.00, "menge": 1},
]
ergebnis = berechne_gesamtpreis(warenkorb)
print("Test 1 – Ohne Rabatt:")
print(f"  Erwartet: 4.0  | Erhalten: {ergebnis} | {'OK' if ergebnis == 4.0 else 'FEHLER'}")

# Fall 2: Einkauf mit 10 % Rabatt
ergebnis = berechne_gesamtpreis(warenkorb, rabatt_prozent=10)
print("Test 2 – Mit 10 % Rabatt:")
print(f"  Erwartet: 3.6  | Erhalten: {ergebnis} | {'OK' if ergebnis == 3.6 else 'FEHLER'}")

# Fall 3: Leerer Warenkorb (Sonderfall)
ergebnis = berechne_gesamtpreis([])
print("Test 3 – Leerer Warenkorb:")
print(f"  Erwartet: 0.0  | Erhalten: {ergebnis} | {'OK' if ergebnis == 0.0 else 'FEHLER'}")

def finde_guenstigsten_artikel(artikel: List[Dict]) -> Dict:
    """
    Gibt den Artikel mit dem niedrigsten Einzelpreis zurück.

    Raises:
        ValueError: Wenn die Liste leer ist.
    """
    if not artikel:
        raise ValueError("Warenkorb ist leer.")
    return min(artikel, key=lambda a: a["preis"])


# ============================================================
# Aufgabe 2b) – Manuelle Tests mit print()
# ============================================================

if __name__ == "__main__":
    # Testdaten
    warenkorb_normal = [
        {"name": "USB-Hub", "preis": 29.99, "menge": 1},
        {"name": "Maus", "preis": 19.99, "menge": 2},
    ]

    warenkorb_leer = []

    # TODO: Test 1 – Normaler Einkauf ohne Rabatt
    # Erwartetes Ergebnis: 69.97
    print("Test 1 – Kein Rabatt:")
    # Dein Code hier

    # TODO: Test 2 – Einkauf mit 10 % Rabatt
    # Erwartetes Ergebnis: 62.97
    print("\nTest 2 – 10 % Rabatt:")
    # Dein Code hier

    # TODO: Test 3 – Leerer Warenkorb (Sonderfall)
    # Erwartetes Ergebnis: 0.0 (keine Exception!)
    print("\nTest 3 – Leerer Warenkorb:")
    # Dein Code hier


# ============================================================
# Aufgabe 1 – Tabelle Teststufen (als Kommentar)
# ============================================================

# | Beschreibung                                           | Teststufe |
# |--------------------------------------------------------|-----------|
# | Testet einzelne Funktionen oder Methoden isoliert      | TODO      |
# | Prüft das Zusammenspiel mehrerer Module                | TODO      |
# | Testet das gesamte System gegen die Anforderungen      | TODO      |
# | Auftraggeber prüft, ob seine Anforderungen erfüllt sind| TODO      |
