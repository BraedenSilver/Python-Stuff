# Function for a mini spelling lesson with a loop
def spanish_lesson():
    while True:
        userinput = input("Spell the word 'spanish': ")
        if userinput == "spanish":
            print("Correct!")
            break  # Exits the loop if the user is correct
        else:
            print("Incorrect, you suck! Try again.")


spanish_lesson()  # Call the function
