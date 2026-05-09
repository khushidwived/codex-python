"""
Given two lists a, b. Check if two lists have at least one element
common in them.
"""

lst1 = {2, 6, "PyTorch", 5, "intensity coding"}
lst2 = {"PyTorch", 2, 5, "intensity coding"}

print(set(lst1) & set(lst2))

# set1 = set(lst1)
# set2 = set(lst2)

# print(set1.intersection(set2))
# print(set1 & set2)
