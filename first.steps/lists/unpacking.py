user = ["Joe", "Bucky", 42]
first, last , age = user
print(first)
print(age)

item = [4, "Pizza", "Plain", 15.90]
quantity, *others, price = item

print(price)
print(others)

#copy
item2 = item.copy()
item3 = item[:]
print(item)
print(item2)
print(item3)

