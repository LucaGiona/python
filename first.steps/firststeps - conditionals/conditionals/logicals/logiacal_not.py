year = input("What year were you born in ?")

if not year.isnumeric():
    year = input("That is not a number: Try again! What year were you born in ?") 

year = int(year)
print(f"You were born {2024 - year} years ago")

