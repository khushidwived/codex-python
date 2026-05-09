# named parameters

def total_marks(physics, maths, science, hindi, english):
    print(f"Your marks in physics = {physics}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in science = {science}")
    print(f"Your marks in hindi = {hindi}")
    print(f"Your marks in english = {english}")
    total =physics + maths + science + hindi + english
    print(f"Your total marks = {total}")


total_marks(98, 99, science=95, hindi=56, english=80)
# total_marks(physics=98, english=80, science=95, maths=99, hindi=56)
