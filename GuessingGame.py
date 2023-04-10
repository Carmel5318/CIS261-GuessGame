#Niki Dekcer
#CIS261
#Guess Game
import random

def display_heading():
    print("Welcome to the Guessing Game!")
    print("-----------------------------")
    
def play_game(LIMIT):    
    number = random.randint(1, LIMIT)
    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1
    guess = int(input("Your guess: "))

    while (guess != number):
        if guess < number:
            print("Your guess is too low. Try again!")
            count += 1
        elif guess > number:
            print("You guessed too high. Try again!")
            count += 1
        guess = int(input("Your guess: "))
    print(f"congratulations! You guessed it in {count} tries.\n")
     
def main():
    display_heading()
    again = "y"
    while again.lower() == "y":
        LIMIT = int(input("Enter the limit: "))
        play_game(LIMIT)
        again = input("Do you want to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

