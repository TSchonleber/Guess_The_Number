import random

def random_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Random Number Generator!")
    print("Generating a random number between 1 and 100...")
    print("The random number is:", random_number())

if __name__ == "__main__":
    main()