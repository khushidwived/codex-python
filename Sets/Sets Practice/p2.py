"""
Python program to find common elements in three lists using sets.
"""

lst1 = {2, 6, "PyTorch", 5, "intensity coding"}
lst2 = {"PyTorch", 2, 5, "intensity coding"}
lst3 = {1, 2, "PyTorch", 2, 8, "intensity coding"}

print(set(lst1) & set(lst2) & set(lst3))

# set1=set(lst1) 
# set2=set(lst2)
# set3=set(lst3)

# x = set1.intersection(set2)
# result= x.intersection(set3)
# print(result)

