# ai_dict = {
#         "framework": "TensorFlow",
#         "category": "deep learning",
#         "intensity": "high"
# }

# # for k in ai_dict.keys():
# #     print(k)

# # for k in ai_dict.keys():
# #     print(ai_dict[k])

# # for v in ai_dict.values():
# #     print(v)
    
my_dict = {
        "maths" : 96,
        "physics" : 98,
        "chemistry" : 100,
}

total_marks = 0
for v in my_dict.values():
    total_marks = total_marks + v

print(total_marks)
