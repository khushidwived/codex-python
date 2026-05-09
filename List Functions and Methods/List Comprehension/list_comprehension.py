# Create a list using list comprehension

my_list=[i for i in range(1,21)]
print(my_list)


# i=1 ODD
# i=2 EVEN
# i=3 ODD
# [ODD,EVEN,ODD,EVEN,ODD,EVEN]

# my_list=["EVEN" if i % 2 == 0 else "ODD" for i in range(1,21)]
# print(my_list)

# [2,4,6,8,.......26,28,30]
my_list=[i for i in range(1,31) if i % 5 == 0]
print(my_list)

