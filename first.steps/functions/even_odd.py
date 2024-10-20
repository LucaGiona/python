def num(am):
    if am % 2 == 0:
        print("even")
    else:
        print("odd")

num(4)
num(5)

def num2(num):
    return num %2 == 0

print(num2(2))
print(num2(5))

def slugify(phrase):
    return phrase.lower().strip().replace(" ", "-")

print(slugify("I love you     and so on    GO FOR IT YOU   will do it"))

def count_vowels(string):
    count = 0
    for char in string:
        if char in "aeiou":
            count +=1
    return count

print(count_vowels("happy"))