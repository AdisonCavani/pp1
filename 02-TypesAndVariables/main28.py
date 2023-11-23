height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

bmi = round(weight / pow(height, 2) * 10000, 1)

print(f"Your BMI index: {bmi}")
print(f"Correct weight: {bmi > 18.5 and bmi < 25}")