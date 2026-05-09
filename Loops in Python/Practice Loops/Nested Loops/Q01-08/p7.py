"""
Ask N from user. N means number of lines. Then print the following pattern.
Enter n = 6
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
6 6 6 6 6
"""
n= int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,6):
        print(i, end=" ")
    print()