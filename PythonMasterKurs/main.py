def greeting(first_name, last_name, academic_title=""):
    if academic_title !="":
        academic_title += " "

    print("Hallo " + academic_title + first_name + " " + last_name)
    print("Herzlich Willkomen!")

greeting("Max", "Mustermann", "Dr.")