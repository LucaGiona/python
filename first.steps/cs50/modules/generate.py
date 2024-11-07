import random

from random import choice
from random import randint

coin = choice(["heads", "tails"])
print(coin)

number = randint(1,33)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)