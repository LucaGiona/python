
**[English Version Below](#english-version)**
# Swim Coach Time Tracker



Ein Schwimmtrainer stoppt regelmäßig die Zeiten seiner Schwimmer (Kinder/Teilnehmer) und notiert diese zunächst auf einem Klemmbrett. Später gibt er diese Zeiten manuell in Excel ein, um sie als kleine Datensätze zu speichern. Er benennt die Dateien dabei nach dem Format **`Name-Alter-Distanz_Art.xls`** und berechnet den Durchschnitt der Zeiten für jeden Schwimmer und jede Disziplin.

### Dateinamen-Format

Die Datei wird nach dem Muster **`Name-Alter-Distanz_Art`** benannt, um eine einheitliche und leicht verständliche Struktur zu haben. Hier ein Beispiel:

- **Beispiel**: `Darius-13-100m-Fly.txt`

  - **Name**: Der Name des Schwimmers (z. B. „Darius“).
  - **Alter**: Das Alter des Schwimmers (z. B. „13“).
  - **Distanz**: Die Schwimmstrecke in Metern (z. B. „100m“).
  - **Art**: Der Schwimmstil (z. B. „Fly“ für Schmetterling).

### Projektziel

Nun hat der Trainer eine neue Stoppuhr, die die Zeiten direkt als CSV-Datei speichert und als `.txt` exportiert. Unsere Aufgabe besteht darin, ihm ein Tool zu entwickeln, das:

1. Ihm schnellen Zugriff auf seine Daten gibt,
2. die Daten in einem einheitlichen Format speichert,
3. die Pflege und Verwaltung der Zeiten erleichtert.

Mit dieser Lösung kann der Trainer die Zeiten seiner Teilnehmer einfacher verwalten und muss sich nicht mehr um die manuelle Berechnung des Durchschnitts kümmern.

---

## English Version

A swimming coach regularly times his swimmers (children/participants) and initially notes these times on a clipboard. Later, he manually enters these times into Excel to create small datasets for each swimmer and event. He names the files using the format **`Name-Age-Distance_Style.xls`** and calculates the average time for each swimmer and discipline.

### File Naming Format

The file is named according to the pattern **`Name-Age-Distance_Style`** for a consistent and clear structure. Here’s an example:

- **Example**: `Darius-13-100m-Fly.txt`

  - **Name**: The swimmer's name (e.g., "Darius").
  - **Age**: The swimmer's age (e.g., "13").
  - **Distance**: The swimming distance in meters (e.g., "100m").
  - **Style**: The swimming style (e.g., "Fly" for butterfly).

### Project Goal

Now, the coach has a new stopwatch that saves times directly as a CSV file and exports them as `.txt`. Our task is to build a tool that:

1. Provides quick access to his data,
2. Stores the data in a consistent format,
3. Simplifies the tracking and management of times.

With this solution, the coach can manage his participants' times more easily and no longer needs to manually calculate averages.

---
