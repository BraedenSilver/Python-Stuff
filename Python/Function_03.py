# Calculator
def calculate():
    print("Type 1 for Addition")
    print("Type 2 for Subtraction")
    print("Type 3 for Multiplication")
    print("Type 4 for Division")
    math = input("Enter choice(1/2/3/4): ")

    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if math == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif math == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif math == "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif math == "4":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Division by zero is not allowed!")
    else:
        print("Invalid input, please enter a number between 1 and 4.")


calculate()
