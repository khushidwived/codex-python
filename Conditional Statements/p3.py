"""
Ask physics and chemistry marks from user
Print PASS, if student is passed in both subjects
Else print FAIL
"""

physics=int(input("Enter physics marks = "))
chemistry=int(input("Enter chemistry marks = "))

if physics>=33 and chemistry>=33:
    print("PASS")
else:
    print("FAIL")
    