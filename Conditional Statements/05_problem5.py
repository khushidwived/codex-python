"""
Write a program to check if the number is ODD, EVEN or Equal to Zero.
"""

num=int(input("Enter a number: "))

if num == 0:
    print("The number is equal to Zero.")
elif num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
    