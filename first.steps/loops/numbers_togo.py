print("Please type in integer numbers. Type in 0 to finish")

number_count = 0
number_sum = 0
pos_count = 0
neg_count = 0

while True:
    number_asked = int(input("Number:"))
    if number_asked == 0:
        break

    number_sum += number_asked

    if number_asked > 0:
        pos_count += 1
    if number_asked < 0:
        neg_count += 1

    number_count +=1


mean = number_sum / number_count

print(f"Numbers typed in {number_count}")
print(f"The sum of the numbers is {number_sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos_count}")
print(f"Negative numbers {neg_count}")


