couples = [
    ["Beyonce", "Jay-Z"],
    ["Johnny", "June"],
    ["John", "Yoko"],
    ["Will", "Jada"]
]

print(couples[2][1])

for couple in couples:
    for person in couple:
        print(f"Sending invite to...{person}")

