def divide(a, b):
    return a / b

n = divide(8,4)
print(n)

def multi(a,b):
    if a == 0 or b == 0:
        return "Dont use 0"
    return a*b

res = multi(2, 4)
print(res)
res = multi(0, 4)
print(res)
res = multi(4, 4)
print(res)
res = multi(4, 0)
print(res)
