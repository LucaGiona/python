### Aufgaben / Challenges

###### 1. Daten aus Dateinamen extrahieren

![bsp Bild](datei-foto-bsp-swimCoach.gif)


````
fn = "Darius-13-100m-Fly.txt"

swimmer, age, distance, stroke = fn.removesuffix('.txt').split("-")

print(swimmer)
print(age)
print(distance)
print(stroke)

````
##### 2. Daten in der Datei verarbieten

