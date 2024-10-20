# https://plum-poppy-0ea.notion.site/BMI-Exercise-82a2fd55bca7481f9957fd06e2e5d451

user_height = float(input("What is you height?"))
user_weight = float(input('What is your weight?'))

bmi = (user_weight * 703) / ( user_height **2)
bmi = round(bmi, 2)

if bmi < 16.0:
    category = "Severly Underweight"
elif 16.0 <= bmi <= 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 29.9:
    category = "normal"
elif 30 <= bmi <= 34.9:
    category = "overweight"
else:
    category = "Morbidly Obese"

print(f"Your bmi is : {bmi} Your are {category}")