"""
Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are different.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a!=b and b!=c and a!=c:
    if a>b:
        if a>c:
            print(f"{a} is the largest number.")
        else:
            print(f"{c} is the largest number.")
    else:
        if b>c:
            print(f"{b} is the largest number.")
        else:
            print(f"{c} is the largest number.")
else:
    print("Please enter three different numbers.")


