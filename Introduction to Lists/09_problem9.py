# Find the sum of all numbers divisible by 3 or 4.

my_list = [45, 27, 23, 72, 82, 93, 100]
total = 0

# iterate by value
for num in my_list:
    if isinstance(num, int):
        if num % 3 == 0 or num % 4 == 0:
            total += num

print("Sum of numbers divisible by 3 or 4:", total)


# iterate using index
for i in range(len(my_list)):
    if my_list[i] % 3 == 0 or my_list[i] % 4 == 0:
        total += my_list[i]

print("Sum =", total)
