# a = "hello world this is python"

# words = a.split()
# print(words)

# a = "hello-world-this-is-python"
# # words = a.split()
# words = a.split("-")
# # print(words)
# print(len(words))

# my_list = ["abc", "xyz", "hello", "world"]

# my_string = " ".join(my_list)
# my_string = "-".join(my_list)
# print(my_string)
# print(type(my_string))

my_list = ["abc", "xyz", "hello", "world", 56]

# my_string = " ".join(str(i) for i in my_list)
my_string = " ".join(str(i)[::-1] for i in my_list)
print(my_string)
print(type(my_string))

