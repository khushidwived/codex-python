"""
Write a program to check if the last digit of a number is divisible by 5 or not.
"""
num =int(input("Enter a number:"))
last_digit = num % 10

if last_digit%5==0:
    print("It is divisible by 5")
else:
    print("No")
    