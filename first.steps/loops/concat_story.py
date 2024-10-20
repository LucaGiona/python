word = ""
last_word = ""

while True:
    user_input = input("Please type in a word: ")
    
    if user_input == "end" or last_word == user_input:
         break
    
    word += user_input + " "
    last_word= user_input
   
print(word)
         


