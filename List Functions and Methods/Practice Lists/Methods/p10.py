"""
Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence.
"""

# Original list with numbers and a string
my_list = [4, 1, 23, 27, "code & debug", 4, 4, 1, 1]

# This list will store only unique elements from my_list
result = []

# Loop through each element in my_list
for num in my_list:
    # If the element is not already in result, add it (helps avoid duplicates)
    if num not in result:
        result.append(num)

# Variables to store the element with highest occurrence
highest_occ_element = 0
highest_occurence = 0

# Loop through each unique element
for num in result:
    # Count how many times the element appears in the original list
    c = my_list.count(num)
    
    # Print how many times the element occurs
    print(f"{num} occurs {c} times")
    
    # Check if this element has the highest occurrence so far
    if c > highest_occurence:
        highest_occurence = c
        highest_occ_element = num

# Print the element with the highest occurrence
print(f"Highest occurence element = {highest_occ_element}")
