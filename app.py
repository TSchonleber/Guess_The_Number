import random

# Function to generate the random number
def random_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Random Number Generator!")
    
    # Step 1: Generate the random number and store it in a variable
    number = random_number()
    print("A random number between 1 and 100 has been generated.")
    
    # Step 2: Ask the user to guess the number
    user_guess = int(input("Enter your guess (between 1 and 100): "))
    
    # Step 3: Print the user's guess and the random number for now (for testing)
    if user_guess > number:
        print("Your guess is too high.")
    elif user_guess < number:
        print("Your guess is too low.")
    else:
        print("Congratulations! You guessed the number correctly.")


if __name__ == "__main__":
    main()