"""
Create a list and prompt the user for an 'old number' followed by a 'new number.'
If the 'old number' exists in the list, replace it with the 'new number' provided by the user.
"""

my_list = [23, 27, 45, 44, 67, 38, 64, 44]

old = int(input("Enter old number ="))
new = int(input("Enter new number ="))
for i in range(0, len(my_list)):
    if my_list[i] == old:
        my_list[i] = new

print(my_list)
