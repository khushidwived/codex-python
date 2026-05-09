# # Print 1 to 10 using While loop
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i = i + 1

# print()  

# Check if a number is palindrome
# n = 11111
# num = n
# result = 0
# while num > 0:
#     ld = num % 10
#     result = (result * 10) + ld
#     num = num // 10

# print(n == result)
n=1112
num = n 
p=0
while num > 0:
    ld = num % 10
    p = (p*10) + ld
    num = num // 10
    
if n == p:
    print("palindrome")
else:
    print("you are madherchoad")
   
    
   
    