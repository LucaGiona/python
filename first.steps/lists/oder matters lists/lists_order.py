def add_twice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    return lst

print("Hello:", add_twice("hi", [1,2,3]))

print(add_twice("Hello"))
print(add_twice("Hi"))

#es werden die Argumente addiert
# um dies zu verhindern mit einem Default arbeiten

def add_twice_two(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst
print(add_twice_two("Hello"))
print(add_twice_two("Hi"))