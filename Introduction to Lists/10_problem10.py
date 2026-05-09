# Print how many positive and negative numbers are here.

my_list = [45, 27, 23, -73, 82, -93, 100]

# Initialize counters
positive_count = 0
negative_count = 0

# Iterate through list
for num in my_list:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

# Print results
print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)
