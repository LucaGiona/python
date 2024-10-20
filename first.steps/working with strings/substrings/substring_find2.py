string = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index != -1:
    index = string.find(character, index)
    
    if index != -1:
        # Überprüfen, ob mindestens zwei Zeichen nach dem gefundenen vorhanden sind
        if index + 2 < len(string):
            print(string[index:index + 3])
        else:
            # Wenn weniger als zwei Zeichen übrig sind, gibt nur den Rest aus
            print(string[index:])
        
        index += 1  # Starte die nächste Suche nach dem gefundenen Zeichen

word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1