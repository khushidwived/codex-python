# Count how many numbers are divisible by both 2 and 5 in that list.

my_list = [45, 27, 23, 73.22, 82, 93, 100]
count = 0

# for i in my_list:
#     # Check if it's an integer and divisible by 10
#     if i % 10 == 0:
#         count += 1

# print("Numbers divisible by both 2 and 5:", count)


for i in range(len(my_list)):
    num = my_list[i]
    if num % 2 == 0 and num % 5 == 0:
        count += 1

print("Count of numbers divisible by both 2 and 5:", count)