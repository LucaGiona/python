import statistics
FOLDER="../download-swim-data/swimdata/"

def read_swim_data(filename):
    '''
    return data from a file

    name of swimmer in filename -> extracts all the data see below:
     '''
    swimmer, age, distance, stroke = filename.removesuffix('.txt').split("-")

    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times= lines[0].strip().split(",")

    converts = []
    for t in times:
        #Anpassung wenn keine Minuten geschwommen wurden
        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hunderths = rest.split(".")
        else:
            minutes = 0
            seconds, hunderths = t.split(".")

        converted_time = (int(minutes) *60*100) + (int(seconds)* 100) + int(hunderths)
        converts.append(converted_time)

    average_hs = statistics.mean(converts)
    min_secs, hunderths = str(round(average_hs / 100 ,2)).split(".")
    minutes = int(min_secs) // 60
    seconds = int(min_secs) - minutes*60
    average = f"{minutes}:{seconds}.{hunderths}"

    

    return swimmer, age, distance, stroke, times, average


   

