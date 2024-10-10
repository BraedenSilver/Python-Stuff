# Basic print examples
print("Hello World")
print(10 + 24)
print("Hello World", 23 + 23)
print("-----------------------")

# User input with error handling
try:
    a = int(input("Enter a number for 'a': "))
    b = int(input("Enter a number for 'b': "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Print the values of a and b
print("a =", a)
print("b =", b)
print("total of a + b =", a + b)
print("-----------------------")

# If/else to compare a and b
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

if a + b >= 5:
    print("a + b is greater or equal to 5")
else:
    print("a + b is less than 5")
print("-----------------------")

# Loop to print numbers from 0 to a-1
for i in range(a):
    print("Loop number:", i)
