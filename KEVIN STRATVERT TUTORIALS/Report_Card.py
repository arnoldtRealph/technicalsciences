percentage = float(input("Enter the Learner's percentage:"))

if percentage < 30:
    print("You have failed, try again")
elif percentage >= 30 and percentage < 40:
    print("You have a level 2")
elif percentage >= 40 and percentage < 50:
    print("You have a level 3")
elif percentage >= 50 and percentage < 60:
    print("You have a level 4")
elif percentage >= 60 and percentage < 70:
    print("You have a level 5")
elif percentage >= 70 and percentage < 80:
    print("You have a level 6")
elif percentage >= 80 and percentage <= 100:
    print("You have a distinction, Well done")
else:
    print("Invalid percentage, please insert a percentage between 0 and 100")






