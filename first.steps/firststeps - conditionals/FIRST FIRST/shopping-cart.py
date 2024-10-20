print("WELCOME TO OUR USELESS STORE !")
print("******************************")

purchase = input("what item are you purchasing? ")
price = float(input(f"what is the price of {purchase}?"))
quantity = int(input(f'how many {purchase} are you buying? '))

total_price = quantity * price

print(f"Added {quantity} {purchase}(s) to shopping cart")
print(f"Subtotal: ${price:.2f}")


