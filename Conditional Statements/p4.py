"""
Ask five marks from user.
Calculate percentage and print it.

91-100 -> A grade
81-90 -> B grade
71-80 -> C grade
61-70 -> D grade
1-60 -> FAIL
Invalid
"""
maths=int(input("Enter marks in maths = "))
physics=int(input("Enter marks in physics = "))
chemistry=int(input("Enter marks in chemistry = "))
english=int(input("Enter marks in english = "))
hindi=int(input("Enter marks in hindi = "))

total=maths+physics+chemistry+english+hindi

Percentage = (total/500)*100
print(f"Percentage scored = {Percentage}")

if Percentage>=91 and Percentage<=100:
    print("A grade")
elif Percentage>=81 and Percentage<=90:
    print("B grade")
elif Percentage>=71 and Percentage<=80:
    print("C grade")
elif Percentage>=61 and Percentage<=70:
    print("D grade")
elif Percentage>=1 and Percentage<=60:
    print("FAIL")
else:
    print("Invalid percentage")
    