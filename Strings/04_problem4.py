"""
Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and
don’t change the other letters.
"""


text = input("Enter a string: ")

# empty string to store result
result = ""

# loop through each character
for ch in text:
    if ch.islower():       # if character is lowercase
        result += ch.upper()
    elif ch.isupper():     # if character is uppercase
        result += ch.lower()
    else:                  # if character is not a letter (number, space, symbol)
        result += ch

print("Converted string:", result)