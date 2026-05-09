# Print the smallest number present in that list.

my_list = [45, 27, 23, 73.22, 82, 93, 100]
smallest = my_list[0]

# Iterate by value
for i in my_list:
    if i < smallest:
        smallest = i
        
print(smallest)
