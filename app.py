import random

# Function to generate the random number
def random_number():
    return random.randint(1, 100)

def play_game():
    print("Welcome to the Random Number Generator!")
        
    # Step 1: Generate the random number and store it in a variable
    number = random_number()
    print("A random number between 1 and 100 has been generated.")
        
    user_guess = None # Initialize user_guess to None to enter the loop
    guess_count = 0
    max_guesses = 10
    # Step 2: Loop until the user guesses the number
    while user_guess != number:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            guess_count += 1
            # Step 3: Print the user's guess and the random number for now (for testing)
            if user_guess > number:
                print("Your guess is too high.")
            elif user_guess < number:
                print("Your guess is too low.")
            else:
                print("Congratulations! You guessed the number correctly.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")

    if guess_count == max_guesses and user_guess != number:
        print("Sorry, you've used all your guesses. The number was:", number)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_game()