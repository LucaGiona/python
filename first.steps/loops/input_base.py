limit = int(input("Upper limit: "))
power = 1
base = int(input("Base: "))


for number in range(limit):  
    if power <= limit:
        print(power)
    power = power * base

