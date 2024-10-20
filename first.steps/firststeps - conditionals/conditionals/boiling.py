unit = input("What unit are you using?")
temp =  int(input("What temperatue is the water?"))

# Kelvin = k Fahrenheit = f Celsius = c

if unit == "f":
    if temp == 212:
        print("Water is boiling")
    else:
        print("Water is not boiling")
elif unit == "c":
    if temp == 100:
        print("Water is boiling")
    else:
        print("Water is not boiling")
elif unit == "k":
    if temp == 373:
        print("Water is boiling")
    else:
        print("Water is not boiling")
else:
    ("Unit not known")