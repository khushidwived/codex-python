"""
Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string.
"""

s = input("Enter a string: ")

alphabets = digits = spaces = symbols = 0

for ch in s:
    if ch.isalpha():         # check if alphabet
        alphabets += 1
    elif ch.isdigit():       # check if digit
        digits += 1
    elif ch.isspace():       # check if space
        spaces += 1
    else:                    # everything else is symbol
        symbols += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Symbols:", symbols)