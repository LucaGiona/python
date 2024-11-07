# try:
#     x = int(input("What's x ? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not a integer")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x ? "))
#         #print(f"x is {x}")
#     except ValueError:
#         print("x is not a integer")
#     #else is braking out of the loop
#     else:
#         break
# print(f"x is {x}")

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass
           # print("x is not a integer")
        # else:
        #    return x
       

main()