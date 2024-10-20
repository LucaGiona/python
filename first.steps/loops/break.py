# for letter in "supermancgoeswild":
#     if letter == "c":
#         break
#     print(letter)

message = input("say hi; ")
while True:
    if message == "Hi":
        break
    message = input("say hi; ")

for char in "fatcat":
    if char == "a":
        continue
    print(char)

print("After loop")