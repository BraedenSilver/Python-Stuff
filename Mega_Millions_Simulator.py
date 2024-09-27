from random import sample, randrange, choice


def play_mega_millions():
    total_spent = 0
    total_won = 0

    while True:
        # Generate winning numbers
        winning_numbers = sample(range(1, 71), 5)
        mega_ball = randrange(1, 26)

        # Random jackpot value between $40 million and $1 billion
        jackpot = randrange(40_000_000, 1_000_000_001)

        # Get a random multiplier for non-jackpot prizes (2x to 5x)
        multiplier = choice([2, 3, 4, 5])

        # Get player's numbers
        print("\nEnter your 5 numbers between 1 and 70:")
        player_numbers = []
        for i in range(5):
            while True:
                num = int(input(f"Enter number {i + 1}: "))
                if 1 <= num <= 70 and num not in player_numbers:
                    player_numbers.append(num)
                    break
                else:
                    print("Invalid number or number already entered. Please try again.")

        player_mega_ball = int(input("Enter your Mega Ball number (1-25): "))

        # Calculate ticket cost
        ticket_cost = 2  # Each Mega Millions ticket costs $2
        total_spent += ticket_cost

        # Check for matches
        matching_numbers = set(player_numbers) & set(winning_numbers)
        match_count = len(matching_numbers)
        mega_ball_match = (player_mega_ball == mega_ball)

        # Display winning numbers and Mega Ball
        print("\nWinning Numbers: ", ' '.join(map(str, winning_numbers)))
        print("Mega Ball: ", mega_ball)
        print(f"Jackpot: ${jackpot:,}")
        print(f"Multiplier: {multiplier}x (for non-jackpot prizes)")

        # Determine prize
        prize = 0
        if match_count == 5 and mega_ball_match:
            prize = jackpot  # Jackpot for matching all numbers and the Mega Ball
            print("Congratulations! You won the GRAND PRIZE (Jackpot)!")
        elif match_count == 5:
            prize = 1_000_000 * multiplier  # Second prize, multiplied
            print("You won the SECOND PRIZE!")
        elif match_count == 4 and mega_ball_match:
            prize = 10_000 * multiplier
            print("You won the THIRD PRIZE!")
        elif match_count == 4:
            prize = 500 * multiplier
            print("You won the FOURTH PRIZE!")
        elif match_count == 3 and mega_ball_match:
            prize = 200 * multiplier
            print("You won the FIFTH PRIZE!")
        elif match_count == 3:
            prize = 10 * multiplier
            print("You won the SIXTH PRIZE!")
        elif match_count == 2 and mega_ball_match:
            prize = 10 * multiplier
            print("You won the SEVENTH PRIZE!")
        elif match_count == 1 and mega_ball_match:
            prize = 4 * multiplier
            print("You won the EIGHTH PRIZE!")
        elif mega_ball_match:
            prize = 2 * multiplier
            print("You won the NINTH PRIZE!")
        else:
            print("Sorry, you didn't win anything this time.")

        # Update total winnings
        total_won += prize

        # Show current money status
        print(f"\nYou spent: ${total_spent:,}")
        print(f"You've won: ${total_won:,}")

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"\nFinal Results: You spent ${total_spent:,} and won ${total_won:,}.")
            print("Thanks for playing!")
            break


# Start the game
play_mega_millions()
