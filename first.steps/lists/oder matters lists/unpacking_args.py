def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)

print(average(1,2,3,4,5,6))