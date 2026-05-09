"""
Write a function that accepts a string and prints the frequency of
each character in the string.

hello

{"h":1,"e":1,"l":2}

h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
"""


def charcount(string):
    # my_dict = {}
    my_dict = dict()  # {"h":1,"e":1,"l":2}
    for ch in string:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charcount("development")
