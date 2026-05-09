"""
Write a function that accepts an integer and prints the
multiplication table for that number up to 10.

5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
..
5 x 10 = 50
"""

def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
        

multiplication_table(10)