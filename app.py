import random
import time

leaderboard = []
player_stats = {}

too_high_messages = ["Too high! Try again.", "Way too high! Try lower.", "You're above the target! Lower it down."]
too_low_messages = ["Too low! Try again.", "Way too low! Aim higher.", "You're below the target! Go higher."]

# Function to generate the random number
def random_number(low, high):
    return random.randint(low, high)

def choose_range():
    print("Choose your custom range:")
    while True:
        try:
            low = int(input("Enter the minimum number: "))
            high = int(input("Enter the maximum number: "))
            if low >= high:
                print("The minimum number must be less than the maximum number. Please try again.")
            elif high - low > 1000:
                # Cap the range if it's too wide
                print("The range is too large. Please choose a smaller range (maximum difference of 1000).")
            else:
                return low, high
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def calculate_guesses(low, high):
    range_size = high - low + 1
    # Calculate one guess per every 10 numbers in the range, with a minimum of 5 guesses
    return max(5, range_size // 10)


def update_leaderboard(player_name, guess_count):
    #Add the player's name and score to the leaderboard
    leaderboard.append((player_name, guess_count))
    #sort the leaderboard by the lowest guess count
    leaderboard.sort(key=lambda x: x[1])

    #display the top players
    print("\nLeaderboard:")
    for i, (name, score) in enumerate(leaderboard[:5], start=1):  # Show top 5 players
        print(f"{i}. {name}: {score} guesses")
    print("\n")
def ask_play_again():
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thank you for playing!")

def give_advanced_hint(number, guess_count):
    # Provide an advanced hint after 3 incorrect guesses
    if guess_count >= 3:
        if number % 2 == 0:
            print(f"Hint: The number is even.")
        else:
            print(f"Hint: The number is odd.")
    
    # Provide a second hint after 6 incorrect guesses
    if guess_count >= 6:
        if number % 10 <= 2 or number % 10 >= 8:
            print(f"Hint: The number is close to a multiple of 10.")
        elif number % 5 == 0:
            print(f"Hint: The number is a multiple of 5.")
def update_player_stats(player_name, won_game, guess_count):
    if player_name not in player_stats:
        player_stats[player_name] = {"total_games": 0, "total_wins": 0, "total_guesses": 0}
    player_stats[player_name]["total_games"] += 1
    if won_game:
        player_stats[player_name]["total_wins"] += 1
    player_stats[player_name]["total_guesses"] += guess_count

def display_player_stats(player_name):
    stats = player_stats[player_name]
    win_rate = stats["total_wins"] / stats["total_games"] * 100 if stats["total_games"] > 0 else 0
    avg_guesses = stats["total_guesses"] / stats["total_games"]
    print(f"\n{player_name}'s Stats: ")
    print(f"Total Games: {stats['total_games']}")
    print(f"Total Wins: {stats['total_wins']}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Average Guesses: {avg_guesses:.2f}")

def play_game():
    player_name = input("Enter your name: ")
    print("Welcome to the Random Number Generator,", player_name + "!")
    
    low, high = choose_range()
    max_guesses = calculate_guesses(low, high)
    # Generate the random number and store it in a variable
    number = random_number(low, high)

    print("Okay", player_name, "I'm thinking of a number between", low, "and", str(high) + ". You have", time_limit, "seconds to guess it.")
        
    user_guess = None # Initialize user_guess to None to enter the loop
    guess_count = 0
    previous_guesses = []

    time_limit = max(30, max_guesses * 6)
    start_time = time.time()
    won_game = False
    # Loop until the user guesses the number
    while user_guess != number and guess_count < max_guesses:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time's up! ", player_name, "You didn't guess the number in time.")
            break
        print("You have", max_guesses - guess_count, "guesses left", player_name + "!")
        print("Time left:", time_limit - elapsed_time, "seconds")
        print("Previous guesses:", previous_guesses)
        try:
            # Ask for user input and compare it to an integer
            user_guess = int(input("Enter your guess (between " + str(low) + " and " + str(high) + "): "))
           
           # Check if user already guessed the number
            if user_guess in previous_guesses:
                print("You already guessed that number. Try something else.")
                continue
               
            guess_count += 1 #increment the guess count
            previous_guesses.append(user_guess) #add the guess to the list of previous guesses
        

           # Compare the user's guess to the random number
            if user_guess > number:
                print(random.choice(too_high_messages))
            elif user_guess < number:
                print(random.choice(too_low_messages))
            else:
                print("Congratulations!", player_name, "You guessed the number correctly in", guess_count, "guesses!")
                update_leaderboard(player_name, guess_count)
                won_game = True
                
            give_advanced_hint(number, guess_count)
       #In case of invalid iSnput
        except ValueError:
            print("Invalid input. Please enter a valid number between", low, "and", high + ".")

    # Provide a hint based on the number of guesses
    if guess_count == 5 and max_guesses > 5:
           if number <= (low + high) // 2:
                print(f"Hint: The number is in the lower half ({low}-{(low + high) // 2}).")
           else:
                print(f"Hint: The number is in the upper half ({(low + high) // 2 + 1}-{high}).")
    
    # check if the user has used all their guesses
    if guess_count == max_guesses and user_guess != number:
        print("Sorry,", player_name, "you've used all your guesses. The number was:", number)
    
    # Update player stats
    update_player_stats(player_name, won_game, guess_count)
    display_player_stats(player_name)
    
    # Ask the user if they want to play again
    ask_play_again()
    if ask_play_again() == "y":
        play_game()
    else:
        print("Thank you for playing", player_name, "goodbye!")

if __name__ == "__main__":
    play_game() #start the game