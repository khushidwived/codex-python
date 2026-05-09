ai_dict = {
        "framework": "TensorFlow",
        "category": "deep learning",
        "intensity": "high"
}

k = input("Enter a key: ")
result = ai_dict.get(k)

if result is not None:
    print(result)
else:
    print("Key does not exists")



# print(ai_dict)
# print(ai_dict["framework"])
# print(ai_dict["xyz"])


# # To get a value
# r = ai_dict.get("framework")
# r = ai_dict.get("xyz")
# print(r)
# print(type(r))


