ai_dict = {
        "framework": "TensorFlow",
        "category": "deep learning",
        "intensity": "high"
}

print(ai_dict)

# # Method 1
# ai_dict["intensity"] = "medium"  # Add/Update
ai_dict["version"] = "2.15"
print(ai_dict)

# Method 2

# # add multiple elements at once
# ai_dict.update({
#     "version": "2.15",
#     "accuracy": "95%"
# })

# print(ai_dict)
