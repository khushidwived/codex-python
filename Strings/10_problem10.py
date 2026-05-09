"""
Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you"
"""

def camel_to_snake(name):
    snake = ""
    for char in name:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

# Example
camel = "helloWorldHowAreYou"
snake = camel_to_snake(camel)
print(snake)