"""
Title, Capitalized, upper, lower, swapcase
isupper, islower, isalpha, isalnum, isspace
"""

# a = "ANIRUDH"
# # x = a.isupper()
# x = a.islower()
# x = a.isalpha()
# x = a.isalnum()
# x = a.isdigit()
# x = a.isspace()
# print(x)

# a = "anirudh123"
a = "123456"

if a.isdigit():
    a = int(a)
    print(a, type(a))
else:
    print("cannot be converted to integer")