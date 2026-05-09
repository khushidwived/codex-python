"""
Write a function that takes three numbers as parameters and prints
the largest among them.
Three numbers are different
"""

def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("num1")
        print(f"{num1} is the largest")
    elif num2 > num1 and num2 > num3:
        print("num2")
        print(f"{num2} is the largest")
    else:
        print("num3")
        print(f"{num3} is the largest")


largest(2, 2, 2)
