import random

def display_heading():
    print("Welcome to the Guessing Game!")
    print("-----------------------------")

def play_game(limit):
    random_number = random.randint(1, limit)
    print(f"I'm thinking of a number between 1 and {limit}. Can you guess it?")
    while True:
        user_guess = int(input("Enter your guess: "))
        if user_guess < random_number:
            print("Too low! Guess again.")
        elif user_guess > random_number:
            print("Too high! Guess again.")
        else:
            print("Congratulations! You guessed the number.")
            break
display_heading()

while True:
    limit = int(input("Enter a limit for the game: "))
    play_game(limit)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "n":
        break

print("Thanks for playing!")

