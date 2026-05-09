students_data = {
    "rahul": {       
        "roll_number": 25,
        "class": "10A",
        "phy" : 98,
        "che" : 92,
        "maths" : 80,
    },
    "krish": {
        "roll_number": 16,
        "class": "10B",
        "phy" : 98,
        "che" : 92,
        "maths" : 80,
    },
    "aman": {        
        "roll_number": 15,
        "class": "10A",
        "phy" : 98,
        "che" : 92,
        "maths" : 80,
    },
}

for name, details in students_data.items():
    total = details["phy"] + details["che"] + details["maths"]
    roll_number = details["roll_number"]
    print(f"{name} -> {total}, roll_number = {roll_number}")

