from random import randint

print("Welcome to the game")

player_one = input("What is your name player 1 ? ")
player_two = input("What is your name player 2 ? ")

toothpicks = int(randint(15, 25))
new_toothpicks = toothpicks
print(f"You start with {toothpicks}: \n {toothpicks * "|"}")

#random number of toothpicks
while True:
   
    take_player_one = int(input(f"How many do you take, {player_one}? \n"))
    if not (1<= take_player_one <=3):
        print("Max allowed sticks are 3")
        continue
    new_toothpicks -= take_player_one
    if new_toothpicks <=0:
        print(f"{player_one} wins!!!")
        break
    print(f"There are {new_toothpicks} left \n{new_toothpicks * "|"}")

    take_player_two = int(input(f"How many do you take, {player_two}? \n"))
    if not (1<= take_player_two <=3):
        print("Max allowed sticks are 3")
        continue
    new_toothpicks -= take_player_two
    if new_toothpicks <=0:
        print(f"{player_two} wins!!!")
        break
    print(f"There are {new_toothpicks} left \n{new_toothpicks * "|"}")

print("Game over")