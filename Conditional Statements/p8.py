"""
Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7.
"""

age = int(input("Enter your age: "))

if age < 12:
    price = 5
elif age <= 65:
    price = 10
else:
    price = 7

print(f"The ticket price is ${price}.")
