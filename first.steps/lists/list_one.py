waitlist = ["juan", "domingo", "pierrot"]

waitlist.append("colt")

print("1st ",waitlist)

people = ["juan", "domingo", "pierrot"]
waitlist.extend(people)

print("2nd:", waitlist)

waitlist.insert(-1, "Jasmine")
print("3rd", waitlist)

waitlist.append("Jasmine")
print("4th", waitlist)

slice = waitlist[1:3]
print("slice", slice)

pop = waitlist.pop()
print("pop: ", pop)
#in python geht auch pop(index)
pop = waitlist.pop(2)
print("pop2:", pop)

multi = waitlist * 2
print("multi: ", multi)

print(waitlist)


