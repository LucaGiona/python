

# Unit Testing in einem Ordner

Dieses Beispiel zeigt die Struktur und Ausführung von Unit-Tests, die in einem separaten Ordner (`test/`) gespeichert sind. Die Tests verwenden **pytest** zur Überprüfung der Funktionen im Hauptprojekt.

## Verzeichnisstruktur

- **main_project/**: Enthält den Hauptcode des Projekts.
- **test/**: Enthält die Testdateien und die Datei `__init__.py` zur Erkennung als Modul.

Beispiel:
```
unit_testing_project/
├── main_project/
│   └── hello.py             # Hauptdatei mit der Funktion 'hello'
└── test/
    ├── __init__.py          # Initialisiert den 'test'-Ordner als Modul
    └── test_hello.py        # Testdatei für Funktionen in 'hello.py'
```

## Voraussetzungen

Stellen Sie sicher, dass **pytest** installiert ist:
```bash
pip install pytest
```

## Tests schreiben

Die Testdateien werden im `test/`-Ordner abgelegt. Beispielsweise enthält `test/test_hello.py` Unit-Tests für die `hello`-Funktion.

Beispiel für eine Testdatei (`test_hello.py`):

```python
from main_project.hello import hello

def test_hello():
    assert hello("World") == "Hello, World!"
```

## Tests ausführen

Um die Tests im `test`-Ordner auszuführen, verwenden Sie den folgenden Befehl im Hauptverzeichnis:

```bash
pytest test/
```

## Beispielausgabe

Bei erfolgreicher Ausführung erhalten Sie eine Zusammenfassung wie:

```
============================= test session starts =============================
collected 1 item

test/test_hello.py .                                                  [100%]

============================== 1 passed in 0.01s ==============================
```

Alle Tests im `test/`-Ordner werden so ausgeführt und in der Ausgabe angezeigt.