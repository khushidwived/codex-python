"""
Write a function that takes an integer and prints whether it is a
prime number.
"""

def is_prime(num): # 17
    factor = 0
    for i in range(1,num+1): # 1,2,3,4,5,.....,20
        if num % i == 0:
            factor +=1
    if factor == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")
        

is_prime(10)
is_prime(11)
