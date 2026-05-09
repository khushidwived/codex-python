"""
Ask a string from user. Count how many alphabets are there in that string.
"""


string = input("Enter a string: ")

# Initialize counter
count = 0

# Loop through each character
for char in string:
    if char.isalpha():   # Check if character is an alphabet
        count += 1

print("Number of alphabets in the string:", count)