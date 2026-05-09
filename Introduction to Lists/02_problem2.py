# Print all the even numbers present in the list.

my_list = [22, 82, 95, 68, 75, 99]

# Iteration by value
for i in my_list:
    if i % 2 == 0:   # check if number is even
        print(i, end=" ") 


# # Iteration by index
# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0:
#         print(my_list[i], end=" ")
