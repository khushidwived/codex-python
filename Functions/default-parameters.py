# default parameters

def total_marks(physics, maths, science=0, hindi=0, english=0):
    print(f"Your marks in physics = {physics}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in science = {science}")
    print(f"Your marks in hindi = {hindi}")
    print(f"Your marks in english = {english}")
    total = physics + maths + science + hindi + english
    print(f"Your total marks = {total}")


total_marks(99, 98)
