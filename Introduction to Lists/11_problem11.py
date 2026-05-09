# Print the largest number present in that list.

my_list = [45, 27, 23, 73.22, 82, 93, 100, 6, 10]
largest = my_list[0]

# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest =  my_list[i]
        
# print(largest)
    
# Iterate by value
for i in my_list:
    if i > largest:
        largest = i
        
print(largest)
