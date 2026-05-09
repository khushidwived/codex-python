# sum of even numbers b/w 20 and 40 both (included)

total = 0

for num in range(20, 41):   # 20 to 40
    if num % 2 == 0:        # check even
        total += num

print("Sum of even numbers from 20 to 40 =", total)