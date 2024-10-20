tweet = input("enter your tweet: ")
char = len(tweet)
if char >= 140:
 print(f"Your {char} char is {char -140} chars too long")
else:
  print(f"That {char} tweet will work!")


print("hallo!")