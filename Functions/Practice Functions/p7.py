"""
write a function that takes a string and prints whether it is a 
palindrome.

abccba
mom
"""

def check_palindrome(string):
    if string ==string[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")


check_palindrome("pop")
check_palindrome("python")