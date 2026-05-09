"""
Ask a string from user. Count the number of uppercase and lowercase characters in that String.
"""


text = input("Enter a string: ")

# Initialize counters
upper_count = 0
lower_count = 0

# Loop through each character
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)