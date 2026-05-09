# for i in range(1,4):
#     print(i)
#     for j in range(10,14):
#         print(j)
        
num = [0,1,2,0,1,2]
def arrangeXYZ(num):
    # Mapping: 1 -> x, 2 -> y, 0 -> z
    low, mid, high = 0, 0, len(num) - 1
    
    while mid <= high:
        if num[mid] == 1:   # x
            num[low], num[mid] = num[mid], num[low]
            low += 1
            mid += 1
        elif num[mid] == 2: # y
            mid += 1
        else:               # z (0)
            num[mid], num[high] = num[high], num[mid]
            high -= 1

# Example

arrangeXYZ(num)
print(num)   # Output: [1,1,2,2,0,0]
     

