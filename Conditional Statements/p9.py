"""
Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
- Underweight: BMI less than 18.5
- Normal weight: BMI 18.5 - 24.9
- Overweight: BMI 25 - 29.9
- Obesity: BMI 30 or greater
"""

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")
elif 25 <= bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
