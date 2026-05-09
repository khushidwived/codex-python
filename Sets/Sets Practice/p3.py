"""
Create 3 sets of your own, find the union of three sets.
"""

lst1 = {2, 6, "PyTorch", 5, "intensity coding"}
lst2 = {"PyTorch", 2, 5, "intensity coding"}
lst3 = {1, 2, "PyTorch", 2, 8, "intensity coding"}

# print(set(lst1) | set(lst2) | set(lst3))

set1=set(lst1) 
set2=set(lst2)
set3=set(lst3)

x = set1.union(set2)
result= x.union(set3)
print(result)
