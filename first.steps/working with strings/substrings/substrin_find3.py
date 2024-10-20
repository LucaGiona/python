string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = 0

# Solange 'find()' das Substring findet, gebe den Index direkt aus
while index != -1:
    index = string.find(substring, index)
    if index != -1:
        print(f"Found at index: {index}")
        index += 1  # Erhöhe den Index, um nach dem nächsten Vorkommen zu suchen




string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = 0
count = 0  # Zähler, um das zweite Vorkommen zu finden

# Schleife, um nach dem Substring zu suchen
while index != -1:
    index = string.find(substring, index)
    if index != -1:
        count += 1  # Erhöhe den Zähler bei jedem Fund
        if count == 2:
            print(f"Second occurrence at index: {index}")
            break  # Beende die Schleife, nachdem der zweite Fund ausgegeben wurde
        index += len(substring)  # Erhöhe den Index, um nach dem nächsten Vorkommen zu suchen


#factorial
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
 
    factorial = 1
    new = 1
    while new <= number:
        factorial *= new
        new += 1
 
    print(f"The factorial of the number {number} is {factorial}")
 
print("Thanks and bye!")