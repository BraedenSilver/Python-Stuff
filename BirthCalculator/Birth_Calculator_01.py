# Figure out the ideal time to conceive based on the month/date you wish the child to be born. For example if you
# wish for your child to be born in June you simply say June, and the program tells you the month you need get busy in.

print("Choices, January, February, March, April, May, June, July, August, September, October, November, December ")
BirthMonth = input("Type in the month you wish your child will be born in: ")

if BirthMonth == "January":
    print("Start conception in April")
elif BirthMonth == "February":
    print("Start conception in May")
elif BirthMonth == "March":
    print("Start conception in June")
elif BirthMonth == "April":
    print("Start conception in July")
elif BirthMonth == "May":
    print("Start conception in August")
elif BirthMonth == "June":
    print("Start conception in September")
elif BirthMonth == "July":
    print("Start conception in October")
elif BirthMonth == "August":
    print("Start conception in November")
elif BirthMonth == "September":
    print("Start conception in December")
elif BirthMonth == "October":
    print("Start conception in January")
elif BirthMonth == "November":
    print("Start conception in February")
elif BirthMonth == "December":
    print("Start conception in March")
else:
    print("Invalid birth month. No fucking scheduled. Restart the program.")

# I remade this awful code in the Birth_Calculator_02.py file.
