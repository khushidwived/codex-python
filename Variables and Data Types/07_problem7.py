""" 
Calculate sum of 5 subjects and Find percentage.
"""
# Input marks of 5 subjects
english = float(input("Enter marks of English: "))
math = float(input("Enter marks of Math: "))
science = float(input("Enter marks of Science: "))
social = float(input("Enter marks of Social Science: "))
computer = float(input("Enter marks of Computer: "))

# Calculate sum and percentage
total = english + math + science + social + computer
percentage = (total / 500) * 100

print("Total Marks =", total)
print("Percentage =", percentage, "%")