# xplanation:

# my_list[::-1] means:

# : → take all elements
# -1 → step backwards (reverse order)


# Print the list in reverse.

my_list = [23, -54, "C&D", 22.22, 100]

# Method 1: Using slicing
print(my_list[::-1])

# Method 2: Using reverse() method
my_list.reverse()
print(my_list)

# Method 3: This is a loop-based method to traverse a list backward
for i in range(len(my_list) -1, -1, -1):
    print(my_list[i], end=" ")
    