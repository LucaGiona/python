from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move

if num == 1:
   pc_move = "rock"
   pc_ascii = rock
elif num == 2:
    pc_move = "paper"
    pc_ascii = paper
elif num == 3:
    pc_move = "scissors"  
    pc_ascii = scissors  

# Ask a user to enter their move

user_input = input("Choose between rock, paper and scissors - take the shorts r, p, s ! \n Your move is: ").lower()

if user_input == "r":
    user_move = "rock"
    user_ascii = rock
    
elif user_input == "p":
    user_move = "paper"
    user_ascii = paper
 
elif user_input == "s":
    user_move = "scissors"
    user_ascii = scissors

else:
    print("Choose propper input see above")
    exit()
    


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("COMPUTER:\n ", pc_ascii)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("YOU: \n",user_ascii)

# Figure out who wins and print the result!
# wenn 

if user_move == pc_move:
    print("It' s a tie !!!")
elif (user_move == "rock"  and pc_move=="scissors") or \
     (user_move == "paper" and pc_move=="rock") or \
     (user_move == "scissors" and pc_move=="paper"):
    print("you WIN !!")
else:
    print("You LOOSE !!!")