"""
Write a program to print the last digit of a number.

Example 1
Input: 45321
Output: 1
Example 2
Input: 459094
Output: 4
"""

num=int(input("Enter a number = "))
last_digit=num%10
print(f"The last digit of {num} is = {last_digit}")