print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let`s play")
score = 0

answer = input("What does CPU stand for?")

if answer == "central proccessing unit":
    print("Correct")
    score +=1
else: 
    print("incorrect")

answer = input("What does CPU stand for?")

if answer == "central proccessing unit":
    print("Correct")
    score +=1
else: 
    print("incorrect")
answer = input("What does CPU stand for?")

if answer == "central proccessing unit":
    print("Correct")
    score +=1
else: 
    print("incorrect")

print("You got " + str(score) + " points")

#prozente ausrechnen