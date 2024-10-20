press_release = """

Doody Calls, a nationwide leader in dog poop removal services, is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. Doody Calls currently cleans up dog poop in over 57 territories across 23 states and has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# Remove the leading and trailing whitespace (new lines) from press_release

release_one = press_release.strip().replace("dog poop", "pet waste").replace("Doody Calls", "DoodyCalls")

# Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet waste" tests better than "dog poop"
print(release_one)

# We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)

print("-------------------------------")

# Our research shows that it's best to shout our press releases. Make the entire press release uppercased!
release_two = release_one.upper()

# 
print(release_two)

print("-------------------------------------------")
print("-------------------------------------------")

age = int(input("How old are you?"))

if age >= 16:
 print("Come in")
 print("########")
print("Hell yeah!")
