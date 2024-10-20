# attempts = 0

# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1

#     if code == "1234":
#         success = True
#         break
#     if attempts == 3:
#         success = False
#         break
#     print("Incorrect... try again")

# if success:
#     print("Correct PIN entered!")
# else:
#     print("Too many attempts...")

# Write your solution here
attempts = 0
correct_pin = 4321



while True:
    pin = int(input("PIN: "))
    attempts += 1
 
    if pin == correct_pin and attempts == 1: 
        print("Correct! It only took you one single attempt!")
        break

    elif pin == correct_pin:
        print(f"Correct! It took you {attempts} attempts")
        break

    elif pin != correct_pin:
        print("Wrong!")
     
