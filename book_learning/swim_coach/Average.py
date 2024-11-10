import os

# Pfad zum swimdata-Ordner
FOLDER = "Data-from-Coach/download-swim-data/swimdata/"

# Dateien auflisten
#for filename in os.listdir(FOLDER):
#    print(filename)

# for item in folder_path.iterdir():
#     print(item)  # Listet alle Dateien und Ordner im Verzeichnis auf

#hier nur Darius da er Hard gecodet ist
FN = "Darius-13-100m-Fly.txt"
with open(FOLDER + FN) as file:
    lines = file.readlines()

print("Lines:", lines)

times = lines[0].strip().split(",")
print(times)

first = times[0]
print(first)

minutes, rest = first.split(":")
print(minutes)
print(rest)

seconds, hunderth = rest.split(".")
print(seconds)
print(hunderth)

converted_time = (int(minutes)* (60*100)) + (int(seconds) * 100) +int(hunderth)
print(converted_time)

print("---------------------------------")
for t in times:
        minutes, rest = t.split(":")
        seconds, hunderths = rest.split(".")
        converted_time = (int(minutes)*60*100) + (int(seconds)*100) + int(hunderths)
        
        print(t)
        print(converted_time)