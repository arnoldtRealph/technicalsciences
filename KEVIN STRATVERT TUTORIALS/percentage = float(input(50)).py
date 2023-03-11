percentage = float(input(50))

if percentage < 30:
    print("Grade: F - Fail")
elif percentage >= 30 and percentage < 40:
    print("Grade: L2 - Level 2")
elif percentage >= 40 and percentage < 50:
    print("Grade: L3 - Level 3")
elif percentage >= 50 and percentage < 60:
    print("Grade: L4 - Level 4")
elif percentage >= 60 and percentage < 70:
    print("Grade: L5 - Level 5")
elif percentage >= 70 and percentage < 80:
    print("Grade: L6 - Level 6")
else:
    print("Grade: D - Distinction")