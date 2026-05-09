# Remove all the even numbers from the list.

a = [45, 44, 99, 65, 74, 87]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)

