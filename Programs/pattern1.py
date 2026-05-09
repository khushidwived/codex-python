# # def is_amsrong_number(num):
      
# n = 153

# num = n
# total = 0 
# nod = len(str(n))

# while num > 0:
#     ld = num % 10
#     total = total + (ld ** nod)
#     num = num // 10

# if total == n:
#     print(f"{n} amstrong number")
# else:
#     print("No")
    
# print(total == n)


# Merge Intervals
# Example

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(merge_intervals(intervals))  # [[1,6],[8,10],[15,18]]

a = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(a):
    res = []  # same as vector<vector<int>> res;

    # initialize first interval
    start1, end1 = a[0]   # like int start1 = a[0][0], end1 = a[0][1]

    # loop through rest
    for i in range(1, len(a)):
        start2, end2 = a[i]   # int start2 = a[i][0], end2 = a[i][1]

        if end1 >= start2:    # overlap condition
            # merge: keep start1, update end1
            end1 = max(end1, end2)
            continue
        # no overlap → push current interval
        res.append([start1, end1])
        start1, end1 = start2, end2

    # push last interval
    res.append([start1, end1])
    return res

print(merge_intervals(a))
