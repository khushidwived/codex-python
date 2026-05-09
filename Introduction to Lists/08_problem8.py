# Find the sum of all even numbers present in that list.

my_list = [45, 27, 23, 73.22, 82, 93, 100]
total = 0

# Iterate by value
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        total = total + my_list[i]
        
print(total)
