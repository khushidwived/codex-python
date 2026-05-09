"""
Write a Python program to swap the values of two variables without using a temporary variable.
"""

# Input values
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping logic (without temp variable)
a, b = b, a

# Output the result
print("After swapping:")
print("a =", a)
print("b =", b)