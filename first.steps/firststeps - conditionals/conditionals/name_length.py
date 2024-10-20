first_name = input("Enter your first name:")
last_name = input("Enter your last name: ")

name_lenght = len(first_name) + len(last_name)
if name_lenght == 12:
  print("Exactly Average!")
elif name_lenght < 12:
  print("Shorter than average")
else: 
  print("longer than average!")