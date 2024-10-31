class Dog:

    species = "canine"

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f"{self.name} says WOOF!")

    def learn_trick(self, *new_trick):
        #hier dopplete iteration da spread opertor gebraucht wird
        for trick in new_trick:
            if trick not in self.tricks:
             self.tricks.append(trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            return trick
        else:
            print(f"Does not know {trick}")
            return ""

elton = Dog("Elton", "Berner", 445646)
elton.learn_trick("sit", "beef")
print(elton.tricks)

print("+++++++++++++++++ \n")

elton.tricks.append("sleep")
print(elton.tricks)

print("+++++++++++++++++ \n")

print(elton.perform_trick("sit"))
print(elton.perform_trick("sleep"))
print(elton.perform_trick("shoot"))

print("+++++++++++++++++ \n")

print(Dog.species)
print(elton.species)