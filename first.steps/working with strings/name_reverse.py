input_string = input("Please type in a string: ")
index = -1
while index >=  (len(input_string)*-1):
    print(input_string[index])
    index -= 1

width = int(input("Width: "))
height = int(input("Height: "))
 
n = 0
while n < height:
    print("#" * width)
    n += 1