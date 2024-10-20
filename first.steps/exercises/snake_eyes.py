import random

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll_count = 1

# while roll1 !=1 or roll2 != 1:
#     print(roll1, roll2)
#     roll1 = random.randint( 1, 6)
#     roll2 = random.randint( 1, 6)
#     roll_count += 1

# print(roll1, roll2)
# print("Yeah snake eyes")
# print(f"it took {roll_count} rolls")

# import random

# roll1 = random.randint(1, 6)
# roll2 = random.randint(1, 6)
# roll_count = 1

while (roll1 !=1 and roll1 !=2 and roll1 !=3) or roll2 != 1:
    print(roll1, roll2)
    roll1 = random.randint( 1, 6)
    roll2 = random.randint( 1, 6)
    roll_count += 1

print(roll1, roll2)
print("Yeah snake eyes")
print(f"it took {roll_count} rolls")

