students_data = {
    "rahul": {
        "roll_number": 25,
        "gender": "male",
        "marks": {"physics": 89, "chemistry": 98, "maths": 95},
    },
    "krish": {
        "roll_number": 16,
        "gender": "male",
        "marks": {"physics": 97, "chemistry": 92, "maths": 91},
    },
    "aman": {
        "roll_number": 15,
        "gender": "male",
        "marks": {"physics": 99, "chemistry": 92, "maths": 90},
    },
}
    
for name, details in students_data.items():
    total = (
        details["marks"]["physics"]
        + details["marks"]["chemistry"]
        + details["marks"]["maths"]
    )
    print(f"{name} has scored {total} marks")
