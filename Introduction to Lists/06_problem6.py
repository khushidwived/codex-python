# Count the number of even numbers present in that list.

my_list = [45, 27, 23, 73.22, 82, 93, 100]

count = 0  # to store number of even numbers

# for num in my_list:
#     if isinstance(num, int) and num % 2 == 0:  # check if the element is an integer and even
#         count += 1

# print("Number of even numbers:", count)

for i in my_list:
    if i % 2 == 0:
        count = count + 1
        
print(f"Total even numbers = {count}")
        