import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"uhu": row["name"], "home": row["home"], "house": row["house"], "year": row["year"]})

for student in sorted(students, key=lambda student: student["uhu"]):
    print(f"{student['uhu']} is from {student['home']}. The house is {student["house"]}, built in the {student["year"]}")


