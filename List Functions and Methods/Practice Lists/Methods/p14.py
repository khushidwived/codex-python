"""
Write a program to split a given list into two halves.
"""

my_list = [1, 2, 3, 4, 5, 6]

# Find the middle index
mid = len(my_list) // 2

# Split the list
first_half = my_list[:mid]
second_half = my_list[mid:]

print("First half:", first_half)
print("Second half:", second_half)

#####
