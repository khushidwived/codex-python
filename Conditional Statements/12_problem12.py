"""
A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
a. Take following input from user
 1. Number of classes held
 2. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not.
"""

classes_held = int(input("Enter total number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    print("NO")
