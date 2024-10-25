# solution for real passing function see passing_function2.py 
#this here works as well, but it is not  passing functions

def input_from_user():
    exam_total = 0
    exercise_total =0
    count = 0
    passed_count = 0
    grades = [0,0,0,0,0,0]

    while True:
        # Eingabe des Benutzers
        user_input = input("Exam points and exercises completed: ")

        if user_input.strip() == "":
            statistic = "Statistic:"
            print(statistic)
         

            if count > 0:
                exam_average = exam_total / count
                exer_average = exercise_total/count
                overall = (exam_average+ exer_average) / 2
                pass_percentage = (passed_count / count) * 100
                
                print(f"Ponints average: {overall:.1f}")
                print(f"Pass percentage: {pass_percentage:.1f}")
                print(f"Grade distribution:")

                for grade in range(5, -1, -1):
                    stars = "*" * grades[grade]
                    print(f" {grade}: {stars}")
                
            break   
                



        exam, exer = user_input.split()
        exam = int(exam)
        exer = int(exer)

      
        exer_points = exer // 10
        total_points = exam + exer_points

        if exam < 10:
            grade = 0  # Automatisch durchgefallen
        elif total_points <= 14:
            grade = 0
        elif total_points <= 17:
            grade = 1
        elif total_points <= 20:
            grade = 2
        elif total_points <= 23:
            grade = 3
        elif total_points <= 27:
            grade = 4
        else:
            grade = 5

        grades[grade] += 1

        if grade > 0:
            passed_count += 1

        exam_total += exam
        exercise_total += exer_points
        count += 1




# Aufruf der Funktion
input_from_user()
