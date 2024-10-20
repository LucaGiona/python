from math import sqrt

while True:
    number = float(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    elif number > 0:
        number_sqrt= sqrt(number)
        print(number_sqrt)
    else:
        break
print("Exiting...")

print("Countdown!")
number = 5
while True:
    print(number)
    number = number - 1
    if number <= 0:
        break

print("Now!")
