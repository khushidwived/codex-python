"""
Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1.
"""
my_list = [4, 6, 23, 27, 4, 11, 93.98, 2]

value = int(input("Enter a value = "))

if value in my_list:
    index = my_list.index(value)
    print(f"index = {index}")
else:
    print(-1)