
# Calculator Tests with Pytest

Dieses Beispiel testet eine `square`-Funktion, die eine Zahl quadriert. Die Tests werden mit **pytest** ausgeführt, um sicherzustellen, dass die Funktion für positive, negative und null Werte korrekt funktioniert.

## Voraussetzungen

Stellen Sie sicher, dass **pytest** installiert ist:
```bash
pip install pytest
```

## Projektstruktur

- **calculator.py**: Enthält die Funktion `square`, die eine Zahl quadriert.
- **test_calculator.py**: Enthält die Testfälle für die Funktion `square`.

## Tests

Die Testfälle überprüfen folgende Szenarien:

1. **Positive Zahlen**: Überprüft, ob `square` die Quadrate positiver Zahlen korrekt berechnet.
2. **Negative Zahlen**: Stellt sicher, dass `square` die Quadrate negativer Zahlen korrekt berechnet.
3. **Null**: Stellt sicher, dass `square` bei der Eingabe `0` ebenfalls `0` zurückgibt.

## Testausführung

Führen Sie die Tests mit folgendem Befehl aus:
```bash
pytest test_calculator.py
```

## Beispielausgabe

Bei erfolgreichem Testlauf gibt pytest eine Zusammenfassung wie folgt aus:

```
============================= test session starts =============================
collected 3 items

test_calculator.py ...                                                    [100%]

============================== 3 passed in 0.03s ==============================
```

Alle Tests sollten grün sein, wenn die Funktion korrekt funktioniert.