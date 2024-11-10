import os
import statistics

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
converts= []
for t in times:
        minutes, rest = t.split(":")
        seconds, hunderths = rest.split(".")
        converted_time = (int(minutes)*60*100) + (int(seconds)*100) + int(hunderths)
        converts.append(converted_time)
        # can be refracturated !!
        print(t)
        print(converted_time)
print("Converts: ", converts)

average = statistics.mean(converts)
print("Average: ", average)

# average = round(average / 100 , 2)
# print("Rounded Average: ", average)

min_sec, hunderths = str(round(average / 100, 2)).split(".")
print("Splited:", min_sec)

minutes = int(min_sec)//60
print("Minutes: ", minutes)
seconds = int(min_sec) - minutes*60
print(seconds)

print("_______________________-")
print(minutes, seconds, hunderths)

average = str(minutes) + ":" + str(seconds) + "." + hunderths

print("Average: ", average)