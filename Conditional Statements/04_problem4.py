class_held=int(input("Enter total classes held = "))
class_attended=int(input("Enter total classes attended = "))

class_per=(class_attended/class_held)*100

print(f"Percentage of class attended = {class_per:.4f}%")

if class_per>=75:
    print("Yes, you can sit in exam")
else:
    print("No, you cannot sit in exam")
    