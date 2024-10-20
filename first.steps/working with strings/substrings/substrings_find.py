# Write your solution here

string = input("Please type in a word: ")
character = input("Please type in a character: ")

index = string.find(character)


if index !=-1 and index + 2 < len(string):
    print(string[index:index + 3])
      
    
       