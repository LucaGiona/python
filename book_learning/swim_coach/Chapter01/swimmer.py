import statistics

FN = "Darius-13-100m-Fly.txt"
FOLDER="../download-swim-data/swimdata/"


with open(FOLDER + FN) as file:
    lines = file.readlines()

swimmer, age, distance, stroke = FN.removesuffix('.txt').split("-")

times= lines[0].strip().split(",")
first = times[0]
minutes, rest = first.split(":")
seconds, hunderths = rest.split(".")
converted_time = (int(minutes) *60*100) + (int(seconds)* 100) + int(hunderths)

converts = []
for t in times:
    minutes, rest = t.split(":")
    seconds, hunderths = rest.split(".")
    converts.append(converted_time)

average_hs = statistics.mean(converts)
min_secs, hunderths = str(round(average_hs / 100 ,2)).split(".")
minutes = int(min_secs) // 60
seconds = int(min_secs) - minutes*60
average = str(minutes) + ":" + str(seconds) + "." + hunderths

print("Name: ",swimmer)
print("Age: ", age)
print("Distance: ", distance)
print("Stroke: " ,stroke)
print("All Times:",times)
print("Average", average)

