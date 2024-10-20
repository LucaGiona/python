# Write your solution here
limit = int(input("Limit: "))
sum_of_numbers = 0  # Variable zum Speichern der laufenden Summe
result_str = ""  # Variable zum Speichern der Zahlen als String

for number in range(1, limit + 1):  
    if sum_of_numbers + number == limit:
        sum_of_numbers += number  
        if number == 1:
            result_str += f"{number}"  
        else:
            result_str += f" + {number}"  
        break  
    elif sum_of_numbers + number > limit:
        sum_of_numbers += number
        result_str += f" + {number}"
        break  
    else:
        sum_of_numbers += number  
        if number == 1:
            result_str += f"{number}"
        else:
            result_str += f" + {number}"


print(f"The consecutive sum: {result_str} = {sum_of_numbers}")
