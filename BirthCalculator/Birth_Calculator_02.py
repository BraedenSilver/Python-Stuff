# Dictionary to map birth month to the corresponding conception month
conception_schedule = {
    "January": "April",
    "February": "May",
    "March": "June",
    "April": "July",
    "May": "August",
    "June": "September",
    "July": "October",
    "August": "November",
    "September": "December",
    "October": "January",
    "November": "February",
    "December": "March"
}

print("Choices: January, February, March, April, May, June, July, August, September, October, November, December")
birth_month = input("Type in the month you wish your child will be born in: ")

# Check if the input is valid
if birth_month in conception_schedule:
    print(f"Start conception in {conception_schedule[birth_month]}")
else:
    print("Invalid birth month. No fucking scheduled. Restart the program.")
