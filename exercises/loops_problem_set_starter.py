
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

for char in word:
    print(char)

print("*" * 20)
# Write a while loop that does the same thing!
index = 0
while index < len(word):
    print(word[index])
    index+= 1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
num = 100
while num <= 140:
    print(num)
    num += 2


print("-" * 10)



# Write a for loop that does the same thing (with range())

for num in range(100, 142, 2):
    print(num)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

password = input("Password required: ")
while password != "sillygoose":
    password = input("Password required: ")