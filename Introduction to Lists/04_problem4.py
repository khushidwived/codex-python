# Print all the elements present at even index position.

my_list = [45, 27, 23, 73, 82, 93, 100]

# print elements at even index positions
for i in range(0, len(my_list), 2):  # step of 2 → even indices only
    # if i % 2 == 0:
    print(my_list[i], end=" ")
    
    
# range(0, len(my_list), 2) → 
# starts from index 0 and goes up to the end, skipping every alternate index (0, 2, 4, 6...).

# my_list[i] → fetches the element at that index.