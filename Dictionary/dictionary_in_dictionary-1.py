"""
rahul -> 400 
krish -> 300
aman -> 480
"""

students_data = {
    "rahul": {       
        "roll_number": 25,
        "gender" : "male",
        "marks" : [98,67,95,80,56],        
    },
    "krish": {
        "roll_number": 16,
        "gender" : "male",
        "marks" : [98,64,92,85,50],
    },
    "aman": {        
        "roll_number": 15,
        "gender" : "male",
        "marks" : [99,68,90,81,69],
    },
}

# for name, details in students_data.items():
#     total = (sum(details["marks"]))
#     print(f"{name} has scored {total} marks")


# Method 2
# calculate total marks without using sum():

for name, details in students_data.items():
    total = 0
    for mark in details["marks"]:   # iterate each mark manually
        total = total + mark        # add marks one by one
    print(f"{name} has scored {total} marks")
    