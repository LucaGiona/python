# Write your solution here
password = input("Password: ")
repeat = input("Repeat password: ")

while True:
    if password != repeat:
        print("They do not match")
        
    else:
        
        print("User account created!")
        break