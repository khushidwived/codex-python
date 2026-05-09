"""
Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.
"""

my_list1 = [4, 6, 8, 1, 2, 2, 10]
my_list2= [4, 6, 1, 2]
result=[]

for num in my_list1:
    if num in my_list2:
        if num not in result:
            result.append(num)
print(result)
