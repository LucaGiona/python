from random import randint
num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))

#q quit

#random number for n dices

# for outer in  range(1,5):
#     print(outer)
#     for inner in range(1,5):
#         print("\t", inner)



while True:
    result = "|"
    for die in range(num_dice):
        rand = randint(1, num_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        break