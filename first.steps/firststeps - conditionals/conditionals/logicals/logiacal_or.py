day = input("What day of the week is it? ")

if day == "Saturday" or day ==" Sunday":
    print("It is the weekend!")
else:
    print(" Is a workday!!!")


age = int(input("How old are you?"))

if age < 5 or age >= 65:
    print("You have not to pay")
else:
    print("You have to pay the entry fee")