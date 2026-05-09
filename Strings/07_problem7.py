"""
Write a program to reverse the order of words

# Example 1
my_string= "hello world"

# Output
world hello


# Example 2
my_string= "python is good"

# Output
good is python

"""

# # Example 1
# my_string = "hello world"

# # Split the string into words
# words = my_string.split()

# # Reverse the list of words
# reversed_words = words[::-1]

# # Join the reversed words back into a string
# reversed_string = " ".join(reversed_words)

# print("Original String:", my_string)
# print("Reversed Order of Words:", reversed_string)



# Example 2
my_string = "python is good"

reversed_string = " ".join(my_string.split()[::-1])
print(reversed_string)