print("\n*********** Age Quiz ***********\n")
# Request user details
age = int(input("Please enter your age : "))
# check the age and display corresponding message
if age < 13:
    print("\n You qualify for a kiddie discount \n")
elif age == 21:
    print("\n Congrats on your 21st! \n")
elif age >= 40 and age < 65:
    print("\n You're over the hill \n")
elif age >= 65 and age <= 100:
    print("\n Enjoy your retirement!\n")
elif age > 100:
    print("\n Sorry, you're dead\n")
else:
    print("\n Age is but a number\n")