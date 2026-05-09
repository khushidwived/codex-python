# Print the sum of all elements present in that list

my_list = [45, 27, 23, 73, 82, 93, 100]
total = 0

# # Calculate the sum of all elements
# total = sum(my_list)
# print("Sum of all elements:", total)


# # Iterate by value 
# for i in my_list:
#     total = total + i
    
# print("Sum of all elements:", total)


# Iterate by index
for i in range(len(my_list)):
    total += my_list[i]   # add element at index i to total

print("Sum of all elements:", total)


