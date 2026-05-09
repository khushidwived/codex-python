"""
Write a Python program to calculate the compound interest for a given principal, rate of interest, and 
time period. Ask everything from the user.
"""

# Compound Interest Calculator

# Taking inputs from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Formula for compound interest: A = P * (1 + R/(100*n))**(n*T)
amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal


print("\nCompound Interest Calculation")
print(f"Principal Amount: ₹{principal}")
print(f"Rate of Interest: {rate}%")
print(f"Time Period: {time} years")
print(f"Compounded {n} times per year")
print(f"Compound Interest: ₹{compound_interest:.2f}")
print(f"Total Amount after {time} years: ₹{amount:.2f}")