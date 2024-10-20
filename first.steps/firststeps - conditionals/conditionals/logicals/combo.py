# oder of conditons (see also doc on python.org ---- #NOT # and # or)

day = "Tuesday"
is_vet = False
age = 56

#Veterans are going in free on Tuesdays
#Infants under 2 get in for free always



if age <= 2 or is_vet and day == "Tuesday":
    print("You are entering for free")
else: 
    print("you have to pay!")