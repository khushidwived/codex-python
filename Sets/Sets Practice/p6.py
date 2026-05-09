"""
Write a Python program to check if two given sets have no elements
in common.
"""

set1 = {2, 5, 6, 1, "code", 7}
set2 = {9, 1, 3, 8, "python"}

result = set1.intersection(set2)

if len(result) == 0:
    print("Both sets have nothing in common")
else:
    print("Both sets have something in common")
    print(result)

