students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

print(students["Hermione"])

for student in students:
    print(student)

#key iteration

for student in students:
    print(student, students[student], sep=", house:  ")