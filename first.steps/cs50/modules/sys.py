import sys

# if len(sys.argv) < 2:
#     sys.exit("Toofew arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too many arguments")

#introducing slice

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)