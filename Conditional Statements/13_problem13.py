"""
Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary = float(input("Enter the current salary of the employee: "))

if salary < 10000:
    increment = salary * 0.05
elif salary <= 20000:
    increment = salary * 0.10
elif salary <= 50000:
    increment = salary * 0.15
else:
    increment = salary * 0.20

new_salary = salary + increment

print(f"Original Salary: ₹{salary:.2f}")
print(f"Increment Amount: ₹{increment:.2f}")
print(f"Updated Salary: ₹{new_salary:.2f}")
