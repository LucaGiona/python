age = int(input("Give age: "))

if 18 <= age <=65:
 print("You can apply")
 if age > 50:
  print("Yo can apply for senior role")
 else:
  print ("you can apply for a junior role")

else:
 print("You are too young")