# for i in [0, 1, 2]:
#     print("meow")

for _ in range(3):
    print("meow")

#using _ for a variable
print("++++++++++++++++++++++")
print("meow\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in  range (n):
    print("meow", end="Tschüüs\n")

print("#####################\n")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n 

def meow(n):
    for _ in range(n):
        print("meow")

main()
