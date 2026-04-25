import random

def play_game():
    print("\n Welcome to the Number Guessing Game!")

    # Difficulty levels
    print("\nChoose Difficulty Level:")
    print("1. Easy (1-50, 4 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        max_range = 50
        max_attempts = 4
    elif choice == '2':
        max_range = 100
        max_attempts = 7
    elif choice == '3':
        max_range = 200
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_range = 100
        max_attempts = 7

    number_to_guess = random.randint(1, max_range)
    attempts = 0

    print(f"\nGuess a number between 1 and {max_range}")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print(" Too low!")
            elif guess > number_to_guess:
                print(" Too high!")
            else:
                print(f"\n Correct! You guessed it in {attempts} attempts.")
                return
        except ValueError:
            print(" Please enter a valid number!")

    print(f"\n Game Over! The correct number was {number_to_guess}")


# Main loop for replay
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for playing! ")
        break