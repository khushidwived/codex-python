"""
Ask the user for a number. Then, from a list of numbers, remove all the numbers
that can be divided by the number the user entered.
"""

numbers = [12, 15, 20, 33, 40, 42, 55, 60]
result = []

n = int(input("Enter a number: "))

for num in numbers:
    if num % n != 0:     
        result.append(num)

print("Original list:", numbers)
print("Updated list:", result)
