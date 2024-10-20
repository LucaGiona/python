string = input("Please type in a word: ")

for n in range(1, len(string) +1):
    print(string[:n])

string2 = input("Please type in a string: ")

length = len(string2)

for n in range(length, -1, -1):
    print(string2[n:])

