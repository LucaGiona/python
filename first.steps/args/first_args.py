def count_stuff(*args):
    print(f"You passed me {len(args)} arguments")



def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum(1,2,3,4,5,6))


#def silly(first, second, * others)
