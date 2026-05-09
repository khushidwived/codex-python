"""
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.

# Example 1
my_string= "hello world"

# Output
World Hello


# Example 2
my_string= "python is good"

# Output
Good Is Python
"""

# # Example 1
# my_string= "hello world"

# # Method 1
# # Program to capitalize first letter of each word and reverse the order
# my_string = input("Enter a string: ")

# capitalized = my_string.title()
# words = capitalized.split()
# reversed_words = " ".join(reversed(words))

# print(reversed_words)



# # Method 2

# my_string = input("Enter a string: ")

# # Split, reverse, and capitalize
# words = my_string.split()
# reversed_words = [word.capitalize() for word in reversed(words)]
# result = " ".join(reversed_words)

# print(result)



# Example 2
my_string= "python is good"
words = my_string.split()

result = " ".join(i.capitalize() for i in words)
print(result)