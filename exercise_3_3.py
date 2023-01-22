score = float(input("Enter Score: "))

if score < 0.0 or score > 1.0:
    print("Error: out of rage!")

if score >= 0.9:
    mark = "A"
elif score >= 0.8:
    mark = "B"
elif score >= 0.7:
    mark = "C"
elif score >= 0.6:
    mark = "D"
elif score < 0.6:
    mark = "F"

print(mark)