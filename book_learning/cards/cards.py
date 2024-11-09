import random

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2,3,4,5,6,7,8,9,10]

deck = set()

for suit in suits:
    for card in faces + numbered:
        deck.add((card, "of", suit))

card = random.choice(list(deck))

print(card)
deck.remove(card)
print(len(deck))
print("2", card)
print(type(card))

def draw():
    card= random.choice(list(deck))
    deck.remove(card)
    return card

print(draw())

