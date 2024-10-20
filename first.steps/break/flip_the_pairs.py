number = int(input("Please type in a number: "))
i = 1


for i in range(1, number +1, 2):
    if i + 1 <=number:
        print(i + 1)
    print(i)
  

number = int(input("Please type in a number: "))
 
index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2
 
if index <= number:
    print(index)

number = int(input("Please type in a number: "))

i = 1
j = number

while i < j:
        print(i)
        print(j)
        i +=1
        j -=1

if i == j:
        print(i)