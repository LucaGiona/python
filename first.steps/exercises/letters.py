# Write your solution here

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

#middle_letter 1

if letter2 < letter1 < letter3 or letter2 > letter1 > letter3:
    print(f"The letter in the middle is {letter1}")

elif letter1 < letter2 < letter3 or letter1 > letter2 > letter3:
    print(f"The letter in the middle is {letter2}")

else:
    print(f"The letter in the middle is {letter3}")



value = int(input("Value of gift: "))
 
if value < 5000:
    tax = 0
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.10
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
else:
    tax = 142100 + (value - 1000000) * 0.17
 
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")